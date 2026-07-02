# agent-browser

> [`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser) · 上游贡献 · Vercel 出品的轻量级 AI Agent 浏览器工具，为 Agent 提供简洁的网页浏览和信息提取能力

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Agent Browser 是 Vercel 实验室出品的轻量级 Agent 浏览器方案——与 Browser-Use（重量级 Playwright 封装）不同，Agent Browser 追求极简：提供 Agent 最常用的几个浏览器操作（navigate/click/screenshot/extract），API 极其简洁。在 Agent 工具生态中，Agent Browser 适合快速原型场景，而 Browser-Use 适合复杂交互场景。

## 项目介绍
> **给 Agent 一个轻量级浏览器——极简 API，核心操作，快速集成到 Next.js Agent 应用中。**

核心场景：
- **Agent 网页信息提取**：打开 URL → 截图 → 提取文本内容
- **轻量网页交互**：点击按钮、填写搜索框、翻页等简单操作
- **Next.js AI App 集成**：与 Vercel AI SDK 无缝集成

## 技术要点
- **极简四操作 API**：`goto`/`click`/`screenshot`/`extract` 四个核心函数
- **Puppeteer 轻量封装**：比 Browser-Use 的 Playwright 更轻量
- **Vercel AI SDK 集成**：与 `ai` 和 `@vercel/ai` 包的 Tool 接口直接对接
- **Serverless 兼容**：设计为在 Vercel Edge/Serverless Functions 中运行

## 技术栈
TypeScript, Puppeteer, Vercel AI SDK, MIT

## 关联
- [`browser-use/browser-use`](../browser-use/) — 竞品，Browser-Use 功能更全面但更重量
- [`vercel-labs`](https://vercel.com/labs) — Vercel 实验室项目

## 开放问题
- [ ] 2026-07-02 Agent Browser 在 Vercel Serverless 环境中的 10s 函数超时限制下，能否完成复杂多步骤的网页操作？
