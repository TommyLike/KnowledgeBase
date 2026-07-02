# A2A

> [`a2aproject/A2A`](https://github.com/a2aproject/A2A) · 上游贡献 · Google 提出的 Agent-to-Agent 开放协议，定义 Agent 之间发现、协商和任务委托的标准化通信规范

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> A2A (Agent-to-Agent Protocol) 是 2025 年 Google 推出的 Agent 间通信协议标准，解决「不同框架/不同厂商的 Agent 如何协作」这一生态刚需。与 MCP（Agent↔Tool 通信）形成互补：MCP 解决 Agent「用什么工具」的问题，A2A 解决 Agent「找谁帮忙」的问题。在 Multi-Agent 和 Agent Mesh 架构中，A2A 是关键的互操作层。团队关注这个协议的标准化进程和行业采纳情况。

## 项目介绍
> **Agent 之间的「名片」和「对话协议」——让不同框架、不同厂商的 Agent 能互相发现、协商任务和交换结果。**

核心场景：
- **跨框架 Agent 协作**：LangChain Agent 发现并委派子任务给 AutoGen Agent，通过 A2A 协议标准化通信
- **Agent Mesh 架构**：企业内部多个 Agent 通过 A2A 组成网格，每个 Agent 暴露 Agent Card 声明能力
- **Agent 市场/目录**：Agent 发布 Agent Card 到注册中心，其他 Agent 按任务类型搜索和选择
- **任务委派与结果回传**：主 Agent 将子任务委托给专业 Agent，通过 A2A Task 生命周期管理任务状态
- **异步长任务**：Agent 接收到任务后异步执行，通过 A2A 的流式更新和状态查询机制回传进度

## 技术要点
- **Agent Card 发现机制**：每个 Agent 通过 `/agent-card` 端点发布 JSON 能力描述（技能、模型、端点 URL、认证方式），这是 Agent 间互相发现的基础
- **Task 生命周期管理**：Task 有明确的 `submitted → working → completed/failed/canceled` 状态机，支持长任务（数小时甚至数天）
- **多模态内容**：Task 消息支持 text / image / audio / file 等 Part 类型，Agent 可交换多媒体信息
- **流式更新 SSE**：通过 Server-Sent Events 实现任务进度的实时推送，Agent 无需轮询
- **HTTP/JSON-RPC 基础**：基于 HTTP + JSON 的简单协议，避免复杂的二进制协议或消息队列依赖
- **认证与安全**：支持 JWT token 和 OAuth，Agent Card 中声明认证方式
- **多语言 SDK**：提供 Python、TypeScript、Java 等 SDK

## 技术栈
Python, TypeScript, HTTP/JSON, SSE, JWT/OAuth, Apache 2.0

## 关联
- [`modelcontextprotocol/modelcontextprotocol`](../modelcontextprotocol/) — 互补协议，MCP 是 Agent↔Tool，A2A 是 Agent↔Agent
- [Google](https://blog.google/technology/ai/a2a-agent-protocol/) — 协议发起方
- [`langchain-ai/langgraph`](../../../agent-framework/langgraph/) — Multi-Agent 框架，A2A 可作为跨图通信的标准协议
- [`crewAIInc/crewAI`](../../../agent-framework/crewAI/) — 内置 A2A 协议支持
- [`agentgateway/agentgateway`](../../gateway/agentgateway/) — A2A Agent Gateway，管理 Agent 的接入和路由

## 开放问题
- [ ] 2026-07-02 A2A vs MCP 的分工是否会交叉？Agent 调用另一个 Agent 和 Agent 调用 Tool 的边界越来越模糊——A2A 是否可能在协议层面合并 MCP 的能力？
