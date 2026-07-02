# browser-use

> [`browser-use/browser-use`](https://github.com/browser-use/browser-use) · 上游贡献 · AI Agent 的浏览器自动化工具，将 Playwright 封装为 Agent 可自然语言调用的浏览器操作接口

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Python · 5,513n/28,454e  
<!-- END AUTO -->

---

## 定位
> Browser-Use 是 Agent 浏览器自动化领域增长最快的项目——让 AI Agent 像人类一样「看网页、点按钮、填表单」，而不只是用代码操作 DOM。在 Agent 生态中，Browser-Use 填补了「Agent 与现实 Web 世界交互」的空白——RAG 只能读静态文本，Browser-Use 让 Agent 真正操作动态网页（登录、搜索、下单、填问卷）。团队关注 AI Agent 驱动的浏览器自动化在未来人机交互中的作用。

## 项目介绍
> **给 Agent 一双「手」和一个「屏幕」——Agent 用自然语言描述操作意图，Browser-Use 将意图转换为浏览器点击、输入和滚动。**

核心场景：
- **Web 自动化 Agent**：Agent 自主完成「打开网站→搜索产品→比较价格→加购物车→填写地址→下单」完整流程
- **数据采集与表单填写**：Agent 浏览多个页面自动提取结构化数据，或自动填写复杂表单
- **Web 应用端到端测试**：Agent 自然语言描述测试用例，Browser-Use 自动执行并报告结果
- **RPA 替代方案**：替代传统 RPA 工具，Agent 通过视觉理解处理动态变化的 Web 页面

## 技术要点
- **Playwright 底层封装**：基于 Playwright 的真实浏览器控制（Chromium/Firefox/WebKit），非模拟请求
- **DOM + 视觉双模式**：同时提取页面 DOM 结构和截图，LLM 通过两种信号理解页面状态
- **Agent Action 接口**：定义了 navigate/click/type/extract/scroll/wait 等 10+ 核心浏览器操作
- **多步骤规划**：Agent 给定最终目标（如「查找 100 美元以下的蓝牙耳机」），Browser-Use 自动分解为多步浏览器操作序列
- **元素定位策略**：索引标签 + 属性选择器 + 视觉定位多种策略，解决动态 DOM 的定位难题
- **多 Tab 管理**：支持打开/切换/关闭标签页的复杂多页面工作流
- **Stealth 模式**：内置反检测机制，减少被网站识别为机器人的概率

## 技术栈
Python, Playwright, LangChain, OpenAI/Anthropic API, Chromium/Firefox/WebKit, MIT

## 关联
- [`browser-use/browser-harness`](../browser-harness/) — 同一团队，Browser-Use 的底层框架
- [`ComposioHQ/composio`](../composio/) — Tool 集成平台，Browser-Use 是其上最重要的工具之一
- [`vercel-labs/agent-browser`](../agent-browser/) — Vercel 轻量级 Agent 浏览器方案
- [Playwright](https://playwright.dev) — 底层浏览器自动化引擎

## 开放问题
- [ ] 2026-07-02 网页反爬和 CAPTCHA 对 Agent 浏览器自动化的影响有多大？是否有绕过 CAPTCHA 的可靠方案？
