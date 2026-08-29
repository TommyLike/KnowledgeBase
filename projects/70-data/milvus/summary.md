# milvus

> [`milvus-io/milvus`](https://github.com/milvus-io/milvus) · 上游贡献 · CNCF 毕业项目，面向万亿级向量数据的云原生分布式向量数据库，GPU 加速索引和混合搜索

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Milvus 是向量数据库领域的「分布式之王」——作为 CNCF 首个向量数据库毕业项目，在大规模（十亿+向量）、高吞吐、低延迟场景中保持领先。与 Chroma（嵌入式）/ Qdrant（单机高性能）/ Weaviate（内置 Pipeline）形成差异化：Milvus 的「存储-计算分离」架构使其能够处理其他向量数据库无法企及的规模。在 Agent 生态中，Milvus 是大规模 RAG 和企业级 Agent 知识平台的首选存储底座。团队关注其云原生架构演进和 GPU 索引加速策略。

## 项目介绍
> **企业级分布式向量数据库——为万亿级非结构化数据提供毫秒级语义搜索，是 RAG Agent 大规模部署的存储基石。**

核心场景：
- **大规模 RAG Agent 知识库**：企业级文档管理，十亿级文档片段的向量化存储和实时检索
- **多模态语义搜索**：文本/图片/视频的统一向量表示和跨模态检索
- **推荐系统**：用户行为向量 + 商品向量，实时相似度匹配推荐
- **Anomaly Detection**：时序数据向量化，异常检测 by 历史相似度比较
- **分子相似性搜索**：AI 制药中的分子结构向量化与相似分子发现

## 技术要点
- **存储计算分离**：Query Node（计算）+ Data Node（写入）+ Index Node（索引构建）+ Proxy（路由），各层独立弹性伸缩
- **四层索引体系**：内存索引（HNSW/IVF_FLAT）+ 磁盘索引（DiskANN）+ GPU 索引（RAFT）+ 标量索引（排序/过滤），自动选择最优索引
- **多向量多列**：每条实体可存储多个向量字段 + 标量字段 + JSON 字段，支持混合搜索（向量相似 + 标量过滤 + 全文搜索）
- **多一致性等级**：Strong / Bounded Staleness / Session / Eventually，按查询场景选择一致性 vs 性能
- **Mmap 内存管理**：向量数据映射到磁盘，支持数据量远大于内存的检索，单机 100M+ 向量无压力
- **Change Data Capture**：内置 CDC 向 Kafka/Pulsar 输出变更事件，支持增量数据处理
- **GPU 加速索引**：RAFT 库加速 IVF-PQ / CAGRA 索引构建（10-50x speedup），NVIDIA cuVS 集成进行中

## 技术栈
Go, C++, Python SDK, gRPC, MinIO/S3, Pulsar/Kafka, etcd, Apache 2.0, CNCF Graduated

## 关联
- [`chroma-core/chroma`](../chroma/) — 竞品，嵌入式向量数据库，开发体验优先
- [`qdrant/qdrant`](../qdrant/) — 竞品，Rust 高性能单机 + 集群模式
- [`weaviate/weaviate`](../weaviate/) — 竞品，内置向量化和混合搜索 Pipeline
- [`opensearch-project/OpenSearch`](../opensearch/) — 标量搜索基准，通过 k-NN 插件获得向量搜索能力
- [`langchain-ai/langchain`](../../agent-framework/langchain/) — LangChain 的一级向量存储集成

## 开放问题
- [ ] 2026-07-02 Milvus 2.4+ 的 GPU 索引（RAFT/CAGRA）在 Agent 场景下的实际检索延迟和内存占用是多少？
