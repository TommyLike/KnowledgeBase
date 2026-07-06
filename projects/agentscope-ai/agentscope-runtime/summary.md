# AgentScope-Runtime

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

AgentScope-Runtime 是 AgentScope 生态中的生产级 Agent 应用运行时框架，专注于为 AI Agent 提供安全的工具执行沙箱和全链路可观测性。本项目属于**上游贡献**范围，团队关注其在沙箱安全、Agent 运行时标准化方向的技术方案，作为自研 Agent 平台的参考。

## 项目介绍

AgentScope-Runtime 是面向 Agent 应用的生产级运行时，核心提供受限环境中的工具执行能力（Code Execution Sandbox）和请求级遥测（tracing/metrics/logging）。它与 AgentScope 框架解耦，可独立接入任意 Agent 编排层，目标是让 Agent 的工具调用"安全可控、可观测、可审计"。

## 核心场景

- **安全工具执行**：Agent 调用代码解释器、Shell 命令等工具时，在隔离沙箱中执行，防止恶意代码或误操作影响宿主环境。
- **多租户 Agent 服务**：在多用户场景下，为每个会话提供独立的沙箱实例，保证租户间隔离。
- **Agent 行为可观测**：通过 OpenTelemetry 标准的 tracing 和 metrics，追踪每个工具调用的耗时、输入输出和异常。
- **生产部署**：提供健康检查、优雅关闭、配置热加载等生产环境必需的运维能力。

## 技术要点

- **沙箱隔离**：基于容器化（Docker）或进程级隔离（如 nsjail/seccomp）实现工具执行沙箱，支持 CPU/内存/网络/文件系统的资源限制。
- **OpenTelemetry 集成**：内置 OTLP 导出器，自动采集 span（工具调用链）、metrics（调用次数/延迟/错误率）和 logs。
- **工具注册机制**：提供声明式的工具注册接口，支持本地函数、远程 HTTP 工具和沙箱内执行三种模式。
- **中间件管道**：请求处理采用中间件链模式（类似 Koa/Express），支持鉴权、限流、审计日志等横切关注点。
- **配置驱动**：通过 YAML/环境变量驱动运行时行为，支持多环境（dev/staging/prod）配置切换。
- **AgentScope 生态兼容**：与 AgentScope 框架共享工具定义规范，但运行时完全独立部署。

## 技术栈

- **语言**：Python 3.10+
- **Web 框架**：FastAPI / Starlette
- **沙箱引擎**：Docker SDK for Python / nsjail
- **可观测性**：OpenTelemetry SDK（tracing + metrics + logging）
- **配置管理**：YAML + pydantic-settings
- **异步**：asyncio + uvicorn

## 关联

- **上游**：AgentScope（agentscope-ai/agentscope）—— Agent 编排框架，AgentScope-Runtime 是其工具执行层的独立实现。
- **同类项目**：e2b-dev/e2b（Code Interpreter SDK）、OpenAI Code Interpreter、ag2ai/ag2（AutoGen 的沙箱执行模块）。
- **团队相关**：团队自研 Agent 平台在工具沙箱安全方案上可参考其容器隔离和资源限制策略。

## 开放问题

- 沙箱逃逸防护的完整性与 e2b 等商业方案相比有哪些差距？
- 多租户场景下的冷启动延迟优化策略？
- 与 AgentScope 框架之外的 Agent 框架（如 LangChain、CrewAI）的集成成熟度？
- 社区活跃度和维护响应速度？
