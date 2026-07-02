# page-agent

> [`alibaba/page-agent`](https://github.com/alibaba/page-agent) · 上游贡献 · 阿里开源的 AI Agent 网页交互工具，将网页 DOM 结构转换为 Agent 可理解的语义化页面表示

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Page-Agent 是阿里巴巴在 Agent 网页理解方向的探索——与 Browser-Use（偏重浏览器操作）不同，Page-Agent 更关注「Agent 如何理解网页结构」：将 DOM 树转换为 LLM 友好的语义化表示。

## 项目介绍
> **让 Agent 看懂网页——DOM → 语义化表示，Agent 用自然语言理解和操作网页内容。**

核心场景：
- **网页结构理解**：DOM 解析 → 提取关键元素（表单、按钮、链接、表格）
- **结构化数据提取**：从网页中提取半结构化数据
- **语义化页面导航**：根据页面语义定位和操作元素

## 技术要点
- **DOM 语义化转换**：HTML DOM → 简化语义树，去噪（广告/导航/页脚）
- **LLM 友好输出**：输出格式针对 LLM 上下文窗口优化
- **阿里生态集成**：与通义大模型集成

## 技术栈
Python, DOM Parser, LLM APIs, Apache 2.0

## 关联
- [`browser-use/browser-use`](../../tool/browser-use/) — 竞品/互补，Browser-Use 偏操作，Page-Agent 偏理解
- [Alibaba AI](https://ai.alibaba.com) — 发起方

## 开放问题
- [ ] 2026-07-02 语义化 DOM 表示的通用性如何？不同网站设计差异是否会导致 Agent 理解偏差？
