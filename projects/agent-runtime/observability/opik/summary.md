# opik

> [`comet-ml/opik`](https://github.com/comet-ml/opik) · 上游贡献 · Comet 开源的全栈 LLM 追踪与评估平台，提供从实验追踪到生产监控的完整 Agent 可观测性方案

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Opik 是 Comet（ML 实验管理先驱）在 LLM 时代的可观测性产品。在 Agent 评估生态中，Opik 的差异化在于「从 ML 实验到 LLM 追踪」的全栈连续性——Comet 老用户用 Opik 无缝追踪 LLM 调用，与原有的 ML 实验管理打通。团队关注 ML 可观测性向 LLM 可观测性演进的技术路径。

## 项目介绍
> **从实验到生产全链路——追踪 Agent 的每次 LLM 调用，评估输出质量，监控生产漂移。**

核心场景：
- **Agent Trace 追踪**：Agent 步骤级 LLM 调用全链路追踪，延迟/token/成本可视化
- **LLM 评估**：内置评估器（Hallucination/RAG/Context Relevance 等）自动评分
- **Prompt 版本管理**：Prompt 模板在 Opik 中管理，对比不同版本的效果
- **实验对比**：A/B 测试不同模型/Prompt/参数的结果对比
- **生产监控**：实时采样 Agent 响应评分，检测质量漂移

## 技术要点
- **OpenTelemetry 兼容**：Trace/Log/Metric 基于 OTel 标准，可直接对接现有可观测性栈
- **Python 装饰器自动插桩**：`@opik.track` 一行装饰器即可追踪函数调用和 LLM 交互
- **Thread/Span 模型**：Trace → Thread → Span 三层结构，映射 Agent 的多步调用层次
- **LLM-as-Judge 评估**：自动生成评估数据集并自动执行评分
- **Dashboard + Analytics**：内置可视化面板和 SQL 查询分析

## 技术栈
Python, Java, OpenTelemetry, ClickHouse, MySQL, React, Apache 2.0

## 关联
- [`langfuse/langfuse`](../langfuse/) — 竞品，Langfuse 社区更大，Opik 有 Comet 实验管理继承优势
- [`Arize-ai/phoenix`](../phoenix/) — 竞品，Arize 开源 LLM 可观测性
- [Comet ML](https://www.comet.com) — 同团队，ML 实验管理平台

## 开放问题
- [ ] 2026-07-02 Opik 在 LLM 评估方面与 RAGAS/DeepEval 等专用框架的差异和优劣？是否会引入专用评估框架的集成？
