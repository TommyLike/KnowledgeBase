# agent-sandbox

> [`kubernetes-sigs/agent-sandbox`](https://github.com/kubernetes-sigs/agent-sandbox) · 上游贡献 · Kubernetes SIG 维护的 Agent 安全沙箱规范与实现，定义 Agent 在 K8s 上安全执行代码的标准接口和隔离策略

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Go · 3,891n/14,401e  
<!-- END AUTO -->

---

## 定位
> Agent Sandbox 是 Kubernetes 社区对「Agent 需要安全执行代码」这一需求的官方回应。作为一个 kubernetes-sigs 项目，它正在定义 Agent 沙箱在 K8s 上的标准 CRD 和行为规范。在 Agent 基础设施中，Agent Sandbox 是 K8s 原生沙箱方案的代表——用 K8s 的 Pod Security + RuntimeClass + Kata/gVisor 实现不同安全等级的 Agent 执行环境。

## 项目介绍
> **Kubernetes 原生的 Agent 安全沙箱——定义 Sandbox CRD，用 K8s 内置隔离机制为 Agent 提供分级代码执行环境。**

核心场景：
- **K8s 上 Agent 代码安全执行**：Agent 在 Sandbox CRD 定义的隔离 Pod 中执行代码
- **多安全等级沙箱**：container（共享内核）、microVM（Kata/gVisor/Firecracker）、VM 三档隔离等级
- **GitOps 管理沙箱策略**：沙箱安全策略以 Git 中的 YAML 文件定义

## 技术要点
- **Sandbox CRD**：定义 Agent 沙箱的资源配置、安全策略、运行时类型（container/vm/microvm）
- **RuntimeClass 集成**：通过 K8s RuntimeClass 选择不同的沙箱运行时（Kata/gVisor/Firecracker）
- **超时与资源配额**：内置执行超时和 CPU/RAM 限制，防止 runaway Agent
- **网络隔离**：沙箱 Pod 可选与集群网络完全隔离或仅允许特定出站

## 技术栈
Go, Kubernetes CRD, RuntimeClass, Kata Containers/gVisor, Apache 2.0

## 关联
- [`e2b-dev/infra`](../../sandbox/infra/) — 竞品，E2B API 式沙箱
- [`firecracker-microvm/firecracker`](../../../agent-infra/firecracker/) — 底层 microVM 引擎
- [Kata Containers](https://katacontainers.io) — K8s 安全容器运行时

## 开放问题
- [ ] 2026-07-02 Sandbox CRD 规范是否会被采纳为 K8s 上游标准？社区共识程度如何？
