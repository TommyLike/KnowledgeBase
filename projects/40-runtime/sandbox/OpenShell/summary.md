# NVIDIA/OpenShell

> [`NVIDIA/OpenShell`](https://github.com/NVIDIA/OpenShell) · 上游贡献 · NVIDIA 开源的自主 AI Agent「安全私有运行时」——Rust 编写，把**沙箱执行 + 受控网络出口网关 + 凭据代理 + GPU 直通**组合成一个运行时。团队作为上游贡献者，关注其凭据隔离网关、多后端沙箱驱动和 GPU passthrough 机制。

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-07-05 · Rust(309) + YAML(100) + TOML(43) + Python(10) · 574文件 · 18.6k 节点 / 80.6k 边
**入口** `crates/openshell-cli/src/main.rs` (CLI) · `crates/openshell-server/src/main.rs` (控制面) · 各 `openshell-driver-*/src/main.rs` (沙箱驱动)
**架构** 15+ Rust crate 工作区：CLI/TUI → openshell-server(控制面 gRPC/HTTP) → openshell-supervisor-network(L7 出口网关+凭据注入) + openshell-driver-{vm,podman,docker,kubernetes}(沙箱后端) + openshell-vfio(GPU 直通) + openshell-policy(OPA 策略) + openshell-ocsf(审计)
**热点** ServerState.new · GuestTlsPaths.from · LifecycleExtensionRegistry · TokenCache.get · TraceBuf.write · DatabaseHealthMonitor.spawn
<!-- END AUTO -->

---

## 定位
> OpenShell 是 NVIDIA 为自主 AI Agent（尤其是 Claude Code / Codex / Copilot / Cursor 这类编码 Agent）打造的**安全私有运行时**。它的重心不是"再造一个 Docker 沙箱"，而是解决 Agent 落地的三个真问题：(1) **凭据不能交给 Agent**——由出口网关在网络边界注入 provider 凭据；(2) **执行要能隔离且可迁移**——同一套接口跑在 microVM / Podman / Docker / Kubernetes 四种后端上；(3) **GPU 要能安全共享**——通过 VFIO 直通把 GPU 交给沙箱。在 Agent Runtime / Sandbox 生态中，OpenShell 代表「凭据网关 + 多后端沙箱 + GPU 直通」的一体化路线，与 [`anthropic-experimental/sandbox-runtime`](../sandbox-runtime/)（本地进程级）、E2B（Firecracker SaaS）形成差异。

## 项目介绍
> **让 AI 编码 Agent 安全地跑起来——沙箱执行 + 出口凭据网关 + GPU 直通，一个 Rust 运行时全包。**

核心场景：
- **凭据零暴露的 LLM 访问**：Agent 需要调用 Claude/Codex/Copilot/Cursor/Bedrock/Vertex 等（`providers/*.yaml` 内置 11 家），API key 由 `openshell-supervisor-network` 在出口处以 SIGv4 签名 / token grant 注入，**Agent 全程看不到原始密钥**。
- **多后端沙箱执行**：同一个 Agent 会话，可按环境落到 microVM（强隔离）、Podman/Docker（本地）、或 Kubernetes（集群）任一后端。
- **GPU Agent 沙箱**：通过 `openshell-vfio` 把 NVIDIA GPU 以 VFIO PCI passthrough 直通进沙箱，供推理/训练类 Agent 使用——这是 NVIDIA 的差异化能力。
- **Agent 驱动的策略审批**：`/v1/proposals` API + RFC 0002，Agent 可**提议**扩权，走 propose → wait → approve 流程，而非硬编码权限。

## 整体架构

```
                            ┌──────────────────────────────────────┐
    使用方 / Agent           │  openshell-cli   │   openshell-tui    │  ← 用户面（命令行 / 终端 UI）
                            └──────────────────┬───────────────────┘
                                               │ gRPC / HTTP
   ═══════════════════════════════════════════╪═══════════════════════════════════  控制面 Control Plane
                                               ▼
                            ┌──────────────────────────────────────┐
                            │          openshell-server             │  控制面核心：会话/沙箱编排、
                            │  ServerState · gRPC provider · 多路复用 │  gRPC 服务、TLS、就绪探针
                            │  路由: /v1/policy /v1/proposals        │  /readyz /healthz /metrics /_ws_tunnel
                            └───┬───────────┬───────────┬───────────┘
                                │           │           │
              ┌─────────────────┘           │           └──────────────────┐
              ▼                             ▼                              ▼
   ┌─────────────────────┐   ┌──────────────────────────┐   ┌──────────────────────┐
   │  openshell-core     │   │ openshell-supervisor-*    │   │   openshell-policy    │
   │  数据模型 / 协议     │   │  network(L7 出口网关)     │   │   OPA / L7 策略引擎   │
   │  (proto: sandbox,   │   │  process(进程监督)        │   │   eval_network/eval_l7│
   │   inference, ...)   │   │  身份: SPIFFE / SIGv4     │   └──────────────────────┘
   └─────────────────────┘   │  凭据: TokenCache/grant   │
                             │  代理: forward_proxy      │            │ 审计事件
                             └────────────┬─────────────┘            ▼
                                          │              ┌──────────────────────┐
                    出口网络流量(注入凭据) │              │   openshell-ocsf      │
                                          ▼              │  OCSF 安全审计日志     │
                             ┌────────────────────────┐  └──────────────────────┘
                             │   外部 LLM Provider     │
                             │  Claude/Codex/Copilot/  │
                             │  Cursor/Bedrock/Vertex/ │
                             │  NVIDIA/GitHub/PyPI ...  │
                             └────────────────────────┘

   ═══════════════════════════════════════════════════════════════════════════════  数据面 / 沙箱驱动层
                                          │ 创建/管理沙箱
        ┌──────────────┬─────────────────┼──────────────────┬──────────────────┐
        ▼              ▼                 ▼                  ▼                  ▼
 ┌────────────┐ ┌────────────┐   ┌────────────┐    ┌────────────────┐  ┌──────────────┐
 │  driver-vm │ │driver-podman│   │driver-docker│   │driver-kubernetes│  │openshell-vfio│
 │  microVM   │ │  Podman     │   │  Docker     │   │  Kubernetes     │  │ GPU 直通      │
 │ (最强隔离) │ │ (本地容器)  │   │ (本地容器)  │    │  (集群编排)     │  │ VFIO PCI     │
 └─────┬──────┘ └─────┬──────┘   └─────┬──────┘    └───────┬────────┘  └──────┬───────┘
       │              │                │                   │                  │
   ════╪══════════════╪════════════════╪═══════════════════╪══════════════════╪════════  底层 Runtime
       ▼              ▼                ▼                   ▼                  ▼
  ┌─────────┐   ┌──────────┐    ┌──────────┐        ┌──────────┐      ┌────────────┐
  │ KVM /   │   │ Podman   │    │ Docker   │        │ K8s API  │      │ NVIDIA GPU │
  │ microVM │   │ runtime  │    │ Engine   │        │ + kubelet│      │ (device    │
  │ + kernel│   │          │    │          │        │ + Helm   │      │  plugin)   │
  └─────────┘   └──────────┘    └──────────┘        └──────────┘      └────────────┘
        └─────────── 沙箱内运行 Agent 生成的代码，出口流量强制经过上方网关 ──────────┘
```

## 组件关系（按真实调用量，来自 codebase-memory boundaries）

```
                          ┌────────────────────────┐
                          │ openshell-supervisor-  │
                          │        network         │   ← 数据面最大模块(1528节点)
                          └───┬──────┬───────┬──────┘      是流量与凭据的中枢
                    299 calls │  224 │   104 │ 103
                              ▼      ▼       ▼      ▼
        ┌────────────────────────┐  │  ┌─────────┐ ┌──────────┐
        │    openshell-server    │◄─┘  │  -ocsf  │ │  -core   │
        │  控制面(2325节点)       │     │ (审计)  │ │ (模型)   │
        └──┬──────────┬─────┬────┘     └─────────┘ └──────────┘
    351call│      93  │  50 │ 35                        ▲
           ▼          ▼     ▼                           │
     ┌──────────┐ ┌────────────┐ ┌──────────────┐       │
     │   -core  │ │ -driver-vm │ │ openshell-vfio│ ──────┘
     │  (模型)  │ │ microVM(554)│ │  GPU 直通(50) │
     └──────────┘ └─────┬──────┘ └──────────────┘
                        │ 130 calls
                        ▼
                  ┌──────────┐   driver-vm 回调 server 上报沙箱生命周期
                  │  server  │
                  └──────────┘

  其余对等沙箱驱动（同层，接口一致）:
    openshell-driver-podman(289) · openshell-driver-docker(264) · openshell-driver-kubernetes(212)
  辅助模块:
    openshell-cli(1085) · openshell-tui(234) · openshell-providers(216) · openshell-policy(211)
    openshell-router · openshell-prover · openshell-bootstrap · openshell-server-macros
```

**关键读法**：`openshell-supervisor-network` 是整个系统调用扇出最集中的地方（对 server 299 次、对 driver-vm 224 次、对 ocsf 104 次）——印证了"网络出口网关 + 凭据注入 + 审计"才是 OpenShell 的架构重心，而不是普通的容器封装。`openshell-server` 是控制面枢纽（扇入 429 / 扇出 572），`openshell-core` 是被大量复用的核心数据模型（扇入 454）。

## 技术要点
- **凭据代理出口网关（核心）**：`openshell-supervisor-network` 内含正向代理（`forward_proxy` / `relay_with_route_selection`）、L7 策略评估（`eval_l7` / `evaluate_network`）、SPIFFE 工作负载身份、AWS SIGv4 签名（`sigv4.rs`）、token 授予与缓存（`TokenCache` / `token_grant.rs`）。Agent 的所有出站流量强制经此网关，凭据在边界注入而非下发给 Agent。
- **多后端沙箱驱动**：`openshell-driver-{vm,podman,docker,kubernetes}` 四套驱动实现同一沙箱接口。`driver-vm` 最大（554 节点），带 `LifecycleExtensionRegistry` 生命周期扩展机制，走 microVM 强隔离路线。
- **GPU VFIO 直通**：`openshell-vfio` 通过 sysfs 操作 PCI 设备（`SysfsPciDevice`），以 VFIO 方式把 NVIDIA GPU 直通进沙箱；配合 `deploy/kube/gpu-manifests/nvidia-device-plugin` 在 K8s 上暴露 GPU。
- **OPA 策略 + Agent 驱动审批**：`openshell-policy` 做网络/L7 策略；`/v1/proposals` 路由（RFC 0002 agent-driven-policy-management）让 Agent 提议策略变更，走 `propose → wait → approve` 异步流程，`/v1/policy/current` 查询当前生效策略。
- **OCSF 标准化审计**：`openshell-ocsf` 以 Open Cybersecurity Schema Framework 记录安全事件，供事后审计与告警。
- **Provider 抽象**：`providers/*.yaml` 声明式接入 11 家（aws-bedrock / claude-code / codex / copilot / cursor / deepinfra / github / google-cloud / google-vertex-ai / nvidia / pypi），`openshell-providers` 加载。
- **多形态分发**：Helm chart（`deploy/helm/openshell`）、Docker、deb/rpm/snap 包、`install.sh` 一键脚本；CLI/TUI 双前端，Python SDK（`python/openshell/sandbox.py`）。

## 技术栈
- **语言**：Rust（309 文件，主体）+ Python（SDK/工具，10 文件）+ 少量 TypeScript（文档站 Fern）
- **通信**：gRPC + Protobuf（`proto/*.proto`：sandbox / inference / compute_driver / datamodel）、HTTP、WebSocket tunnel
- **沙箱后端**：microVM(KVM) / Podman / Docker / Kubernetes
- **策略/身份**：OPA、SPIFFE、AWS SIGv4、TLS(自签 PKI)
- **GPU**：VFIO PCI passthrough、NVIDIA device plugin
- **审计**：OCSF
- **部署**：Helm、Docker、deb/rpm/snap、Nix(flake.nix)、mise

## 关联
- [`anthropic-experimental/sandbox-runtime`](../sandbox-runtime/) — 竞品/互补。srt 是本地进程级 OS 沙箱（无网关、无 GPU、无多后端）；OpenShell 是带凭据网关和 GPU 直通的服务端运行时，量级更重、面向团队/集群。
- [`kubernetes-sigs/agent-sandbox`](../agent-sandbox/) — 同为 K8s Agent 沙箱，但 OpenShell 的 K8s 只是四种驱动之一，且额外提供出口凭据网关。
- [`volcano-sh/agentcube`](../agentcube/) — 同类 K8s Agent 沙箱；OpenShell 不依赖特定调度器，靠自有 driver + VFIO 做 GPU。
- **上游生态**：VFIO / NVIDIA device plugin（GPU）、OPA（策略）、SPIFFE（身份）、containerd/Podman/Docker/K8s（运行时）。
- **下游/接入方**：Claude Code、Codex、Copilot、Cursor 等编码 Agent 通过 `providers/*.yaml` 接入。

## 开放问题
- [ ] 2026-07-05 出口网关注入凭据的模型，如何防止沙箱内 Agent 通过侧信道（如让网关代访问后回传）反向套取凭据？信任边界具体划在哪一层？
- [ ] 2026-07-05 VFIO GPU 直通给沙箱后，多租户下的 GPU 显存/MIG 隔离与回收如何保证？是否依赖 MIG 或 time-slicing？
- [ ] 2026-07-05 四种沙箱驱动的隔离强度差异很大（microVM vs Docker），策略层是否能感知后端隔离等级并据此调整可授予权限？
- [ ] 2026-07-05 RFC 0002 的 Agent 驱动策略审批，approve 环节是人工还是可自动？自动审批会不会成为提权绕过点？
- [ ] 2026-07-05 NVIDIA 对该项目的定位：是 NVIDIA AI 生态的基础设施组件，还是有独立商业化/标准化意图？
