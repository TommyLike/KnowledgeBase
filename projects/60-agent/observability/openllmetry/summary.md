# openllmetry

> [`traceloop/openllmetry`](https://github.com/traceloop/openllmetry) · 上游贡献 · 基于 OpenTelemetry 标准的 LLM 应用可观测性 SDK，为 LangChain/OpenAI SDK 等框架提供标准化自动插桩

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> OpenLLMetry 是 Traceloop 推出的 OpenTelemetry 标准化 LLM 观测方案——不是另一个独立的追踪平台，而是在 OpenTelemetry 标准之上为 LLM 调用定义专用的 Span 类型和属性。在 Agent 可观测性生态中，OpenLLMetry 的价值在于：一次插桩，所有兼容 OTel 的后端（Jaeger/Tempo/Datadog/Langfuse）都能接收和分析 LLM 追踪数据。

## 项目介绍
> **用 OpenTelemetry 标准追踪 LLM——自动插桩 OpenAI/LangChain/Anthropic SDK，追踪数据发送到任何 OTel 兼容后端。**

核心场景：
- **LLM 调用的 OTel 标准化追踪**：Agent 的每次 LLM 调用以标准 Span 形式记录，兼容所有 OTel 后端
- **多框架自动插桩**：LangChain / OpenAI SDK / Anthropic SDK / LlamaIndex 等无需手动埋点
- **与现有基础设施集成**：企业已有 Jaeger/Datadog/Honeycomb 等 OTel 后端，OpenLLMetry 直接接入

## 技术要点
- **OpenTelemetry Traces**：基于 OTel 标准的 Span 模型，定义 `llm_request`/`llm_response`/`tool_call` 等专属 Span 类型
- **自动插桩 Instrumentation**：Python 装饰器或 monkey-patch 方式，不侵入业务代码
- **向量数据库追踪**：Weaviate / Chroma / Pinecone 等向量存储的 query 延迟和结果追踪
- **Traceloop Dashboard**：可选配合 Traceloop 云平台使用，开源 SDK 可独立运行

## 技术栈
Python, OpenTelemetry, LangChain/OpenAI SDK, Apache 2.0

## 关联
- [`langfuse/langfuse`](../langfuse/) — 互补，Langfuse 是消费端，OpenLLMetry 是生产端
- [OpenTelemetry](https://opentelemetry.io) — 底层可观测性标准
- [Traceloop](https://www.traceloop.com) — 同团队，商业可观测性平台

## 开放问题
- [ ] 2026-07-02 OpenTelemetry 的 LLM Span 语义规范是否已被上游采纳？社区标准化的进度如何？
