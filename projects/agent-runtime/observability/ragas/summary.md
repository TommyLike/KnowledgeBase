# ragas

> [`vibrantlabsai/ragas`](https://github.com/vibrantlabsai/ragas) · 上游贡献 · RAG 应用评估的业界基准框架，提供 Contextual Precision/Recall/Faithfulness 等 10+ 专用于检索增强生成的评估指标

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> RAGAS (RAG Assessment) 是 RAG 评估领域的开创者——在 LLM 评估框架百花齐放的背景下，RAGAS 是唯一聚焦「检索增强生成」这一特定架构的评估方案。在做 RAG Agent 时，你需要回答「检索到的文档是否相关」「生成的回答是否忠实于检索结果」「是否漏掉了重要文档」——RAGAS 将这些问题量化为数学指标。团队将其作为 RAG Agent 质量保障的核心工具。

## 项目介绍
> **RAG 应用的专用评估框架——不用写评估逻辑，RAGAS 自动计算检索质量、生成忠实度和答案相关性。**

核心场景：
- **Retriever 质量评估**：评估检索组件返回的文档与 query 的 Contextual Precision/Recall
- **Generator 忠实度检测**：判断生成的回答是否有「幻觉」——是否忠实于检索到的上下文
- **RAG Pipeline 调优**：对比不同 chunk size、top-k、embedding 模型的 RAGAS 得分，找到最优组合
- **Agent 知识库质量监测**：RAG Agent 上线后持续采样，监测检索质量漂移
- **合成评估数据生成**：从知识库文档自动演化出评估数据集（问题 + ground truth 答案）

## 技术要点
- **Retriever 指标**：Contextual Precision（检索到的相关文档在结果列表中的排名）、Contextual Recall（ground truth 中提到的文档是否被检索到）、Contextual Entities Recall
- **Generator 指标**：Faithfulness（生成的答案是否有不可从上下文中推导的声明）、Answer Relevancy（答案是否实际上回答了问题）、Answer Correctness
- **E2E 指标**：Answer Semantic Similarity（语义相似度）、Answer Correctness（事实正确性）
- **Synthetic Test Data Generation**：从文档自动生成 (question, contexts, answer) 三元组，减少手工评估数据准备
- **LLM-as-Judge 驱动**：全部指标通过 LLM prompt 驱动计算，不依赖人工标注
- **与 LangChain/LlamaIndex 集成**：直接包装 RAG pipeline 的 chain，自动记录中间步骤用于评估

## 技术栈
Python, LangChain/LlamaIndex, OpenAI/Anthropic API, Apache 2.0

## 关联
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — RAGAS 最常用于评估 LangChain RAG 应用
- [`confident-ai/deepeval`](../deepeval/) — 竞品，DeepEval 指标覆盖面更广，RAGAS 在 RAG 场景更深
- [`truera/trulens`](../trulens/) — 竞品，TruLens 同时提供 RAG 评估和反馈函数
- [`infiniflow/ragflow`](../../memory/ragflow/) — RAG 平台，可用 RAGAS 评估其检索质量

## 开放问题
- [ ] 2026-07-02 RAGAS 指标是否能捕捉 RAG 质量的边界情况？如「检索到了相关文档但信息已过时」这种时效性相关的问题？
