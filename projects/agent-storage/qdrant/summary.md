# qdrant

> [`qdrant/qdrant`](https://github.com/qdrant/qdrant) · 上游贡献 · Rust 实现的高性能向量搜索引擎，以极致查询延迟和极简 API 著称

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Rust · 29,629n/140,935e  
<!-- END AUTO -->

---

## 定位
> Qdrant 是性能至上的向量数据库——用 Rust 从零构建，在单机场景下提供行业领先的 QPS 和延迟。在 Agent 生态中，Qdrant 的「单二进制部署 + 极致性能」使其成为中大型 RAG Agent 的最佳性价比选择——不像 Chroma 那样有嵌入式模式的规模瓶颈，也不像 Milvus 那样需要分布式基础设施。团队关注其在 Agent Memory 场景中的性能基准和实践。

## 项目介绍
> **Rust 赋能的极致性能向量搜索引擎——单二进制部署，毫秒级延迟，RAG Agent 的高性价比存储方案。**

核心场景：
- **实时语义搜索**：用户查询 → embedding → Qdrant 检索 → 返回 top-k 相关文档片段的 RAG 流程
- **Agent 对话记忆**：全文对话历史向量化存储，后续对话检索最相关的历史片段
- **推荐系统**：Item Embedding 存储 + 实时相似度计算，支撑个性化推荐
- **图像/视频搜索**：CLIP 等多模态模型生成的向量在 Qdrant 中索引和检索
- **Payload 过滤搜索**：向量相似度 + 结构化字段（日期、标签、用户 ID）组合过滤

## 技术要点
- **纯 Rust 实现**：无 GC 停顿时延，内存使用确定性强，安全性保证，比 C++/Java 实现更可靠
- **HNSW 索引优化**：自定义 HNSW 实现，支持索引构建时的并行化（多线程构建）和索引分片（shard）
- **Payload 索引与过滤**：支持 Keyword / Integer / Float / Geo / Datetime 类型字段的独立索引，过滤条件可与向量搜索同时使用
- **Quantization 压缩**：Scalar / Product / Binary Quantization 三种量化模式，内存减少最高 32 倍，精度损失可配置
- **WAL + 持久化**：写前日志保证 crash 安全，RocksDB 作为底层存储引擎
- **gRPC + REST 双协议**：同时提供高性能 gRPC 和易用的 RESTful API
- **集群模式**：基于 Raft 共识协议的分布式集群，支持水平扩展和自动故障转移

## 技术栈
Rust, gRPC, REST API, RocksDB, HNSW, Raft, Apache 2.0

## 关联
- [`chroma-core/chroma`](../chroma/) — 竞品，嵌入式开发体验优先，性能不敌 Qdrant
- [`milvus-io/milvus`](../milvus/) — 竞品，分布式优先，规模更大但运维复杂
- [`weaviate/weaviate`](../weaviate/) — 竞品，内置向量化 Pipeline 降低集成复杂度
- [`langchain-ai/langchain`](../../agent-framework/langchain/) — LangChain Qdrant 集成（`langchain-qdrant`）

## 开放问题
- [ ] 2026-07-02 Qdrant 的 Raft 集群模式在设计上的一致性保证是否影响查询延迟？单机 vs 集群的性能差距有多大？
