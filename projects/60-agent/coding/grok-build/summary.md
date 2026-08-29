# grok-build

> [`xai-org/grok-build`](https://github.com/xai-org/grok-build) · 上游贡献 · SpaceXAI (xAI) 的终端 AI 编程代理，Rust 全屏 TUI，支持鼠标交互、ACP 协议、沙箱隔离

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `8adf901` · Rust · 2735文件/53MB · 1,439K 行 · 2238 `.rs` 文件  
**入口** `crates/codegen/xai-grok-pager-bin` (TUI 入口) · `crates/codegen/xai-grok-shell` (Agent runtime) · `crates/codegen/xai-grok-tools` (工具实现)  
**架构** 三层：TUI 渲染层 (pager, prompt, modal) → Agent 运行时 (shell, tools, workspace) → 基础层 (config, MCP, markdown, sandbox)  
**热点** TUI rendering · agent runtime · tool dispatch · sandbox (Docker) · vendored codex/opencode tools
<!-- END AUTO -->

---

## 定位
> Grok Build 是 xAI 生态的终端编程代理，与 Claude Code、Codex CLI 处于同一赛道。不同于 opencode（社区驱动、全开源、TypeScript），grok-build 是 SpaceXAI 内部 monorepo 的周期性公开快照——不接受外部贡献、不开放开发过程。其 Rust 实现、全屏 TUI、ACP 协议支持展示了 xAI 对编程代理的工具定位：不仅是 CLI 工具，更是可嵌入编辑器的 Agent 运行时。团队跟踪其作为「闭源转公开快照」模式对开源编程代理赛道的冲击。

## 项目介绍
> **xAI 的终端 AI 编程助手——Rust 全屏 TUI、鼠标交互、支持 ACP（Agent Client Protocol）嵌入编辑器、headless 模式用于脚本/CI。**

核心场景：
- **终端全屏交互**：`grok` 命令启动全屏 TUI，支持鼠标操作、滚动回看、内联预览
- **ACP 嵌入编辑器**：通过 Agent Client Protocol 嵌入编辑器（如 VS Code），无需编辑器本身集成 AI
- **Headless 自动化**：CI/CD 和脚本中非交互式执行编码任务
- **沙箱隔离执行**：Docker 沙箱执行 Shell 命令和代码，操作前自动创建 checkpoint 支持回滚
- **MCP/Skills/Plugins/Hooks**：完整扩展体系，覆盖工具、技能、插件、钩子四层扩展
- **Web Search + Voice**：内置语音输入和网络搜索能力

## 技术要点
- **monorepo 公开快照模式**：仓库从 SpaceXAI 内部 monorepo 定期同步（`SOURCE_REV` 记录原始提交 SHA），不接受外部 PR。根 `Cargo.toml` 是生成的（workspace members + deps + lints 由工具自动生成），不可手动编辑
- **三层架构**：Pager（TUI 渲染，scrollback/prompt/modals）→ Shell（Agent runtime，leader/stdio/headless 三种入口）→ Tools + Workspace（工具实现 + 文件系统/VCS/沙箱/checkpoint）
- **vendored 第三方代码**：`third_party/` 目录包含 Mermaid 图表栈的完整 vendor；工具层（`xai-grok-tools`）复制了 openai/codex 和 sst/opencode 的工具实现，标注在 THIRD_PARTY_NOTICES 中
- **Sandbox 系统**：`crates/codegen/xai-grok-sandbox` 实现 Docker 容器隔离执行，结合 Workspace 的 checkpoint 机制提供安全回滚
- **ACP 协议**：Agent Client Protocol 允许编辑器作为 Client 接入 Grok Build 的 Agent 运行时，编辑器不需要内置 AI 能力
- **Agent 文档体系**：`crates/codegen/xai-grok-pager/docs/user-guide/` 包含完整的用户指南（认证、快捷键、slash commands、配置、主题、MCP、skills、插件、hooks、headless、沙箱）

## 技术栈
Rust (2238 .rs 文件, workspace 34+ crates), Ratatui TUI, Docker, MCP, ACP, vendored openai/codex + sst/opencode tool ports, Apache 2.0

## 关联
- [`anomalyco/opencode`](../opencode/) — 竞品/代码来源：grok-build 的工具层直接复制了 opencode 和 codex 的工具实现
- [OpenAI Codex](https://github.com/openai/codex) — 竞品/代码来源：grok-build 同样 vendored 了 codex 的工具实现
- [`vllm-project/agentic-api`](../../vllm-project/agentic-api/) — 互补：agentic-api 做服务端 Agent API，grok-build 做客户端 Agent 工具
- [Anthropic Claude Code](https://claude.com/code) — 竞品

## 开发模式注意
- **不接受外部贡献**：`CONTRIBUTING.md` 明确声明
- **根 Cargo.toml 只读**：所有 workspace 配置由内部工具自动生成
- **需 DotSlash + protoc** 才能编译

## 开放问题
- [ ] 2026-07-17 grok-build 的 periodic sync 频率是多少？公开快照与内部 monorepo 的延迟有多大？
- [ ] 2026-07-17 vendored opencode/codex 工具代码的版本如何维护？上游更新后是否需要重新 sync？
- [ ] 2026-07-17 ACP 协议是 xAI 自研还是社区标准？与 MCP 的关系是什么？
