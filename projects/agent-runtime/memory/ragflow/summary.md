# ragflow

> [`infiniflow/ragflow`](https://github.com/infiniflow/ragflow) · 上游贡献 · 开源 RAG 全流程平台，以深度文档理解（DeepDoc）为核心，提供从文档解析到知识检索的端到端可视化方案

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> RAGFlow 是中文 RAG 生态中最有影响力的开源平台，由 infiniflow 团队打造。与 LangChain/LlamaIndex 需要编码不同，RAGFlow 提供完整的可视化 RAG Pipeline——上传 PDF/Word/图片 → 自动解析版面/表格/图表 → 嵌入 → 知识库问答，全流程在 UI 中完成。在 Agent 生态中，RAGFlow 提供了「RAG 知识库即服务」的能力，Agent 通过 API 直接查询 RAGFlow 知识库。

## 项目介绍
> **你的企业知识库就在一个部署里——上传文档即自动构建语义知识库，Agent 可直接调用 RAG API 查询。**

核心场景：
- **企业知识库 Agent**：上传所有内部文档 → RAGFlow 自动解析和索引 → Agent 用自然语言查询
- **复杂文档深度理解**：带表格和图表的 PDF，RAGFlow 的 DeepDoc 引擎能精准提取结构化信息
- **可视化 RAG Pipeline**：非技术人员也能通过 UI 上传文档、调整分块策略、测试检索效果
- **多租户知识库管理**：多个项目/团队的独立知识库，共享 RAGFlow 实例

## 技术要点
- **DeepDoc 深度文档解析**：不仅是文本提取，而是版面分析→表格识别→图表理解→语义分块的完整 Pipeline
- **RAPTOR 递归摘要**：文档自动分层聚类并生成层级摘要，支持跨页面/跨节的多粒度检索
- **混合检索**：关键词 + 向量 + 知识图谱三重检索，不依赖单一的语义匹配
- **Infinity 向量引擎**：自研 Rust 实现的向量数据库，支持 Tensor + float16 精度
- **可视化配置界面**：文档上传、chunk 配置、embedding 模型选择、检索测试全在 UI 中操作
- **Agent 集成 API**：标准 REST API，任何 Agent 框架可通过 API 查询 RAGFlow 知识库

## 技术栈
Python, TypeScript, DeepDoc (CV+OCR), Infinity (Rust 向量数据库), Elasticsearch, Redis, PostgreSQL

## 关联
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — RAGFlow 可与 LangChain 结合使用，作为知识库后端
- [`vibrantlabsai/ragas`](../../observability/ragas/) — 可用 RAGAS 评估 RAGFlow 的检索质量
- [`chroma-core/chroma`](../../../agent-storage/chroma/) — 嵌入式向量数据库，RAGFlow 用自研 Infinity 替代

## 开放问题
- [ ] 2026-07-02 DeepDoc 对中文文档（特别是复杂表格和无边界表格）的解析精度是否能达到企业级要求？
