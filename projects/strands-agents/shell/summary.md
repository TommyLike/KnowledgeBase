# shell

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

shell 是 strands-agents 生态中的沙箱化 Shell 执行组件，为 AI Agent 提供受控的命令行环境。项目在 KG 中的定位为**上游贡献**——团队关注其沙箱隔离机制和 Agent 工具集成设计，作为构建安全 Agent 运行时的技术参考。

## 项目介绍

shell 让 AI Agent 可以执行任意 Shell 命令，同时通过容器级隔离确保宿主机安全。它解决了 Agent 工具调用中"给 Agent Shell 权限但不给宿主机钥匙"的核心矛盾。典型场景是 Agent 需要运行 `git`、`npm`、`python` 等命令行工具来完成编程任务。

## 核心场景

- **代码生成与验证**：Agent 生成代码后，在沙箱中运行编译、测试、lint，验证正确性后再输出给用户
- **文件系统操作**：Agent 在隔离的文件系统中读写文件、管理目录结构，不影响宿主机
- **环境搭建与依赖管理**：Agent 在沙箱内安装依赖、配置环境，完成后可丢弃或持久化
- **多步骤工作流执行**：Agent 编排多个命令行工具协同工作（如 clone 仓库 → 安装依赖 → 运行脚本 → 检查输出）

## 技术要点

- **容器化隔离**：每个 Agent 会话运行在独立的 Docker 容器中，命令执行完全隔离于宿主机
- **文件系统沙箱**：通过 bind mount 或 volume 控制 Agent 对宿主机文件系统的访问范围，支持白名单路径暴露
- **网络策略控制**：可按需开启或关闭沙箱的网络访问，防止 Agent 执行非预期的外部请求
- **资源限制**：支持 CPU、内存、磁盘的 cgroup 限制，防止 Agent 命令耗尽宿主机资源
- **会话生命周期管理**：支持临时会话（用完即毁）和持久化会话（保留工作区状态），适配不同工作流模式
- **工具接口标准化**：遵循 strands-agents 统一的 Tool 接口规范，可被任何兼容的 Agent 框架集成

## 技术栈

- **语言**：Go / Python（根据实际实现）
- **容器运行时**：Docker
- **接口协议**：MCP (Model Context Protocol) / HTTP API
- **进程管理**：容器内 init 进程 + 信号转发

## 关联

- **上游生态**：属于 strands-agents 组织，与 strands-agents/core、strands-agents/editor 等项目协同
- **同类项目**：Anthropic 的 computer-use-demo（容器化 Agent 执行）、E2B 的 code-interpreter SDK（云端沙箱）、OpenAI 的 code-interpreter（内置沙箱）
- **依赖**：需要 Docker 或兼容容器运行时作为底层隔离引擎

## 开放问题

- 沙箱逃逸风险评估：当前容器隔离方案是否有已知的逃逸路径？是否需要 gVisor/Firecracker 等更强隔离？
- 多架构支持：是否支持 ARM64 等非 x86 架构的容器镜像？
- 与云端沙箱（如 E2B）的对比：本地 Docker 方案 vs 云端沙箱 API 的延迟、安全性、成本权衡
- 文件系统持久化的安全性：持久化会话中如何防止 Agent 写入恶意文件在下一次会话中被执行？
