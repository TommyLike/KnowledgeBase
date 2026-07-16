# agentic-api

> [`vllm-project/agentic-api`](https://github.com/vllm-project/agentic-api) · 上游贡献 · vLLM 官方的有状态 Agentic API 层，用 Rust 在推理引擎之上实现 OpenAI Responses API、服务端工具执行和 Codex 兼容

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `acd6846` · Rust · 228文件/3.5MB · 99,281 行 · 103 `.rs` 文件  
**入口** `crates/agentic-server/` (Axum HTTP/SSE/WS 服务) · `crates/agentic-server-core/` (协议类型、执行器、工具框架、持久化)  
**架构** Client → Agentic API Gateway (Rust) → vLLM Core：Responses API 转型层负责状态 hydration、工具 orchestration、持久化存储（SQLite），把原本在客户端的多轮编排逻辑搬到推理服务端  
**热点** Agentic API state machine · tool execution dispatch · Responses protocol translation · SSE/WS transport
<!-- END AUTO -->

---

## 定位
> Agentic API 是 vLLM 生态从「推理引擎」走向「Agent 服务平台」的战略产品。传统 vLLM 只负责模型推理（给 token 返回 token），Agent 应用需要的**对话状态管理、工具调用循环、多轮编排**全部在客户端代码中。Agentic API 把这些逻辑搬到 vLLM 之上成为服务端能力，让客户端只需发送一次 API 调用即可获得完整的 Agent 体验。在 AI Agent 生态中，Agentic API 代表了「推理即服务 → Agent 即服务」的范式升级。团队将其作为 vLLM 从 engine 到 platform 的关键一环跟踪。

## 项目介绍
> **vLLM 的 Agent 能力层——在 vLLM 推理引擎之上实现 OpenAI Responses API 协议，将对话状态、工具执行和多轮编排从客户端搬到服务端。**

核心场景：
- **有状态 Agent 对话**：客户端传 `previous_response_id` 即可延续对话，服务端自动回复上下文，无需客户端重放完整历史
- **服务端工具执行**：Agentic API 区分 gateway-owned / client-owned / provider-owned 三种工具所有权，服务端自动执行 web search 等 gateway 工具，将 client 工具返回给客户端，模型多步工具链自动编排
- **Codex 替代后端**：Agentic API 完全兼容 OpenAI Responses API wire protocol（含 WebSocket），可直接对接 Codex CLI，用开源模型 + 自有 GPU 跑完整 Codex 体验
- **多传输协议**：非流式 HTTP + SSE 流式 + WebSocket 全双工，覆盖从批量到交互式全场景
- **与 vLLM 零摩擦部署**：Rust 单二进制，启动即连接 vLLM server，复用 vLLM 模型管理

## 技术要点
- **Responses API 状态机**：服务端维护每个 response 的完整状态（input items、tool calls、tool outputs、assistant output），通过 `previous_response_id` 实现状态 hydration，客户端可用最少的 context window 消耗继续长时间对话
- **三种工具所有权模型**：Gateway-owned（服务端执行，如 web search、MCP tools）→ Client-owned（返回客户端，如 Codex shell/editor）→ Provider-owned（透传给上游推理引擎），未识别工具类型默认不执行，防止意外调用
- **SQLite 持久化**：response store 基于 SQLite 存储完整会话历史和状态，为后续 Messages API 和 Interactions API 提供共享存储基元
- **WebSocket + SSE 双流式传输**：Axum 框架实现 SSE 逐 token 流式 + WebSocket 全双工（Codex 依赖），统一路由层处理三种传输
- **Open Responses 兼容性验证**：通过 Open Responses 兼容性套件（openresponses.org）的 replay-cassette 回归测试，与真实 OpenAI 和 vLLM 流量对比
- **Rust 原生实现**：纯 Rust（103 个 .rs 源文件），无 FFI 依赖，性能敏感的热路径零拷贝、异步 I/O，内存占用远低于 Python 同类
- **后台执行 fire-and-forget**：支持非阻塞的长时间 Agent 任务，客户端无需保持连接
- **后续规划**：Messages API（Anthropic 风格有状态消息）+ Interactions API（更高级的持久化 Agent 工作流）

## 技术栈
Rust (Axum/Tokio), vLLM inference engine, SQLite, OpenAI Responses API protocol, SSE/WebSocket/HTTP, Apache 2.0

## 关联
- [`vllm-project/vllm`](../vllm/) — 底层推理引擎，Agentic API 作为其上层 Agent 服务层
- [`vllm-project/router`](../router/) — vLLM 生态的请求路由网关，与 Agentic API 同为 vLLM serving 层组件但职责不同（router 做请求分发，Agentic API 做 Agent 编排）
- [`vllm-project/semantic-router`](../semantic-router/) — 语义路由，同属 vLLM 上层生态
- [`MetaFARS/codex-relay`](https://github.com/MetaFARS/codex-relay) — 竞品：轻量 Responses→Chat 翻译桥，与 Agentic API 同做 OpenAI Responses 协议但路线不同（翻译 vs 原生实现）
- [`lightseekorg/smg`](https://github.com/lightseekorg/smg) — 竞品/互补：全功能 Rust LLM Gateway，也支持 Responses API 但定位更广（KV-cache 路由、多引擎 mesh）
- [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses) — 协议参考实现
- [OpenAI Codex](https://github.com/openai/codex) — Agentic API 的直接对接客户端

## 开放问题
- [ ] 2026-07-16 Agentic API 的 SQLite 持久化是否能支撑生产环境的高并发 Agent 会话？后续存储后端的规划是什么？
- [ ] 2026-07-16 Agentic API 是否需要兼容 MCP 协议的工具集成？目前仅支持内置 web search，工具生态尚窄
