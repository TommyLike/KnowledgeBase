# langfuse

> [`langfuse/langfuse`](https://github.com/langfuse/langfuse) · 上游贡献 · 最流行的开源 LLM 可观测性平台，提供 Trace/Evaluation/Prompt Management 三位一体的 Agent 观测方案

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · TypeScript · 20,975n/58,483e  
<!-- END AUTO -->

---

## 定位
> Langfuse 是 LLM 可观测性领域的开源标杆——在 LangSmith（商业闭源）之外为社区提供了功能同等的全栈方案。Agent 调用了多少次 LLM、每次调用消耗了多少 token、哪个步骤延迟最高、Retriever 检索到了什么文档——这些观测数据都通过 Langfuse 的 OpenTelemetry 风格的 Trace 结构记录和可视化。团队将其作为 Agent 可观测性的主要参照平台。

## 项目介绍
> **LLM 应用的开源追踪平台——像分布式追踪看微服务一样，看 Agent 的每一步 LLM 调用、工具使用和检索操作。**

核心场景：
- **Agent 调用链追踪**：Agent → LLM call 1 → Tool call → LLM call 2 → Output 的完整 Trace，每步延迟和 token 用量可见
- **RAG 质量评估**：对比检索到的文档和生成的回答，评估 ground truth 一致性
- **Prompt 版本管理**：像代码一样管理 Prompt 模板的版本迭代，追踪不同版本的性能差异
- **成本归因分析**：按 Session/User/Feature 维度分析 LLM 调用成本
- **在线评估**：生产流量中实时采样评分，检测质量漂移

## 技术要点
- **OTel 风格 Trace 模型**：Trace → Span（Generation/Span/Event）三级嵌套，直接映射 Agent 的调用层次结构
- **自动插桩 vs 手动埋点**：LangChain/LlamaIndex/OpenAI SDK 自动插桩（decorator），也支持原生 SDK `langfuse.trace()` 手动埋点
- **Score 评估体系**：可附加 numeric/categorical/boolean 分数到任意 Trace/Span，支持用户反馈、LLM-as-Judge、人工评分等多种评估源
- **Prompt Management**：Prompt 模板在 Langfuse 中管理（支持 chat/text 类型和多版本），SDK 拉取后填充变量，版本回滚一键操作
- **Playground 调试**：在 UI 中修改 Prompt 模板并实时对比不同模型的输出，加速 Prompt 迭代
- **ClickHouse 存储**：高基数时间序列数据以 ClickHouse 为存储引擎，支撑大规模 Tracing 数据的实时查询
- **自建部署**：Docker Compose 一键部署，也可使用 Langfuse Cloud 托管服务

## 技术栈
TypeScript, Next.js, ClickHouse, PostgreSQL, Prisma, OpenTelemetry, MIT (core) + EE

## 关联
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — LangChain Callback 集成，自动追踪 Chain/Tool/LLM 调用
- [LangSmith](https://smith.langchain.com) — 竞品，LangChain 官方平台，功能更全但闭源
- [`Arize-ai/phoenix`](../phoenix/) — 竞品，Arize 开源 LLM 可观测性平台
- [`comet-ml/opik`](../opik/) — 竞品，Comet 开源 LLM 评估与追踪
- [`BerriAI/litellm`](../../gateway/litellm/) — AI Gateway 集成，LiteLLM 调用自动上报到 Langfuse

## 开放问题
- [ ] 2026-07-02 Langfuse 的开源版和企业版功能边界如何界定？核心评估和 Prompt 管理是否会在企业版独占？
