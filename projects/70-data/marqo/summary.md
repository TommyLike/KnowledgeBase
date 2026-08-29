# marqo

> [`marqo-ai/marqo`](https://github.com/marqo-ai/marqo) · 上游贡献 · 端到端的张量搜索引擎，将 embedding 模型与向量存储深度融合，以 Tensor Search 实现超越传统向量搜索的多模态检索

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Marqo 是向量搜索领域中「张量优先」的代表——传统向量数据库存储预计算的向量，而 Marqo 在存储层引入张量计算，支持跨模态检索、Late Interaction 重排序等高级语义操作。在 Agent 生态中，Marqo 的端到端多模态能力让 Agent 不需要分别集成 embedding 服务和向量数据库，一套 Marqo 同时搞定文本、图像和跨模态检索。

## 项目介绍
> **张量搜索引擎——不只是存向量，而是让存储本身就具备张量级别的语义理解能力。**

核心场景：
- **多模态 Agent 记忆**：Agent 的对话文本 + 截图 + 文档混合存储，统一张量空间跨模态检索
- **Late Interaction 重排序**：粗筛候选文档后，通过 ColBERT 等 Late Interaction 模型精细重排序，提升 RAG 精度
- **图像搜索**：以图搜图 + 以文搜图，支持电商商品搜索、版权图片管理等
- **混合搜索**：文本 + 标签 + 向量在多张量空间中的组合检索
- **多语言语义搜索**：同一查询跨语言检索，嵌入模型内部处理语言转换

## 技术要点
- **张量存储引擎**：不预计算固化向量，而是存储文档级别的张量表示，查询时动态计算相似度，支持更丰富的匹配模式
- **Late Interaction (ColBERT)**：Token-level 的交互式匹配，检索时不只看全局 embedding 相似度，还看每对 token 的交互得分
- **内置 Embedding Pipeline**：内置 100+ 预训练模型（CLIP、SBERT、OpenCLIP、E5 等），写入自动 embedding
- **多模态统一索引**：文本+图像在同一索引中，统一张量空间进行跨模态检索
- **开源核心 + 托管云**：Marqo Cloud 提供 GPU 加速向量化和 API 调用，开源版 Docker 一键部署

## 技术栈
Python, PyTorch, ONNX, CLIP/BERT, Vespa (底层搜索引擎), Docker, Apache 2.0

## 关联
- [`weaviate/weaviate`](../weaviate/) — 同为全栈向量数据库（内置 embedding），Weaviate 偏 GraphQL 全文搜索，Marqo 偏张量多模态
- [`chroma-core/chroma`](../chroma/) — 嵌入式向量数据库，API 更简单但功能更基础
- [`milvus-io/milvus`](../milvus/) — 大规模向量存储，Marqo 的优势在多模态小规模高精度场景
- ColBERT / PLAID — Marqo 核心依赖的 Late Interaction 检索算法

## 开放问题
- [ ] 2026-07-02 Late Interaction (ColBERT) 在 10M+ 文档规模下的实时检索延迟能否满足 Agent 的交互体验（< 1s）？
