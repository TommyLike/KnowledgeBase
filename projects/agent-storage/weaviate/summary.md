# weaviate

> [`weaviate/weaviate`](https://github.com/weaviate/weaviate) · 上游贡献 · 内置向量化和混合搜索 Pipeline 的 AI 原生向量数据库，将向量搜索、标量过滤和全文搜索统一在单一查询中

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Weaviate 是向量数据库中的「全栈方案」——不只是一个向量存储引擎，而是内置了完整的 AI 向量化 Pipeline（自动 embedding + 分类 + 生成）。与 Milvus/Qdrant 要求外部 embedding 服务不同，Weaviate 可直接对接 OpenAI/Cohere/HuggingFace 等模型，在写入和查询时自动完成向量化。在 Agent 生态中，Weaviate 适合快速构建 RAG 原型——只需写入原始文本，Weaviate 自动完成 embedding 到检索的全流程。

## 项目介绍
> **自带 AI Pipeline 的向量数据库——写入原始文本即自动向量化，GraphQL 接口一站式完成语义搜索、标量过滤和生成增强检索。**

核心场景：
- **零代码 RAG 原型**：写入文本 → Weaviate 自动 embedding → GraphQL 查询 → 返回相关文档 + 生成回答
- **多模态检索**：文本+图像在同一 Collection 中统一查询，自动处理多模态 embedding
- **混合搜索（Hybrid Search）**：BM25 全文搜索 + 向量语义搜索在一个查询中组合，alpha 参数灵活调整权重
- **Agent 知识平台**：多租户 Collection + 元数据过滤，支撑多团队 Agent 共享向量数据库

## 技术要点
- **内置向量化模块**：配置 vectorizer 后自动完成 embedding（text2vec-openai / text2vec-huggingface / img2vec-neural 等），用户无需预计算向量
- **Generative Search**：检索后自动调用 LLM 对检索结果进行总结和回答生成（RAG-Token / RAG-Summarization）
- **Hybrid Search**：`hybrid` 参数统一 BM25 全文搜索 + 向量语义搜索，`alpha` 参数实现灵活的精度-召回权衡
- **GraphQL API**：使用表达力强大的 GraphQL 作为唯一查询接口，支持嵌套查询、聚合、过滤等复杂操作
- **多租户隔离**：Collection 级别的隔离，支持 RBAC 权限控制，适合企业多 Agent 共享
- **HNSW + 量化**：基于 HNSW 的高性能向量索引，支持 PQ/BQ 量化压缩，在精度与内存间灵活取舍
- **复制与分片**：支持 Collection 级别的多副本和高可用

## 技术栈
Go, GraphQL, HNSW, BM25, OpenAI/HuggingFace/Cohere, Apache 2.0

## 关联
- [`chroma-core/chroma`](../chroma/) — 竞品，嵌入式部署，开发体验优先
- [`milvus-io/milvus`](../milvus/) — 竞品，分布式优先级更高
- [`qdrant/qdrant`](../qdrant/) — 竞品，单机性能更高
- [`langchain-ai/langchain`](../../agent-framework/langchain/) — LangChain 集成，Weaviate 是常用 VectorStore 后端

## 开放问题
- [ ] 2026-07-02 内置 vectorizer 模块的 vendor 锁定风险如何？对于需要自定义 embedding 模型的企业场景，灵活性是否足够？
