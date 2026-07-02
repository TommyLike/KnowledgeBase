# mempalace

> [`MemPalace/mempalace`](https://github.com/MemPalace/mempalace) · 上游贡献 · 本地优先、纯原文检索的 AI 长期记忆系统，LongMemEval 基准第一

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> MemPalace 是 AI Agent 长期记忆领域的一个独特方案：它拒绝传统的 LLM 摘要/抽取范式，坚持**原文存储 + 结构化检索**路线，在 LongMemEval 上以 96.6% R@5（无 LLM）达到基准最高分。其"记忆宫殿"隐喻将空间记忆术与 Zettelkasten 方法结合，提供 Wing/Room/Drawer 多层命名空间结构，仅此结构就比平铺检索提升 +34% 召回。对于关注 AI 记忆系统演进方向、特别是"不用 LLM 记忆"路线的团队，该项目是重要的对照参考。

## 项目介绍
> **MemPalace 是一个开源、本地优先的 AI 长期记忆系统，将对话历史作为原文逐字存储，通过语义检索和结构化"记忆宫殿"实现高效回忆，不做摘要、不抽取、不改写。**

核心场景：
- **AI Agent 跨会话记忆**：与 Claude Code、Gemini CLI、Cursor IDE 等集成，通过 MCP Server 提供 35 个记忆工具，Agent 在会话开始时通过 `wake-up` 用约 170 tokens 加载身份和关键事实即可恢复上下文
- **代码项目知识挖掘**：`mempalace mine` 可将整个项目代码库、文档、笔记吸入记忆宫殿，后续通过语义搜索快速定位历史决策、架构讨论、代码修改原因
- **多 Agent 协作记忆**：每个 Specialist Agent 在宫殿中拥有独立 Wing 和 Diary，运行时通过 `mempalace_list_agents` 互相发现，无需膨胀 system prompt
- **时间感知知识图谱**：存储带有效时间窗口的实体-关系三元组，支持 `as_of` 时间点查询、事实过期自动失效、矛盾检测，避免 AI 基于过时信息行动
- **隐私敏感场景**：默认全部本地运行（ChromaDB + SQLite），零遥测，无需 API Key，外部后端（Qdrant、pgvector）需显式 opt-in

## 技术要点
- **记忆宫殿结构（Method of Loci）**：借鉴古希腊空间记忆术，将信息组织为 Wing（人或项目）→ Room（具体话题，如 "auth-migration"）→ Drawer（原始原文对话，永不摘要）→ Closet（AAAK 压缩摘要，指向原文）的层次空间结构。Hall 是跨 Wing 共享的记忆类型走廊（facts/events/discoveries/preferences/advice），Tunnel 是不同 Wing 中相同话题的跨 Wing 连接。仅结构层次就比平铺检索提升 +34% 召回率（60.9% → 94.8% R@10）
- **纯原文存储策略**：与 Mem0、Zep、Hindsight 等做 LLM 摘要/抽取的方案不同，MemPalace 的核心设计哲学是"不做摘要"——所有对话以原文逐字保存在 Drawer 中，语义检索在原文向量上执行。这避免了 LLM 摘要引入的信息畸变和关键细节丢失，也是其 LongMemEval 96.6% R@5 的基础
- **AAAK 压缩方言**：Annotated Abstract Artifact Kode，一种为 AI Agent 设计的简写方言。约 30 倍压缩率（将数月上下文压缩至约 120 tokens），无需解码器——Claude、GPT、Gemini、Llama、Mistral 均可原生阅读。需注意这是有损压缩（实体编码、句子截断），在小规模下不节省 tokens，AAAK 模式在 LongMemEval 上 R@5 为 84.2%，低于原文模式的 96.6%
- **4 层记忆加载栈**：L0（身份描述，约 50 tokens，始终加载）→ L1（关键事实：团队/项目/偏好，约 120 tokens AAAK，始终加载）→ L2（房间召回：当前会话、当前项目相关，按需加载）→ L3（深度搜索：全宫殿语义检索，显式触发）。Agent 醒来仅需约 170 tokens
- **混合检索管线**：原始语义搜索（embeddinggemma-300m 或 all-MiniLM-L6-v2）为基础，混合模式叠加关键词增强、时间邻近度增强、偏好模式提取等启发式策略。可选的 LLM Rerank 阶段支持 Claude Haiku/Sonnet、minimax-m2.7 等模型，可将 LongMemEval R@5 推到 99%+
- **可插拔存储后端**：默认 ChromaDB（本地向量存储），替代方案包括 sqlite_exact（本地精确向量校验）、Qdrant（REST 外部向量库）、pgvector（Postgres JSONB 存储）。外部后端通过环境变量配置，自动写本地标记文件防止误连，明确声明"数据离开本机"是显式 opt-in 行为
- **时间知识图谱**：基于本地 SQLite 的实体-关系图，每条三元组带有效时间窗口（valid_from/valid_to），支持 add/query/invalidate/timeline 四种操作。`as_of` 参数支持时间点查询（"X 日期时我们知道什么"），旧事实 invalidate 而非删除，自动检测矛盾（错误关联、任期不匹配等）
- **MCP Server（35 个工具）**：覆盖宫殿读写、知识图谱操作、跨 Wing 导航、Drawer 管理、Agent Diary 等功能。通过 stdio JSON-RPC 协议与任何 MCP 兼容客户端（Claude Code、Gemini CLI、Cursor IDE 等）集成
- **自动保存 Hook**：内置 Claude Code、Codex CLI、Cursor IDE 的自动保存钩子，在会话中定期保存和上下文压缩前触发。`mempalace sweep` 命令支持逐消息级别的 idempotent 召回，断点续传安全
- **嵌入模型可选**：首次安装时提供 onboarding 选择——推荐 embeddinggemma-300m（多语言、100+ 种语言支持、约 300 MB）或 all-MiniLM-L6-v2（仅英文、约 30 MB），无需 GPU

## 技术栈
Python 3.9+, ChromaDB, SQLite, embeddinggemma-300m / all-MiniLM-L6-v2, gRPC, numpy, Docker (CPU/GPU), MCP stdio JSON-RPC, Qdrant (可选), pgvector (可选)

## 关联
- [`agent-runtime/memory/mem0`](../mem0/) — 同类 AI 记忆系统，LLM 摘要/抽取路线，与 MemPalace 的原文路线形成对照
- [`agent-runtime/memory/letta`](../letta/) — Agent 记忆平台，侧重记忆管理框架和 Agent 状态持久化，互补关系
- [`agent-runtime/memory/hindsight`](../hindsight/) — 同类 AI 记忆系统，事件抽取路线，同为对照参考

## 开放问题
- [ ] 2026-07-02 AAAK 有损压缩在原文路线中的定位是什么？既然原文模式 96.6% > AAAK 84.2%，AAAK 主要适用场景是上下文窗口极小（如 170 tokens 的 L1 层）的场景，但在上下文窗口快速扩大的趋势下，这个优势会不会被稀释？
- [ ] 2026-07-02 MemPalace 坚持"不做摘要"的哲学在超长对话（数万轮）场景下是否面临检索精度和存储成本的瓶颈？目前 LongMemEval 仅 500 问，LoCoMo 仅 1986 问，实际生产环境的 scale 验证还不充分
- [ ] 2026-07-02 项目由非专业开发者（Milla Jovovich 为演员背景）在 Claude Code 辅助下构建，其架构决策在多大程度上受 AI 辅助编码影响？这对 AI 辅助开发的工程实践有何启示？
