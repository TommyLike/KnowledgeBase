# 80-workflow · 工作流 / 消息


> **MOC 导览页** · 本层 7 个项目 · [↑ 返回栈总览](../README.md)

把 Agent 的多步任务变成**可靠、可重放、可恢复**的工作流：持久化执行引擎（temporal/restate）、事件与消息中枢（nats/redpanda）。解决"长时任务中途挂了怎么办"。

## 项目（7）

- [`inngest--inngest`](inngest/) — agent
- [`nats-io--nats-server`](nats-server/) — agent
- [`redpanda-data--redpanda`](redpanda/) — agent
- [`restatedev--restate`](restate/) — agent
- [`temporalio--temporal`](temporal/) — agent
- [`triggerdotdev--trigger.dev`](trigger.dev/) — agent
- [`wagoodman--dive`](dive/) — container、image、analysis
