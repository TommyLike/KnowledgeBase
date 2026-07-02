# inngest

> [`inngest/inngest`](https://github.com/inngest/inngest) · 上游贡献 · 事件驱动的持久化函数执行引擎，让开发者在无运维负担的情况下构建可靠的多步骤异步工作流

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Inngest 是持久化执行（Durable Execution）领域的云原生选手——与 Temporal 和 Restate 同赛道，但更侧重「事件驱动 + Serverless 部署」体验。在 Agent 基础设施中，Inngest 可以作为 Agent 的后台任务引擎：用户触发 Agent 任务 → Inngest 管理多步骤执行、重试、延迟和事件等待。团队关注其事件驱动的 Step Function 模型在 Agent 工作流中的适用性。

## 项目介绍
> **用事件和函数构建可靠工作流——定义事件触发函数，Inngest 自动处理重试、流控和故障恢复。**

核心场景：
- **多步骤 Agent 工作流**：Agent 需求分析 → 代码生成 → 测试 → 部署，每一步是 Inngest Step，自动重试和恢复
- **事件驱动编排**：Webhook 触发 → 数据清洗 → LLM 调用 → 结果存储，失败时自动重试或人工介入
- **延迟执行**：Agent 设定定时任务，Inngest 按时触发执行，支持从秒级到天级的延迟
- **并行 Fan-Out**：Agent 同时对多个源进行搜索，结果汇总后继续下一步流程
- **人工审批流**：Agent 挂起等待审批 → Inngest 持久化等待 → 审批后继续执行

## 技术要点
- **事件驱动模型**：一切以事件为起点，函数通过 `inngest.createFunction()` 订阅特定事件，触发后自动执行多步骤流程
- **Step 持久化**：每个 `step.run()` 的结果自动持久化到 Inngest 的 Event Store，故障恢复后从最后成功步骤继续
- **自动重试与退避**：内置指数退避重试策略，无需手写重试逻辑
- **流控与并发控制**：支持按函数级别的并发限制和速率限制，防止下游 API 过载
- **多语言 SDK**：TypeScript (核心) + Python + Go，主要投资在 TypeScript 生态
- **Serverless 友好**：设计为与 Vercel/Netlify/Cloudflare Workers 等 Serverless 平台原生兼容
- **DevServer 本地开发**：提供本地模拟服务器，开发阶段即可完整测试工作流

## 技术栈
TypeScript, Go (executor), Python, Vercel/Netlify, AWS Lambda, Event Store

## 关联
- [`temporalio/temporal`](../temporal/) — 竞品，Temporal 提供更完整的企业级工作流引擎
- [`restatedev/restate`](../restate/) — 竞品，Restate 提供协议层持久化执行
- [`triggerdotdev/trigger.dev`](../trigger.dev/) — 相似定位，事件驱动工作流 API

## 开放问题
- [ ] 2026-07-02 Inngest 的 Step 模型与 Temporal 的 Workflow 模型在灵活性上的差距是否限制了复杂 Agent 流程的编排？
