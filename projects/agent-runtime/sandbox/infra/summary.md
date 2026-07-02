# infra

> [`e2b-dev/infra`](https://github.com/e2b-dev/infra) · 上游贡献 · E2B 的 Agent 安全沙箱基础设施，基于 Firecracker microVM 提供 <200ms 启动的隔离代码执行环境

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Go · 19,923n/94,277e  
<!-- END AUTO -->

---

## 定位
> E2B Infra 是 Agent 安全代码执行领域的标杆基础设施——将 Firecracker microVM 封装为 API，让 Agent 在 <200ms 内获得一个硬件级隔离的 Linux 环境来执行任意代码。在 Agent 生态中，E2B 是 Agent Sandbox 的核心玩家：当 Agent 需要执行代码、安装依赖、操作文件时，E2B 提供安全且高性能的沙箱。团队关注其在 Agent 安全执行场景中的性能极限和规模化运维。

## 项目介绍
> **Agent 的安全代码执行沙箱——API 调用即获得独立 Linux VM，任意代码安全运行，<200ms 冷启动。**

核心场景：
- **Agent 代码执行沙箱**：Agent 生成的 Python/Bash 代码在隔离 Firecracker VM 中安全执行
- **多语言运行时**：Python/Node.js/Go/Rust/Java 等预构建环境模板
- **文件系统操作**：Agent 在沙箱内创建/编辑/删除文件，支持文件上传下载
- **交互式 Terminal**：Agent 通过 API 获得完整交互式终端体验

## 技术要点
- **Firecracker 底层**：每个沙箱是独立 Firecracker microVM，KVM 硬件隔离
- **<200ms 冷启动**：通过预构建 rootfs 模板和 VM 快照实现极速启动
- **API 优先**：`sandbox.create()` / `sandbox.runCode()` / `sandbox.process.start()` 等 REST API
- **环境模板**：预构建 Python/Node.js/Bash 等模板，支持自定义 Dockerfile
- **超时与资源限制**：每个沙箱设定 CPU/RAM/执行超时，超限自动终止
- **SDK 多语言**：Python / TypeScript / Go SDK

## 技术栈
Go, Firecracker microVM, KVM, REST API, TypeScript/Python SDK, Docker

## 关联
- [`firecracker-microvm/firecracker`](../../../agent-infra/firecracker/) — 底层虚拟化引擎
- [`coder/coder`](../../sandbox/coder/) — 同类，Coder 偏开发环境，E2B 偏 API 式代码执行
- [`kubernetes-sigs/agent-sandbox`](../../sandbox/agent-sandbox/) — K8s 原生的 Agent 沙箱方案

## 开放问题
- [ ] 2026-07-02 E2B 在 1000+ 并发 Agent 沙箱场景下的调度延迟和 Firecracker 资源碎片化如何优化？
