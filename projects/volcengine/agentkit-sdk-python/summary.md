# agentkit-sdk-python

<!-- 快照行 -->
<!-- 入口行 -->
<!-- 架构行 -->
<!-- 热点行 -->

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

AgentKit 是火山引擎（Volcengine）开源的 AI Agent 开发与部署工具包，提供 Python SDK 和 CLI 脚手架工具。团队以**上游贡献**方式参与，关注其在 Agent 运行时、沙箱执行、工具编排方面的设计思路，作为团队自研 Agent 基础设施的参考实现。

## 项目介绍

面向 Python 开发者的 AI Agent 快速启动工具包，通过 CLI 一键生成 Agent 项目骨架，提供标准化的工具注册、沙箱执行、LLM 调用等 SDK 能力，帮助开发者将 Agent 从原型快速推向生产部署。

## 核心场景

- **Agent 快速原型开发**：CLI 工具一键生成项目脚手架，内置常用 Agent 模板（如 ReAct、Plan-and-Execute），降低 Agent 开发门槛。
- **工具编排与沙箱执行**：提供标准化的工具注册与调用接口，支持在受控沙箱环境中执行 Agent 生成的代码，保障宿主系统安全。
- **多模型适配**：SDK 抽象了 LLM 调用层，支持接入火山方舟、OpenAI 兼容等多家模型提供商，开发者无需关心底层 API 差异。
- **生产级 Agent 部署**：提供配置管理、日志追踪、错误处理等工程化能力，帮助 Agent 从实验阶段过渡到线上服务。

## 技术要点

- **CLI 脚手架工具**：基于 Click/Typer 框架构建，支持交互式项目初始化、模板选择、依赖安装，生成符合最佳实践的项目结构。
- **工具注册机制**：提供 `@tool` 装饰器风格的函数注册方式，自动生成 JSON Schema 供 LLM Function Calling 使用，支持同步/异步工具。
- **沙箱执行引擎**：Agent 生成的代码在隔离沙箱中运行，支持 Docker/进程级隔离，限制网络、文件系统、系统调用等权限，防止恶意代码执行。
- **多协议支持**：除了原生工具调用外，兼容 MCP（Model Context Protocol）协议，可接入外部 MCP Server 扩展 Agent 能力边界。
- **可观测性**：内置 OpenTelemetry 追踪，记录 Agent 推理链路的每一步（LLM 调用、工具执行、中间结果），便于调试和性能分析。
- **插件化架构**：LLM Provider、Memory 存储、工具后端均可通过插件接口替换，支持开发者按需定制组件。

## 技术栈

- 语言：Python 3.10+
- CLI 框架：Click / Typer
- LLM 接入：火山方舟 SDK、OpenAI 兼容 API
- 沙箱：Docker、subprocess 隔离
- 可观测性：OpenTelemetry
- 协议：MCP（Model Context Protocol）
- 包管理：Poetry / uv

## 关联

- 上游：火山方舟（Volcengine Ark）大模型平台
- 同类项目：Anthropic Claude Code SDK、OpenAI Agents SDK、LangChain/langgraph、CrewAI、AutoGen
- 协议依赖：MCP（Model Context Protocol）规范

## 开放问题

- 沙箱隔离的安全性是否经过独立审计？
- 社区活跃度如何？核心维护者是否以火山引擎员工为主（bus factor 风险）？
- 与 LangChain/langgraph 等成熟框架的差异化定位是否足够清晰？
- 是否支持多 Agent 协作编排（multi-agent orchestration）？
- Python 版本兼容性策略：最低支持 Python 3.10 是否会随社区趋势上调？
