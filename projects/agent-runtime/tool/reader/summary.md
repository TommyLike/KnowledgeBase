# reader

> [`jina-ai/reader`](https://github.com/jina-ai/reader) · 上游贡献 · 将任意 URL 一键转换为 LLM 友好格式的通用内容提取引擎

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh
<!-- END AUTO -->

---

## 定位
> Reader 是 Jina AI 开源的 Web 内容提取与搜索服务，解决了 LLM / RAG 系统从原始网页中摄取干净结构化文本的核心痛点。它通过 `r.jina.ai` 前缀即可将任何 URL 转化为 Markdown，同时提供 `s.jina.ai` 搜索引擎集成，自动抓取并处理搜索结果页内容。在 Agent 生态中，Reader 作为最轻量的内容获取工具之一，无需部署爬虫集群即可让 Agent 获得阅读全网内容的能力，是构建搜索增强型 Agent 的关键基础设施。我们关注它，是因为它是 Web Agent 信息获取链路中与 Firecrawl、Browser-Use 互补的重要组件。

## 项目介绍
> **一款零配置、支持自托管的 URL 到 LLM 格式转换服务，让 AI Agent 可以像人类一样"阅读"网页、PDF、Office 文档和图片。**

核心场景：
- **RAG 知识库构建**：将任意网页、文档 URL 转换为结构化 Markdown，直接喂入向量数据库或 LLM 上下文，无需编写爬虫脚本
- **AI 搜索引擎增强**：Agent 调用 `s.jina.ai` 搜索关键词，自动抓取前 5 条结果并返回完整处理后的正文，而非仅有标题和摘要
- **Agent 自主浏览**：配合 `x-preset: agent` 预设，Agent 可以动态浏览网页、提取关键信息，支持 CSS 选择器精确定位目标内容区域
- **多格式文档解析**：统一处理网页 HTML、PDF、Word、Excel、PowerPoint 和图片，图片通过 VLM 自动生成文字描述，纯文本 LLM 也能理解视觉内容
- **深度研究辅助**：`x-preset: research` 预设为 AI 研究代理提供结构化、可引用的输出，适合学术调研和竞品分析场景

## 技术要点
- **双引擎抓取架构**：同时支持 Puppeteer 无头浏览器渲染（处理 SPA、JS 动态页面）和 curl-impersonate 轻量级抓取（模拟浏览器 TLS 指纹，处理静态页面），通过智能引擎选择在速度与完整性之间自动平衡，用户也可通过 `x-engine` 头手动指定
- **三服务器分离设计**：Crawl Server（`r.jina.ai`，URL 转 Markdown）、Search Server（`s.jina.ai`，搜索 + 抓取）、SERP Server（搜索引擎结果页专用抓取）三个独立入口，各自针对不同场景优化，共享底层抓取和渲染能力
- **基于 tsyringe 的依赖注入架构**：使用 `tsyringe` + `AsyncService` 生命周期管理，构建在 `civkit` 框架之上，`ThreadedServiceRegistry` 管理 Worker 线程池并基于 CPU 核心数自动扩缩，支持 HTTP/2 h2c 和 HTTP/1.1 双端口
- **多格式文档解析管线**：PDF 通过 PDF.js 解析，Office 文档通过 LibreOffice 转为 HTML/PDF 后再处理，图片通过 VLM 自动生成描述文本（`x-with-generated-alt`），最终统一经 Turndown 转换为 Markdown 输出
- **丰富的输出格式与控制头**：支持 Markdown、HTML、纯文本、截图（screenshot/pageshot）、Frontmatter 等多种输出格式；提供 `x-target-selector`（CSS 选择器限定提取范围）、`x-wait-for-selector`（等待元素出现）、`x-respond-timing`（控制返回时机，如 network-idle）等精细控制头
- **语义切片（Markdown Chunking）**：`x-markdown-chunking` 头支持基于标题层级或块级语义的智能文本切片，输出 JSON 数组或分隔符文本，直接适配 RAG 索引和向量化管线的分段需求
- **预设配置系统（x-preset）**：提供 `reader`（人类阅读）、`index`（语义索引）、`research`（可引用研究）、`agent`（Agent 日常浏览）、`spider`（递归爬取）五套预设，一键组合多个配置头，简化 Agent 集成
- **反爬对抗工具箱**：提供多级对抗策略——从 API Key 提升信任池、绕过缓存（`x-no-cache`）、强制浏览器引擎（`x-engine: browser`）、SaaS 代理池轮换 IP（`x-proxy: auto`），到自带 SOCKS4/5/HTTP 代理（`x-proxy-url`），覆盖从轻度到重度的反爬需求
- **自托管与可扩展缓存**：Docker 单镜像部署，默认无状态运行即可使用；通过环境变量可接入任意 S3 兼容对象存储（如 MinIO）实现响应缓存，降低重复抓取成本并提升响应速度
- **搜索增强的站点定向**：`s.jina.ai` 搜索端点不仅支持通用 Web 搜索，还提供 `site` 参数实现在指定域名内搜索（如 `?site=arxiv.org&site=github.com`），对学术调研和技术文档搜索特别实用

## 技术栈
TypeScript, civkit, tsyringe, Puppeteer, curl-impersonate, PDF.js, LibreOffice, Turndown, Koa, Docker, MinIO/S3

## 关联
- [`firecrawl/firecrawl`](../firecrawl/) — 同属 Web 内容提取工具，Firecrawl 更侧重站点级爬取和结构化数据提取，Reader 更轻量、以单 URL 即时转换为核心
- [`browser-use/browser-use`](../browser-use/) — Agent 浏览器自动化框架，Reader 可作为其轻量替代，在不需要完整浏览器交互时用 URL 前缀即用模式降低复杂度

## 开放问题
- [ ] 2026-07-02 Reader 的 OSS 分支不包含 MongoDB 存储层（仅 S3 缓存），在需要持久化抓取历史、去重和增量更新的生产场景中，自建存储层的方案和成本如何？
