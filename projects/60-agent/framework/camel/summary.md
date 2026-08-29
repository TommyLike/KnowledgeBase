# camel

> [`camel-ai/camel`](https://github.com/camel-ai/camel) · 上游贡献 · 最早的多 Agent 框架之一，聚焦「寻找 Agent 规模定律」，支持百万级 Agent 社会模拟和角色扮演协作

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> CAMEL 是多 Agent 协作框架的开创者——在 2023 年就提出了角色扮演式 Agent 协作（Communicative Agents），是第一个多 Agent 框架学术成果（NeurIPS 2023）。在生态中，CAMEL 定位独特：不追求生产级编排（如 CrewAI），而是研究导向——探索 Agent 数量、协作模式、角色关系与任务完成效率之间的「规模定律」。团队关注其大规模 Agent 社会模拟的研究方法和 Code-as-Prompt 设计哲学。

## 项目介绍
> **多 Agent 框架的学术先驱——从角色扮演式协作起步，发展到支持百万级 Agent 的社会规模模拟与研究平台。**

核心场景：
- **角色扮演式任务协作**：Agent 扮演不同专业角色（医生、律师、工程师），通过结构化对话协同完成任务
- **大规模 Agent 社会模拟**：模拟高达百万 Agent 的交互行为，用于社会行为实验和 AI 社会研究（OASIS 项目）
- **LLM 训练数据生成**：通过多 Agent 交互自动生成思维链数据、指令数据等高质量训练集
- **RAG Agent 集成**：Agent + 知识库问答，支持向量数据库和检索增强的多轮对话
- **学术 Benchmark**：内置多种标准化 Agent 能力评估基准，支持可复现的 Agent 能力比较

## 技术要点
- **Code-as-Prompt 设计原则**：代码即 Agent 的 prompt，要求代码结构清晰到人和 Agent 都能理解——这是该框架最独特的设计哲学
- **百万级 Agent 架构**：为大规模仿真设计的通信和资源管理架构，支持高效的多 Agent 并发
- **角色扮演器 RolePlaying**：TaskSpecifyAgent + AssistantAgent + CriticAgent 三角协作，明确角色分配和任务边界
- **四大模块化设计**：Agents / Agent Societies / Data Generation / Models / Tools / Memory / Storage 等十余个独立模块
- **有状态记忆**：Agent 在多次交互间保留历史上下文，支持多轮交互的持续学习和上下文关联
- **多模型支持**：OpenAI / Anthropic / DeepSeek / Qwen / Ollama 等 20+ 模型后端可插拔
- **OWL 多 Agent 研究系统**：基于 CAMEL 构建的面向任务的多 Agent 系统，支持浏览器自动化、代码执行等复杂场景

## 技术栈
Python (95.9%), TypeScript, uv, OpenAI API, Apache 2.0

## 关联
- [OWL](https://github.com/camel-ai/owl) — 同一团队，基于 CAMEL 的多 Agent 任务自动化系统
- [OASIS](https://github.com/camel-ai/oasis) — 同一团队，百万级 Agent 社会模拟项目
- [`microsoft/autogen`](../autogen/) — 同为学术风格多 Agent 框架，AutoGen 偏对话驱动，CAMEL 偏角色扮演
- [ChatDev](https://github.com/OpenBMB/ChatDev) — 第三方，用 CAMEL 做多 Agent 软件开发的研究项目

## 开放问题
- [ ] 2026-07-02 百万级 Agent 模拟的瓶颈在哪？大规模并发下 Agent-to-Agent 通信的可扩展性如何？
