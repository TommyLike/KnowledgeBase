# phoenix

> [`arize-ai/phoenix`](https://github.com/Arize-ai/phoenix) · 上游贡献 · 基于 OpenTelemetry 的 LLM 可观测性平台，提供全链路追踪、自动评估与提示词实验管理

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> Phoenix 是 Arize AI 开源的 LLM 可观测性平台，在 OpenTelemetry 标准之上定义了 OpenInference 语义约定，为 AI 应用提供统一的追踪、评估和实验能力。本项目属于上游贡献跟踪范畴，关注其在 LLM 可观测性领域的标准化进展、与主流 Agent 框架的集成深度，以及 OpenInference 语义约定在行业中的采纳情况。Phoenix 与 Langfuse、Opik、OpenLLMetry 等项目构成 LLM 可观测性赛道的主要竞争者，共同推动 AI 应用可观测性从专有方案走向开放标准。

## 项目介绍
> **Phoenix 是面向 LLM 应用的端到端可观测性平台，通过 OpenTelemetry 自动插桩捕获完整调用链，结合 LLM-as-a-Judge 评估、版本化数据集管理和提示词实验，形成"观测—评估—改进"的迭代闭环。**

核心场景：
- **LLM 应用运行时追踪**：通过 30+ 自动插桩器（LangChain、LlamaIndex、OpenAI、Anthropic、Bedrock 等），捕获 LLM 调用的完整 Span 层级（LLM Span、Tool Span、Agent Span、Retriever Span 等），支持多轮对话的 Session 聚合和延迟/Token/成本可视化。
- **LLM-as-a-Judge 自动化评估**：内置检索质量评估（retrieval evals）和响应质量评估（response evals）模板，支持对工具调用准确性、幻觉检测等进行自动化打分，无需人工标注即可建立评估基准。
- **提示词实验与版本管理**：提供 Playground 环境对比不同 prompt、模型和参数的效果，支持 prompt 版本化管理、批量回放 traced 调用，以及系统化的 A/B 实验追踪。
- **数据集构建与迭代**：从生产 trace 中提取和标注数据，创建版本化数据集（datasets），用于离线评估、实验对比和模型微调，形成"观测 → 评估 → 改进"的数据飞轮。
- **多框架多语言统一可观测**：支持 Python、TypeScript、Java 三种语言的自动插桩，覆盖 30+ 框架和模型提供商，通过 OpenInference 标准统一 AI 应用的可观测性数据模型。

## 技术要点
- **OpenInference 语义约定**：在 OpenTelemetry 基础上定义了 AI 专用的 Span Kind（LLM、TOOL、AGENT、CHAIN、RETRIEVER、EMBEDDING、RERANKER、GUARDRAIL 等）和标准化属性名（llm.input_messages、llm.token_count.total、output.value 等），确保跨工具和跨平台的可移植性，是 Phoenix 最核心的技术贡献。
- **30+ 自动插桩器**：覆盖 LangChain、LangGraph、LlamaIndex、AutoGen、CrewAI、DSPy、Haystack、Vercel AI SDK、Pydantic AI、Semantic Kernel 等 Agent 框架，以及 OpenAI、Anthropic、Bedrock、VertexAI、Mistral、LiteLLM 等模型提供商，通过 monkey-patch 或回调机制自动注入 OpenTelemetry Span。
- **Session 机制**：将同一用户多轮对话的多个 Trace 按 session_id 聚合为 Session 视图，支持按会话维度查看完整的 Agent 交互历史、状态变迁和跨轮次的上下文传递，是调试复杂 Agent 行为的关键能力。
- **多模式部署**：支持 pip install 本地运行、Jupyter Notebook 内嵌（%phoenix 魔法命令）、Docker 容器化部署（带持久化存储）、Kubernetes Helm Chart 生产部署，可在开发、调试和生产环境无缝切换。
- **PXI（Phoenix Intelligence）**：内建的 AI 工程 Agent，可自动分析 trace 数据中的异常模式、辅助 prompt 迭代建议和问题根因定位，将 AI 能力应用于可观测性本身。
- **成本追踪**：自动捕获每次 LLM 调用的 token 消耗和对应成本（按模型定价），支持按 trace/span/项目维度过滤和聚合可视化，帮助团队控制 LLM 应用的成本。
- **MCP Server**：提供 TypeScript 实现的 MCP Server（@arizeai/phoenix-mcp），可将 Phoenix 的可观测性数据和分析能力集成到 MCP 生态中，供其他 AI 工具消费。
- **弹性许可（ELv2）**：使用 Elastic License 2.0，允许非商业免费使用，商业环境使用存在限制，与 Apache 2.0 / MIT 等宽松许可有本质区别。

## 技术栈
Python (45.7%), TypeScript/React (39.2%), Jupyter Notebook (13.8%), OpenTelemetry Protocol (OTLP), OpenInference Semantic Conventions, Docker, Kubernetes (Helm), Elastic License 2.0

## 关联
- [`agent-runtime/observability/openllmetry`](../openllmetry/summary.md) — 同为 OpenTelemetry 生态的 LLM 可观测性项目（Traceloop 出品），OpenInference 与 OpenLLMetry 在语义约定层面存在竞争/互补关系
- [`agent-runtime/observability/langfuse`](../langfuse/summary.md) — 同赛道的 LLM 可观测性平台，Langfuse 偏向自建后端+全功能平台，Phoenix 偏向 OpenTelemetry 标准+本地化体验
- [`agent-runtime/observability/opik`](../opik/summary.md) — Comet ML 出品的 LLM 可观测性平台，同样提供评估和实验能力，与 Phoenix 存在功能重叠

## 开放问题
- [ ] 2026-07-02 OpenInference 语义约定在行业中的采纳程度如何？是否有其他可观测性平台或框架开始原生支持 OpenInference Span Kind？
- [ ] 2026-07-02 Phoenix 的 Elastic License 2.0 是否会限制其在商业产品中的集成使用？社区是否有转向更宽松许可的计划？
- [ ] 2026-07-02 Phoenix 与 OpenLLMetry 的语义约定差异多大？两者是否有可能合并为一个统一的 LLM 可观测性标准？
