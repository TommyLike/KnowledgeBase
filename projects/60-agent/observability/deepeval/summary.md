# deepeval

> [`confident-ai/deepeval`](https://github.com/confident-ai/deepeval) · 上游贡献 · LLM 评估框架，提供从单元测试级单指标到完整 Agent 系统评估的全谱系测试能力

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Python · 23,574n/84,824e  
<!-- END AUTO -->

---

## 定位
> DeepEval 是 LLM 评估领域「像写 pytest 一样评估 Agent」理念的代表——将 LLM 质量评估包装为 Python 测试的形式，让 LLM 评估融入 CI/CD 流程。在 Agent 生态中，DeepEval 的独特价值在于：它不仅是评估框架，更是「LLM 质量门禁」——你可以在 CI 中断言「Agent 的幻觉率 < 5%」「答案相似度 > 0.8」，测试不通过则不能部署。

## 项目介绍
> **LLM 应用的 PyTest 式评估框架——`assert_test(hallucination() < 0.5)` 让 AI 质量成为 CI 流水线的一部分。**

核心场景：
- **RAG 质量评估**：评估检索相关性（Contextual Relevancy）和生成忠实度（Faithfulness/Hallucination）
- **Agent 回归测试**：每次 Agent 代码变更后，自动运行评估套件检测性能退化
- **CI/CD 质量门禁**：`deepeval test run` 集成到 GitHub Actions，未达标阻止合并
- **幻觉检测**：通过对比生成回答与检索到的上下文，判断是否存在幻觉
- **微调效果对比**：量化比较 Prompt 改动或模型切换前后的质量差异

## 技术要点
- **PyTest 风格 API**：`deepeval.assert_test(test_case, [metrics])`，熟悉 pytest 的开发者 10 分钟上手
- **15+ 内置评估指标**：Answer Relevancy / Faithfulness / Hallucination / Contextual Recall / Toxicity / Bias / Summarization 等
- **LLM-as-Judge + 传统指标**：一部分指标通过 LLM 评分（如 Answer Relevancy），一部分通过统计方法（如 BLEU/ROUGE）
- **Synthesizer 数据生成**：从一个文档/URL 自动生成评估数据集（问题 + 标准答案），减少手工创建评估集的工作量
- **Confident AI 平台集成**：DeepEval 的开源部分可独立使用，Confident AI 云平台提供可视化、团队协作和历史追踪
- **Callback 自动收集**：LangChain/LlamaIndex 集成自动捕获 Trace，无需手动埋点
- **测试报告**：生成 HTML/JSON 格式的详细测试报告，包含每项指标的得分和分析

## 技术栈
Python, PyTest, LangChain/LlamaIndex, OpenAI/Anthropic API, Apache 2.0

## 关联
- [`vibrantlabsai/ragas`](../ragas/) — 竞品，RAGAS 专注 RAG 评估，DeepEval 覆盖面更广
- [`truera/trulens`](../trulens/) — 竞品，TruLens 偏 Agent 可观测性+评估
- [`langfuse/langfuse`](../langfuse/) — 互补，Langfuse 做追踪，DeepEval 做评估
- [`EleutherAI/lm-evaluation-harness`](../lm-evaluation-harness/) — LM 基准测试 vs DeepEval 的 LLM 应用测试
- Confident AI — 同团队，商业评估管理平台

## 开放问题
- [ ] 2026-07-02 LLM-as-Judge 指标的自我参照偏差如何校准？评估用的 LLM 与被评估的 LLM 存在系统性偏差时如何处理？
