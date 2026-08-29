# cwc-long-running-agents

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

Anthropic 官方发布的长时间运行 Agent 参考实现，基于 Claude Computer Use (CWC) 能力构建。该项目展示了如何在沙箱环境中让 Agent 持续工作数小时甚至数天，是本团队在 agent-runtime/sandbox 方向的上游参考项目，用于跟踪 Anthropic 在长时 Agent 工程实践方面的最新进展。

## 项目介绍

cwc-long-running-agents 是 Anthropic 开源的长时间运行 Agent 参考实现，为 Claude 提供计算机使用（computer use）能力的持久化运行框架。项目通过 Docker 沙箱环境让 Claude Agent 可以执行复杂的多步骤任务，支持任务中断恢复、状态持久化和人机协作，目标场景是让 Agent 在隔离环境中自主工作数小时。

## 核心场景

- **长时间自主任务执行**：Agent 在 Docker 沙箱中持续运行，完成需要数小时的复杂工作流程，如代码库分析、数据处理、文档编写等
- **任务中断与恢复**：支持 Agent 在任务执行过程中保存状态，中断后可从中断点恢复继续工作，避免重复劳动
- **人机协作审查**：Agent 完成任务后生成工作产物，人类可在审查阶段介入检查、修正或补充
- **安全隔离执行**：所有 Agent 操作在 Docker 容器沙箱内完成，与宿主机环境隔离，保障安全性

## 技术要点

- **Docker 沙箱隔离**：使用 Docker 容器作为 Agent 执行环境，提供文件系统、网络和进程级别的隔离，确保 Agent 操作不影响宿主机
- **Computer Use 协议**：基于 Claude 的 computer use 能力，Agent 通过截图观察环境、通过模拟键盘鼠标操作与环境交互
- **任务编排与状态管理**：支持将复杂任务拆分为多个子步骤，每个步骤完成后保存检查点，实现断点续传式的工作模式
- **审查与干预机制**：提供人类审查环节，允许在 Agent 完成工作后由人类检查和修改结果，形成 Human-in-the-Loop 工作流
- **配置化任务定义**：任务通过配置文件定义，支持自定义 Agent 行为参数、工具集和环境变量
- **产物输出与归档**：Agent 工作完成后自动将产物（代码、文档、分析报告等）输出到指定目录，便于后续使用

## 技术栈

- **语言**：Python（主要编排逻辑）、Shell（容器启动脚本）
- **容器化**：Docker
- **核心依赖**：Anthropic Claude API（Computer Use）、Anthropic SDK
- **运行环境**：Linux（推荐），macOS 支持有限

## 关联

- **上游**：Anthropic Claude Computer Use 能力、Anthropic SDK
- **同类项目**：OpenAI Codex CLI、SWE-Agent、Devin（均为 Agent 长时间运行方向的参考项目）
- **团队关联**：在本 KG 中归类于 agent-runtime/sandbox 子方向，作为上游参考

## 开放问题

- 长时间运行中 Agent 的上下文窗口管理策略（如何避免上下文膨胀导致性能下降或成本失控）
- 沙箱环境的文件系统持久化方案选择（Volume 挂载 vs 对象存储）
- Computer Use 模式下的操作可靠性（截图识别失败时的重试与降级策略）
- 多 Agent 协作场景下的任务分配与通信机制
