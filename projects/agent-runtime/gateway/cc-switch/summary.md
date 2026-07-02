# cc-switch

> [`farion1231/cc-switch`](https://github.com/farion1231/cc-switch) · 上游贡献 · 多 AI 编程工具的 API 提供商、MCP 服务器、Skills 与 Prompts 一站式配置管理中心

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> CC Switch 是面向 AI 编程工具生态的**桌面级统一配置管理层**，解决 Claude Code、Codex、Gemini CLI 等多款工具各自维护独立配置文件、切换 API 提供商繁琐的痛点。团队关注该项目以跟踪 AI 编程工具配置管理的最佳实践，理解多工具互操作的演进方向，并为自身工具链的配置体验优化提供参考。

## 项目介绍
> **跨平台桌面应用，为 Claude Code、Codex、Gemini CLI 等 AI 编程工具提供统一的 API 提供商、MCP 服务器、Skills 和 Prompts 配置管理，支持一键切换和一键同步。**

核心场景：
- **多工具 API 提供商统一切换**：一处配置 API Key 后自动同步到 Claude Code、Codex、Gemini CLI 等所有工具的配置文件，支持 50+ 内置提供商预设（AWS Bedrock、NVIDIA NIM、SiliconFlow 等），一键切换无需手动编辑 JSON/TOML/.env。
- **本地代理与自动故障转移**：内置 HTTP 代理支持请求热切换、自动故障转移（circuit breaker 模式）、提供商健康监控，可独立代理每个工具，确保 API 调用不中断。
- **MCP 服务器统一管理**：在单一面板中管理 Claude、Codex、Gemini、OpenCode、Hermes 的 MCP 服务器配置，支持双向同步和 Deep Link（ccswitch://）一键导入。
- **Prompts 与 Skills 跨应用同步**：Markdown 编辑器管理 CLAUDE.md / AGENTS.md / GEMINI.md，跨应用同步且支持回填保护；Skills 支持从 GitHub 仓库或 ZIP 一键安装。
- **用量统计与成本追踪**：仪表盘展示消费金额、请求数、Token 量及趋势图，支持自定义模型定价，以及跨工具会话历史浏览、搜索与恢复。

## 技术要点
- **SSOT 数据架构**：所有数据存储于 SQLite（~/.cc-switch/cc-switch.db），以单数据源保证一致性，设备级 UI 偏好单独存 JSON，避免配置漂移。
- **双向同步机制**：切换工具时写入对应应用的实时配置文件，编辑配置文件时回填到数据库，保证数据库与文件系统的一致性。
- **原子写入**：采用 temp file + rename 模式写配置文件，防止并发写入导致配置损坏，是配置管理类工具的核心安全策略。
- **双层存储**：SQLite 存可同步数据（providers、MCP、prompts、skills），JSON 存设备级 UI 偏好，兼顾数据可迁移性和设备独立性。
- **Tauri IPC 通信**：React 前端通过 Tauri IPC 与 Rust 后端通信，保证桌面级性能和安全隔离，前端不直接访问文件系统。
- **Deep Link 协议**：自定义 URL scheme（ccswitch://）支持一键导入 providers、MCP 服务器、prompts 和 skills，降低配置分发成本。
- **本地代理与路由**：Rust 实现的 HTTP 代理服务器，支持 hot-switch、故障转移、circuit breaker、请求整形，每个工具可配置独立代理策略。
- **并发安全分层架构**：Mutex 保护的数据库连接，Tauri 命令层 → 服务层 → DAO 层 → 数据库，职责清晰，避免竞态条件。

## 技术栈
Rust 61.5%, TypeScript 36.9%, React 18, Vite, TailwindCSS 3.4, Tauri 2.8, TanStack Query v5, shadcn/ui, react-i18next, zod, SQLite, pnpm, vitest, MSW

## 关联
- [`agent-runtime/gateway/litellm`](../litellm/summary.md) — 同为 API 提供商管理层，LiteLLM 侧重服务端统一代理，CC Switch 侧重桌面端多工具配置同步
- [`agent-runtime/gateway/mcp-gateway-registry`](../mcp-gateway-registry/summary.md) — 同为 MCP 服务器管理，CC Switch 在桌面端做 MCP 统一配置，互补视角
- [`agent-runtime/gateway/agentgateway`](../agentgateway/summary.md) — 同为 agent 网关类项目，侧重不同层次的 agent 工具链管理
- **上游依赖**：Tauri 2（桌面框架）、React（UI 框架）、SQLite（数据存储）
- **管理的下游工具**：Claude Code、Claude Desktop、Codex（OpenAI）、Gemini CLI（Google）、OpenCode、OpenClaw、Hermes Agent

## 开放问题
- [ ] 2026-07-02 该项目 112k+ stars 的增长驱动力是什么？是 AI 编程工具爆发式增长的自然结果，还是独特的社区运营策略？
- [ ] 2026-07-02 双向同步机制在多个工具同时运行时如何处理竞态？目前的设计是否依赖文件系统事件监听？
- [ ] 2026-07-02 内置代理的 hot-switch 在流式响应（SSE）场景下是否会出现中断？故障转移策略对流式请求的支持程度如何？

