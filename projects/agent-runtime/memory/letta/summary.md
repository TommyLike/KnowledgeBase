# letta

> [`letta-ai/letta`](https://github.com/letta-ai/letta) · 上游贡献 · 具有自托管持久记忆的开源 Agent 框架，在 Agent 进程中维护有状态的 Memory Block 和自主计算模型

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Letta (前 MemGPT) 是 Agent Memory 领域的学术先驱——最早提出「将 Agent 内存抽象为操作系统虚拟内存」的思想，让 LLM 自主管理其上下文窗口（类似 OS 管理 RAM 和磁盘的页面交换）。在 Agent 生态中，Letta 代表了一种激进的 Agent Memory 哲学：不是外挂向量数据库，而是在 Agent 进程内实现有状态的 Memory Block 管理。团队关注其 Memory 架构的思想创新和 Agentic Memory 的发展方向。

## 项目介绍
> **给 Agent 一个「操作系统级的自管理内存」——Agent 自动决定哪些记忆页面换入上下文，哪些换出到持久化存储。**

核心场景：
- **长对话 Agent**：Agent 维护超出模型上下文窗口的长篇对话历史，自动换入换出记忆块
- **带持久状态的 Agent Server**：Agent 以有状态服务方式部署，状态在重启后保留
- **自托管 Agent Memory**：用户完全控制 Memory 存储，数据不离开自有服务器
- **沙箱化 Agent 环境**：每个 Agent 实例拥有独立文件系统和执行环境

## 技术要点
- **虚拟上下文管理**：源自 OS 虚拟内存概念——LLM 的上下文窗口是「物理内存」，Agent 的完整记忆是「虚拟内存」，LLM 自主决策分页调入/调出
- **Memory Block 模型**：记忆以 Block 为单位（Persona / Human / Conversation / Archival），Agent 自主选择哪些 Block 进当前上下文
- **Self-Editing Memory**：Agent 不仅读取记忆，还能在对话中自我更新记忆——添加、修改、删除记忆块
- **ADEPT 框架**：Server 级别的 Agent 部署框架，支持 REST API 和 WebSocket 的 Agent serving
- **Stateful Agent**：Letta 的 Agent 是有状态实体——拥有独立的 ID、Memory、Context、执行环境，生命周期与进程解耦
- **沙箱化工具执行**：Agent 的代码执行和工具调用在受控环境中运行

## 技术栈
Python, FastAPI, REST/WebSocket, LLM APIs, PostgreSQL, Apache 2.0

## 关联
- [`mem0ai/mem0`](../mem0/) — 竞品，Mem0 提供独立的记忆层 API，Letta 将记忆内嵌在 Agent 进程中
- [`chroma-core/chroma`](../../../agent-storage/chroma/) — Letta 支持的向量存储后端之一
- [MemGPT 论文](https://arxiv.org/abs/2310.08560) — Letta 的学术起源

## 开放问题
- [ ] 2026-07-02 虚拟上下文管理在极端长对话（1000+ 轮）中，LLM 的「自主页面调度」策略是否会退化为低质量决策？
