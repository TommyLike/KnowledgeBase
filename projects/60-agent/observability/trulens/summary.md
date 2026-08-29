# trulens

> [`truera/trulens`](https://github.com/truera/trulens) · 上游贡献 · Snowflake 背书的 LLM 应用评测与可观测性框架，用可编程反馈函数替代"感觉型"评估

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> TruLens 是 Snowflake（原 TruEra）推出的 LLM 应用评测与可观测性开源框架（MIT 协议），在 Agent 可观测性生态中占据评估与追踪交汇点的独特位置。它首创了 RAG 三合一（Answer Relevance / Context Relevance / Groundedness）评估范式，并针对 Agentic 场景扩展了七种专用评估器。我们关注它是因为它是 Agent 质量保障的关键基础设施，团队内部搭建 RAG 或 Agent 应用时可直接复用其评测体系。

## 项目介绍
> **以 OpenTelemetry 原生追踪为基础、可编程反馈函数为核心的 LLM 应用评测框架，覆盖 RAG 系统、Agent 工作流和工具调用全链路的可观测性与质量度量。**

核心场景：
- **RAG 系统质量评估**：通过 RAG 三合一（答案相关性、上下文相关性、事实一致性）自动评测检索增强生成系统，在每次 Prompt/模型/检索策略变更后快速发现退化。
- **Agent 行为监控**：七种 Agent 专用评估器（逻辑一致性、执行效率、计划遵循度、计划质量、工具选择、工具调用、工具质量）量化 Agent 每一步决策的正确性。
- **实验追踪与版本对比**：在 Streamlit Dashboard 中可视化对比不同配置（Prompt、模型、参数）下的评测指标，支持迭代式 Prompt 工程和模型选型。
- **多框架集成评测**：通过 `@instrument` 装饰器零侵入接入 LangChain、LlamaIndex、LangGraph 等框架的应用代码，也可装饰任意自定义函数。
- **生产环境可观测性**：基于 OpenTelemetry 的 Span 追踪可导出至 Jaeger、Grafana Tempo、Datadog 等标准后端，打通从实验到生产的观测链路。

## 技术要点
- **OpenTelemetry 原生追踪**：TruLens v2.x 将追踪后端从自定义实现替换为 OpenTelemetry，支持跨语言（Python/Go/Java）的分布式追踪和 MCP/A2A 协议的语义约定。每个 LLM 调用、检索、工具调用都产生结构化 OTEL Span，可导出至任意 OTLP 兼容后端。
- **反馈函数机制**：将评测逻辑抽象为 `Feedback` 对象，通过链式 DSL（`.on_input().on_output()`）绑定到 Span 属性上。反馈函数由 Provider（OpenAI/HuggingFace/Bedrock/LiteLLM 等）驱动，支持 LLM-as-a-Judge、NLP 指标、自定义函数三类实现模式。
- **RAG 三合一评估范式**：TruLens 首创的 Context Relevance（检索文档是否相关）、Groundedness（回答是否有上下文支撑）、Answer Relevance（回答是否直接回应问题）三项指标已成为 RAG 评测的事实标准。
- **Agent 七维评估体系**：针对 Agentic 场景推出 LogicalConsistency、ExecutionEfficiency、PlanAdherence、PlanQuality、ToolSelection、ToolCalling、ToolQuality 七种评估器，覆盖从规划到执行的完整 Agent 行为链路。
- **Selector / Lens 数据提取机制**：基于 JSONPath 思想的 `Lens` 选择器，以声明式方式从序列化的 App/Record 结构中定位输入、输出、检索上下文和中间结果，避免硬编码路径，也支持 OTEL Span 属性的语义化寻址。
- **模块化包架构**：采用 `trulens-core`（核心抽象）+ `trulens-providers-*`（评测后端）+ `trulens-apps-*`（框架集成）+ `trulens-connectors-*`（数据库连接器）的分层设计，用户可按需安装最小依赖。
- **批量与并发评测**：支持同步在线评测（Context Manager 模式）和离线批量评测（Run API），批量模式下可并发调用应用生成记录，再并发计算指标，适合大规模回归测试和 CI 集成。
- **MCP 工具调用追踪**：内置 `SpanType.MCP` 支持 Model Context Protocol 工具调用的全链路追踪，捕获工具名称、参数、输出和延迟，与 Agent 级评估器协同工作。

## 技术栈
Python, OpenTelemetry, Streamlit, SQLite/PostgreSQL/Snowflake, Poetry, Azure Pipelines, MkDocs

## 关联
- [`agent-runtime/observability/ragas`](../ragas/) — 同属 LLM 评测领域，Ragas 聚焦 RAG 评测指标创新，TruLens 侧重全栈可观测性 + Agent 评估
- [`agent-runtime/observability/deepeval`](../deepeval/) — LLM 单元测试框架，与 TruLens 在评估范式和 Provider 生态上形成互补
- [`agent-runtime/observability/phoenix`](../phoenix/) — Arize Phoenix 同为 OTEL 原生的 LLM 可观测性工具，在 Trace 可视化和评估侧各有侧重
- [`agent-framework/langchain`](../../agent-framework/langchain/) — TruLens 内置 LangChain/LangGraph 集成，可作为其评测和观测插件
- [`agent-runtime/observability/lm-evaluation-harness`](../lm-evaluation-harness/) — 模型基准评测框架，TruLens 则聚焦应用级评测和可观测性

## 开放问题
- [ ] 2026-07-02 TruLens 的 Agent 七维评估器（如 LogicalConsistency）依赖 LLM-as-a-Judge 实现，是否存在 Judge Bias 导致评估结果系统性偏移？是否有与人工标注的对齐数据验证其准确性？
