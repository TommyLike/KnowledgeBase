# restate

> [`restatedev/restate`](https://github.com/restatedev/restate) · 上游贡献 · 轻量级持久化执行引擎，将 RPC/REST 调用自动升级为自动重试、故障可恢复的持久化步骤

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Rust · 25,310n/109,087e  
<!-- END AUTO -->

---

## 定位
> Restate 是介于 Temporal（重量级工作流）和纯 RPC（无保障）之间的持久化执行协议实现。在 Agent 基础设施中，Restate 解决「Agent 在调用多个 API 过程中某一步失败时需要可靠恢复」的问题——将 Agent 的每个工具调用和 LLM 请求包装为可恢复的持久化步骤。与 Temporal 不同的是，Restate 以「协议」而非「框架」的方式运行，不需要改写代码为 Workflow 模式。

## 项目介绍
> **让任意 RPC/REST 调用自动获得持久化执行的保障——用 Restate 协议透明地处理重试、恢复和幂等性。**

核心场景：
- **Agent 工具调用可靠性**：Agent 调用搜索 API → 调用数据库 → 调用 LLM 这一多步流程中，前两步成功后第三步失败，Restate 从第三步恢复而非从头开始
- **Long-Running Agent 任务**：Agent 需等待外部事件（人工审批、Webhook）数小时甚至数天，Restate 持久化挂起状态
- **事件驱动 Agent 编排**：通过延迟执行 + 定时唤醒，实现 Agent 的 CronJob 式周期任务
- **微服务 Saga 事务**：Agent 操作多个微服务，某步失败时 Restate 执行补偿操作保证最终一致性
- **Journalling 模式**：每次操作的结果记录到 Journal，恢复时从上次失败的步骤继续

## 技术要点
- **原生持久化协议**：不是 SDK/框架，而是一个协议——服务通过 Restate API 注册，每个 invocation 自动获得持久化 Journal 保障
- **Journal 日志模型**：每步操作记录到 Event Log Journal，重放时根据已完成步骤跳过或补偿
- **Awakeable 机制**：支持 `ctx.sleep()` 等多天级等待，状态持久化到磁盘，不占用线程/内存等昂贵资源
- **非侵入式集成**：支持 HTTP/gRPC SDK 和原生 Lambda 适配器 (TypeScript/Java/Kotlin/Python/Rust/Go)
- **单二进制部署**：Rust 实现，内存占用远低于 Temporal，适合轻量级 Agent 场景中的嵌入部署
- **Virtual Object 模型**：每个对象（如一个 Agent session）有独立持久化状态，支持租约和互斥访问
- **列式后台任务**：支持延迟 callback (`ctx.sleep()`) 和定时唤醒来实现 Agent 的周期触发

## 技术栈
Rust, TypeScript/Java/Kotlin/Python/Go SDK, gRPC, HTTP, RocksDB (storage)

## 关联
- [`temporalio/temporal`](../temporal/) — 竞品/互补，Temporal 是工作流引擎，Restate 是轻量级持久化协议
- [`inngest/inngest`](../inngest/) — 同领域竞品，事件驱动持久化执行
- [`triggerdotdev/trigger.dev`](../trigger.dev/) — 类似的持久化执行平台

## 开放问题
- [ ] 2026-07-02 Restate 的 Journal 模型在大量 Agent 并发场景下，日志恢复性能是否会退化为瓶颈？
