# substrate

> [`agent-substrate/substrate`](https://github.com/agent-substrate/substrate) · 上游贡献 · Google/K8s 生态的高密度 Agent 运行时——利用 gVisor checkpoint/restore 将数百个 Agent 会话复用到少量 K8s Pod 上，实现 30x+ 超卖

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `3ed6aa0` · Go · 842文件/6MB · 153K 行 · 408 `.go` 文件  
**入口** `cmd/` (kubectl-ate CLI, ate-api-server, atelet, ateom, atenet-router) · `internal/` (控制面逻辑) · `pkg/` (公共 API 类型)  
**架构** 控制面(ate-api-server, Redis state store)→节点代理(atelet DaemonSet)→Sandbox Herder(ateom, per-Pod)→gVisor/microVM sandbox。路由层 atenet(Envoy+ext_proc)→atunnel(TLS to Worker)  
**热点** ate-api-server(actor调度) · atelet(快照流式传输) · ateom-gvisor(runsc checkpoint/restore) · atenet-router(请求拦截+actor唤醒)
<!-- END AUTO -->

---

## 定位
> Agent Substrate 是 AI Agent 基础设施中「多租户超卖」路线的唯一代表——它不追求协议标准化（OpenSandbox）或凭据注入（OpenShell）或 GPU 直通，而是解决一个更基础的经济学问题：Agent 工作负载 95% 时间在等待 LLM 回复，K8s Pod 却占着 CPU/内存不放。Substrate 用 gVisor 的 checkpoint/restore 实现亚秒级 actor 挂起/恢复，将 250 个 Agent 会话复用到 8 个 Pod 上（30:1）。在 Agent Sandbox 生态中，它是唯一将「密度」作为核心指标的方案——目标 10 亿 actor/集群、100ms 激活延迟。团队将其作为 Agent 基础设施「从 VM 粒度到会话粒度」范式转变的标志性项目跟踪。

## 项目介绍
> **Kubernetes 之上的 Agent 专用调度层——不是又一个沙箱，而是一个让沙箱里的 Agent 可以随时"冻住→存盘→让出位置→下次唤醒"的多租户复用系统。**

核心场景：
- **高密度 Agent 托管**：数百个 Agent 会话（Claude Code、Codex、LangChain、ADK）复用少量物理 Pod，利用 Agent I/O 等待的空闲时间做超卖
- **即时会话恢复**：用户关掉终端，下次打开时 Agent 在**任何节点**上亚秒级恢复，保留完整内存和文件系统状态
- **沙箱化 MCP Server**：部署安全沙箱化的 MCP Server 作为 Substrate Actor，为 LLM 提供持久化工具
- **批量 Agent 评测/训练**：大规模创建和销毁 Agent 会话，利用快照做快速重置

## 技术要点
- **Actor→Worker 超卖核心机制**：利用 gVisor 的 `runsc checkpoint`（冻结进程树 + 保存内存/磁盘快照到 GCS）和 `runsc restore`（从快照恢复），将 actor 生命周期与 Pod 生命周期解耦。Worker Pod 是长期运行的"插座"，actor 是随时可插拔的"插头"。当 actor 空闲时 checkpoint→释放 worker→下一个 actor 用这个 worker restore。激活延迟目标 100ms（绕过 K8s scheduler）
- **三层组件架构**：控制面 `ate-api-server`（gRPC + Redis/ValKey state store，管理 actor↔worker 映射）+ 节点层 `atelet` DaemonSet（管理本节点 worker Pod 池，流式传输快照）+ Pod 内 `ateom`（每个 sandbox 类型一个 herder 镜像，执行 RunWorkload/CheckpointWorkload/RestoreWorkload）
- **Agent 感知路由**：`atenet-router`（Envoy + ext_proc 外部处理器）拦截 HTTP 请求，从 Host header 提取 actor 名，调控制面 ResumeActor，获得 worker IP 后通过 mTLS tunnel 转发到 `atunnel`→actor。请求可以 park 在路由器等待 worker 释放，而非返回 503
- **双模态状态存储**：CRD（WorkerPool/ActorTemplate，低频声明式，走 K8s API） + Redis（Actor/Worker 实时状态，高频操作，走控制面专用存储）。K8s API server 完全不在热路径上
- **快照生命周期**：golden snapshot（首次运行的模板快照）→ memory snapshot（RAM） + working volume（磁盘写层）。支持 Data scope（含持久化目录，microVM 下 host-backed）和 S3/GCS 持久化
- **Defense-in-Depth 安全**：gVisor 内核级隔离 + Actor 独立身份 + 统一 DNS 路由鉴权 + mTLS 全内部通信
- **框架无关 OCI 容器**：任何 OCI 镜像可注册为 ActorTemplate。已有 ADK / LangChain / Claude Code / Codex / MCP Server 的集成案例

## 技术栈
Go (408 .go files), Kubernetes (CRDs + controller-runtime), gVisor (runsc checkpoint/restore), Redis/ValKey (state store), Envoy (ext_proc), GCS/S3 (snapshot storage), protobuf/gRPC, mTLS, Apache 2.0

## 关联
- [`opensandbox-group/OpenSandbox`](../OpenSandbox/) — 竞品/互补：OpenSandbox 做通用沙箱协议+多语言SDK，Substrate 做沙箱之上的多租户调度层。理论上可以叠用
- [`NVIDIA/OpenShell`](../OpenShell/) — 竞品：同为 K8s 上 Agent 运行时，OpenShell 做凭据网关+GPU，Substrate 做密度+快照
- [`kubernetes-sigs/agent-sandbox`](../agent-sandbox/) — 互补：K8s 原生 Agent 沙箱，Substrate 可作为其上层调度器
- [gVisor](https://gvisor.dev) — 核心依赖，checkpoint/restore 是 Substrate 超卖的基石
- [Kata Containers](https://katacontainers.io/) — microVM sandbox class 的底层
- [kagent](https://kagent.dev) — 生态集成项目，演示 Substrate 的完整用法

## 开放问题
- [ ] 2026-08-03 目前 snapshot 仍绑定特定 ActorTemplate 版本（代码版本与内存快照耦合），如何实现跨版本快照兼容？这直接决定能否在不停服的情况下滚动升级
- [ ] 2026-08-03 快照的数据局部性（data locality）问题尚未解决——actor 的最新鲜快照在哪个节点，请求就该路由到哪，或者需要快速迁移。目前的全局 GCS 方案高延迟
- [ ] 2026-08-03 microVM 的 `userfaultfd` 内存按需分页在生产负载下的性能和稳定性如何？gVisor 的 `--allow-connected-on-save` workaround 是否会在未来版本成为正式特性？
- [ ] 2026-08-03 控制面自身的高可用尚未设计——ate-api-server 挂了之后，所有 actor 激活都会失败
