# langchain

> [`langchain-ai/langchain`](https://github.com/langchain-ai/langchain) · 上游贡献 · LLM 应用开发框架的事实标准，提供 Chain/Agent/Tool 三层抽象

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> LangChain 是当前最主流的 LLM 应用开发框架，定义了 Chain（链式调用）、Agent（自主决策）、Tool（工具集成）三层抽象范式。在 Agent 生态中，LangChain 是连接 LLM 与外部世界的「操作系统级」中间件——几乎所有主流 LLM Provider、Vector Store、Tool 都有 LangChain 集成。团队关注其架构演进（特别是 LangChain v1.0 后的稳定性和 LCEL 表达式的设计思想），以及其在多 Agent 编排场景中的实践。

## 项目介绍
> **LLM 应用开发的「瑞士军刀」——通过可组合的 Chain/Agent/Tool 抽象，让开发者用最少的代码将 LLM 与任意外部系统连接。**

核心场景：
- **模型统一调用**：通过统一的 LLM/ChatModel 接口屏蔽 OpenAI/Anthropic/Google/HuggingFace 等 50+ 模型提供商的 API 差异，支持流式输出、缓存、速率限制
- **RAG 全流程**：从 Document Loader（100+ 格式）→ Text Splitter → Embedding → Vector Store（50+）→ Retriever 到 Chatbot 完整链路
- **Tool Calling Agent**：定义 Tool 接口后，Agent 自主决策调用链——OpenAI Functions / ReAct / Plan-and-Execute 等多种 Agent 范式
- **多步推理链**：SequentialChain / RouterChain / LLMChain 等组合模式，实现复杂业务流程编排
- **Memory 管理**：ConversationBufferMemory / SummaryMemory / VectorStoreRetMemory 等，解决 LLM 无状态问题

## 技术要点
- **LCEL（LangChain Expression Language）**：基于管道操作符 `|` 的声明式编程模型，链的定义与执行解耦，自动获得流式、异步、并行化支持，v0.2+ 成为推荐的链构建方式
- **Runnable 协议**：所有组件（LLM/ChatModel/Retriever/Tool 等）实现统一 `invoke/batch/stream` 接口，实现了标准化的流式语义和一致性错误处理
- **Model I/O 三层**：Prompt Template（模板化提示词）→ Language Model（统一模型接口）→ Output Parser（结构化输出解析），每个环节可独立替换
- **Agent 抽象演进**：从 AgentExecutor（v0.1 的回调式 Agent）→ 基于 Tool Calling 的 create_tool_calling_agent（v0.2）→ 中间件式 LangGraph Agent（v0.3+），逐步走向更可控的 Agent 架构
- **多模态支持**：ChatModel 接口原生支持 text+image 多模态输入，GPT-4V/Claude Vision 等多模态模型通过统一接口使用
- **Ecosystem 包拆分**：`langchain-core`（核心抽象）→ `langchain-community`（社区集成）→ `langchain`（高层 API）+ 独立 provider 包（如 `langchain-openai`），避免依赖爆炸
- **Callback 系统**：可插拔的事件钩子，覆盖 LLM start/end、Tool start/end、Chain start/end 等全部生命周期，LangSmith 追踪基于此实现
- **1000+ 集成**：涵盖 LLM Provider（50+）、Vector Store（50+）、Document Loader（100+）、Tool、Embedding Model、Retriever 等

## 技术栈
Python, TypeScript (LangChain.js), OpenAI/Anthropic SDK, Pydantic, LangSmith (observability), LangGraph (agent orchestration)

## 关联
- [`langchain-ai/langgraph`](../langgraph/) — 同一团队，LangGraph 是 LangChain 的 Agent 编排引擎，弥补了 Chain 抽象在循环/分支/状态管理上的不足
- [`vibrantlabsai/ragas`](../../agent-runtime/observability/ragas/) — RAG 评估框架，常用于评估 LangChain RAG 应用质量
- [`langfuse/langfuse`](../../agent-runtime/observability/langfuse/) — LLM 应用追踪平台，LangChain 的一级集成
- [LangSmith](https://smith.langchain.com) — 同团队，LLM 应用的调试/测试/评估/监控平台

## 开放问题
- [ ] 2026-07-02 LangChain v1.0 发布后，与 LangGraph 的职责边界是否更清晰？Chain 抽象是否被 LangGraph StateGraph 替代？
