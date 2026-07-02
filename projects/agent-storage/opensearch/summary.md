# opensearch

> [`opensearch-project/opensearch`](https://github.com/opensearch-project/OpenSearch) · 上游贡献 · AWS 主导的 Elasticsearch 开源分支，通过 k-NN 插件将向量搜索能力集成到全文检索引擎中

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> OpenSearch 是搜索引擎领域的「全能选手」——从 Elasticsearch 7.10 分叉而来，保留了 ES 的全部文本搜索能力，同时通过 k-NN 插件增加了现代向量搜索。在 Agent 生态中，OpenSearch 的「全文+向量」混合搜索能力使其成为企业级 RAG 的常选方案：不需要额外部署向量数据库，一套 OpenSearch 就搞定关键字搜索、语义搜索和日志分析。

## 项目介绍
> **兼容 Elasticsearch 的开源搜索与分析引擎——集全文搜索、向量搜索、日志分析、安全告警于一体。**

核心场景：
- **RAG 混合检索**：BM25 关键词搜索 + k-NN 向量搜索组合，兼顾精确匹配和语义理解
- **企业日志与分析**：Agent 运行日志、LLM 调用日志的集中存储、搜索和可视化
- **异常检测与安全**：基于 ML Commons 的实时异常检测，Agent 行为监控
- **Dashboard 可观测性**：Agent 的追踪数据和指标在 OpenSearch Dashboard 中可视化展示
- **全文搜索引擎**：传统的关键词搜索场景（电商商品搜索、帮助文档搜索等）

## 技术要点
- **k-NN 向量搜索**：通过 k-NN 插件，支持 HNSW 和 IVF 两种向量索引算法，向量搜索与全文搜索在同一查询中混合使用
- **BM25 + 向量混合搜索**：`hybrid` query 在 ES 级别融合文本相关性和向量相似度分数，归一化排序
- **ML Commons 插件**：内置机器学习框架，支持预训练模型加载和在线推理，可做文本 embedding 等任务
- **Neural Search V2**：进一步简化 AI 搜索的开发体验，自动处理 embedding 生成和检索
- **Lucene 引擎**：继承自 Elasticsearch 的成熟分布式搜索架构，分片/副本/快照恢复经过大规模生产验证
- **兼容 Elasticsearch**：API 和生态工具（Kibana / Logstash / Beats）几乎完全兼容
- **Alerting + Anomaly Detection**：内置告警引擎和 ML-based 异常检测，适合 Agent 运维监控

## 技术栈
Java, Lucene, k-NN Plugin, ML Commons, OpenSearch Dashboard, Apache 2.0

## 关联
- [`chroma-core/chroma`](../chroma/) / [`milvus-io/milvus`](../milvus/) / [`qdrant/qdrant`](../qdrant/) — 向量数据库竞品
- Elasticsearch — 上游项目（已分叉），团队管理和社区治理模式变更为 OpenSearch 的核心驱动力
- [`langfuse/langfuse`](../../agent-runtime/observability/langfuse/) — Agent 追踪数据可写入 OpenSearch 分析

## 开放问题
- [ ] 2026-07-02 OpenSearch 的 k-NN 性能与专用向量数据库（Qdrant/Milvus）在高维向量（如 4096d embedding）下的差距有多大？
