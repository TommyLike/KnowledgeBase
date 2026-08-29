# browser-harness

> [`browser-use/browser-harness`](https://github.com/browser-use/browser-harness) · 上游贡献 · Browser-Use 的底层浏览器控制框架，将 Playwright 封装为可配置的浏览器自动化 harness

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Browser Harness 是 Browser-Use 项目的基础设施层——从 Browser-Use 中抽取出的纯浏览器控制框架，不包含 Agent 逻辑。在 Agent 工具生态中，Browser Harness 为需要自定义浏览器控制逻辑的开发者提供了比 Browser-Use 更底层、更灵活的抽象。

## 项目介绍
> **Browser-Use 的浏览器控制底座——如果你不需要 AI Agent 层，只想要一个干净的浏览器自动化框架。**

核心场景：
- **自定义浏览器 Agent**：在 Browser Harness 上构建自己的 AI 浏览器操作逻辑
- **浏览器自动化测试**：不依赖 Agent 框架的纯浏览器自动化测试
- **数据抓取**：高级网站抓取，绕过 SPA/JS 渲染挑战

## 技术要点
- **Playwright 封装**：围绕 Playwright 的高级抽象
- **可配置 Harness**：浏览器启动参数、代理、Cookie 等全面可配置
- **与 Browser-Use 关系**：Browser-Use = Browser Harness + AI Agent 决策层

## 技术栈
Python, Playwright, MIT

## 关联
- [`browser-use/browser-use`](../browser-use/) — 上层 Agent 浏览器框架
- [Playwright](https://playwright.dev) — 底层浏览器自动化引擎

## 开放问题
- [ ] 2026-07-02 Browser Harness 的 API 稳定性如何？是否随 Browser-Use 快速迭代而变化？
