# CLIProxyAPI

> [`router-for-me/CLIProxyAPI`](https://github.com/router-for-me/CLIProxyAPI) · 上游贡献 · 面向 CLI 工具的本地 AI API 代理，让命令行工具无需复杂集成即可调用 LLM

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> CLIProxyAPI 是一个轻量级的本地 AI API 代理方案——为 CLI 工具提供统一的 LLM API 转发层。在 Agent 工具生态中，CLIProxyAPI 解决了「如何在已有命令行工具中最简单地接入 LLM 能力」的细分问题。

## 项目介绍
> **命令行工具的 LLM 加速器——本地运行轻量代理，任何 CLI 工具通过标准 API 获得 LLM 能力。**

核心场景：
- **CLI 工具 AI 赋能**：已有命令行工具通过 CLIProxyAPI 获得自然语言处理能力
- **本地 API 统一代理**：多个 CLI 工具共享一个本地 LLM API 代理

## 技术要点
- **本地轻量代理**：单进程低资源运行
- **API 格式转换**：简单 HTTP 请求转标准 LLM API 调用
- **多 Provider 支持**：OpenAI / Anthropic 等

## 技术栈
Go, HTTP, OpenAI API, MIT

## 关联
- [`BerriAI/litellm`](../litellm/) — 全方位 AI Gateway，CLIProxyAPI 是轻量本地特化方案

## 开放问题
- [ ] 2026-07-02 作为单点代理，生产环境的可靠性和安全性如何保障？
