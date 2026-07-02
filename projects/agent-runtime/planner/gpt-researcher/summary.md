# gpt-researcher

> [`assafelovic/gpt-researcher`](https://github.com/assafelovic/gpt-researcher) · 上游贡献 · 基于多智能体协作的自主研究 Agent 框架，自动生成数千字结构化调研报告

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> GPT Researcher 是自主 AI 研究 Agent 领域的标杆开源项目（28k+ Stars），在 Agent 规划能力评估体系中处于 Planner 子类（研究规划与执行流水线）。项目采用 Planner-Executor-Publisher 三阶段流水线和树状递归搜索策略，为团队的 Agent 研究提供了多智能体协作、深度调研和引用追踪的参考实现。我们关注该项目作为上游参考，了解自主研究 Agent 的前沿设计范式，以及 MCP 协议在实际 Agent 框架中的集成方式。

## 项目介绍
> **GPT Researcher 是一个基于多智能体协作的自主研究 Agent 框架，通过规划、执行、发布三阶段流水线自动生成结构化深度报告，解决传统手动研究耗时、LLM 幻觉和数据源偏差等问题。**

核心场景：
- **深度研究报告生成**：自动生成 2,000+ 词的调研报告，支持 PDF/Word/Markdown 三种格式导出
- **递归深度研究（Deep Research）**：采用树状搜索策略逐层探索子主题，可配置广度和深度，约 5 分钟完成单次研究，成本约 $0.40（o3-mini）
- **多智能体协作研究**：基于 LangGraph 或 AG2 框架，多个专业 Agent 并行完成规划、信息采集和汇总，产出 5-6 页结构化报告
- **多源信息聚合与引用追踪**：聚合超过 20 个网络和本地文档来源，自动过滤不可靠信源，生成带完整引用的客观结论
- **含 AI 图片的研究报告**：支持智能图片抓取与过滤，并通过 Google Gemini 在报告中嵌入 AI 生成的插图
- **MCP 协议扩展**：可作为 MCP Server 向外部 Agent 提供研究能力，也可作为 MCP Client 接入 GitHub、数据库、自定义 API 等外部数据源

## 技术要点
- **Planner-Executor-Publisher 三阶段流水线**：Planner 根据用户研究主题自动生成一组研究问题，Executor（Crawler Agent 集群）并行爬取并摘要每个问题对应的网页资源，Publisher 最终将分散的摘要聚合为逻辑连贯的完整报告
- **Deep Research 递归搜索策略**：采用广度优先的树状搜索，每个节点为一个子主题，branches 间并行处理并共享上下文，通过可配置的 depth（深度）和 breadth（广度）控制探索范围，灵感源自 STORM 学术论文
- **多框架多智能体编排**：同时支持 LangGraph（基于有向图的 Agent 编排 + LangSmith 可观测性追踪）和 AG2（原 AutoGen）两套多 Agent 框架，动态创建 Planner Agent、Crawler Agent 和 Reporter Agent 完成协作
- **全流程异步架构**：基于 FastAPI + Uvicorn + aiohttp 构建后端，支持 SSE（Server-Sent Events）实时推送研究进度到前端，各爬虫任务通过 asyncio 并行执行
- **多 LLM Provider 兼容**：通过 LangChain 统一接口支持 OpenAI、Anthropic、Google、Groq、Mistral、Cohere 等云端模型，并通过 Ollama 支持本地模型，LiteLLM 提供统一 LLM 调用的 fallback 与路由能力
- **MCP 协议集成**：完整支持 Model Context Protocol，gpt-researcher 自身可作为 MCP Server 供其他 Agent 调用研究能力，也可作为 MCP Client 接入外部工具和数据源（GitHub、数据库、API 等）
- **持久化与状态管理**：SQLAlchemy ORM 持久化研究任务与结果，LangGraph Checkpoint 机制支持工作流断点续跑，Pydantic 用于配置验证和数据模型定义
- **多格式报告生成管线**：支持 Markdown / PDF / DOCX 三种导出格式，依赖 python-docx、md2pdf、WeasyPrint 等库完成格式转换，报告自动包含引用来源和层级目录结构

## 技术栈
Python ≥ 3.11, FastAPI + Uvicorn（后端）, LangChain + LangGraph（Agent 编排）, AG2 可选（第二多 Agent 框架）, LiteLLM（统一 LLM 调用）, Tavily / DuckDuckGo / Arxiv（搜索检索）, PyMuPDF / Unstructured / BeautifulSoup4（文档解析）, SQLAlchemy + Pydantic（数据层）, MCP 协议, Next.js + Tailwind / 轻量 HTML-CSS-JS（前端可选）, Docker 部署

## 关联
- [`agent-runtime/worker/tavily`](待确认) — GPT Researcher 深度依赖 Tavily 搜索 API 作为主要检索后端，用于网页搜索和信息采集
- [`stanford-oval/storm`](待确认) — STORM 论文提供了 Deep Research 方法论灵感（树状子主题探索 + 多 Agent 协作），是学术上游参考
- [`langchain-ai/langgraph`](待确认) — LangGraph 是 GPT Researcher 多 Agent 模式的主要编排运行时，需持续关注版本兼容性
- [`opensourceways/agentgateway`](../../opensourceways/agentgateway) — 团队自研的 Agent 网关项目，GPT Researcher 的多 Agent 编排模式可作为参考设计

## 开放问题
- [ ] 2026-07-02 Deep Research 树状搜索的分支间上下文共享机制具体如何实现？是否会因分支过多导致 Token 成本线性增长？
- [ ] 2026-07-02 GPT Researcher 的 MCP 集成在团队 Agent 网关架构中能否作为可插拔的研究服务模块直接复用？
- [ ] 2026-07-02 当前多 Agent 框架在 LangGraph 和 AG2 之间切换是否存在兼容性差异？团队如果后续引入多 Agent 编排，应优先评估哪个框架？
