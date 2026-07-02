# agno

> [`agno-agi/agno`](https://github.com/agno-agi/agno) · 上游贡献 · 全栈 Agent 平台 SDK，以控制面统一管理多 Agent 的生命周期，内置 100+ 工具集成和多租户支持

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Agno 是 Agent 生态中的「平台型」框架——不同于 LangChain/CrewAI 聚焦 Agent 开发体验，Agno 关注 Agent 平台运维：多租户隔离、RBAC 权限、审计日志、内置 Cron 调度、100+ 生产即用工具。如果你要构建一个对外的 Agent 服务平台（类似 ChatGPT 的 GPTs 商店），Agno 提供了完整的控制面基础设施。团队关注 Agent-as-a-Service 的架构模式。

## 项目介绍
> **构建 Agent 服务平台的全栈 SDK——开箱即用的多租户、权限控制、定时调度和 100+ 工具集成。**

核心场景：
- **Agent 服务平台**：多租户、多用户 Agent 平台，支持 JWT + RBAC 权限隔离，每个用户拥有独立 Agent
- **生产级工具集成**：100+ 即用工具（Slack、Google Drive、维基百科、MCP 等），降低集成成本
- **跨渠道 Agent**：一套 Agent 定义，通过 Slack/Telegram/WhatsApp/Discord 等多渠道同时暴露
- **定时 Agent 自动化**：内置 Cron 调度器，Agent 可按计划自动执行任务，无需外部基础设施
- **自带可观测性**：OpenTelemetry 追踪 + 审计日志，满足企业合规要求

## 技术要点
- **控制面架构**：核心 Agent 逻辑与平台能力（认证、调度、监控）分离，用户只需定义 Agent 行为
- **用户自有数据库**：会话、记忆、知识库、追踪数据均存储在用户数据库而非 Agno 托管，保证数据主权
- **Cron 调度器**：Agent 任务以 Cron 表达式定义，框架自动在后台执行，不依赖 K8s CronJob 或外部调度器
- **Multi-Agent 会话管理**：支持 Agent 间会话上下文共享和多轮对话状态保持
- **部署无关**：Docker 一键部署，支持 Railway / AWS / GCP 等任意容器环境
- **多协议支持**：AG-UI（前端协议）+ A2A（Agent-to-Agent 协议）+ MCP（工具协议）全覆盖
- **Python 原生**：纯 Python 实现，`pip install agno` 即可，无外部服务依赖

## 技术栈
Python, OpenTelemetry, MCP, A2A, Docker, PostgreSQL, Apache 2.0

## 关联
- [`crewAIInc/crewAI`](../crewAI/) — CrewAI 偏开发体验，Agno 偏平台运维
- [`modelcontextprotocol/modelcontextprotocol`](../../agent-runtime/protocol/modelcontextprotocol/) — MCP 工具接入
- [`a2aproject/A2A`](../../agent-runtime/protocol/A2A/) — Agent 间通信协议

## 开放问题
- [ ] 2026-07-02 控制面架构是否支持跨集群 Agent 调度？在大规模多租户下的状态隔离机制是否成熟？
