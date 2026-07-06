# TencentDB-Agent-Memory

> [`TencentCloud/TencentDB-Agent-Memory`](https://github.com/TencentCloud/TencentDB-Agent-Memory) · 上游贡献 · 腾讯云开源的 Agent 长期记忆系统，全本地部署，为 AI Agent 提供持久化上下文记忆能力

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> TencentDB-Agent-Memory 是腾讯云在 Agent 记忆领域的开源探索，解决 AI Agent「失忆」问题——让 Agent 在跨会话、跨场景下保持对用户偏好、历史交互、知识的长期记忆。不同于云端托管的记忆方案（如 ChatGPT Memory），本项目的核心卖点是**全本地部署**，数据完全留在用户侧，满足隐私敏感场景（企业内网、合规行业）的刚需。团队作为上游贡献者，关注 Agent 记忆层的架构演进与社区反馈。

## 项目介绍
> **为 AI Agent 提供全本地、持久化的长期记忆系统——记住用户偏好、历史上下文和知识事实，让 Agent 越用越聪明。**

核心场景：
- **个性化 Agent 助手**：记住用户姓名、偏好、习惯、历史任务，跨会话保持一致的交互体验，避免每次对话「从零开始」
- **企业知识 Agent**：沉淀企业内部知识、项目上下文、决策历史，Agent 可基于长期记忆给出更精准的回答和建议
- **客户服务 Agent**：记录客户画像、历史工单、偏好沟通方式，客服 Agent 在多轮服务中保持上下文连贯
- **研发辅助 Agent**：记住项目架构决策、代码变更历史、Bug 修复经验，研发 Agent 在代码审查和问题定位中提供上下文感知的建议
- **私密合规场景**：全本地部署确保用户数据不出境/不出企业网络，适合金融、医疗、政府等强合规行业

## 技术要点
- **全本地部署架构**：记忆存储和检索全部在用户本地环境完成，无需连接云端服务，数据主权完全归用户所有
- **长期记忆管理**：支持记忆的创建、更新、检索和过期淘汰，模仿人脑的遗忘曲线机制，自动清理低价值或过时记忆
- **向量化检索**：记忆内容通过 Embedding 模型向量化后存储，语义检索替代关键词匹配，支持模糊意图的精准回忆
- **多模态记忆**：不仅记忆文本对话，还支持代码片段、结构化数据、文档内容的记忆与检索
- **Agent 集成接口**：提供与主流 Agent 框架（LangChain、LlamaIndex 等）的适配接口，Agent 可透明接入记忆层
- **记忆安全与隔离**：支持多租户记忆隔离，不同的 Agent/用户之间的记忆空间完全独立

## 技术栈
Python, Vector Database (ChromaDB / Milvus / FAISS), Embedding Models, LangChain / LlamaIndex 集成, SQLite / PostgreSQL (元数据存储), Apache 2.0

## 关联
- [`mem0ai/mem0`](../../agent-runtime/mem0ai/mem0/) — Mem0 是另一款 Agent 记忆层，提供托管云服务和开源版，TencentDB-Agent-Memory 强调全本地部署的差异化定位
- [`langchain-ai/langchain`](../../agent-framework/langchain-ai/langchain/) — LangChain Memory 模块是 Agent 记忆的早期探索，TencentDB-Agent-Memory 可作为其记忆后端
- [`letta-ai/letta`](../../agent-runtime/letta-ai/letta/) — Letta（原 MemGPT）提供 OS 级记忆管理，TencentDB-Agent-Memory 侧重数据库级持久化

## 开放问题
- [ ] 2026-07-05 全本地部署下，多设备/多终端之间的记忆同步机制如何实现？是否需要引入 P2P 同步或自建同步服务？
- [ ] 2026-07-05 长期记忆的遗忘策略如何平衡召回率和存储开销？在记忆量达到百万级时检索延迟是否可控？
- [ ] 2026-07-05 与腾讯云 TDSQL / 向量数据库产品的集成路径是什么？是否计划提供托管版？
