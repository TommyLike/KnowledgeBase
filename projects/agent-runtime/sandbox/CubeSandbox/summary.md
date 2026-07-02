# CubeSandbox

> [`TencentCloud/CubeSandbox`](https://github.com/TencentCloud/CubeSandbox) · 上游贡献 · 腾讯云开源的 Agent 安全沙箱方案，基于轻量级虚拟化为 Agent 提供隔离的代码执行环境

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> CubeSandbox 是腾讯云在 Agent 安全执行领域的开源贡献——与 E2B（Firecracker 路线）和 Agent Sandbox（K8s 路线）形成差异化的云厂商方案。

## 项目介绍
> **腾讯云的 Agent 安全沙箱——为 AI Agent 提供隔离的代码执行环境。**

核心场景：
- **Agent 代码安全执行**：不受信任代码在隔离沙箱中运行
- **多租户 Agent 隔离**：不同用户/团队的 Agent 实例互相隔离

## 技术要点
- **容器安全增强**：基于腾讯云容器技术的高级安全隔离，配合 seccomp/AppArmor 内核安全策略
- **可插拔运行时**：Python/Node.js/Go 等多种执行环境模板，支持自定义 Dockerfile
- **资源配额管理**：每个沙箱独立 CPU/Memory/Disk 配额，超限自动回收

## 技术栈
Go, Kubernetes, Containerd, Apache 2.0

## 关联
- [`e2b-dev/infra`](../../sandbox/infra/) — 竞品，Firecracker 路线
- [`kubernetes-sigs/agent-sandbox`](../../sandbox/agent-sandbox/) — 竞品，K8s 官方方案
- [腾讯云](https://cloud.tencent.com) — 发起方

## 开放问题
- [ ] 2026-07-02 与腾讯云基础设施的绑定程度？是否支持独立部署？
