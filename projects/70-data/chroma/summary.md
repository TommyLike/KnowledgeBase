# chroma

> [`chroma-core/chroma`](https://github.com/chroma-core/chroma) · 上游贡献 · AI 原生开源向量数据库，以最简单 API 为 LLM 应用提供嵌入存储、语义搜索和元数据过滤

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Rust · 29,200n/147,549e  
<!-- END AUTO -->

---

## 定位
> Chroma 是 Agent 应用中使用最广泛的嵌入式向量数据库。与 Milvus/Qdrant/Weaviate 等独立部署的向量数据库不同，Chroma 定位为「AI 原生的嵌入式存储」——以 Python 库方式运行在应用进程内，零运维启动即可用。在 RAG Agent 中，Chroma 是最常见的记忆和知识库存储方案。团队关注其在 Agent Memory 场景的应用，尤其是 Chroma 在长对话记忆和跨会话知识保留方面的策略。

## 项目介绍
> **为 AI 应用而生的嵌入式向量数据库——`pip install chromadb` 即可在代码中直接使用，无需独立服务。**

核心场景：
- **RAG Agent 知识库**：文档分块 → 嵌入 → 存入 Chroma → Agent 查询时检索相关上下文
- **Agent 长期记忆**：Agent 对话历史以向量形式存储，后续对话时检索相关历史记忆
- **语义搜索**：通过文本相似度而非关键词匹配搜索，典型用于代码搜索、文档搜索
- **多模态检索**：文本+图像统一嵌入空间，支持以文搜图和图文混合检索

## 技术要点
- **嵌入式部署模式**：Python 库直接导入使用，数据以本地文件或 SQLite 存储，零配置启动
- **多模态集合**：同一 Collection 中存储文本、图像、音频等多种模态的嵌入向量
- **元数据过滤**：每条文档可附带任意元数据标签，查询时按标签过滤（如 `{"source": "wiki", "date": "2024"}`）
- **HNSW 索引**：基于 HNSW 算法的高维向量索引，查询延迟亚毫秒级
- **Distance 多度量**：支持 L2 / Cosine / Inner Product 三种距离度量
- **多 Embedding 模型**：内置 SentenceTransformers、OpenAI、Cohere 等嵌入模型，也支持自定义
- **Client-Server 模式（可选）**：生产环境下可部署为独立服务器，多客户端共享一个 Chroma 实例

## 技术栈
Rust (core engine), Python (SDK), TypeScript (client), HNSW, SQLite, Apache 2.0

## 关联
- [`qdrant/qdrant`](../qdrant/) — 竞品，Rust 实现，性能更高但需独立部署
- [`milvus-io/milvus`](../milvus/) — 竞品，分布式云原生向量数据库，万亿级规模
- [`weaviate/weaviate`](../weaviate/) — 竞品，向量数据库 + 内置向量化 Pipeline
- [`langchain-ai/langchain`](../../agent-framework/langchain/) — 常用集成方，LangChain 提供 Chroma 的 Document Loader 和 Retriever 集成

## 开放问题
- [ ] 2026-07-02 嵌入式模式在 100M+ 向量规模下的查询性能衰减严重吗？是否有自动分片的计划？
