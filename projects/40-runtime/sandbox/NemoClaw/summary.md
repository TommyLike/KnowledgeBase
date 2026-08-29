# NemoClaw

> 快照: 首次录入 `2026-07-05` | 无 codebase 数据 | Stars: 21521

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

NVIDIA 开源的 Agent 安全运行时环境，用于在 NVIDIA OpenShell 内安全运行 Hermes、OpenClaw 等 AI Agent。属于团队上游贡献范畴，关注其 sandbox 安全隔离机制和 agent 运行时架构设计。

## 项目介绍

NemoClaw 是 NVIDIA 推出的 Agent 执行沙箱，将 Agent 进程隔离在 OpenShell 容器环境中运行，提供文件系统隔离、网络访问控制、权限审计等安全能力，确保 Agent 在受控环境下执行敏感操作。

## 核心场景

- **企业 Agent 安全部署**：在合规要求严格的企业环境中安全运行 AI Agent，满足审计和安全策略需求
- **Agent 多租户隔离**：在同一主机上同时运行多个 Agent 实例，彼此间通过 OpenShell 容器实现进程和文件系统隔离
- **敏感操作审计**：对 Agent 的所有文件读写、网络请求、系统调用进行日志记录和事后审计
- **CI/CD 集成**：在 CI/CD 流水线中安全运行 Agent 驱动的自动化任务（代码审查、发布检查等），不暴露宿主机凭证

## 技术要点

- **OpenShell 沙箱**：基于 NVIDIA OpenShell 容器技术实现轻量级进程隔离，启动开销远小于传统虚拟机
- **细粒度权限控制**：支持按文件路径、网络地址、系统调用维度的 Agent 权限白名单策略
- **Agent 运行时生命周期管理**：统一的 Agent 启动、监控、优雅关闭和异常恢复机制
- **凭证注入**：通过加密通道向沙箱内 Agent 注入临时凭证，凭证不落盘，防止泄露
- **可观测性**：内置 Agent 行为遥测（prompt/response 日志、工具调用追踪、token 用量统计）
- **与 Hermes/OpenClaw 协议兼容**：原生支持主流 Agent 框架的 API 协议，无需修改 Agent 代码即可接入沙箱

## 技术栈

- 语言：Python（优先级高）、Rust（沙箱底层组件）
- 容器运行时：NVIDIA OpenShell
- 通信协议：gRPC、HTTP/2
- 认证：OAuth 2.0 + 短期令牌

## 关联

- 上游依赖：NVIDIA OpenShell（容器运行时）、NVIDIA NGC（基础镜像）
- 生态位置：与 Anthropic MCP、OpenAI Agents SDK 等 Agent 框架互补——NemoClaw 提供底层的安全执行环境，上层可接入任意 Agent 协议
- 竞品/参照：Docker-based agent sandboxing、gVisor、Firecracker microVM 方案

## 开放问题

- OpenShell 容器的安全边界具体实现了哪些 syscall 过滤器？与 gVisor/seccomp 的综合对比如何？
- NemoClaw 在生产环境（尤其是多租户 GPU 集群中）的规模化部署方案是什么？
- 与 NVIDIA AI Enterprise 产品线的集成计划——是否会被吸收为企业产品的安全模块？
