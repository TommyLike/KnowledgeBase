# codex-app-transfer

> [`Cmochance/codex-app-transfer`](https://github.com/Cmochance/codex-app-transfer) · 上游贡献 · Rust + Tauri 的桌面端 Codex 配置网关，用 GUI 管理国产 LLM 供应商并将 Responses API 翻译为 Chat Completions

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> Codex App Transfer 是 Codex 生态中「桌面 GUI 供应商管理」路线的代表——与 codex-relay（CLI 代理）和 Agentic API（服务端原生）不同，它提供 Tauri 桌面应用 + 系统托盘后台运行，面向非技术用户提供可视化供应商配置和模型映射。在 AI Agent Gateway 生态中，它是唯一带有完整 GUI 的方案。团队关注 AI 工具的桌面端网关形态。

## 项目介绍
> **Codex 的桌面配置中心——Tauri GUI 管理供应商、转发 Responses API、实时日志面板，让国产 LLM 用户零命令行配置跑 Codex。**

核心场景：
- **国产 LLM + Codex**：内置 DeepSeek / 月之暗面 Kimi / 智谱 GLM / 阿里百炼 / 小米 MiMo / MiniMax / 腾讯 CodeBuddy / 阿里 Qoder 等 10+ 国产供应商配置模板
- **桌面 GUI 全托管**：仪表盘、供应商管理、模型映射、端口配置、日志面板全部在 Tauri 应用中完成
- **系统托盘后台运行**：关闭窗口后缩到托盘继续转发，右键托盘退出才停止服务
- **Codex 用量可视化**：在 Codex Desktop 顶栏注入独立的「Usage」分区——5 小时/周/月配额、余额、实时 Token 速率、上下文用量 breakdown
- **Codex Desktop 主题注入**：通过 CDT 运行时注入 11 套二次元主题背景 + 自定义上传

## 技术要点
- **Tauri v2 桌面框架**：Rust 后端 + Web 前端，跨平台桌面应用（macOS/Windows/Linux）
- **Responses → Chat Completions 翻译**：与 codex-relay 同类的协议翻译，但对国产 LLM 供应商的特殊行为做了大量适配和 workaround
- **国产 LLM 供应商适配层**：每个供应商（DeepSeek/Kimi/GLM/百炼等）有独立的 model property 模板和请求变换逻辑
- **Codex Desktop CDT 注入**：通过 Chromium DevTools Protocol 运行时注入 CSS/JS，实现主题和用量显示的 best-effort 注入

## 技术栈
Rust, Tauri 2.x, React (前端), Chromium DevTools Protocol, MIT

## 关联
- [`MetaFARS/codex-relay`](../codex-relay/) — 竞品/互补：同做 Responses→Chat 翻译，codex-relay 是 CLI 纯代理，codex-app-transfer 是 GUI 全功能
- [`vllm-project/agentic-api`](../../../vllm-project/agentic-api/) — 互补：Agentic API 是服务端原生 Responses API，codex-app-transfer 是客户端协议翻译
- [OpenAI Codex](https://github.com/openai/codex) — 被代理的客户端
- [月之暗面 Kimi](https://kimi.moonshot.cn) / [DeepSeek](https://deepseek.com) / [智谱 GLM](https://zhipuai.cn) — 主要对接的国产 LLM 供应商

## 开放问题
- [ ] 2026-07-16 项目自称「仅对两家供应商完成端到端测试」——生产可靠性存疑。国产 LLM API 的快速迭代是否会导致适配层持续追赶？
