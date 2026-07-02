# composio

> [`ComposioHQ/composio`](https://github.com/ComposioHQ/composio) · 上游贡献 · Agent 工具集成平台，提供 200+ 预配置认证工具，一次集成让 Agent 通过自然语言调用 Gmail/Slack/GitHub/Salesforce 等 SaaS API

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · TypeScript · 9,676n/30,586e  
<!-- END AUTO -->

---

## 定位
> Composio 解决 Agent 工具集成中最繁琐的问题——认证和权限管理。在 Agent 生态中，工具调用的用户体验瓶颈不是「Agent 能不能理解 API」，而是「使用者如何安全地授权 Agent 访问自己的 Gmail/GitHub/Notion」。Composio 提供了一个标准化的 Managed Auth 层：Agent 框架只需调用 Composio API，认证、Token 刷新、权限范围管理全部由 Composio 处理。团队关注 Agent 工具集成层的标准化和安全性。

## 项目介绍
> **Agent 的工具「应用商店」——200+ 预认证 SaaS 工具，OAuth 流自动化，Agent 即插即用。**

核心场景：
- **SaaS 自动化 Agent**：Agent 自动读邮件（Gmail）→ 在日历找空档（Google Calendar）→ 创建任务（Jira）→ 发通知（Slack）
- **代码管理 Agent**：Agent 读 PR（GitHub）→ 跑 CI（GitHub Actions）→ 更新文档（Notion）→ 合并后通知（Discord）
- **多工具 Agent 编排**：一个 Agent 同时连接 10+ SaaS 工具，用户只需在 Composio 中做一次授权
- **企业 Agent 工具治理**：管理员在 Composio 中统一配置每个 Agent 可访问的工具和操作

## 技术要点
- **Managed Auth 托管认证**：支持 OAuth2 / API Key / Basic Auth / JWT 等 7 种认证方式，自动处理 Token 刷新、过期和撤销
- **200+ 预配置工具**：Gmail / Slack / GitHub / Salesforce / Jira / Notion / Linear / Discord 等，每个工具的 API 已封装为标准 Tool 接口
- **Action 级别权限控制**：不是「给 Agent Gmail 访问权」，而是「给 Agent Gmail 的 read 权限但不给 send 权限」
- **多框架兼容**：LangChain / CrewAI / AutoGen / OpenAI / Anthropic Tool Use / LangGraph 等所有主流框架
- **Managed Execution Env**：工具调用在 Composio 管理的环境中执行，VPC 隔离，支持审计日志
- **Trigger 事件订阅**：Agent 可订阅外部事件（如收到新邮件、新 Issue 创建），事件触发时自动调用 Agent

## 技术栈
TypeScript, Python, OAuth2, 200+ SaaS API 集成, PostgreSQL, Apache 2.0

## 关联
- [`browser-use/browser-use`](../browser-use/) — Browser-Use 是 Composio 上的高频工具，用于网页操作
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — LangChain Tool 集成，Composio 提供 Managed Auth 的 Tool
- [`microsoft/autogen`](../../../agent-framework/autogen/) — AutoGen 的推荐工具集成平台
- [`crewAIInc/crewAI`](../../../agent-framework/crewAI/) — CrewAI 的默认工具提供源

## 开放问题
- [ ] 2026-07-02 Managed Auth 在自托管场景下的安全性如何保证？Token 存储和加解密的密钥管理机制是怎样的？
