# beads

> [`gastownhall/beads`](https://github.com/gastownhall/beads) · 上游贡献 · 面向 AI Agent 的高性能混合搜索引擎，原生融合向量语义搜索、全文索引和图关系查询

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Go · 24,180n/118,488e  
<!-- END AUTO -->

---

## 定位
> Beads 是 AI 搜索引擎领域的新生力量，尝试将向量搜索、全文索引和图查询融合为单一引擎。与传统向量数据库需要外部全文搜索（Elasticsearch）和图数据库（Neo4j）不同，Beads 的目标是在一个引擎内完成三种搜索范式的统一。24k nodes 的规模表明其代码复杂度较高。团队关注统一搜索引擎在 Agent Memory 场景中的实用价值。

## 项目介绍
> **AI Agent 的统一搜索引擎——不需要 Elasticsearch + Qdrant + Neo4j 三个系统，Beads 一个引擎搞定向量、全文和图查询。**

核心场景：
- **Agent 统一检索**：Agent 的语义搜索 + 关键词搜索 + 关系遍历在一个查询中组合
- **知识图谱增强 RAG**：实体关系图 + 语义搜索混合，提升复杂问题的检索精度
- **实时混合索引**：数据写入时同时建立向量/全文/图三种索引，查询自动选择最优策略

## 技术要点
- **三合一混合索引**：向量（HNSW 等）+ 全文（倒排索引）+ 图（邻接表）在单一引擎中维护
- **统一查询语言**：一种查询语法同时表达语义搜索、关键词过滤和图遍历
- **Go 实现**：从头用 Go 构建，内存效率和并发性能优于 Python/Java 实现
- **嵌入式模式**：可作为 Go 库嵌入 Agent 进程，也可独立部署为服务

## 技术栈
Go, HNSW, 倒排索引, 图数据库引擎, Apache 2.0

## 关联
- [`chroma-core/chroma`](../../../agent-storage/chroma/) / [`qdrant/qdrant`](../../../agent-storage/qdrant/) — 纯向量数据库，Beads 增加了全文和图查询
- [Elasticsearch](https://www.elastic.co/elasticsearch/) + Neo4j — Beads 试图替代的传统组合

## 开放问题
- [ ] 2026-07-02 三合一混合索引在写入性能上是否有显著瓶颈？向量+全文+图的同步更新一致性如何保证？
