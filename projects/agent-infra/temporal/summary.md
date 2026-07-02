# temporal

> [`temporalio/temporal`](https://github.com/temporalio/temporal) · 上游贡献 · 持久化执行平台，让开发者像写单机程序一样写分布式应用

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> Temporal 是当前业界最成熟的持久化执行（Durable Execution）平台，由 Uber Cadence 团队核心成员创立。在 Agent 生态中，Temporal 是 Agent 工作流编排的基石：它提供故障自动恢复、状态持久化、长时运行管理等能力，让 Agent 开发者无需手动处理重试逻辑、状态恢复和分布式事务协调。OpenAI、NVIDIA、Cloudflare 等头部公司均在生产环境使用 Temporal 编排 AI Agent 和 MCP 管道。

## 项目介绍
> **Temporal 是一个开源的持久化执行引擎，自动处理工作流的故障恢复、重试和状态持久化，让开发者可以编写"仿佛故障不存在"的可靠分布式应用。**

核心场景：
- **AI Agent 与 MCP 管道编排**：编排多步 LLM 调用、工具执行和人工审批的 Agent 工作流，每个步骤自动重试，状态持久化保证 Agent 不会因中间故障丢失进度
- **人机协同（Human-in-the-Loop）**：支持在工作流中等待人工审批或输入，工作流可以暂停数天甚至数周后继续执行
- **长时运行业务流程**：订单履约、用户注册、数据迁移等跨服务、跨天数的业务流程编排，自动处理服务中断和超时
- **Saga 分布式事务**：以 try...catch 模式的补偿事务替代复杂的分布式事务协调代码，自动执行回滚和补偿操作
- **CI/CD 管道**：为部署流水线提供可靠的重试、回滚和可观测性，替代脆弱的 Shell 脚本编排

## 技术要点
- **Workflow + Activity 编程模型**：Workflow 是业务逻辑的确定性函数（支持 Go/Java/Python/TypeScript/.NET 等 SDK），Activity 是与外部世界交互的非确定性操作（API 调用、数据库写入等）。Temporal 将 Workflow 的执行状态自动持久化，确保即使服务器宕机也能从中断点恢复
- **事件溯源（Event Sourcing）架构**：所有 Workflow 的状态变更记录为不可变事件历史，Worker 崩溃后重建时通过重放（Replay）事件历史恢复状态，无需额外的检查点或快照机制
- **多服务架构**：Frontend（gRPC 网关）→ History（状态管理与事件持久化）→ Matching（任务分发队列）→ Worker（业务逻辑执行），各服务独立扩展
- **任务队列与负载均衡**：Workflow 和 Activity 任务通过命名队列分发，Worker 按队列拉取任务，支持按场景隔离资源和动态扩缩容
- **可配置重试策略**：每个 Activity 可独立配置初始重试间隔、最大重试次数、退避系数、不可重试异常类型等，支持指数退避和自定义重试条件
- **多租户与命名空间隔离**：通过 Namespace 实现多团队、多环境的完全隔离，每个命名空间有独立的保留策略、吞吐配额和访问控制
- **Web UI 与全链路可观测性**：内置 Web 控制台可查看每个 Workflow 的完整执行历史、当前状态、输入输出和错误信息，无需翻查日志
- **多后端持久化**：支持 Cassandra 和 SQL（MySQL/PostgreSQL）两种持久化后端，Cassandra 适合超大规模部署，SQL 适合中小规模运维简化
- **本地开发体验**：提供 temporal server start-dev 一键启动嵌入式开发服务器，无需部署复杂基础设施即可开始开发
- **Cloud 托管模式**：Temporal Cloud 提供全托管服务，代码仍在用户侧执行，Temporal 只持久化状态而看不到业务代码

## 技术栈
Go, Protocol Buffers, gRPC, Cassandra, MySQL/PostgreSQL

## 关联
- [`restate`](../restate/) — 同为持久化执行平台，Restate 更偏函数式编程模型，Temporal 更重编排
- [`inngest`](../inngest/) — 事件驱动的持久化执行，面向 Event-Driven 场景的轻量级替代
- [`trigger.dev`](../trigger.dev/) — 面向特定触发场景的工作流引擎，与 Temporal 有部分场景重叠

## 开放问题
- [ ] 2026-07-02 Temporal 在 Agent 场景的 Workflow 确定性约束（不能直接调用 LLM SDK，必须通过 Activity 包装）是否增加了开发复杂度？
- [ ] 2026-07-02 与 Restate 相比，Temporal 的 History 事件量级是否在超大规模 Workflow（百万级）场景下成为存储瓶颈？
