# agentcube

> [`volcano-sh/agentcube`](https://github.com/volcano-sh/agentcube) · 上游贡献 · Kubernetes 批量调度系统的 Agent 沙箱方案，以 Volcano 调度能力为 Agent 提供 GPU/CPU 混合资源管控

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> AgentCube 是 Volcano（CNCF K8s 批量调度项目）生态中的 Agent 沙箱方案，将 Volcano 的批量调度和资源管理能力应用于 AI Agent 场景。在 Agent 运行时生态中，AgentCube 代表「K8s 批量调度的 Agent 沙箱」路线。

## 项目介绍
> **用 Volcano 批量调度能力为 Agent 提供弹性沙箱——GPU/CPU 混合资源管控 + K8s 原生调度。**

核心场景：
- **GPU Agent 沙箱**：为需要 GPU 的 Agent（LLM 推理）提供 GPU 资源隔离的沙箱环境
- **批量 Agent 任务调度**：多个 Agent 任务的优先级调度、排队和资源分配
- **K8s 原生 Agent 部署**：与 K8s 生态（Volcano、Kuberay）原生集成

## 技术要点
- **Volcano 调度集成**：基于 CNCF Volcano 的 gang-scheduling 和公平调度
- **GPU/CPU 混合资源管理**：支持 GPU 显存分配和 CPU 内存联合配额
- **K8s CRD 管理**：以 K8s 自定义资源定义 Agent 沙箱生命周期

## 技术栈
Go, Kubernetes, Volcano, Apache 2.0

## 关联
- [Volcano](https://volcano.sh) — 上游 K8s 批量调度系统
- [`kubernetes-sigs/agent-sandbox`](../agent-sandbox/) — K8s 官方 Agent 沙箱方案
- [`openkruise/agents`](../agents/) — 同类 K8s Agent 沙箱方案

## 开放问题
- [ ] 2026-07-05 AgentCube 的 GPU 沙箱隔离粒度是否能做到进程级？还是只能做到容器级？
