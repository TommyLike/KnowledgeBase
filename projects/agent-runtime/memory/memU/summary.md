# memU

> [`NevaMind-AI/memU`](https://github.com/NevaMind-AI/memU) · 上游贡献 · 面向 LLM/AI Agent 的 Agentic Memory 框架，将多模态原始数据编译为三层持久化记忆工作区

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> memU 是 Agentic Memory 领域的重要开源方案，将对话、文档、工具调用轨迹等原始数据编译为三层结构化记忆（Resource/Item/Category），使 Agent 具备跨会话的上下文连续性，而无需每次推理时将完整历史塞入 prompt。我们将其纳入 KG 以追踪 Agent Memory 这一基础设施方向的技术演进，对比 mem0、Zep/Letta 等同类方案的设计取舍，为团队在 Agent 应用中的记忆层选型提供参考。

## 项目介绍
> **面向 LLM Agent 的 Agentic Memory 框架，自动将多模态交互数据编译为结构化、可检索、持久化的三层记忆工作区。**

核心场景：
- **跨会话持久记忆**：Agent 用户在多次对话中保持一致的个人档案、偏好和目标记忆，无需每次重复自我介绍
- **工具模式自学习**：从 Agent 的工具调用轨迹中自动提取可复用的工作流（Skill），下次遇类似任务直接匹配
- **多模态知识库构建**：将文档、图片、音视频、URL 等混合输入统一索引为结构化记忆，支持 RAG 或 LLM 两种检索策略
- **主动性 Agent**：基于 salience-aware 强化记忆追踪（reinforcement_count），Agent 可自主识别待办任务并主动推进
- **多租户记忆服务**：通过 memU-server + memU-ui 提供带用户系统、RBAC 的企业级记忆中台

## 技术要点
- **三层记忆架构**：Resource（原始素材，不可变）→ Item（原子记忆单元，含 profile/event/knowledge/behavior/skill/tool 六种类型）→ Category（自动聚类主题文件夹 + 摘要 + embedding），层间可溯源，支持记忆更新后自动重编译
- **双检索策略**：rag 模式基于 pgvector/SQLite 向量余弦相似度快速召回；llm 模式由 LLM 直接做深层语义排序，更深但更慢，用户可按场景自由切换或组合
- **六类定型记忆抽取**：将原始输入自动分类为 profile（身份偏好）、event（事件）、knowledge（知识）、behavior（行为模式）、skill（技能）、tool（工具执行统计含耗时/Token/成功率），分类即定型，便于下游精准检索
- **自组织文件夹**：无需手动打标签，框架自动按主题构建 Category 树，生成链接、摘要和 embedding，支持记忆合并与去重
- **Salience 强化记忆**：为每条记忆维护 reinforcement_count 和 last_reinforced_at，高频访问的记忆权重自动提升，实现"越用越聪明"的遗忘/强化机制
- **Tool Memory 去重与统计**：基于 MD5 哈希对工具调用去重，跟踪执行成功率、耗时、Token 成本，自动生成 when_to_use 使用建议
- **多后端存储**：支持 in-memory（原型验证）、SQLite（本地开发）、PostgreSQL + pgvector（生产）三种存储后端，架构统一接口层隔离
- **可配置 LLM Profile**：chat / embedding / vision / transcription 四大推理能力分别路由到不同模型（OpenAI / DeepSeek / Gemini / Voyage / OpenRouter），灵活控制成本与精度

## 技术栈
Python 3.13+ (含 Rust 扩展), uv 包管理, asyncio 异步框架, SQLite / PostgreSQL + pgvector, OpenAI / DeepSeek / Gemini / OpenRouter / Voyage, MarkItDown 文档解析

## 关联
- [`memory/mem0`](../mem0/) — 同类竞品，侧重轻量 API 的 Agent Memory 框架
- [`memory/letta`](../letta/) — 同类竞品（前身 MemGPT），以 OS 视角管理 Agent 记忆
- [`memory/zep`](../zep/) — 同类竞品，面向企业级 Agent 的持久化记忆服务

## 开放问题
- [ ] 2026-07-02 三层架构的编译开销在长会话下是否会成为瓶颈？Resource → Item 的抽取依赖 LLM 调用，高频交互场景下 Token 成本如何优化？
- [ ] 2026-07-02 memU 与 mem0 在跨会话检索准确率（Locomo Benchmark 92.09%）上的表现差异成因是什么？是否与六类定型分类策略直接相关？
- [ ] 2026-07-02 memU-server 的多租户 RBAC 实现与 Zep 的企业级方案相比有何优劣势？
- [ ] 2026-07-02 框架强制要求 Python 3.13+ 是否限制了实际落地场景（企业环境 Python 版本往往较旧）？
