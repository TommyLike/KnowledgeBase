# NVIDIA/OpenShell

> 定位：NVIDIA 开源的 AI Agent 安全沙箱运行时，为自主 AI Agent 提供隔离、安全的代码执行环境。团队作为上游贡献者参与，关注其沙箱隔离机制、Agent 工具集成模式和运行时安全模型。

## 项目介绍

OpenShell 是 NVIDIA 推出的用于自主 AI Agent 的安全私有运行时。它提供了一套完整的沙箱环境，使 AI Agent 可以在隔离的容器中安全执行代码、访问文件系统和调用外部工具，同时确保宿主环境不受恶意或错误操作的影响。与传统的 CI/CD runner 或简单的 Docker 封装不同，OpenShell 专为 AI Agent 的工作流设计，内置了权限控制、资源限制和审计追踪能力。

## 核心场景

- **AI Agent 代码执行沙箱**：为 LLM 生成的代码提供安全隔离的执行环境，防止恶意代码或误操作影响宿主系统。
- **多 Agent 协作隔离**：在多个自主 Agent 并行工作时，为每个 Agent 分配独立的沙箱实例，确保互不干扰且数据隔离。
- **工具调用安全网关**：Agent 通过 OpenShell 调用 Shell 命令、文件操作、网络请求等，所有操作经过权限校验和审计记录。
- **本地私有部署**：支持完全本地运行，数据不出用户机器，满足隐私敏感场景（如企业代码库操作、个人文件处理）的需求。

## 技术要点

- **沙箱隔离机制**：基于容器技术（如 Docker/Podman）实现进程级隔离，可选 gVisor/Firecracker 等更强隔离方案，提供多层次的安全边界。
- **权限模型**：细粒度的 Capability 权限控制，Agent 只能执行预先授权的操作（文件读写白名单、网络访问策略、命令黑名单等），支持动态权限提升的用户确认流程。
- **Agent 协议集成**：支持 MCP（Model Context Protocol）和自定义工具协议，Agent 框架（如 LangChain、CrewAI、AutoGen）可通过标准接口接入 OpenShell 运行时。
- **审计与可观测性**：完整的操作日志记录，包括执行的命令、文件变更、网络调用等，支持事后审计和实时告警。
- **资源管控**：CPU、内存、磁盘 IO 和网络带宽的配额限制，防止单个 Agent 资源滥用影响整体系统稳定性。
- **跨平台支持**：支持 Linux、macOS（实验性）和 WSL2，覆盖开发者和生产环境的主要平台。

## 技术栈

- **语言**：Go / TypeScript (CLI/SDK)
- **容器运行时**：Docker / Podman / containerd
- **沙箱技术**：gVisor（可选）/ Firecracker（可选）
- **协议**：MCP（Model Context Protocol）、gRPC、REST API
- **构建**：Go modules、npm

## 关联

- **上游**：基于容器生态（Docker/containerd）构建，参考了 gVisor、Firecracker 等沙箱方案的设计思路。
- **同类项目**：E2B（AI Agent 沙箱平台，商业化竞品）、Anthropic Computer Use（浏览器沙箱方案）、Morph Labs（Agent 托管平台）。
- **下游集成**：可被 LangChain、CrewAI、AutoGen、MetaGPT 等 Agent 框架作为执行后端调用。

## 开放问题

- OpenShell 的生产环境安全边界是否经过第三方安全审计？在大规模多租户场景下的隔离强度如何？
- 与 E2B 等商业化竞品相比，OpenShell 在性能开销和启动延迟方面的表现如何？
- NVIDIA 对该项目的长期投入规划是什么？是否有商业化计划或仅作为 NVIDIA AI 生态的基础设施组件？
- Windows 原生支持的时间表如何？当前仅支持 WSL2 是否限制了企业 Windows 用户的采用？

<!-- BEGIN AUTO -->
<!-- END AUTO -->
