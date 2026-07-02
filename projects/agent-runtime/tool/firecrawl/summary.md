# firecrawl

> [`firecrawl/firecrawl`](https://github.com/firecrawl/firecrawl) · 上游贡献 · AI 就绪的网页抓取和转换引擎，将任意网页转为 LLM 可直接处理的 Markdown/结构化数据

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · TypeScript · 13,614n/48,798e  
<!-- END AUTO -->

---

## 定位
> Firecrawl 是 RAG Agent 的「数据入口」——在 Agent 进行 RAG（检索增强生成）之前，Firecrawl 解决信息获取的第一步：将互联网上的任意网页（动态渲染、需要登录、有反爬保护的）自动抓取并转成干净的 Markdown 格式。在 Agent 生态中，Firecrawl 是信息输入 Pipeline 的关键环节，独立于爬虫框架（Scrapy/Puppeteer），专为 LLM 内容消费优化。

## 项目介绍
> **将整个网站变成 LLM 可读的 Markdown——自动处理渲染、登录、反爬和分页，Agent 只需一个 URL 即可获取干净内容。**

核心场景：
- **RAG 数据源准备**：Agent 编写文档→抓取技术博客→转为 Markdown→存入向量数据库的完整 Pipeline
- **竞品信息采集 Agent**：自动抓取竞品网站→提取价格/功能/评价→结构化汇总
- **网站内容迁移**：旧网站内容批量抓取并转为新 CMS 兼容格式
- **SEO / 内容审核**：抓取整站内容分析 SEO 健康度或敏感内容
- **LLM Fine-tuning 数据准备**：批量抓取特定领域网站构建训练语料

## 技术要点
- **JS 渲染 + 静态抓取双模式**：静态 HTML 爬取快但不支持 SPA，JS 渲染（无头浏览器）支持 React/Vue/Angular 页面
- **LLM 友好的输出格式**：默认输出 Markdown（保留标题层级、列表、代码块、表格），可选结构化 JSON 和 Screenshot
- **智能内容提取**：自动识别页面主体内容（去导航栏/侧边栏/广告/页脚），输出纯正文
- **深度爬取（Crawl）**：从一个 URL 开始，自动发现并抓取同域名下所有链接页面，支持深度限制和路径过滤
- **反反爬策略**：代理轮换、UA 伪装、速率控制、Cookie/登录态保持
- **API + SDK**：REST API 托管服务 + Python/TypeScript/Go SDK
- **自托管选项**：开源版 Docker 部署，数据不出企业网络

## 技术栈
TypeScript, Rust (部分模块), Puppeteer/Playwright, Redis, PostgreSQL, Markdown, MIT + EE

## 关联
- [`jina-ai/reader`](../reader/) — 竞品，Jina Reader 也是 URL→Markdown 转换工具
- [`browser-use/browser-use`](../browser-use/) — 互补，browser-use 侧重操作网页，firecrawl 侧重提取内容
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — LangChain Document Loader 集成 (`FireCrawlLoader`)
- [`infiniflow/ragflow`](../../memory/ragflow/) — RAG 平台，Firecrawl 是其知识库导入的数据源

## 开放问题
- [ ] 2026-07-02 大规模网站抓取的速率限制和 IP 封禁如何策略化处理？自托管和云版本在反反爬能力上的差距？
