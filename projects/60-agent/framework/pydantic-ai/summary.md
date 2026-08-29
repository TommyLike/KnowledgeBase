# pydantic-ai

> [`pydantic/pydantic-ai`](https://github.com/pydantic/pydantic-ai) · 上游贡献 · Pydantic 团队打造的以类型安全为核心的 Python Agent 框架，定位「GenAI 时代的 FastAPI」

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> pydantic-ai 由 Python 数据校验事实标准 Pydantic 的团队打造，将类型安全理念带入 Agent 开发。在 Agent 框架生态中独树一帜——不是通过字符串拼接 prompt 和 JSON 解析，而是用泛型 `Agent<T>` 在编译期就绑定输入输出类型。Pydantic 团队的生态影响力（FastAPI、Pydantic V2、Logfire）使其有潜力成为 Python Agent 开发的类型安全底座。

## 项目介绍
> **类型安全的 Agent 框架——用 Pydantic 校验确保 Agent 输入/输出/工具调用在类型层面可靠，让 Agent 开发像写 FastAPI 路由一样直观。**

核心场景：
- **类型安全的 Agent 开发**：Agent 的依赖类型和输出类型通过泛型约束，IDE 完整自动补全
- **多模型切换**：一套 API 适配 OpenAI、Anthropic、Gemini、DeepSeek、Grok 等 20+ 模型
- **结构化输出 Agent**：Agent 输出直接反序列化为 Pydantic 模型，无需手动 JSON 解析
- **持久化执行**：Agent 在失败或重启后保持执行进度，适合长时间异步任务
- **全栈可观测性**：Logfire + OpenTelemetry 实时监控 Agent 行为和工具调用链路

## 技术要点
- **泛型 Agent 类型**：`Agent[DepsType, OutputType]` 对依赖和输出做编译期类型约束，IDE 从 prompt 到返回值全链路自动补全
- **依赖注入 RunContext**：工具函数通过 `ctx: RunContext[Deps]` 参数注入外部服务实例（数据库连接、API 客户端等）
- **模型无关设计**：通过统一的 `Model` 接口适配 20+ 提供商，包括公有云（Azure、Bedrock、Vertex AI）和本地（Ollama）
- **流式结构化输出**：支持实时校验的流式响应，数据到达时即时 Pydantic 校验和解析
- **Logfire 集成**：基于 OpenTelemetry 的全栈可观测性，追踪 agent 运行的每一步——prompt token、tool call 参数、响应延迟
- **声明式 Agent 定义**：支持 YAML/JSON 无代码定义 Agent，降低非 Python 团队的使用门槛
- **MCP 协议集成**：原生支持 Model Context Protocol，可与外部 MCP 工具服务互联

## 技术栈
Python, Pydantic, OpenTelemetry, Logfire, uv, MkDocs, MIT

## 关联
- Pydantic Logfire — 同团队的可观测性平台，pydantic-ai 的原生监控方案
- [FastAPI](https://github.com/fastapi/fastapi) — 设计理念参考（类型安全 Web 框架 → 类型安全 Agent 框架）
- [`langchain-ai/langchain`](../langchain/) — LangChain 提供生态广度，pydantic-ai 提供类型深度

## 开放问题
- [ ] 2026-07-02 pydantic-ai 在 Multi-Agent 协作场景的设计尚未成熟——未来是与 LangGraph/AutoGen 合作还是自建编排层？
