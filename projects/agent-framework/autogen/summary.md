# autogen

> [`microsoft/autogen`](https://github.com/microsoft/autogen) · 上游贡献 · 微软推出的多智能体对话式编程框架，基于异步消息传递和事件驱动实现 Agent 间自主协作

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> AutoGen 是微软研究院推出的多 Agent 协作框架，在 Agent 生态中开创了「对话即编程」的范式——Agent 之间通过结构化的对话消息进行任务分工、信息交换和结果整合。目前已进入社区维护模式，官方推荐迁移至 Microsoft Agent Framework。团队将其作为 Agent 框架演进史中的重要参考点，关注多 Agent 对话式协作模式的设计思想及其在后续框架中的延续。

## 项目介绍
> **通过对话驱动多 Agent 自主协作的编程框架，让 AI Agent 像团队会议一样通过多轮对话完成复杂任务。**

核心场景：
- **多 Agent 角色分工**：数学专家 + 代码专家 + 通用助手等角色组成 Agent 团队，各司其职协同解决问题
- **Human-in-the-Loop 协作**：Agent 在关键步骤暂停，等待人类输入反馈后继续执行
- **AutoGen Studio 无代码原型**：通过 Web GUI 拖拽式搭建多 Agent 工作流原型
- **代码生成与执行**：Agent 生成代码 → 另一个 Agent 执行代码 → 结果反馈形成闭环
- **跨语言运行时**：Python（Core/AgentChat/Extensions）+ .NET（Core.Grpc），满足不同企业技术栈

## 技术要点
- **分层架构**：Core API（消息传递+事件驱动）→ AgentChat API（高层对话抽象）→ Extensions API（LLM 客户端、代码执行、MCP 工具），层次分明可独立选用
- **异步消息传递**：Agent 间通过消息总线通信，支持 Topic 订阅和点对点消息，实现了松耦合的多 Agent 交互
- **对话驱动 Agent**：使用 AssistantAgent 封装 LLM，通过 GroupChat 将多个 Agent 组织成对话圈，由 GroupChatManager 控制发言顺序
- **代码执行沙箱**：内置 Docker 代码执行器，Agent 生成的代码在隔离容器中运行，支持本地命令行和 Docker 两种模式
- **MCP 协议集成**：原生支持 Model Context Protocol，可将外部 MCP Server（如 Playwright）作为 Agent 工具接入
- **AgentTool 嵌套**：允许将一个完整 Agent 封装为另一个 Agent 的工具，实现递归式 Agent 协作
- **可插拔 LLM 客户端**：支持 OpenAI、Azure OpenAI，可扩展对接其他模型提供商

## 技术栈
Python (61.7%), C# (25.1%), TypeScript (12.4%), OpenAI GPT-4o, gRPC, MCP, Docker

## 关联
- [`microsoft/semantic-kernel`](../semantic-kernel/) — 同为微软出品，SK 定位企业级 AI 编排 SDK，AutoGen 定位多 Agent 对话式协作
- [`langchain-ai/langgraph`](../langgraph/) — 竞品，LangGraph 用状态图编排，AutoGen 用对话编排
- [`crewAIInc/crewAI`](../crewAI/) — 竞品，CrewAI 提供更高层的角色型多 Agent 抽象
- Microsoft Agent Framework — 官方继任者，整合 AutoGen + Semantic Kernel 为统一企业 Agent 框架

## 开放问题
- [ ] 2026-07-02 AutoGen 进入维护模式后，其对话式多 Agent 编排范式在 Microsoft Agent Framework 中是保留核心地位、还是被其他模式替代？
