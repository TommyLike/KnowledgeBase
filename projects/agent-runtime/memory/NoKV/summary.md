# NoKV

> [`NoKV-Lab/NoKV`](https://github.com/NoKV-Lab/NoKV) · 上游贡献 · 去 Key-Value 化的新型存储引擎，以无 Schema 的文档存储模型为 AI Agent 提供灵活的记忆持久化

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> NoKV 探索「非 KV」的存储范式——传统 KV 存储将所有数据以 Key-Value 对存储，而 NoKV 使用更接近文档/对象的原生存储模型，减少 Agent 应用中的序列化开销和 Schema 设计负担。

## 项目介绍
> **超越 Key-Value 的存储引擎——Agent 的对象和状态直接以原生格式持久化。**

核心场景：
- **Agent 状态持久化**：会话状态以原生对象形式存储和恢复
- **灵活 Schema**：无预定义 Schema，适应 Agent 记忆的动态结构

## 技术要点
- **非 KV 存储模型**：对象/文档原生存储，去 Key-Value 抽象层
- **无 Schema 设计**：存储结构自适应数据形状
- **轻量嵌入**：可作为库嵌入 Agent 进程

## 技术栈
Rust, MIT

## 关联
- [`chroma-core/chroma`](../../../agent-storage/chroma/) — Chroma 是向量存储，NoKV 是非 KV 的文档存储

## 开放问题
- [ ] 2026-07-02 非 KV 存储在读写吞吐和并发性能上与成熟 KV 引擎（RocksDB）的差距？
