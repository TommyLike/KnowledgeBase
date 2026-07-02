# hindsight

> [`vectorize-io/hindsight`](https://github.com/vectorize-io/hindsight) · 上游贡献 · 面向事件溯源和时序数据的持久化存储引擎，为 Agent 的动作历史和决策轨迹提供不可变的事件日志

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Hindsight 是 Vectorize 推出的持久化事件日志引擎，灵感来自 Event Sourcing 架构模式。在 Agent 基础设施中，Hindsight 可以扮演 Agent 的「审计日志」和「决策溯源」角色——Agent 执行的每一步操作以不可变事件记录，可追溯任意时间点的 Agent 状态和决策路径。

## 项目介绍
> **Agent 的不可变操作日志——每次 LLM 调用、工具使用和状态变更以 Event 形式永久记录。**

核心场景：
- **Agent 决策溯源**：回溯 Agent 为何在特定时刻做了特定决策
- **审计与合规**：Agent 操作的全量不可变事件日志
- **状态重建**：Agent 崩溃后通过事件重放恢复完整状态

## 技术要点
- **Event Sourcing 模式**：所有状态变更以事件序列而非 CRUD 记录
- **时序索引**：按时间范围快速检索事件
- **不可变存储**：事件写入后不可修改或删除

## 技术栈
Python, Event Sourcing, Apache 2.0

## 关联
- [Vectorize.io](https://vectorize.io) — 同一团队，RAG 平台
- [`temporalio/temporal`](../../../agent-infra/temporal/) — 工作流引擎，也有事件历史但面向 Workflow

## 开放问题
- [ ] 2026-07-02 不可变事件日志的存储膨胀如何控制？大量 Agent 操作下的事件保留策略？
