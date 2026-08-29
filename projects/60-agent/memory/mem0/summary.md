# mem0

> [`mem0ai/mem0`](https://github.com/mem0ai/mem0) · 上游贡献 · AI 原生的 Agent 记忆层，将对话历史和用户偏好自动提取为结构化记忆，提供跨会话的个性化上下文

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Python · 11,479n/41,048e  
<!-- END AUTO -->

---

## 定位
> Mem0 是 Agent Memory 细分领域的先行者——提供一个独立的记忆层 API，让 Agent「记住」用户偏好、历史决策和关键上下文。在 Agent 生态中，Mem0 解决了「每次对话都从零开始」的核心痛点：Agent 通过 Mem0 存储和检索长期记忆，实现跨会话的个性化和连贯性。团队关注 Agent Memory 的分类学（用户记忆/会话记忆/知识记忆）和检索策略的演进。

## 项目介绍
> **Agent 的「海马体」——自动提取、存储和检索用户交互中的关键信息，让每次对话都能延续上一次的上下文。**

核心场景：
- **个性化 Agent**：Agent 记住用户姓名、偏好、习惯，不同用户使用同一 Agent 获得个性化体验
- **跨会话上下文延续**：上次数小时前的对话，Agent 本次仍记得关键决策和待办事项
- **用户画像自动构建**：从多轮交互中自动提取用户特征、兴趣和偏好
- **减少重复信息输入**：用户说过的背景信息自动记忆，不再每次都问「您是什么角色/公司/场景」
- **知识积累**：Agent 在使用过程中持续积累领域知识，越用越聪明

## 技术要点
- **Mem0 三层记忆分类**：User Memory（用户画像、偏好）+ Session Memory（当前会话上下文）+ Agent Memory（Agent 自身的知识积累），三类记忆独立管理但统一检索
- **自动记忆提取**：不依赖开发者手动 add，Mem0 自动从对话消息中提取和更新记忆条目（通过 LLM 驱动的提取 Pipeline）
- **双存储引擎**：向量数据库（Qdrant/Chroma/Weaviate/Pinecone 等可插拔）+ 图数据库（Neo4j），向量负责语义检索，图负责记忆间关系
- **记忆冲突与更新**：同一主题的新记忆自动更新旧记忆，支持记忆衰减、合并和删除
- **多粒度检索**：顶层语义检索 → 底层关系图遍历，兼顾宽泛和精确的记忆匹配
- **API-First 设计**：`mem0.add()` / `mem0.search()` / `mem0.update()` 四个核心 API，Python/TypeScript SDK
- **LLM 无关**：记忆提取和检索依赖的 LLM 可配置（OpenAI/Anthropic/Gemini/等）

## 技术栈
Python, Qdrant/Chroma/Weaviate (向量), Neo4j (图), OpenAI/Anthropic API, Apache 2.0

## 关联
- [`letta-ai/letta`](../letta/) — 竞品，Letta 也提供 Agent 记忆管理，但更侧重自托管和 Stateful Agent
- [`chroma-core/chroma`](../../../agent-storage/chroma/) — Mem0 支持的向量存储后端之一
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — LangChain 的 Memory 模块竞品，Mem0 更独立和专注

## 开放问题
- [ ] 2026-07-02 记忆提取的 LLM 成本如何控制？高频对话下自动提取是否会造成高昂的 LLM API 费用？
