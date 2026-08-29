# trigger.dev

> [`triggerdotdev/trigger.dev`](https://github.com/triggerdotdev/trigger.dev) · 上游贡献 · 面向 TypeScript 生态的持久化执行平台，以 API 优先的方式为开发者提供可靠的后台任务和工作流编排

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Trigger.dev 是持久化执行领域最「TypeScript 友好」的平台——与 Temporal 的 Java 传统和 Inngest 的通用型定位不同，Trigger.dev 深度绑定 TypeScript/Node.js 生态，提供一流的 Zod 校验、OpenAI SDK 集成和 Next.js 适配。在 Agent 基础设施中，Trigger.dev 让 TypeScript Agent 开发者用最少的代码将 LLM call / API call / 数据库操作编排为可靠的多步骤工作流。

## 项目介绍
> **TypeScript 原生持久化任务平台——用熟悉的 async/await 风格编写多步骤 Agent 工作流，自动获得重试、持久化和可观测性。**

核心场景：
- **Agent 多步骤任务编排**：Research → LLM Summary → Email → Slack Notify 每个步骤自动持久化和重试
- **Webhook 可靠处理**：接收第三方 Webhook → 签名校验 → 数据处理 → 触发下游流程，任何失败自动恢复
- **定时 Agent 任务**：每日/每周定时触发 Agent 执行任务（日报生成、数据采集等）
- **人机协同审批**：Agent 挂起等人工审批 → 审批后自动继续
- **AI SDK 集成**：与 OpenAI / Anthropic / LangChain 的深度 TypeScript 集成，LLM 调用自动重试和超时处理

## 技术要点
- **TypeScript 原生**：工作流以 async/await 风格的 TypeScript 函数编写，Zod schema 校验输入输出
- **持久化执行语义**：每个 task.run() 结果自动持久化，重启后从最后成功步骤继续
- **AI SDK 深度集成**：内置 OpenAI task 类型，LLM 调用自动注入重试/超时/速率限制
- **多触发源**：Webhook / 定时 Cron / 事件订阅 / 手动触发等 5 种以上触发方式
- **Next.js 原生适配**：与 Vercel / Next.js App Router 深度集成，一键部署为 Serverless Function
- **可配置重试策略**：每个步骤独立设置重试次数、退避策略和幂等性保证

## 技术栈
TypeScript, Next.js, Zod, Vercel, OpenAI/Anthropic SDK, PostgreSQL

## 关联
- [`inngest/inngest`](../inngest/) — 同领域竞品，事件驱动持久化执行
- [`temporalio/temporal`](../temporal/) — 竞品，企业级工作流引擎
- [`restatedev/restate`](../restate/) — 竞品，协议层持久化执行

## 开放问题
- [ ] 2026-07-02 深度绑定 TypeScript 生态是否限制了多语言 Agent 团队采用？有 Go/Python SDK 计划吗？
