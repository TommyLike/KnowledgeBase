# modelcontextprotocol

> [`modelcontextprotocol/modelcontextprotocol`](https://github.com/modelcontextprotocol/modelcontextprotocol) · 上游贡献 · Anthropic 提出的 AI 与外部工具/数据源对接的开放协议标准，定义 Client-Server 的 JSON-RPC 工具调用规范

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · TypeScript · 2,919n/3,977e  
<!-- END AUTO -->

---

## 定位
> MCP (Model Context Protocol) 是 2025-2026 年 Agent 生态中最重要的协议标准之一——由 Anthropic 提出，目标是成为「AI 应用的 USB-C 接口」。MCP 定义了 LLM Client（如 Claude Desktop）与外部工具/数据 Server 之间的标准化通信协议：Server 暴露 `tools/list`、`tools/call`、`resources/read` 等 JSON-RPC 端点，Client 通过标准协议发现和调用。在 Agent 生态中，MCP 是解决「每个 Agent 框架都要写一遍工具集成」问题的关键——一次编写 MCP Server，所有 MCP Client 框架都能用。团队深度关注此项标准。

## 项目介绍
> **AI 与外部世界连接的开放标准——让任何 LLM 通过统一协议访问文件系统、数据库、API 和第三方服务。**

核心场景：
- **统一工具接口**：MCP Server 一次开发，所有 MCP Client（Claude Desktop、Cursor、VS Code Copilot 等）即插即用
- **Agent 访问外部系统**：Agent 通过 MCP Server 访问文件系统、PostgreSQL 数据库、Slack API、Jira 等
- **AI IDE 集成**：VS Code/Cursor/IntelliJ 通过 MCP 为 AI 编程助手提供项目上下文和工具访问
- **Enterprise Tool Gateway**：企业部署 MCP Gateway，统一管理和审计所有 AI 工具调用
- **多 Agent 工具共享**：多个 Agent 实例共享同一套 MCP Server，工具复用，权限集中管理

## 技术要点
- **JSON-RPC 2.0 传输层**：基于 JSON-RPC 2.0 的请求-响应协议，支持 stdio（本地进程通信）和 HTTP+SSE（远程通信）两种传输方式
- **三大核心原语**：Tools（LLM 可调用的功能函数）、Resources（结构化数据读取，如文件/数据库查询）、Prompts（预定义的可重用提示模板）
- **Tool 发现机制**：Client 通过 `tools/list` 发现可用的工具及其参数 schema（JSON Schema 格式），LLM 自主决定何时调用哪个工具
- **双向能力协商**：Server 声明 capabilities（支持的工具/资源/提示类型），Client 声明 roots 和 sampling 能力
- **安全的审批流程**：Client 可要求用户对敏感操作（如文件写入、API 调用）进行确认后才实际执行
- **Python/TypeScript 双 SDK**：`mcp` (TypeScript) + `mcp` (Python) SDK 让开发者用熟悉语言快速开发 MCP Server
- **多传输支持**：stdio（本地进程）+ Streamable HTTP（远程）+ WebSocket（待定），支持不同部署拓扑

## 技术栈
TypeScript, Python, JSON-RPC 2.0, JSON Schema, SSE, HTTP, MIT (spec)

## 关联
- [`a2aproject/A2A`](../A2A/) — 互补协议，MCP 定义 Agent↔Tool 通信，A2A 定义 Agent↔Agent 通信
- [Anthropic](https://www.anthropic.com) — 协议发起方，Claude Desktop 是 MCP 的首个参考 Client 实现
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — LangChain MCP Adapter，支持 LangChain Agent 通过 MCP 调用工具
- [`agentic-community/mcp-gateway-registry`](../../gateway/mcp-gateway-registry/) — MCP Server 注册中心和服务网关
- [`kagent-dev/kagent`](../../../agent-framework/kagent/) — K8s 原生 Agent 框架，深度集成 MCP

## 开放问题
- [ ] 2026-07-02 MCP 协议是否会被 IETF/W3C 等正式标准化组织采纳？Streamable HTTP 传输层的规范是否稳定？
