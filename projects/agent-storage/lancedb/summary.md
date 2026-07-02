# lancedb

> [`lancedb/lancedb`](https://github.com/lancedb/lancedb) · 上游贡献 · 基于自研 Lance 列式存储格式的开源嵌入式向量数据库，为 AI/ML 应用提供多模态向量检索引擎

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> LanceDB 是嵌入到应用进程内的向量数据库，与需要独立部署的 Milvus/Qdrant 形成差异化定位。以自研 Lance 列式格式为存储底座，通过 Apache Arrow 零拷贝生态与 Pandas/Polars/DuckDB 无缝互操作。团队关注其在 RAG 和多模态 AI 数据管理场景中的演进，作为上游贡献跟踪其 Rust 核心引擎和 Python/TypeScript SDK 的版本变化。

## 项目介绍
> **LanceDB 是一个以 Rust 为核心引擎的嵌入式向量数据库，基于自研 Lance 列式格式，支持十亿级向量毫秒级检索，可作为库直接嵌入 Python/Node.js/Rust 应用进程，无需独立服务器。**

核心场景：
- **RAG 应用后端**：为 LLM 提供向量检索，支持混合查询（向量 + 全文搜索 + SQL 过滤），原生集成 LangChain 和 LlamaIndex
- **多模态 AI 数据管理**：统一存储和查询文本、图像、视频、点云等多模态原始数据及其向量嵌入，无需维护两套存储系统
- **本地/嵌入式 AI 应用**：无独立服务器，作为库直接嵌入应用进程，适合边缘设备、桌面应用和本地开发场景
- **大规模向量检索**：十亿级向量毫秒级搜索，GPU 加速索引构建，适合语义搜索和推荐系统
- **数据分析 + 向量搜索混合负载**：通过 Apache Arrow 零拷贝与 Pandas/Polars/DuckDB 互操作，同一数据集上执行 SQL 分析和向量检索

## 技术要点
- **Lance 列式存储格式**：基于 Apache Arrow 的自研列式格式，支持零拷贝读取和高效向量化 I/O，是 LanceDB 的存储底座。提供自动版本控制（类似 Delta Lake 时间旅行）、快照、回滚和增量更新能力
- **嵌入式架构**：以库嵌入应用进程运行，无需独立部署和额外运维，与 Milvus/Qdrant 的独立服务模式形成差异化。提供 Python/TypeScript/Rust/Java SDK，同时提供 REST API 供跨语言调用
- **多索引策略**：支持 IVF-PQ、IVF-HNSW 等多种向量索引算法，可按数据规模和检索精度灵活选择。GPU 加速索引构建，显著缩短大规模数据入库时间
- **混合查询引擎**：向量相似度检索 + 全文搜索 (FTS) + SQL 过滤的组合查询能力。SQL 引擎基于 Apache DataFusion，支持复杂过滤和聚合
- **Arrow 生态融合**：与 Pandas/Polars/DuckDB 零拷贝互操作，数据在组件间无需序列化/反序列化开销，兼顾分析性能和开发效率
- **Cloud 托管服务**：LanceDB Cloud 为 serverless 托管版，兼容开源 API，支持自动扩缩容，当前处于 public beta 阶段

## 技术栈
Rust (核心引擎), Lance (自研列式存储格式), Apache Arrow, Apache DataFusion (SQL 引擎), Python/Typescript/Java (SDK), IVF-PQ/IVF-HNSW (向量索引), LangChain/LlamaIndex (生态集成), Apache-2.0

## 关联
- [`milvus-io/milvus`](../../agent-storage/milvus/summary.md) — 竞品，分布式向量数据库，需独立部署，知识图谱内已有深度分析
- [`chroma-core/chroma`](../../agent-storage/chroma/summary.md) — 竞品，同为 AI 原生嵌入式向量库，Python 生态为主
- [`qdrant/qdrant`](../../agent-storage/qdrant/summary.md) — 竞品，Rust 向量搜索引擎，需独立服务部署
- [`lancedb/lance`](https://github.com/lancedb/lance) — 上游依赖，Lance 列式存储格式，是 LanceDB 的存储引擎
- [`lancedb/vectordb-recipes`](https://github.com/lancedb/vectordb-recipes) — 官方教程和示例仓库

## 开放问题
- [ ] 2026-07-02 LanceDB 0.x beta 阶段的 API 稳定性如何，何时计划发布 1.0 正式版？
- [ ] 2026-07-02 LanceDB Cloud 托管版与开源版的 feature gap 有多大，团队是否有评估将其用于生产环境的计划？
