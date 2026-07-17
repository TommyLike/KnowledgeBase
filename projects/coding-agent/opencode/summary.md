# opencode

> [`anomalyco/opencode`](https://github.com/anomalyco/opencode) · 上游贡献 · 全球最大的开源 AI 编程代理，TypeScript 全栈，TUI + 桌面应用双端，⭐187K

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `08fb473` · TypeScript · 6280文件/121MB · 1,352K 行 · 2486 `.ts` + 591 `.tsx` 文件  
**入口** `packages/opencode/` (CLI/TUI agent 核心) · `packages/console/` (Web 控制台) · `packages/desktop/` (Tauri 桌面应用)  
**架构** Monorepo: CLI agent 核心 → Console Web UI → Desktop Tauri App → SDK (JS/Go/Python) → Stats → Client  
**热点** CLI agent loop · tool system (Bash/Edit/Read/...) · TUI rendering · multi-provider LLM · Tauri desktop
<!-- END AUTO -->

---

## 定位
> OpenCode 是 2025-2026 年增长最快的开源 AI 编程代理——从 2025 年 4 月创立到 ⭐187K 仅用 14 个月，是全球最大的 AI 编程工具开源项目。不同于 grok-build 的「闭源内部 monorepo 公开快照」模式，OpenCode 是彻底的社区驱动模型：所有 PR 来自社区、开发过程全透明、20+ 语言 README。在 AI 编程代理赛道中，OpenCode 代表了「全开源、全平台、全语言」的极致覆盖路线。团队将其作为 AI 编程代理赛道的标杆跟踪。

## 项目介绍
> **全球最大开源 AI 编程代理——终端 TUI + 桌面应用 + Web 控制台三端覆盖，npm/homebrew/scoop/choco/pacman/nix 全包管理器分发，20+ 语言文档。**

核心场景：
- **终端 TUI 编程**：`opencode` 命令启动终端交互式编程，内置 build（全权限）/ plan（只读分析）两种 Agent，Tab 切换
- **桌面应用**：Tauri 原生桌面应用（macOS/Windows/Linux），提供完整 GUI 体验
- **多 Provider 支持**：对接 OpenAI / Anthropic / Google / Grok / DeepSeek / 任意 OpenAI 兼容 API
- **多 SDK**：JS/TypeScript SDK (`@opencode-ai/sdk`) + Go SDK + Python SDK，支持嵌入应用
- **MCP 集成**：原生 MCP 协议支持，可对接任何 MCP Server 扩展工具
- **Web 控制台 + Stats 面板**：`packages/console/` 提供 Web UI，`packages/stats/` 提供用量统计面板

## 技术要点
- **TypeScript 全栈 Monorepo**：packages/ 下 10+ 子包协同——opencode（CLI agent）、console（Web UI）、desktop（Tauri）、sdk（多语言 SDK）、stats（统计面板）、client（共享客户端）、codemode（代码迁移工具）
- **双 Agent 模型**：build agent（全权限开发）+ plan agent（只读分析），与 grok-build 的单一 Agent 模式不同
- **多 Provider 抽象层**：统一的 LLM Provider 接口，支持 OpenAI / Anthropic / Google / Grok / DeepSeek 等，与 agentic-api 的服务端 provider 抽象形成客户端—服务端对应
- **Tool System**：Bash（命令执行）、Edit（文件编辑）、Read（文件读取）、WebSearch、WebFetch、Task（子任务）等内置工具，与 Claude Code 工具集高度相似
- **TUI 渲染引擎**：自研终端 UI 系统（非 Ratatui），支持 split pane、滚动、交互式 prompt
- **Desktop Tauri v2**：Rust + React 的桌面应用，Tauri v2 框架，支持系统托盘
- **测试**：`packages/opencode/test/` 包含完整测试套件（tool fixtures、CLI help snapshots、config fixtures）
- **国际化**：30+ 语言 README + i18n 目录支持，面向全球开发者

## 技术栈
TypeScript (2486 .ts + 591 .tsx), React, Tauri v2 (Rust), Go, Python, SQL, MIT

## 关联
- [`xai-org/grok-build`](../grok-build/) — 竞品/下游：grok-build 的 `xai-grok-tools` vendored 了 opencode 的工具实现
- [OpenAI Codex](https://github.com/openai/codex) — 竞品
- [Anthropic Claude Code](https://claude.com/code) — 竞品
- [`vllm-project/agentic-api`](../../vllm-project/agentic-api/) — 互补：agentic-api 做服务端 Agent API，opencode 做客户端 Agent 工具

## 开放问题
- [ ] 2026-07-17 OpenCode 的 Tauri 桌面应用与终端 TUI 的功能对等程度如何？桌面应用是否缺少某些 CLI 功能？
- [ ] 2026-07-17 build vs plan Agent 模型是否会被更多编程代理采用？grok-build 目前只有一个 Agent 模式
