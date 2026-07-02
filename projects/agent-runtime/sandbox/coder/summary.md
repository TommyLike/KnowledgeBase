# coder

> [`coder/coder`](https://github.com/coder/coder) · 上游贡献 · 面向开发团队的自托管远程开发平台，将开发环境迁移到云端，通过 Terraform 模板在 K8s/Docker/VM 上按需创建隔离的 Agent 工作空间

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Coder 是「开发环境即代码」理念的实践者——将开发环境从本地机器迁移到云端，用 Terraform 模板定义工作空间，实现开发环境的按需创建、销毁和计费。在 Agent 基础设施中，Coder 的方案直接适用于 Agent 沙箱：为每个 Agent 实例创建隔离的云上执行环境（IDE + Terminal + 文件系统），Agent 在受控环境中执行代码。

## 项目介绍
> **将开发环境搬到云上——开发者打开浏览器就有完整 Linux 环境，Agent 获得独立隔离的工作空间。**

核心场景：
- **远程开发环境**：开发者浏览器打开 VS Code/JetBrains/SSH，背后是云上 Linux 工作空间
- **Agent 隔离执行环境**：每个 Agent 获得独立 Coder 工作空间（CPU/RAM/Disk 配额），Agent 代码在隔离环境中运行
- **按需环境创建**：新成员入职自动创建标准化开发环境，离职自动销毁
- **Terraform 模板化**：工作空间定义以代码形式存储在 Git，版本管理和复用

## 技术要点
- **Terraform Provider**：工作空间以 Terraform 资源配置，支持 K8s/Docker/GCP/AWS/Azure 等 Provider
- **Web IDE 集成**：内嵌 code-server (VS Code) 和 JetBrains Gateway 集成
- **资源配额与自动休眠**：每个工作空间设定 CPU/RAM/Disk 配额，空闲自动休眠节省成本
- **Dotfiles 个性化**：启动时自动应用个人配置文件，环境个性化但模板化创建

## 技术栈
Go, TypeScript, Terraform, K8s/Docker, code-server, PostgreSQL, AGPL/Enterprise

## 关联
- [`e2b-dev/infra`](../../sandbox/infra/) — 竞品/互补，E2B 偏 Agent 沙箱 API，Coder 偏开发者工作空间
- [`coder/coder`](https://github.com/coder/coder) — 同类产品，Gitpod / GitHub Codespaces

## 开放问题
- [ ] 2026-07-02 Coder 的工作空间启动延迟（冷启动 ~30s-2min）是否能满足 Agent 快速弹性伸缩的需求？
