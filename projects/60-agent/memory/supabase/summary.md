# supabase

> [`supabase/supabase`](https://github.com/supabase/supabase) · 上游贡献 · 开源的 Firebase 替代方案，以 PostgreSQL 为核心为 Agent 应用提供数据库、向量存储、实时订阅和身份认证的后端基础设施

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Supabase 是「开源 Firebase」的标杆，在 Agent 生态中扮演「Agent 应用后端基础设施」的角色。当 Agent 需要持久化存储用户数据、管理对话历史、做向量搜索和实时数据同步时，Supabase 提供了一站式的 PostgreSQL 底座。特别是 pgvector 扩展使其成为最自然的「SQL + 向量」混合方案——Agent 的记忆/知识库/用户数据用同一套 PostgreSQL 查询。

## 项目介绍
> **Agent 应用的开源后端——PostgreSQL 数据库 + 向量搜索 + 实时订阅 + 身份认证，一套后端满足 Agent 所有数据需求。**

核心场景：
- **Agent 用户数据管理**：用户画像、偏好设置、Agent 配置以结构化数据存储
- **Agent 对话历史**：对话记录存储在 PostgreSQL，pgvector 索引支持语义检索历史
- **实时 Agent 协同**：WebSocket 实时推送 Agent 状态变化给前端
- **认证与授权**：Row Level Security 确保每个用户只访问自己的 Agent 数据

## 技术要点
- **pgvector 向量扩展**：PostgreSQL 原生向量存储和搜索，避免独立向量数据库的运维成本
- **PostgREST 自动 REST API**：直接从 PostgreSQL schema 生成 RESTful API，无需后端编码
- **Row Level Security**：数据库级别的行级安全，与认证系统集成实现精细权限控制
- **Realtime 引擎**：通过 PostgreSQL logical replication 实现 WebSocket 实时数据推送
- **自托管或云服务**：开源版 Docker 部署，Supabase Cloud 提供托管服务

## 技术栈
TypeScript, PostgreSQL, pgvector, PostgREST, GoTrue (auth), Elixir (realtime), MIT + EE

## 关联
- [`chroma-core/chroma`](../../../agent-storage/chroma/) / [`qdrant/qdrant`](../../../agent-storage/qdrant/) — 专用向量数据库，当 pgvector 性能不足时的替代方案
- [`letta-ai/letta`](../letta/) — Agent Memory 框架，可用 Supabase 作为存储后端

## 开放问题
- [ ] 2026-07-02 pgvector 在 10M+ 向量规模下的查询性能与专用向量数据库（Qdrant/Milvus）的差距？
