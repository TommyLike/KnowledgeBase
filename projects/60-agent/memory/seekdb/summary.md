# seekdb

> [`oceanbase/seekdb`](https://github.com/oceanbase/seekdb) · 上游贡献 · OceanBase 推出的 AI 原生分布式搜索数据库，将全文搜索和向量检索深度集成到关系型分布式数据库中

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> SeekDB 是 OceanBase（蚂蚁集团分布式数据库）团队在 AI 搜索方向的探索——将向量搜索和全文搜索能力内建到分布式 SQL 数据库中。在 Agent 基础设施中，SeekDB 代表了「一个数据库解决所有查询」的愿景。

## 项目介绍
> **SQL + 向量 + 全文一体——在分布式关系数据库中原生获得 AI 搜索能力。**

核心场景：
- **Agent 数据一站式存储**：结构化数据 + 向量索引 + 全文搜索在同一数据库中
- **大规模分布式搜索**：OceanBase 分布式能力支撑十亿级文档

## 技术要点
- **OceanBase 分布式底座**：Paxos 共识、自动分片、异地多活
- **内建向量索引**：与 SQL 引擎深度集成的 HNSW
- **SQL 原生向量查询**：`ORDER BY vec_distance` 作为标准 SQL 语法

## 技术栈
C++, SQL, OceanBase, HNSW, Paxos, Apache 2.0

## 关联
- [OceanBase](https://github.com/oceanbase/oceanbase) — 上游数据库引擎
- [`milvus-io/milvus`](../../../agent-storage/milvus/) — 专用向量数据库竞品

## 开放问题
- [ ] 2026-07-02 内建向量搜索的 QPS 能否达到专用向量数据库？分布式特性是否增加向量搜索延迟？
