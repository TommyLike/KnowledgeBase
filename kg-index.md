# KG 全局索引

> 自动生成于 2026-07-10 04:13 UTC · 617 projects · 497 有摘要 · 5 references

## 快速导航

- [🎯 Agent 开发框架](#agent-framework) (19 projects)
- [⚙️ Agent 运行时](#agent-runtime) (72 projects)
  - [🛡️ 沙箱运行时](#agent-runtime-sandbox) (27 projects)
  - [🧠 记忆层](#agent-runtime-memory) (14 projects)
  - [🚪 网关](#agent-runtime-gateway) (10 projects)
  - [📊 可观测性](#agent-runtime-observability) (10 projects)
  - [🔧 工具](#agent-runtime-tool) (7 projects)
  - [📡 协议](#agent-runtime-protocol) (2 projects)
  - [🗺️ 规划器](#agent-runtime-planner) (1 projects)
  - [🔒 安全](#agent-runtime-security) (1 projects)
- [💾 Agent 存储](#agent-storage) (7 projects)
- [🏗️ Agent 基础设施](#agent-infra) (7 projects)
- [☁️ 多云](#multi-cloud) (2 projects)
- [🏢 OpenSourceWay (团队仓库群)](#opensourceways) (397 projects)
- [🔬 COSDT (团队仓库群)](#cosdt) (23 projects)
- [🚀 vLLM Project (上游)](#vllm-project) (39 projects)
- [⚡ SGL Project (上游)](#sgl-project) (22 projects)
- [🔺 Triton Lang (上游)](#triton-lang) (5 projects)
- [🔥 PyTorch (上游)](#pytorch) (18 projects)
- [🧩 Tile-AI (上游)](#tile-ai) (6 projects)

---

## 🎯 Agent 开发框架

*19 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [adk-python](projects/agent-framework/adk-python/summary.md) | Python, Java, A2A Protocol, Google Cloud | `agent` `framework` `上游贡献` |
| [agent-framework](projects/agent-framework/agent-framework/summary.md) | Python, C#, Azure, Durable Functions | `agent` `framework` `上游贡献` |
| [agno](projects/agent-framework/agno/summary.md) | - **Agent 服务平台**：多租户、多用户 Agent 平台，支持 JWT + RBAC 权限隔离，每个用户拥有独立 Agent | `agent` |
| [autogen](projects/agent-framework/autogen/summary.md) | - **多 Agent 角色分工**：数学专家 + 代码专家 + 通用助手等角色组成 Agent 团队，各司其职协同解决问题 | `agent` |
| [camel](projects/agent-framework/camel/summary.md) | - **角色扮演式任务协作**：Agent 扮演不同专业角色（医生、律师、工程师），通过结构化对话协同完成任务 | `agent` |
| [crewAI](projects/agent-framework/crewAI/summary.md) | - **角色型多 Agent 协作**：定义 Researcher / Writer / Reviewer 等角色，Agent 按角色分工完成研究→撰写→审核流程 | `agent` |
| [dify](projects/agent-framework/dify/summary.md) | Python(后端), TypeScript(前端), PostgreSQL, Redis | `agent` `framework` `上游贡献` |
| [Flowise](projects/agent-framework/Flowise/summary.md) | TypeScript, Node.js, LangChain.js | `agent` `framework` `上游贡献` |
| [harness-sdk](projects/agent-framework/harness-sdk/summary.md) | - **Agent 回归测试**：代码变更后自动验证 Agent 行为是否退化 | `agent` |
| [kagent](projects/agent-framework/kagent/summary.md) | - **K8s 集群运维 Agent**：Agent 自动巡检集群健康、响应 Prometheus 告警、执行 Helm 部署 | `agent` |
| [langchain](projects/agent-framework/langchain/summary.md) | - **模型统一调用**：通过统一的 LLM/ChatModel 接口屏蔽 OpenAI/Anthropic/Google/HuggingFace 等 50+ 模型提供商的 API 差异，支持流式输出 | `agent` |
| [langgraph](projects/agent-framework/langgraph/summary.md) | - **ReAct Agent 循环**：Think → Act → Observe 经典循环，LLM 自主决定停止/调工具/求助 | `agent` |
| [llama_index](projects/agent-framework/llama_index/summary.md) | Python, TypeScript, 向量数据库 | `agent` `framework` `上游贡献` |
| [mastra](projects/agent-framework/mastra/summary.md) | TypeScript, Node.js | `agent` `framework` `上游贡献` |
| [NeMo-Agent-Toolkit](projects/agent-framework/NeMo-Agent-Toolkit/summary.md) | Python, NVIDIA NIM, CUDA | `agent` `framework` `上游贡献` |
| [openai-agents-python](projects/agent-framework/openai-agents-python/summary.md) | Python, OpenAI API | `agent` `framework` `上游贡献` |
| [pydantic-ai](projects/agent-framework/pydantic-ai/summary.md) | - **类型安全的 Agent 开发**：Agent 的依赖类型和输出类型通过泛型约束，IDE 完整自动补全 | `agent` |
| [semantic-kernel](projects/agent-framework/semantic-kernel/summary.md) | - **企业 AI 聊天机器人**：将 LLM 与企业客服系统、工单系统连接，Agent 自动分类和处理工单 | `agent` |
| [smolagents](projects/agent-framework/smolagents/summary.md) | - **Agent 原型快速构建**：核心逻辑仅约 1000 行 Python 代码，开发者可在极短时间内理解并扩展 Agent 行为，适合研究和快速实验 | `agent` |

## ⚙️ Agent 运行时

*72 projects across 8 sub-domains*

### agent-runtime › sandbox

*🛡️ 沙箱运行时 — 27 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [agent-aegis](projects/agent-runtime/sandbox/agent-aegis/summary.md) | - **Prompt Injection 防护**：检测并拦截恶意 prompt 注入攻击 | `agent` `sandbox` `security` `上游贡献` |
| [agent-sandbox](projects/agent-runtime/sandbox/agent-sandbox/summary.md) | - **K8s 上 Agent 代码安全执行**：Agent 在 Sandbox CRD 定义的隔离 Pod 中执行代码 | `agent` |
| [agentcore-cli](projects/agent-runtime/sandbox/agentcore-cli/summary.md) | - **Agent 本地开发与测试**：`agentcore dev` 本地运行和调试 Agent | `agent` `runtime` `aws` `cli` `上游贡献` |
| [agentcore-samples](projects/agent-runtime/sandbox/agentcore-samples/summary.md) | Amazon Bedrock Agentcore 的官方示例和参考实现仓库，由 AWS 实验室（awslabs）维护。展示如何利用 Bedrock Agentcore 平台将 AI Agent 从原型 | `agent` `runtime` `aws` `上游贡献` |
| [agentcube](projects/agent-runtime/sandbox/agentcube/summary.md) | - **GPU Agent 沙箱**：为需要 GPU 的 Agent（LLM 推理）提供 GPU 资源隔离的沙箱环境 | `agent` `sandbox` `kubernetes` `上游贡献` |
| [agentkit-sdk-python](projects/agent-runtime/sandbox/agentkit-sdk-python/summary.md) | AgentKit 是火山引擎（Volcengine）开源的 AI Agent 开发与部署工具包，提供 Python SDK 和 CLI 脚手架工具。团队以**上游贡献**方式参与，关注其在 Agent | `agent` `runtime` `sdk` `上游贡献` |
| [agents](projects/agent-runtime/sandbox/agents/summary.md) | OpenKruise 团队推出的 Agent 沙箱 Operator，为 Kubernetes 上运行 AI Agent 所需的代码执行沙箱提供快速、低成本的部署与管理方案。本项目属于上游贡献范畴，团 | `agent` `sandbox` `kubernetes` `上游贡献` |
| [agentscope-runtime](projects/agent-runtime/sandbox/agentscope-runtime/summary.md) | AgentScope-Runtime 是 AgentScope 生态中的生产级 Agent 应用运行时框架，专注于为 AI Agent 提供安全的工具执行沙箱和全链路可观测性。本项目属于**上游贡献* | `agent` `runtime` `sandbox` `上游贡献` |
| [agentscope-runtime-java](projects/agent-runtime/sandbox/agentscope-runtime-java/summary.md) | agentscope-runtime-java 是 AgentScope 生态的 Java 运行时组件，定位为 AI Agent 的部署执行环境和工具沙箱。项目属于上游贡献范畴，团队关注其在 Java | `agent` `runtime` `java` `上游贡献` |
| [AgentTeams](projects/agent-runtime/sandbox/AgentTeams/summary.md) | AgentTeams 是 agentscope-ai 组织下的开源协作式多智能体操作系统（Collaborative Multi-Agent OS），面向需要透明编排、人机协同的多智能体场景。项目在知 | `agent` `runtime` `multi-agent` `上游贡献` |
| [ax](projects/agent-runtime/sandbox/ax/summary.md) | Google 开源的分布式 Agent 运行时，属于 agent-runtime/sandbox 类别。团队以**上游贡献**方式参与，关注分布式 Agent 编排、沙箱执行环境、以及多 Agent  | `agent` `runtime` `distributed` `上游贡献` |
| [bedrock-agentcore-starter-toolkit](projects/agent-runtime/sandbox/bedrock-agentcore-starter-toolkit/summary.md) | Amazon Bedrock AgentCore 的官方 CLI 启动工具包，属于 AWS 团队的上游贡献项目。提供一套标准化的 Python 命令行工具，帮助开发者在本地快速创建、配置、测试和部署  | `agent` `runtime` `aws` `上游贡献` |
| [coder](projects/agent-runtime/sandbox/coder/summary.md) | - **远程开发环境**：开发者浏览器打开 VS Code/JetBrains/SSH，背后是云上 Linux 工作空间 | `agent` |
| [cohere-terrarium](projects/agent-runtime/sandbox/cohere-terrarium/summary.md) | Terrarium 是 Cohere 开源的一个轻量级 Python 代码沙箱，专为 LLM 数据 Agent 场景设计。在我们的知识图谱中归类为 agent-runtime/sandbox，属于上游 | `agent` `sandbox` `上游贡献` |
| [CubeSandbox](projects/agent-runtime/sandbox/CubeSandbox/summary.md) | - **Agent 代码安全执行**：不受信任代码在隔离沙箱中运行 | `agent` |
| [cwc-long-running-agents](projects/agent-runtime/sandbox/cwc-long-running-agents/summary.md) | Anthropic 官方发布的长时间运行 Agent 参考实现，基于 Claude Computer Use (CWC) 能力构建。该项目展示了如何在沙箱环境中让 Agent 持续工作数小时甚至数天， | `agent` `runtime` `long-running` `上游贡献` |
| [DTVM](projects/agent-runtime/sandbox/DTVM/summary.md) | DTVM（DeTerministic Virtual Machine）是一个面向 AI Agent 的确定性虚拟机项目，由 DTVMStack 组织维护。本项目在知识图谱中标记为**上游贡献**，团队 | `agent` `runtime` `vm` `上游贡献` |
| [infra](projects/agent-runtime/sandbox/infra/summary.md) | - **Agent 代码执行沙箱**：Agent 生成的 Python/Bash 代码在隔离 Firecracker VM 中安全执行 | `agent` |
| [NemoClaw](projects/agent-runtime/sandbox/NemoClaw/summary.md) | NVIDIA 开源的 Agent 安全运行时环境，用于在 NVIDIA OpenShell 内安全运行 Hermes、OpenClaw 等 AI Agent。属于团队上游贡献范畴，关注其 sandbo | `agent` `runtime` `security` `上游贡献` |
| [OpenSandbox](projects/agent-runtime/sandbox/OpenSandbox/summary.md) | - **Coding Agent 代码执行**：为 Claude Code、Gemini CLI、OpenAI Codex CLI、Qwen Code、Kimi CLI 等编程 Agent 提供隔离的 | `agent` |
| [OpenShell](projects/agent-runtime/sandbox/OpenShell/summary.md) | - **凭据零暴露的 LLM 访问**：Agent 需要调用 Claude/Codex/Copilot/Cursor/Bedrock/Vertex 等（`providers/*.yaml` 内置 11 | `agent` `sandbox` `runtime` `上游贡献` |
| [OpenShell-Community](projects/agent-runtime/sandbox/OpenShell-Community/summary.md) | - **社区贡献入口**：向 OpenShell 生态贡献的第一个目标仓库 | `agent` `runtime` `community` `上游贡献` |
| [sandbox](projects/agent-runtime/sandbox/sandbox/summary.md) | - **沙箱实现可替换**：Agent 框架按标准接口调用，底层沙箱可切换 E2B/Firecracker/Docker | `agent` |
| [sandbox-runtime](projects/agent-runtime/sandbox/sandbox-runtime/summary.md) | - **Agent 命令安全执行**：Claude Code 的 Bash 命令、MCP Server 调用自动通过 srt 沙箱化，防止 Agent 读取敏感文件或访问未授权网络 | `agent` `sandbox` `上游贡献` |
| [sandbox-sdk](projects/agent-runtime/sandbox/sandbox-sdk/summary.md) | Cloudflare Sandbox SDK 是 Cloudflare 开源的边缘沙箱运行环境方案，团队以**上游贡献**方式参与。该 SDK 允许开发者在 Cloudflare 全球边缘网络上创建和 | `agent` `sandbox` `边缘计算` `上游贡献` |
| [shell](projects/agent-runtime/sandbox/shell/summary.md) | shell 是 strands-agents 生态中的沙箱化 Shell 执行组件，为 AI Agent 提供受控的命令行环境。项目在 KG 中的定位为**上游贡献**——团队关注其沙箱隔离机制和 A | `agent` `sandbox` `上游贡献` |
| [WindowsAgentArena](projects/agent-runtime/sandbox/WindowsAgentArena/summary.md) | Windows Agent Arena 是微软研究院推出的面向 Windows 操作系统的 AI Agent 基准测试与可扩展沙盒平台。该项目在知识图谱中归类为 agent-runtime/sandb | `agent` `runtime` `windows` `上游贡献` |

### agent-runtime › memory

*🧠 记忆层 — 14 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [beads](projects/agent-runtime/memory/beads/summary.md) | - **Agent 统一检索**：Agent 的语义搜索 + 关键词搜索 + 关系遍历在一个查询中组合 | `agent` |
| [hindsight](projects/agent-runtime/memory/hindsight/summary.md) | - **Agent 决策溯源**：回溯 Agent 为何在特定时刻做了特定决策 | `agent` |
| [letta](projects/agent-runtime/memory/letta/summary.md) | - **长对话 Agent**：Agent 维护超出模型上下文窗口的长篇对话历史，自动换入换出记忆块 | `agent` |
| [mem0](projects/agent-runtime/memory/mem0/summary.md) | - **个性化 Agent**：Agent 记住用户姓名、偏好、习惯，不同用户使用同一 Agent 获得个性化体验 | `agent` |
| [mempalace](projects/agent-runtime/memory/mempalace/summary.md) | - **AI Agent 跨会话记忆**：与 Claude Code、Gemini CLI、Cursor IDE 等集成，通过 MCP Server 提供 35 个记忆工具，Agent 在会话开始时通 | `agent` |
| [memU](projects/agent-runtime/memory/memU/summary.md) | - **跨会话持久记忆**：Agent 用户在多次对话中保持一致的个人档案、偏好和目标记忆，无需每次重复自我介绍 | `agent` |
| [NoKV](projects/agent-runtime/memory/NoKV/summary.md) | - **Agent 状态持久化**：会话状态以原生对象形式存储和恢复 | `agent` |
| [OpenViking](projects/agent-runtime/memory/OpenViking/summary.md) | OpenViking 是字节跳动/火山引擎开源的面向 AI Agent 的上下文数据库，为团队在上游 Agent 基础设施层的关注项目。我们关注其在高性能向量检索、混合存储引擎、以及 Agent 记忆 | `agent` `memory` `context` `上游贡献` |
| [powermem](projects/agent-runtime/memory/powermem/summary.md) | PowerMem 是 OceanBase 开源的 AI Memory 插件，属于 agent-runtime 生态中的记忆管理组件。本项目为上游贡献关注，团队关注其在 AI Agent 记忆管理领域的 | `agent` `memory` `上游贡献` |
| [ragflow](projects/agent-runtime/memory/ragflow/summary.md) | - **企业知识库 Agent**：上传所有内部文档 → RAGFlow 自动解析和索引 → Agent 用自然语言查询 | `agent` |
| [ReMe](projects/agent-runtime/memory/ReMe/summary.md) | ReMe 是 AgentScope 团队开源的 Agent 记忆管理工具包，为 LLM Agent 提供可扩展的长期记忆能力。团队将其纳入知识图谱作为上游贡献项目，关注其在记忆检索、记忆总结和跨会话上 | `agent` `memory` `上游贡献` |
| [seekdb](projects/agent-runtime/memory/seekdb/summary.md) | - **Agent 数据一站式存储**：结构化数据 + 向量索引 + 全文搜索在同一数据库中 | `agent` |
| [supabase](projects/agent-runtime/memory/supabase/summary.md) | - **Agent 用户数据管理**：用户画像、偏好设置、Agent 配置以结构化数据存储 | `agent` |
| [TencentDB-Agent-Memory](projects/agent-runtime/memory/TencentDB-Agent-Memory/summary.md) | - **个性化 Agent 助手**：记住用户姓名、偏好、习惯、历史任务，跨会话保持一致的交互体验，避免每次对话「从零开始」 | `agent` `memory` `上游贡献` |

### agent-runtime › gateway

*🚪 网关 — 10 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [agentgateway](projects/agent-runtime/gateway/agentgateway/summary.md) | - **Agent 注册与发现**：Agent 启动时注册到网关，声明能力和端点 | `agent` |
| [ai-gateway](projects/agent-runtime/gateway/ai-gateway/summary.md) | - **LLM 流量统一网关**：所有服务调用 LLM API 统一通过 Envoy AI Gateway，集中管理 API Key 和审计 | `agent` |
| [cc-switch](projects/agent-runtime/gateway/cc-switch/summary.md) | - **多工具 API 提供商统一切换**：一处配置 API Key 后自动同步到 Claude Code、Codex、Gemini CLI 等所有工具的配置文件，支持 50+ 内置提供商预设（AWS | `agent` |
| [CLIProxyAPI](projects/agent-runtime/gateway/CLIProxyAPI/summary.md) | - **CLI 工具 AI 赋能**：已有命令行工具通过 CLIProxyAPI 获得自然语言处理能力 | `agent` |
| [higress](projects/agent-runtime/gateway/higress/summary.md) | - **AI 模型统一接入**：作为企业内所有 LLM 调用（OpenAI、通义千问、DeepSeek、vLLM、Ollama 等 100+ 提供商）的统一入口，提供 OpenAI 兼容协议转换、多模 | `agent` |
| [kgateway](projects/agent-runtime/gateway/kgateway/summary.md) | - **K8s 集群内 AI 流量管理**：Agent 微服务通过 kgateway 访问外部 LLM API，统一鉴权和速率控制 | `agent` |
| [litellm](projects/agent-runtime/gateway/litellm/summary.md) | - **Agent 多模型切换**：Agent 代码只写一次，通过修改 `model` 参数在 GPT-4o / Claude / Gemini / DeepSeek 间自由切换 | `agent` |
| [mcp-gateway-registry](projects/agent-runtime/gateway/mcp-gateway-registry/summary.md) | - **企业 MCP 服务器统一接入**：AI 编码助手和 Agent 通过单一 Nginx 网关接入，自动路由到后端多个 MCP 服务器，消除每个 IDE 单独配置 MCP 端点的痛点，集中管理认证 | `agent` |
| [new-api](projects/agent-runtime/gateway/new-api/summary.md) | - **多模型统一接入**：通过单一 API 入口管理 OpenAI、Claude、Gemini、Midjourney、Suno 等多个厂商的模型，无需在各平台分别申请 Key | `agent` |
| [rtk](projects/agent-runtime/gateway/rtk/summary.md) | - **Git 操作输出截断**：`git status`、`git diff`、`git log` 等高频命令输出常达数千 Token，rtk 提取统计数据后仅输出摘要，压缩率达 85–99%。 | `agent` |

### agent-runtime › observability

*📊 可观测性 — 10 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [deepeval](projects/agent-runtime/observability/deepeval/summary.md) | - **RAG 质量评估**：评估检索相关性（Contextual Relevancy）和生成忠实度（Faithfulness/Hallucination） | `agent` |
| [langfuse](projects/agent-runtime/observability/langfuse/summary.md) | - **Agent 调用链追踪**：Agent → LLM call 1 → Tool call → LLM call 2 → Output 的完整 Trace，每步延迟和 token 用量可见 | `agent` |
| [lm-evaluation-harness](projects/agent-runtime/observability/lm-evaluation-harness/summary.md) | - **学术基准测试**：在 MMLU、HellaSwag、ARC、GSM8K、TruthfulQA 等 60+ 学术基准上评估模型能力，支持生成式 (generate_until) 和对数似然 (l | `agent` |
| [openlit](projects/agent-runtime/observability/openlit/summary.md) | - **GPU 资源监控**：实时追踪 Agent 推理时的 GPU 利用率、显存、温度 | `agent` |
| [openllmetry](projects/agent-runtime/observability/openllmetry/summary.md) | - **LLM 调用的 OTel 标准化追踪**：Agent 的每次 LLM 调用以标准 Span 形式记录，兼容所有 OTel 后端 | `agent` |
| [opik](projects/agent-runtime/observability/opik/summary.md) | - **Agent Trace 追踪**：Agent 步骤级 LLM 调用全链路追踪，延迟/token/成本可视化 | `agent` |
| [phoenix](projects/agent-runtime/observability/phoenix/summary.md) | - **LLM 应用运行时追踪**：通过 30+ 自动插桩器（LangChain、LlamaIndex、OpenAI、Anthropic、Bedrock 等），捕获 LLM 调用的完整 Span 层级 | `agent` |
| [promptfoo](projects/agent-runtime/observability/promptfoo/summary.md) | - **Prompt Injection 测试**：批量执行已知注入攻击向量，检测模型是否被 bypass | `agent` |
| [ragas](projects/agent-runtime/observability/ragas/summary.md) | - **Retriever 质量评估**：评估检索组件返回的文档与 query 的 Contextual Precision/Recall | `agent` |
| [trulens](projects/agent-runtime/observability/trulens/summary.md) | - **RAG 系统质量评估**：通过 RAG 三合一（答案相关性、上下文相关性、事实一致性）自动评测检索增强生成系统，在每次 Prompt/模型/检索策略变更后快速发现退化。 | `agent` |

### agent-runtime › tool

*🔧 工具 — 7 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [agent-browser](projects/agent-runtime/tool/agent-browser/summary.md) | - **Agent 网页信息提取**：打开 URL → 截图 → 提取文本内容 | `agent` |
| [browser-harness](projects/agent-runtime/tool/browser-harness/summary.md) | - **自定义浏览器 Agent**：在 Browser Harness 上构建自己的 AI 浏览器操作逻辑 | `agent` |
| [browser-use](projects/agent-runtime/tool/browser-use/summary.md) | - **Web 自动化 Agent**：Agent 自主完成「打开网站→搜索产品→比较价格→加购物车→填写地址→下单」完整流程 | `agent` |
| [composio](projects/agent-runtime/tool/composio/summary.md) | - **SaaS 自动化 Agent**：Agent 自动读邮件（Gmail）→ 在日历找空档（Google Calendar）→ 创建任务（Jira）→ 发通知（Slack） | `agent` |
| [firecrawl](projects/agent-runtime/tool/firecrawl/summary.md) | - **RAG 数据源准备**：Agent 编写文档→抓取技术博客→转为 Markdown→存入向量数据库的完整 Pipeline | `agent` |
| [page-agent](projects/agent-runtime/tool/page-agent/summary.md) | - **网页结构理解**：DOM 解析 → 提取关键元素（表单、按钮、链接、表格） | `agent` |
| [reader](projects/agent-runtime/tool/reader/summary.md) | - **RAG 知识库构建**：将任意网页、文档 URL 转换为结构化 Markdown，直接喂入向量数据库或 LLM 上下文，无需编写爬虫脚本 | `agent` |

### agent-runtime › protocol

*📡 协议 — 2 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [A2A](projects/agent-runtime/protocol/A2A/summary.md) | - **跨框架 Agent 协作**：LangChain Agent 发现并委派子任务给 AutoGen Agent，通过 A2A 协议标准化通信 | `agent` |
| [modelcontextprotocol](projects/agent-runtime/protocol/modelcontextprotocol/summary.md) | - **统一工具接口**：MCP Server 一次开发，所有 MCP Client（Claude Desktop、Cursor、VS Code Copilot 等）即插即用 | `agent` |

### agent-runtime › planner

*🗺️ 规划器 — 1 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [gpt-researcher](projects/agent-runtime/planner/gpt-researcher/summary.md) | - **深度研究报告生成**：自动生成 2,000+ 词的调研报告，支持 PDF/Word/Markdown 三种格式导出 | `agent` |

### agent-runtime › security

*🔒 安全 — 1 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [llm-guard](projects/agent-runtime/security/llm-guard/summary.md) | - **Prompt Injection 检测**：识别用户输入中的恶意注入指令，防止绕过 Agent 的 system prompt | `agent` |

## 💾 Agent 存储

*7 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [chroma](projects/agent-storage/chroma/summary.md) | - **RAG Agent 知识库**：文档分块 → 嵌入 → 存入 Chroma → Agent 查询时检索相关上下文 | `agent` |
| [lancedb](projects/agent-storage/lancedb/summary.md) | - **RAG 应用后端**：为 LLM 提供向量检索，支持混合查询（向量 + 全文搜索 + SQL 过滤），原生集成 LangChain 和 LlamaIndex | `agent` |
| [marqo](projects/agent-storage/marqo/summary.md) | - **多模态 Agent 记忆**：Agent 的对话文本 + 截图 + 文档混合存储，统一张量空间跨模态检索 | `agent` |
| [milvus](projects/agent-storage/milvus/summary.md) | - **大规模 RAG Agent 知识库**：企业级文档管理，十亿级文档片段的向量化存储和实时检索 | `agent` |
| [opensearch](projects/agent-storage/opensearch/summary.md) | - **RAG 混合检索**：BM25 关键词搜索 + k-NN 向量搜索组合，兼顾精确匹配和语义理解 | `agent` |
| [qdrant](projects/agent-storage/qdrant/summary.md) | - **实时语义搜索**：用户查询 → embedding → Qdrant 检索 → 返回 top-k 相关文档片段的 RAG 流程 | `agent` |
| [weaviate](projects/agent-storage/weaviate/summary.md) | - **零代码 RAG 原型**：写入文本 → Weaviate 自动 embedding → GraphQL 查询 → 返回相关文档 + 生成回答 | `agent` |

## 🏗️ Agent 基础设施

*7 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [firecracker](projects/agent-infra/firecracker/summary.md) | - **Agent 代码执行沙箱**：Agent 生成的不受信任代码在 Firecracker microVM 中安全运行，即使代码恶意也无法突破 VM 边界 | `agent` |
| [inngest](projects/agent-infra/inngest/summary.md) | - **多步骤 Agent 工作流**：Agent 需求分析 → 代码生成 → 测试 → 部署，每一步是 Inngest Step，自动重试和恢复 | `agent` |
| [nats-server](projects/agent-infra/nats-server/summary.md) | - **微服务间异步通信**：作为服务网格的消息总线，通过 Subject-Based Pub/Sub 实现服务间松耦合异步通信，支持请求-回复（Request-Reply）模式实现 RPC 语义，可 | `agent` |
| [redpanda](projects/agent-infra/redpanda/summary.md) | - **实时消息队列与事件流**：作为 Kafka 的即插即用替代品，支撑微服务间异步通信、事件溯源和 CDC（变更数据捕获）。 | `agent` |
| [restate](projects/agent-infra/restate/summary.md) | - **Agent 工具调用可靠性**：Agent 调用搜索 API → 调用数据库 → 调用 LLM 这一多步流程中，前两步成功后第三步失败，Restate 从第三步恢复而非从头开始 | `agent` |
| [temporal](projects/agent-infra/temporal/summary.md) | - **AI Agent 与 MCP 管道编排**：编排多步 LLM 调用、工具执行和人工审批的 Agent 工作流，每个步骤自动重试，状态持久化保证 Agent 不会因中间故障丢失进度 | `agent` |
| [trigger.dev](projects/agent-infra/trigger.dev/summary.md) | - **Agent 多步骤任务编排**：Research → LLM Summary → Email → Slack Notify 每个步骤自动持久化和重试 | `agent` |

## ☁️ 多云

*2 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [karmada](projects/multi-cloud/karmada/summary.md) | - 分离式架构：Resource Template（标准 K8s 资源）+ PropagationPolicy（调度策略）+ OverridePolicy（差异化配置） | `上游贡献` `multi-cluster` `kubernetes` `scheduling` `cncf` |
| [liqo](projects/multi-cloud/liqo/summary.md) | - Virtual Kubelet 虚拟节点：远程集群映射为本地 K8s Node，标准 K8s 调度器即可使用 | `上游贡献` `multi-cluster` `kubernetes` `scheduling` |

## 🏢 OpenSourceWay (团队仓库群)

*397 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [2022shanghai-covid](projects/opensourceways/2022shanghai-covid/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `community` `python` `团队主导` |
| [agent-development-specification](projects/opensourceways/agent-development-specification/summary.md) | *待补充* | `ai-agent` `ci-cd` `shell` `团队主导` |
| [agent-framwork](projects/opensourceways/agent-framwork/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `python` `团队主导` |
| [agent-skills](projects/opensourceways/agent-skills/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `python` `团队主导` |
| [ai-auto-test](projects/opensourceways/ai-auto-test/summary.md) | *待补充* | `ai-agent` `shell` `团队主导` |
| [ai-native-develop-infra](projects/opensourceways/ai-native-develop-infra/summary.md) | *待补充* | `ai-agent` `shell` `团队主导` |
| [ai-proxy](projects/opensourceways/ai-proxy/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `python` `团队主导` |
| [aibrix-deploy](projects/opensourceways/aibrix-deploy/summary.md) | - YAML (K8S/Helm) | `ai-agent` `deploy` `团队主导` |
| [aidigest](projects/opensourceways/aidigest/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `python` `团队主导` |
| [apig-discovery-service](projects/opensourceways/apig-discovery-service/summary.md) | - Python · Git · Docker · CI/CD | `backend` `python` `团队主导` |
| [apig-openapi-registry](projects/opensourceways/apig-openapi-registry/summary.md) | - Markdown (文档) | `backend` `团队主导` |
| [apig-registry-tools](projects/opensourceways/apig-registry-tools/summary.md) | - Python · Git · Docker · CI/CD | `backend` `cli` `python` `团队主导` |
| [APIMagic](projects/opensourceways/APIMagic/summary.md) | - MAXScript | `backend` `团队主导` |
| [app-bot](projects/opensourceways/app-bot/summary.md) | - YAML (K8S/Helm) | `团队主导` |
| [app-bugzilla](projects/opensourceways/app-bugzilla/summary.md) | *待补充* | `community` `docker` `团队主导` |
| [app-cla-server](projects/opensourceways/app-cla-server/summary.md) | - Go · Git · Docker · CI/CD | `auth` `backend` `go` `repo-management` `团队主导` |
| [app-cla-signing](projects/opensourceways/app-cla-signing/summary.md) | - Go · Git · Docker · CI/CD | `auth` `go` `团队主导` |
| [app-cla-stat](projects/opensourceways/app-cla-stat/summary.md) | - Go · Git · Docker · CI/CD | `auth` `data` `go` `团队主导` |
| [app-cla-webui](projects/opensourceways/app-cla-webui/summary.md) | - JavaScript | `auth` `frontend` `javascript` `团队主导` |
| [app-community-metadata](projects/opensourceways/app-community-metadata/summary.md) | - Go · Git · Docker · CI/CD | `community` `data` `go` `团队主导` |
| [app-cve-backend](projects/opensourceways/app-cve-backend/summary.md) | - Java · Git · Docker · CI/CD | `backend` `java` `security` `团队主导` |
| [app-cve-frontend](projects/opensourceways/app-cve-frontend/summary.md) | *待补充* | `css` `frontend` `security` `团队主导` |
| [app-jenkins](projects/opensourceways/app-jenkins/summary.md) | *待补充* | `ci-cd` `团队主导` |
| [app-kubernetes-maintenance](projects/opensourceways/app-kubernetes-maintenance/summary.md) | *待补充* | `ai-agent` `docker` `frontend` `kubernetes` `repo-management` `团队主导` |
| [app-mailman](projects/opensourceways/app-mailman/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `email` `frontend` `kubernetes` `python` `团队主导` |
| [app-meeting-server](projects/opensourceways/app-meeting-server/summary.md) | - Python · Git · Docker · CI/CD | `backend` `community` `python` `团队主导` |
| [app-meetingbot](projects/opensourceways/app-meetingbot/summary.md) | *待补充* | `community` `docker` `团队主导` |
| [app-patchtracking](projects/opensourceways/app-patchtracking/summary.md) | *待补充* | `community` `docker` `团队主导` |
| [app-pkgmanage](projects/opensourceways/app-pkgmanage/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [app-publish](projects/opensourceways/app-publish/summary.md) | - Java · Git · Docker · CI/CD | `java` `团队主导` |
| [app-repo](projects/opensourceways/app-repo/summary.md) | *待补充* | `backend` `css` `repo-management` `团队主导` |
| [app-robot-server](projects/opensourceways/app-robot-server/summary.md) | - Starlark | `backend` `bot` `团队主导` |
| [app-robot-webui](projects/opensourceways/app-robot-webui/summary.md) | *待补充* | `bot` `frontend` `团队主导` |
| [app-ssh-tunnel](projects/opensourceways/app-ssh-tunnel/summary.md) | *待补充* | `docker` `kubernetes` `团队主导` |
| [argocd-application](projects/opensourceways/argocd-application/summary.md) | - YAML (K8S/Helm) | `ci-cd` `deploy` `团队主导` |
| [argus-controller](projects/opensourceways/argus-controller/summary.md) | - Go · Git · Docker · CI/CD | `ci-cd` `git-platform` `go` `workflow` `团队主导` |
| [argus-worker](projects/opensourceways/argus-worker/summary.md) | - Go · Git · Docker · CI/CD | `ci-cd` `git-platform` `go` `kubernetes` `workflow` `团队主导` |
| [argus-workflow-demo](projects/opensourceways/argus-workflow-demo/summary.md) | - Go · Git · Docker · CI/CD | `git-platform` `go` `workflow` `团队主导` |
| [ascend-ci-argocd](projects/opensourceways/ascend-ci-argocd/summary.md) | - Mustache | `ascend` `ci-cd` `git-platform` `团队主导` |
| [ascend-ci-deployment](projects/opensourceways/ascend-ci-deployment/summary.md) | *待补充* | `ascend` `ci-cd` `deploy` `kubernetes` `shell` `团队主导` |
| [ascend-ci-permission](projects/opensourceways/ascend-ci-permission/summary.md) | *待补充* | `ascend` `ci-cd` `团队主导` |
| [ascend-ci-project](projects/opensourceways/ascend-ci-project/summary.md) | *待补充* | `ai-agent` `ascend` `ci-cd` `deploy` `repo-management` `团队主导` |
| [ascend-runner-onboarding](projects/opensourceways/ascend-runner-onboarding/summary.md) | - Go · Git · Docker · CI/CD | `ascend` `go` `团队主导` |
| [ascend_optimization_scripts](projects/opensourceways/ascend_optimization_scripts/summary.md) | - Python · Git · Docker · CI/CD | `ascend` `community` `python` `团队主导` |
| [audit-lib](projects/opensourceways/audit-lib/summary.md) | - Markdown (文档) | `observability` `sdk` `团队主导` |
| [auth-center](projects/opensourceways/auth-center/summary.md) | - Java · Git · Docker · CI/CD | `auth` `java` `团队主导` |
| [backlog](projects/opensourceways/backlog/summary.md) | - **AI 需求分析**：提交 `[需求]` Issue → AI 自动生成需求分析说明书→ 人评审合入 | `python` `团队主导` |
| [benchmark_llm](projects/opensourceways/benchmark_llm/summary.md) | - Python · Git · Docker · CI/CD | `llm` `python` `团队主导` |
| [bigfiles-lfs-all](projects/opensourceways/bigfiles-lfs-all/summary.md) | - Markdown (文档) | `团队主导` |
| [calculator-umbrella](projects/opensourceways/calculator-umbrella/summary.md) | - Makefile | `ai-agent` `makefile` `repo-management` `团队主导` |
| [cdn-check](projects/opensourceways/cdn-check/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [cdn-cronjob](projects/opensourceways/cdn-cronjob/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [cdn-nginx](projects/opensourceways/cdn-nginx/summary.md) | *待补充* | `docker` `团队主导` |
| [certification-all](projects/opensourceways/certification-all/summary.md) | - Markdown (文档) | `团队主导` |
| [certification-server](projects/opensourceways/certification-server/summary.md) | - Java · Git · Docker · CI/CD | `backend` `java` `团队主导` |
| [certification-website](projects/opensourceways/certification-website/summary.md) | *待补充* | `frontend` `vue` `团队主导` |
| [China-CID](projects/opensourceways/China-CID/summary.md) | *待补充* | `ci-cd` `vue` `团队主导` |
| [ci-all](projects/opensourceways/ci-all/summary.md) | - Markdown (文档) | `ci-cd` `团队主导` |
| [cla](projects/opensourceways/cla/summary.md) | *待补充* | `auth` `团队主导` |
| [cla-all](projects/opensourceways/cla-all/summary.md) | - Markdown (文档) | `auth` `团队主导` |
| [code-server-operator](projects/opensourceways/code-server-operator/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `kubernetes` `团队主导` |
| [codearts-CI](projects/opensourceways/codearts-CI/summary.md) | - Python · Git · Docker · CI/CD | `ci-cd` `python` `团队主导` |
| [codearts-ci-config](projects/opensourceways/codearts-ci-config/summary.md) | *待补充* | `ci-cd` `shell` `团队主导` |
| [codearts-workflow-image](projects/opensourceways/codearts-workflow-image/summary.md) | *待补充* | `shell` `workflow` `团队主导` |
| [cola-golang](projects/opensourceways/cola-golang/summary.md) | *待补充* | `团队主导` |
| [community-health](projects/opensourceways/community-health/summary.md) | - Python · Git · Docker · CI/CD | `cli` `community` `observability` `python` `repo-management` `团队主导` |
| [community-robot-lib](projects/opensourceways/community-robot-lib/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `sdk` `团队主导` |
| [community-robots](projects/opensourceways/community-robots/summary.md) | *待补充* | `bot` `community` `shell` `团队主导` |
| [community-sig-monitor](projects/opensourceways/community-sig-monitor/summary.md) | - Python · Git · Docker · CI/CD | `community` `frontend` `git-platform` `observability` `python` `团队主导` |
| [compass-ci](projects/opensourceways/compass-ci/summary.md) | - YAML (K8S/Helm) | `ci-cd` `deploy` `团队主导` |
| [copr_design](projects/opensourceways/copr_design/summary.md) | *待补充* | `html` `团队主导` |
| [copr_docker](projects/opensourceways/copr_docker/summary.md) | *待补充* | `docker` `团队主导` |
| [cora](projects/opensourceways/cora/summary.md) | - **跨平台数据查询**：`cora gitcode issues list --owner my-org --state open` 一行命令查 GitCode Issue | `cli` `community` `go` `团队主导` |
| [cve-manager](projects/opensourceways/cve-manager/summary.md) | - Go · Git · Docker · CI/CD | `go` `security` `团队主导` |
| [cve-manager-ng](projects/opensourceways/cve-manager-ng/summary.md) | - Go · Git · Docker · CI/CD | `go` `security` `团队主导` |
| [cve-sa-backend](projects/opensourceways/cve-sa-backend/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `security` `团队主导` |
| [dataarts_tasks](projects/opensourceways/dataarts_tasks/summary.md) | *待补充* | `data` `团队主导` |
| [DataMagic](projects/opensourceways/DataMagic/summary.md) | - Java · Git · Docker · CI/CD | `data` `java` `团队主导` |
| [datastat-manage-website](projects/opensourceways/datastat-manage-website/summary.md) | *待补充* | `data` `frontend` `vue` `团队主导` |
| [datastat-server](projects/opensourceways/datastat-server/summary.md) | - Java · Git · Docker · CI/CD | `backend` `data` `java` `团队主导` |
| [defect-manager](projects/opensourceways/defect-manager/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [deploy](projects/opensourceways/deploy/summary.md) | - Go Template | `deploy` `团队主导` |
| [design-workflow](projects/opensourceways/design-workflow/summary.md) | *待补充* | `workflow` `团队主导` |
| [discourse-analytics](projects/opensourceways/discourse-analytics/summary.md) | - JavaScript | `data` `javascript` `团队主导` |
| [discourse-audit-cronjob](projects/opensourceways/discourse-audit-cronjob/summary.md) | - Python · Git · Docker · CI/CD | `observability` `python` `团队主导` |
| [discourse-easecheck](projects/opensourceways/discourse-easecheck/summary.md) | *待补充* | `ruby` `团队主导` |
| [discourse_config](projects/opensourceways/discourse_config/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [discourse_theme](projects/opensourceways/discourse_theme/summary.md) | - JavaScript | `javascript` `团队主导` |
| [doc-search-input](projects/opensourceways/doc-search-input/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `ascend` `auth` `python` `团队主导` |
| [docs](projects/opensourceways/docs/summary.md) | - JavaScript | `frontend` `javascript` `repo-management` `团队主导` |
| [docs-archived](projects/opensourceways/docs-archived/summary.md) | *待补充* | `团队主导` |
| [easy-editor-website](projects/opensourceways/easy-editor-website/summary.md) | *待补充* | `frontend` `vue` `团队主导` |
| [easyeditor-server](projects/opensourceways/easyeditor-server/summary.md) | - Java · Git · Docker · CI/CD | `backend` `java` `团队主导` |
| [easymodel-plugins](projects/opensourceways/easymodel-plugins/summary.md) | - Python · Git · Docker · CI/CD | `llm` `python` `团队主导` |
| [easypackages](projects/opensourceways/easypackages/summary.md) | *待补充* | `shell` `团队主导` |
| [EasySearch](projects/opensourceways/EasySearch/summary.md) | - Java · Git · Docker · CI/CD | `elasticsearch` `java` `团队主导` |
| [EasySearch-RAGSearch](projects/opensourceways/EasySearch-RAGSearch/summary.md) | - Python · Git · Docker · CI/CD | `elasticsearch` `python` `团队主导` |
| [EasySearch-RAGSearch-frontend](projects/opensourceways/EasySearch-RAGSearch-frontend/summary.md) | - JavaScript | `elasticsearch` `frontend` `javascript` `团队主导` |
| [EasySearchImport](projects/opensourceways/EasySearchImport/summary.md) | - Java · Git · Docker · CI/CD | `elasticsearch` `java` `团队主导` |
| [EasySoftware-autorepair](projects/opensourceways/EasySoftware-autorepair/summary.md) | - Markdown (文档) | `ai-agent` `团队主导` |
| [easysoftware-autoupgrade](projects/opensourceways/easysoftware-autoupgrade/summary.md) | - Java · Git · Docker · CI/CD | `java` `团队主导` |
| [easysoftware-pr-autohandle](projects/opensourceways/easysoftware-pr-autohandle/summary.md) | - Java · Git · Docker · CI/CD | `java` `团队主导` |
| [EasySoftwareInput](projects/opensourceways/EasySoftwareInput/summary.md) | - Java · Git · Docker · CI/CD | `ascend` `java` `团队主导` |
| [EasySoftwareService](projects/opensourceways/EasySoftwareService/summary.md) | - Java · Git · Docker · CI/CD | `java` `团队主导` |
| [easywhisperx](projects/opensourceways/easywhisperx/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [easywhisperx-website](projects/opensourceways/easywhisperx-website/summary.md) | *待补充* | `css` `frontend` `团队主导` |
| [etherpad-lite](projects/opensourceways/etherpad-lite/summary.md) | - TypeScript | `typescript` `团队主导` |
| [eur-build-all](projects/opensourceways/eur-build-all/summary.md) | - Markdown (文档) | `frontend` `团队主导` |
| [flexcompute-sdk](projects/opensourceways/flexcompute-sdk/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `团队主导` |
| [flexcompute-server](projects/opensourceways/flexcompute-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `团队主导` |
| [forum-reply-robot](projects/opensourceways/forum-reply-robot/summary.md) | - Python · Git · Docker · CI/CD | `bot` `community` `python` `团队主导` |
| [foundation-model-server](projects/opensourceways/foundation-model-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `llm` `团队主导` |
| [geo-develop-workflow](projects/opensourceways/geo-develop-workflow/summary.md) | - JavaScript | `javascript` `workflow` `团队主导` |
| [geo-question-sets](projects/opensourceways/geo-question-sets/summary.md) | *待补充* | `团队主导` |
| [geo-workflow](projects/opensourceways/geo-workflow/summary.md) | - Python · Git · Docker · CI/CD | `python` `workflow` `团队主导` |
| [git-access-sdk](projects/opensourceways/git-access-sdk/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `团队主导` |
| [gitcode-ascend-trans](projects/opensourceways/gitcode-ascend-trans/summary.md) | - Python · Git · Docker · CI/CD | `ascend` `git-platform` `python` `团队主导` |
| [gitcode-migrate-script](projects/opensourceways/gitcode-migrate-script/summary.md) | - Python · Git · Docker · CI/CD | `git-platform` `python` `团队主导` |
| [go-atomgit](projects/opensourceways/go-atomgit/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [go-ddd-framework](projects/opensourceways/go-ddd-framework/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `团队主导` |
| [go-gitcode](projects/opensourceways/go-gitcode/summary.md) | - Go · Git · Docker · CI/CD | `backend` `git-platform` `go` `sdk` `团队主导` |
| [go-gitee](projects/opensourceways/go-gitee/summary.md) | - Go · Git · Docker · CI/CD | `git-platform` `go` `sdk` `团队主导` |
| [go-github-adapter](projects/opensourceways/go-github-adapter/summary.md) | - Go · Git · Docker · CI/CD | `git-platform` `go` `团队主导` |
| [golang-ddd-framework](projects/opensourceways/golang-ddd-framework/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `团队主导` |
| [happy-new-year](projects/opensourceways/happy-new-year/summary.md) | *待补充* | `vue` `团队主导` |
| [hdc-task-manager](projects/opensourceways/hdc-task-manager/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [helm-chart-value](projects/opensourceways/helm-chart-value/summary.md) | - YAML (K8S/Helm) | `deploy` `kubernetes` `团队主导` |
| [helm-charts](projects/opensourceways/helm-charts/summary.md) | - Go Template | `deploy` `kubernetes` `团队主导` |
| [hifloat-website](projects/opensourceways/hifloat-website/summary.md) | *待补充* | `frontend` `团队主导` |
| [hot-topic-website-backend](projects/opensourceways/hot-topic-website-backend/summary.md) | - Go · Git · Docker · CI/CD | `backend` `frontend` `go` `团队主导` |
| [hotopic-all](projects/opensourceways/hotopic-all/summary.md) | *待补充* | `shell` `团队主导` |
| [hotopic-data-clean](projects/opensourceways/hotopic-data-clean/summary.md) | - Python · Git · Docker · CI/CD | `community` `data` `python` `团队主导` |
| [hotopic-mining](projects/opensourceways/hotopic-mining/summary.md) | - Python · Git · Docker · CI/CD | `community` `python` `团队主导` |
| [hwid-website](projects/opensourceways/hwid-website/summary.md) | *待补充* | `css` `frontend` `团队主导` |
| [image-scanning](projects/opensourceways/image-scanning/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [inference-perf-dashboard](projects/opensourceways/inference-perf-dashboard/summary.md) | - Python · Git · Docker · CI/CD | `frontend` `python` `团队主导` |
| [inference-platform](projects/opensourceways/inference-platform/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [infra-audit-service](projects/opensourceways/infra-audit-service/summary.md) | - Go · Git · Docker · CI/CD | `go` `observability` `团队主导` |
| [infra-common](projects/opensourceways/infra-common/summary.md) | - Python · Git · Docker · CI/CD | `python` `repo-management` `团队主导` |
| [infra-community](projects/opensourceways/infra-community/summary.md) | - Python · Git · Docker · CI/CD | `community` `python` `repo-management` `团队主导` |
| [infra-landscape](projects/opensourceways/infra-landscape/summary.md) | *待补充* | `docker` `团队主导` |
| [infra-mindspore](projects/opensourceways/infra-mindspore/summary.md) | *待补充* | `community` `mindspore` `repo-management` `shell` `团队主导` |
| [infra-openeuler](projects/opensourceways/infra-openeuler/summary.md) | - YAML (K8S/Helm) | `community` `openeuler` `repo-management` `团队主导` |
| [infra-openfuyao](projects/opensourceways/infra-openfuyao/summary.md) | - YAML (K8S/Helm) | `community` `团队主导` |
| [infra-opengauss](projects/opensourceways/infra-opengauss/summary.md) | *待补充* | `community` `opengauss` `repo-management` `团队主导` |
| [infra-openlookeng](projects/opensourceways/infra-openlookeng/summary.md) | - YAML (K8S/Helm) | `community` `团队主导` |
| [infra-openmind](projects/opensourceways/infra-openmind/summary.md) | - YAML (K8S/Helm) | `团队主导` |
| [infra-openubmc](projects/opensourceways/infra-openubmc/summary.md) | - YAML (K8S/Helm) | `openubmc` `团队主导` |
| [infra-pytorch](projects/opensourceways/infra-pytorch/summary.md) | - YAML (K8S/Helm) | `pytorch` `团队主导` |
| [infra-radar](projects/opensourceways/infra-radar/summary.md) | - Go · Git · Docker · CI/CD | `ci-cd` `go` `observability` `团队主导` |
| [infraAIService](projects/opensourceways/infraAIService/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `python` `团队主导` |
| [infrastructure](projects/opensourceways/infrastructure/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [insights](projects/opensourceways/insights/summary.md) | *待补充* | `data` `团队主导` |
| [integration-tests](projects/opensourceways/integration-tests/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `python` `repo-management` `团队主导` |
| [ip-geo-fastapi](projects/opensourceways/ip-geo-fastapi/summary.md) | - Python · Git · Docker · CI/CD | `backend` `ci-cd` `python` `团队主导` |
| [issue-cli](projects/opensourceways/issue-cli/summary.md) | *待补充* | `cli` `团队主导` |
| [issue_pr_board](projects/opensourceways/issue_pr_board/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [issue_state_monitor](projects/opensourceways/issue_state_monitor/summary.md) | - Go · Git · Docker · CI/CD | `data` `go` `observability` `团队主导` |
| [istio-demo](projects/opensourceways/istio-demo/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [jenkins-log-scanner](projects/opensourceways/jenkins-log-scanner/summary.md) | - Go · Git · Docker · CI/CD | `ci-cd` `cli` `community` `frontend` `go` `团队主导` |
| [kafka-lib](projects/opensourceways/kafka-lib/summary.md) | - Go · Git · Docker · CI/CD | `go` `messaging` `sdk` `团队主导` |
| [keycloak-social-gitee](projects/opensourceways/keycloak-social-gitee/summary.md) | *待补充* | `auth` `ci-cd` `git-platform` `html` `团队主导` |
| [lfs-website](projects/opensourceways/lfs-website/summary.md) | *待补充* | `css` `frontend` `团队主导` |
| [lingqu-website](projects/opensourceways/lingqu-website/summary.md) | *待补充* | `css` `frontend` `团队主导` |
| [llm-wiki](projects/opensourceways/llm-wiki/summary.md) | *待补充* | `llm` `团队主导` |
| [lxc-launcher](projects/opensourceways/lxc-launcher/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [maillist-templates](projects/opensourceways/maillist-templates/summary.md) | *待补充* | `ai-agent` `email` `repo-management` `团队主导` |
| [mailman](projects/opensourceways/mailman/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `docker` `email` `frontend` `python` `团队主导` |
| [MCP-gateway](projects/opensourceways/MCP-gateway/summary.md) | - TypeScript | `backend` `mcp` `typescript` `团队主导` |
| [meeting-cann-website](projects/opensourceways/meeting-cann-website/summary.md) | - TypeScript | `community` `frontend` `typescript` `团队主导` |
| [meeting-center](projects/opensourceways/meeting-center/summary.md) | - Python · Git · Docker · CI/CD | `ci-cd` `community` `frontend` `python` `团队主导` |
| [meeting-mcp](projects/opensourceways/meeting-mcp/summary.md) | *待补充* | `community` `mcp` `团队主导` |
| [meeting-platform](projects/opensourceways/meeting-platform/summary.md) | - Python · Git · Docker · CI/CD | `community` `python` `团队主导` |
| [meeting-server](projects/opensourceways/meeting-server/summary.md) | *待补充* | `backend` `community` `shell` `团队主导` |
| [meeting-website](projects/opensourceways/meeting-website/summary.md) | *待补充* | `community` `frontend` `vue` `团队主导` |
| [message-bus-all](projects/opensourceways/message-bus-all/summary.md) | - Markdown (文档) | `messaging` `团队主导` |
| [message-collect](projects/opensourceways/message-collect/summary.md) | - Go · Git · Docker · CI/CD | `go` `messaging` `团队主导` |
| [message-collect-cron](projects/opensourceways/message-collect-cron/summary.md) | - Go · Git · Docker · CI/CD | `go` `messaging` `团队主导` |
| [message-collect-githook](projects/opensourceways/message-collect-githook/summary.md) | - Go · Git · Docker · CI/CD | `go` `messaging` `团队主导` |
| [message-manager](projects/opensourceways/message-manager/summary.md) | - **多源消息聚合**：论坛回帖、会议通知、CVE 警报、Issue 更新 → 统一收件箱 | `go` `messaging` `团队主导` |
| [message-manager-website](projects/opensourceways/message-manager-website/summary.md) | *待补充* | `frontend` `html` `messaging` `团队主导` |
| [message-push](projects/opensourceways/message-push/summary.md) | - Go · Git · Docker · CI/CD | `go` `messaging` `团队主导` |
| [message-transfer](projects/opensourceways/message-transfer/summary.md) | - Go · Git · Docker · CI/CD | `go` `messaging` `团队主导` |
| [mindspore-jenkins-repo](projects/opensourceways/mindspore-jenkins-repo/summary.md) | *待补充* | `ci-cd` `community` `html` `mindspore` `repo-management` `团队主导` |
| [mongodb-lib](projects/opensourceways/mongodb-lib/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `团队主导` |
| [om-check](projects/opensourceways/om-check/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [om-collection](projects/opensourceways/om-collection/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [om-dataarts](projects/opensourceways/om-dataarts/summary.md) | - **多平台数据采集**：GitHub/Gitee/GitCode 的 PR/Issue/Commit/Star/Fork 全覆盖，含速率限制和 Token 轮换 | `data` `python` `团队主导` |
| [om-dataarts-back](projects/opensourceways/om-dataarts-back/summary.md) | - Python · Git · Docker · CI/CD | `data` `python` `团队主导` |
| [om-dataarts-deployment](projects/opensourceways/om-dataarts-deployment/summary.md) | - Python · Git · Docker · CI/CD | `data` `deploy` `python` `团队主导` |
| [om-datacenter](projects/opensourceways/om-datacenter/summary.md) | *待补充* | `data` `shell` `团队主导` |
| [om-deployment](projects/opensourceways/om-deployment/summary.md) | - YAML (K8S/Helm) | `deploy` `团队主导` |
| [om-kafka](projects/opensourceways/om-kafka/summary.md) | - Java · Git · Docker · CI/CD | `java` `messaging` `团队主导` |
| [om-magicai](projects/opensourceways/om-magicai/summary.md) | - Java · Git · Docker · CI/CD | `ai-agent` `java` `团队主导` |
| [om-search](projects/opensourceways/om-search/summary.md) | - Markdown (文档) | `团队主导` |
| [om-webserver](projects/opensourceways/om-webserver/summary.md) | - Java · Git · Docker · CI/CD | `backend` `frontend` `java` `团队主导` |
| [oneid-all](projects/opensourceways/oneid-all/summary.md) | *待补充* | `ai-agent` `auth` `repo-management` `shell` `团队主导` |
| [oneid-server](projects/opensourceways/oneid-server/summary.md) | - Java · Git · Docker · CI/CD | `auth` `backend` `java` `团队主导` |
| [oneid-website](projects/opensourceways/oneid-website/summary.md) | *待补充* | `auth` `frontend` `vue` `团队主导` |
| [oneid-workbench](projects/opensourceways/oneid-workbench/summary.md) | - Java · Git · Docker · CI/CD | `auth` `java` `团队主导` |
| [oneid-workbench-website](projects/opensourceways/oneid-workbench-website/summary.md) | *待补充* | `auth` `frontend` `vue` `团队主导` |
| [openApiTest](projects/opensourceways/openApiTest/summary.md) | - Python · Git · Docker · CI/CD | `backend` `python` `团队主导` |
| [OpenDesignPlus](projects/opensourceways/OpenDesignPlus/summary.md) | *待补充* | `团队主导` |
| [openeuler-images](projects/opensourceways/openeuler-images/summary.md) | *待补充* | `openeuler` `团队主导` |
| [openeuler-jenkins-repo](projects/opensourceways/openeuler-jenkins-repo/summary.md) | *待补充* | `ci-cd` `community` `openeuler` `repo-management` `团队主导` |
| [openeuler-sig-info-check](projects/opensourceways/openeuler-sig-info-check/summary.md) | - Go · Git · Docker · CI/CD | `openeuler` `团队主导` |
| [openeuler-website-v2](projects/opensourceways/openeuler-website-v2/summary.md) | - JavaScript | `frontend` `javascript` `openeuler` `团队主导` |
| [opengauss-jenkins-repo](projects/opensourceways/opengauss-jenkins-repo/summary.md) | *待补充* | `ci-cd` `community` `html` `opengauss` `repo-management` `团队主导` |
| [opengauss_infra](projects/opensourceways/opengauss_infra/summary.md) | *待补充* | `html` `opengauss` `团队主导` |
| [opengecko](projects/opensourceways/opengecko/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `python` `团队主导` |
| [openlookeng-jenkins-repo](projects/opensourceways/openlookeng-jenkins-repo/summary.md) | *待补充* | `ci-cd` `community` `html` `repo-management` `团队主导` |
| [opensource-radar-web](projects/opensourceways/opensource-radar-web/summary.md) | - JavaScript | `frontend` `javascript` `observability` `团队主导` |
| [opensource101](projects/opensourceways/opensource101/summary.md) | *待补充* | `团队主导` |
| [opensourceway](projects/opensourceways/opensourceway/summary.md) | *待补充* | `html` `团队主导` |
| [opensourceways-repo-monitor](projects/opensourceways/opensourceways-repo-monitor/summary.md) | - Python · Git · Docker · CI/CD | `observability` `python` `repo-management` `团队主导` |
| [openUBMC-portal](projects/opensourceways/openUBMC-portal/summary.md) | *待补充* | `css` `openubmc` `团队主导` |
| [ops-mgmt](projects/opensourceways/ops-mgmt/summary.md) | - Markdown (文档) | `security` `团队主导` |
| [osi-task-manager](projects/opensourceways/osi-task-manager/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [osinfra-jenkins-repo](projects/opensourceways/osinfra-jenkins-repo/summary.md) | *待补充* | `ci-cd` `html` `repo-management` `团队主导` |
| [patch-manager](projects/opensourceways/patch-manager/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [patch-manager-website](projects/opensourceways/patch-manager-website/summary.md) | - Markdown (文档) | `frontend` `团队主导` |
| [patchwork](projects/opensourceways/patchwork/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [permission-manage-website](projects/opensourceways/permission-manage-website/summary.md) | - Markdown (文档) | `frontend` `团队主导` |
| [playground-app](projects/opensourceways/playground-app/summary.md) | *待补充* | `vue` `团队主导` |
| [playground-courses](projects/opensourceways/playground-courses/summary.md) | - Markdown (文档) | `团队主导` |
| [playground-images](projects/opensourceways/playground-images/summary.md) | - PLpgSQL | `团队主导` |
| [playground-manager](projects/opensourceways/playground-manager/summary.md) | - Go · Git · Docker · CI/CD | `go` `团队主导` |
| [pod_exporter_monitoring](projects/opensourceways/pod_exporter_monitoring/summary.md) | - Python · Git · Docker · CI/CD | `observability` `python` `团队主导` |
| [portal-mcp-servers](projects/opensourceways/portal-mcp-servers/summary.md) | - JavaScript | `backend` `javascript` `mcp` `团队主导` |
| [portal-workflow](projects/opensourceways/portal-workflow/summary.md) | - JavaScript | `javascript` `workflow` `团队主导` |
| [postgresql-lib](projects/opensourceways/postgresql-lib/summary.md) | *待补充* | `sdk` `团队主导` |
| [pr-issue-report](projects/opensourceways/pr-issue-report/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `community` `python` `repo-management` `团队主导` |
| [public_issue](projects/opensourceways/public_issue/summary.md) | *待补充* | `团队主导` |
| [python-gitee](projects/opensourceways/python-gitee/summary.md) | - Python · Git · Docker · CI/CD | `git-platform` `python` `团队主导` |
| [QA](projects/opensourceways/QA/summary.md) | *待补充* | `团队主导` |
| [rag-ci-deploy](projects/opensourceways/rag-ci-deploy/summary.md) | - Python · Git · Docker · CI/CD | `ci-cd` `deploy` `python` `团队主导` |
| [redis-lib](projects/opensourceways/redis-lib/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `团队主导` |
| [release-mgmt](projects/opensourceways/release-mgmt/summary.md) | - Python · Git · Docker · CI/CD | `deploy` `python` `团队主导` |
| [repo-file-cache](projects/opensourceways/repo-file-cache/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `团队主导` |
| [repo-owners-cache](projects/opensourceways/repo-owners-cache/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `团队主导` |
| [reproducible-backend](projects/opensourceways/reproducible-backend/summary.md) | - Java · Git · Docker · CI/CD | `backend` `ci-cd` `java` `团队主导` |
| [reproducible-builds-libfaketime](projects/opensourceways/reproducible-builds-libfaketime/summary.md) | *待补充* | `ci-cd` `frontend` `sdk` `团队主导` |
| [reproducible-website](projects/opensourceways/reproducible-website/summary.md) | - Markdown (文档) | `ci-cd` `frontend` `团队主导` |
| [RM-Check](projects/opensourceways/RM-Check/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [robot-framework-lib](projects/opensourceways/robot-framework-lib/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `sdk` `团队主导` |
| [robot-gitcode-hook-delivery](projects/opensourceways/robot-gitcode-hook-delivery/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitcode-software-package](projects/opensourceways/robot-gitcode-software-package/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `git-platform` `go` `团队主导` |
| [robot-gitee-access](projects/opensourceways/robot-gitee-access/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-approve](projects/opensourceways/robot-gitee-approve/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-assign](projects/opensourceways/robot-gitee-assign/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-assign-issue](projects/opensourceways/robot-gitee-assign-issue/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-associate](projects/opensourceways/robot-gitee-associate/summary.md) | - Go · Git · Docker · CI/CD | `bot` `ci-cd` `git-platform` `go` `团队主导` |
| [robot-gitee-checkpr](projects/opensourceways/robot-gitee-checkpr/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-cla](projects/opensourceways/robot-gitee-cla/summary.md) | - Go · Git · Docker · CI/CD | `auth` `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-cve-issue-suspending-check](projects/opensourceways/robot-gitee-cve-issue-suspending-check/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `security` `团队主导` |
| [robot-gitee-hook-delivery](projects/opensourceways/robot-gitee-hook-delivery/summary.md) | - Go · Git · Docker · CI/CD | `bot` `frontend` `git-platform` `go` `messaging` `团队主导` |
| [robot-gitee-hook-dispatcher](projects/opensourceways/robot-gitee-hook-dispatcher/summary.md) | - Go · Git · Docker · CI/CD | `bot` `frontend` `git-platform` `go` `messaging` `团队主导` |
| [robot-gitee-keeper-approve](projects/opensourceways/robot-gitee-keeper-approve/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-label](projects/opensourceways/robot-gitee-label/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-lgtm](projects/opensourceways/robot-gitee-lgtm/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-lib](projects/opensourceways/robot-gitee-lib/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `sdk` `团队主导` |
| [robot-gitee-lifecycle](projects/opensourceways/robot-gitee-lifecycle/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-openeuler-responsible-guide](projects/opensourceways/robot-gitee-openeuler-responsible-guide/summary.md) | *待补充* | `bot` `frontend` `git-platform` `openeuler` `团队主导` |
| [robot-gitee-openeuler-review](projects/opensourceways/robot-gitee-openeuler-review/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-gitee-openeuler-upstream-monitor](projects/opensourceways/robot-gitee-openeuler-upstream-monitor/summary.md) | - Java · Git · Docker · CI/CD | `bot` `git-platform` `java` `observability` `openeuler` `团队主导` |
| [robot-gitee-openeuler-welcome](projects/opensourceways/robot-gitee-openeuler-welcome/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-gitee-opengauss-review](projects/opensourceways/robot-gitee-opengauss-review/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `opengauss` `团队主导` |
| [robot-gitee-opengauss-sigguide](projects/opensourceways/robot-gitee-opengauss-sigguide/summary.md) | - Starlark | `bot` `frontend` `git-platform` `opengauss` `团队主导` |
| [robot-gitee-owners-monitor](projects/opensourceways/robot-gitee-owners-monitor/summary.md) | - Starlark | `bot` `git-platform` `observability` `团队主导` |
| [robot-gitee-python-lib](projects/opensourceways/robot-gitee-python-lib/summary.md) | - Python · Git · Docker · CI/CD | `bot` `git-platform` `python` `sdk` `团队主导` |
| [robot-gitee-repo-watcher](projects/opensourceways/robot-gitee-repo-watcher/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `repo-management` `团队主导` |
| [robot-gitee-review-trigger](projects/opensourceways/robot-gitee-review-trigger/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-scavenger](projects/opensourceways/robot-gitee-scavenger/summary.md) | - Go · Git · Docker · CI/CD | `bot` `data` `git-platform` `go` `团队主导` |
| [robot-gitee-size](projects/opensourceways/robot-gitee-size/summary.md) | *待补充* | `bot` `git-platform` `团队主导` |
| [robot-gitee-software-package](projects/opensourceways/robot-gitee-software-package/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-sweepstakes](projects/opensourceways/robot-gitee-sweepstakes/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-synchronizer](projects/opensourceways/robot-gitee-synchronizer/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `observability` `repo-management` `团队主导` |
| [robot-gitee-tech4dx-label](projects/opensourceways/robot-gitee-tech4dx-label/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-tide](projects/opensourceways/robot-gitee-tide/summary.md) | - Starlark | `bot` `git-platform` `团队主导` |
| [robot-gitee-version-freezer](projects/opensourceways/robot-gitee-version-freezer/summary.md) | *待补充* | `bot` `git-platform` `团队主导` |
| [robot-gitee-welcome](projects/opensourceways/robot-gitee-welcome/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-github-access](projects/opensourceways/robot-github-access/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `团队主导` |
| [robot-github-cla](projects/opensourceways/robot-github-cla/summary.md) | - Go · Git · Docker · CI/CD | `auth` `bot` `git-platform` `go` `团队主导` |
| [robot-github-hook-delivery](projects/opensourceways/robot-github-hook-delivery/summary.md) | - Go · Git · Docker · CI/CD | `bot` `frontend` `git-platform` `go` `messaging` `团队主导` |
| [robot-github-hook-dispatcher](projects/opensourceways/robot-github-hook-dispatcher/summary.md) | - Go · Git · Docker · CI/CD | `bot` `ci-cd` `frontend` `git-platform` `go` `messaging` `团队主导` |
| [robot-github-lib](projects/opensourceways/robot-github-lib/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `sdk` `团队主导` |
| [robot-github-openeuler-assign](projects/opensourceways/robot-github-openeuler-assign/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-github-openeuler-label](projects/opensourceways/robot-github-openeuler-label/summary.md) | - Starlark | `bot` `git-platform` `openeuler` `团队主导` |
| [robot-github-openeuler-lifecycle](projects/opensourceways/robot-github-openeuler-lifecycle/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-github-openeuler-repo-watcher](projects/opensourceways/robot-github-openeuler-repo-watcher/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `openeuler` `repo-management` `团队主导` |
| [robot-github-openeuler-review](projects/opensourceways/robot-github-openeuler-review/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-github-openeuler-welcome](projects/opensourceways/robot-github-openeuler-welcome/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-github-synchronizer](projects/opensourceways/robot-github-synchronizer/summary.md) | - Go · Git · Docker · CI/CD | `bot` `git-platform` `go` `observability` `repo-management` `团队主导` |
| [robot-gitlab-access](projects/opensourceways/robot-gitlab-access/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `团队主导` |
| [robot-gitlab-label](projects/opensourceways/robot-gitlab-label/summary.md) | - Starlark | `bot` `团队主导` |
| [robot-gitlab-lib](projects/opensourceways/robot-gitlab-lib/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `sdk` `团队主导` |
| [robot-gitlab-repo-watcher](projects/opensourceways/robot-gitlab-repo-watcher/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `repo-management` `团队主导` |
| [robot-gitlab-review](projects/opensourceways/robot-gitlab-review/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `团队主导` |
| [robot-gitlab-sync-repo](projects/opensourceways/robot-gitlab-sync-repo/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `repo-management` `团队主导` |
| [robot-gitlab-welcome](projects/opensourceways/robot-gitlab-welcome/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `团队主导` |
| [robot-hook-dispatcher](projects/opensourceways/robot-hook-dispatcher/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `团队主导` |
| [robot-issue-manage](projects/opensourceways/robot-issue-manage/summary.md) | - Python · Git · Docker · CI/CD | `bot` `community` `git-platform` `python` `workflow` `团队主导` |
| [robot-openeuler-ci-tools](projects/opensourceways/robot-openeuler-ci-tools/summary.md) | - Python · Git · Docker · CI/CD | `bot` `ci-cd` `cli` `openeuler` `python` `团队主导` |
| [robot-plugin-syncfile](projects/opensourceways/robot-plugin-syncfile/summary.md) | *待补充* | `bot` `repo-management` `团队主导` |
| [robot-tools](projects/opensourceways/robot-tools/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `bot` `cli` `data` `deploy` `git-platform` `python` `workflow` `团队主导` |
| [robot-universal-access](projects/opensourceways/robot-universal-access/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `团队主导` |
| [robot-universal-agreements](projects/opensourceways/robot-universal-agreements/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `团队主导` |
| [robot-universal-assign](projects/opensourceways/robot-universal-assign/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `团队主导` |
| [robot-universal-associate](projects/opensourceways/robot-universal-associate/summary.md) | - Go · Git · Docker · CI/CD | `bot` `ci-cd` `community` `go` `团队主导` |
| [robot-universal-cache](projects/opensourceways/robot-universal-cache/summary.md) | *待补充* | `bot` `community` `团队主导` |
| [robot-universal-ci-tools](projects/opensourceways/robot-universal-ci-tools/summary.md) | - Python · Git · Docker · CI/CD | `bot` `ci-cd` `cli` `python` `团队主导` |
| [robot-universal-cla](projects/opensourceways/robot-universal-cla/summary.md) | - Go · Git · Docker · CI/CD | `auth` `bot` `community` `go` `团队主导` |
| [robot-universal-comment](projects/opensourceways/robot-universal-comment/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `团队主导` |
| [robot-universal-hook-delivery](projects/opensourceways/robot-universal-hook-delivery/summary.md) | - Go · Git · Docker · CI/CD | `bot` `frontend` `go` `messaging` `团队主导` |
| [robot-universal-issue-workflow](projects/opensourceways/robot-universal-issue-workflow/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `workflow` `团队主导` |
| [robot-universal-label](projects/opensourceways/robot-universal-label/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `团队主导` |
| [robot-universal-lifecycle](projects/opensourceways/robot-universal-lifecycle/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `团队主导` |
| [robot-universal-quality-gate-trigger](projects/opensourceways/robot-universal-quality-gate-trigger/summary.md) | - Go · Git · Docker · CI/CD | `bot` `ci-cd` `cli` `community` `go` `repo-management` `团队主导` |
| [robot-universal-repo-watcher](projects/opensourceways/robot-universal-repo-watcher/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `repo-management` `团队主导` |
| [robot-universal-review](projects/opensourceways/robot-universal-review/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `团队主导` |
| [robot-universal-scavenger](projects/opensourceways/robot-universal-scavenger/summary.md) | - Go · Git · Docker · CI/CD | `bot` `go` `observability` `团队主导` |
| [robot-universal-welcome](projects/opensourceways/robot-universal-welcome/summary.md) | - Go · Git · Docker · CI/CD | `bot` `community` `go` `团队主导` |
| [sbom-deploy](projects/opensourceways/sbom-deploy/summary.md) | *待补充* | `deploy` `docker` `团队主导` |
| [sbom-repo-service](projects/opensourceways/sbom-repo-service/summary.md) | - Java · Git · Docker · CI/CD | `java` `repo-management` `团队主导` |
| [sbom-service](projects/opensourceways/sbom-service/summary.md) | - Java · Git · Docker · CI/CD | `java` `团队主导` |
| [sbom-tools](projects/opensourceways/sbom-tools/summary.md) | *待补充* | `cli` `团队主导` |
| [sbom-website](projects/opensourceways/sbom-website/summary.md) | *待补充* | `frontend` `vue` `团队主导` |
| [search-all](projects/opensourceways/search-all/summary.md) | - Markdown (文档) | `团队主导` |
| [security-cve-all](projects/opensourceways/security-cve-all/summary.md) | *待补充* | `security` `shell` `团队主导` |
| [server-common-lib](projects/opensourceways/server-common-lib/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `sdk` `团队主导` |
| [sig-miniprogram](projects/opensourceways/sig-miniprogram/summary.md) | - JavaScript | `javascript` `团队主导` |
| [smart_tools](projects/opensourceways/smart_tools/summary.md) | - Python · Git · Docker · CI/CD | `cli` `python` `团队主导` |
| [software-package-all](projects/opensourceways/software-package-all/summary.md) | - Markdown (文档) | `团队主导` |
| [software-package-gateway](projects/opensourceways/software-package-gateway/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `团队主导` |
| [software-package-github-server](projects/opensourceways/software-package-github-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `git-platform` `go` `团队主导` |
| [software-package-server](projects/opensourceways/software-package-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `团队主导` |
| [software-package-sync-pr](projects/opensourceways/software-package-sync-pr/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `团队主导` |
| [software-package-sync-repo](projects/opensourceways/software-package-sync-repo/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `团队主导` |
| [software-package-website](projects/opensourceways/software-package-website/summary.md) | *待补充* | `frontend` `vue` `团队主导` |
| [space-k8s-operator](projects/opensourceways/space-k8s-operator/summary.md) | - Go · Git · Docker · CI/CD | `go` `kubernetes` `团队主导` |
| [space-server](projects/opensourceways/space-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `团队主导` |
| [space-server-monitor](projects/opensourceways/space-server-monitor/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `observability` `团队主导` |
| [study](projects/opensourceways/study/summary.md) | *待补充* | `团队主导` |
| [sync-agent](projects/opensourceways/sync-agent/summary.md) | - Go · Git · Docker · CI/CD | `ai-agent` `backend` `git-platform` `go` `repo-management` `团队主导` |
| [sync-bot](projects/opensourceways/sync-bot/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `团队主导` |
| [sync-file-server](projects/opensourceways/sync-file-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `repo-management` `团队主导` |
| [sync-mirror-repos](projects/opensourceways/sync-mirror-repos/summary.md) | - Python · Git · Docker · CI/CD | `git-platform` `python` `repo-management` `团队主导` |
| [sync-model-openpangu](projects/opensourceways/sync-model-openpangu/summary.md) | - Python · Git · Docker · CI/CD | `llm` `python` `repo-management` `团队主导` |
| [sync-repo-file](projects/opensourceways/sync-repo-file/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `团队主导` |
| [sync-repo-file-job](projects/opensourceways/sync-repo-file-job/summary.md) | - Markdown (文档) | `repo-management` `团队主导` |
| [sync-repository-file](projects/opensourceways/sync-repository-file/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `团队主导` |
| [test](projects/opensourceways/test/summary.md) | - Markdown (文档) | `团队主导` |
| [test-infra](projects/opensourceways/test-infra/summary.md) | - Go · Git · Docker · CI/CD | `go` `kubernetes` `团队主导` |
| [test-pub](projects/opensourceways/test-pub/summary.md) | *待补充* | `团队主导` |
| [test1](projects/opensourceways/test1/summary.md) | *待补充* | `团队主导` |
| [tools-collection](projects/opensourceways/tools-collection/summary.md) | *待补充* | `cli` `shell` `团队主导` |
| [translator](projects/opensourceways/translator/summary.md) | - Python · Git · Docker · CI/CD | `cli` `python` `repo-management` `团队主导` |
| [ttfhw](projects/opensourceways/ttfhw/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [ttfhw-backup](projects/opensourceways/ttfhw-backup/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [uvp](projects/opensourceways/uvp/summary.md) | - Java · Git · Docker · CI/CD | `java` `security` `团队主导` |
| [uvp-website](projects/opensourceways/uvp-website/summary.md) | *待补充* | `frontend` `security` `vue` `团队主导` |
| [vLLM-dashboard-website](projects/opensourceways/vLLM-dashboard-website/summary.md) | *待补充* | `frontend` `llm` `vllm` `vue` `团队主导` |
| [vscode-doc-tools](projects/opensourceways/vscode-doc-tools/summary.md) | - TypeScript | `cli` `typescript` `团队主导` |
| [vscode-portal-cms](projects/opensourceways/vscode-portal-cms/summary.md) | *待补充* | `vue` `团队主导` |
| [whitebox](projects/opensourceways/whitebox/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [workflow-control-tower](projects/opensourceways/workflow-control-tower/summary.md) | *待补充* | `ai-agent` `repo-management` `shell` `workflow` `团队主导` |
| [xihe-aicc-finetune](projects/opensourceways/xihe-aicc-finetune/summary.md) | - Go · Git · Docker · CI/CD | `ai-agent` `go` `xihe` `团队主导` |
| [xihe-all](projects/opensourceways/xihe-all/summary.md) | *待补充* | `shell` `xihe` `团队主导` |
| [xihe-audit-sdk](projects/opensourceways/xihe-audit-sdk/summary.md) | - Markdown (文档) | `observability` `sdk` `xihe` `团队主导` |
| [xihe-audit-server](projects/opensourceways/xihe-audit-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `observability` `xihe` `团队主导` |
| [xihe-audit-sync-sdk](projects/opensourceways/xihe-audit-sync-sdk/summary.md) | - Go · Git · Docker · CI/CD | `go` `observability` `repo-management` `sdk` `xihe` `团队主导` |
| [xihe-cronjob](projects/opensourceways/xihe-cronjob/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-docs](projects/opensourceways/xihe-docs/summary.md) | - TypeScript | `typescript` `xihe` `团队主导` |
| [xihe-extra-services](projects/opensourceways/xihe-extra-services/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-finetune](projects/opensourceways/xihe-finetune/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-git-access](projects/opensourceways/xihe-git-access/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-git-access-sdk](projects/opensourceways/xihe-git-access-sdk/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `xihe` `团队主导` |
| [xihe-git-hook-delivery](projects/opensourceways/xihe-git-hook-delivery/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-gitea](projects/opensourceways/xihe-gitea/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-gitea-sdk](projects/opensourceways/xihe-gitea-sdk/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `xihe` `团队主导` |
| [xihe-gitlab-hook-delivery](projects/opensourceways/xihe-gitlab-hook-delivery/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-grpc-protocol](projects/opensourceways/xihe-grpc-protocol/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-image-build](projects/opensourceways/xihe-image-build/summary.md) | *待补充* | `frontend` `html` `xihe` `团队主导` |
| [xihe-internal-server](projects/opensourceways/xihe-internal-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `xihe` `团队主导` |
| [xihe-jupyter-server](projects/opensourceways/xihe-jupyter-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `xihe` `团队主导` |
| [xihe-message-server](projects/opensourceways/xihe-message-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `messaging` `xihe` `团队主导` |
| [xihe-resource-script](projects/opensourceways/xihe-resource-script/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-script](projects/opensourceways/xihe-script/summary.md) | - Go · Git · Docker · CI/CD | `go` `xihe` `团队主导` |
| [xihe-sdk](projects/opensourceways/xihe-sdk/summary.md) | - Go · Git · Docker · CI/CD | `go` `sdk` `xihe` `团队主导` |
| [xihe-server](projects/opensourceways/xihe-server/summary.md) | - Go · Git · Docker · CI/CD | `backend` `go` `xihe` `团队主导` |
| [xihe-sop](projects/opensourceways/xihe-sop/summary.md) | *待补充* | `xihe` `团队主导` |
| [xihe-statistics](projects/opensourceways/xihe-statistics/summary.md) | - Go · Git · Docker · CI/CD | `data` `go` `xihe` `团队主导` |
| [xihe-sync-repo](projects/opensourceways/xihe-sync-repo/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `xihe` `团队主导` |
| [xihe-training-center](projects/opensourceways/xihe-training-center/summary.md) | - Go · Git · Docker · CI/CD | `ai-agent` `go` `xihe` `团队主导` |
| [xihe-website](projects/opensourceways/xihe-website/summary.md) | *待补充* | `frontend` `vue` `xihe` `团队主导` |
| [xihe-website-v2](projects/opensourceways/xihe-website-v2/summary.md) | *待补充* | `frontend` `vue` `xihe` `团队主导` |
| [yabot](projects/opensourceways/yabot/summary.md) | - Go · Git · Docker · CI/CD | `go` `repo-management` `团队主导` |

## 🔬 COSDT (团队仓库群)

*23 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [ci-infra](projects/cosdt/ci-infra/summary.md) | - Python · Git · Docker · CI/CD | `ci-cd` `python` `团队主导` |
| [cosdt.github.io](projects/cosdt/cosdt.github.io/summary.md) | *待补充* | `git-platform` `html` `团队主导` |
| [dockerfiles](projects/cosdt/dockerfiles/summary.md) | *待补充* | `docker` `团队主导` |
| [DownStream1](projects/cosdt/DownStream1/summary.md) | *待补充* | `团队主导` |
| [DownStream2](projects/cosdt/DownStream2/summary.md) | *待补充* | `团队主导` |
| [elastic-tool](projects/cosdt/elastic-tool/summary.md) | - Python · Git · Docker · CI/CD | `cli` `elasticsearch` `python` `团队主导` |
| [llama.cpp](projects/cosdt/llama.cpp/summary.md) | *待补充* | `llm` `shell` `团队主导` |
| [onnxruntime](projects/cosdt/onnxruntime/summary.md) | *待补充* | `onnx` `shell` `团队主导` |
| [op-plugin](projects/cosdt/op-plugin/summary.md) | - C++ · Git · Docker · CI/CD | `ascend` `cpp` `npu` `pytorch` `团队主导` |
| [openeuler-keynote-2020](projects/cosdt/openeuler-keynote-2020/summary.md) | *待补充* | `openeuler` `repo-management` `shell` `团队主导` |
| [oss-map](projects/cosdt/oss-map/summary.md) | - Python · Git · Docker · CI/CD | `python` `团队主导` |
| [pytorch](projects/cosdt/pytorch/summary.md) | - Jupyter | `jupyter` `pytorch` `团队主导` |
| [pytorch-integration-tests](projects/cosdt/pytorch-integration-tests/summary.md) | - Python · Git · Docker · CI/CD | `python` `pytorch` `团队主导` |
| [PyTorchInsight](projects/cosdt/PyTorchInsight/summary.md) | - Python · Git · Docker · CI/CD | `community` `data` `python` `pytorch` `团队主导` |
| [skills](projects/cosdt/skills/summary.md) | - Python · Git · Docker · CI/CD | `ai-agent` `cli` `python` `团队主导` |
| [test-infra](projects/cosdt/test-infra/summary.md) | - TypeScript | `typescript` `团队主导` |
| [torch_backend](projects/cosdt/torch_backend/summary.md) | - C++ · Git · Docker · CI/CD | `ascend` `backend` `cpp` `npu` `pytorch` `团队主导` |
| [torchcomms-bak](projects/cosdt/torchcomms-bak/summary.md) | - C++ · Git · Docker · CI/CD | `cpp` `pytorch` `团队主导` |
| [triton-ascend](projects/cosdt/triton-ascend/summary.md) | - C++ · Git · Docker · CI/CD | `ascend` `compiler` `cpp` `npu` `triton` `团队主导` |
| [UpStream](projects/cosdt/UpStream/summary.md) | - YAML (K8S/Helm) | `团队主导` |
| [vllm-ascend](projects/cosdt/vllm-ascend/summary.md) | - Python · Git · Docker · CI/CD | `ascend` `ci-cd` `git-platform` `llm` `python` `vllm` `团队主导` |
| [vllm-ascend-integration-ci](projects/cosdt/vllm-ascend-integration-ci/summary.md) | - Python · Git · Docker · CI/CD | `ascend` `ci-cd` `llm` `python` `vllm` `团队主导` |
| [vllm-benchmarks](projects/cosdt/vllm-benchmarks/summary.md) | - Python · Git · Docker · CI/CD | `llm` `python` `vllm` `团队主导` |

## 🚀 vLLM Project (上游)

*39 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [agentic-api](projects/vllm-project/agentic-api/summary.md) | *待补充* | `上游贡献` |
| [aibrix](projects/vllm-project/aibrix/summary.md) | - Go · Git · Docker · CI/CD | `上游贡献` |
| [bart-plugin](projects/vllm-project/bart-plugin/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [ci-infra](projects/vllm-project/ci-infra/summary.md) | *待补充* | `上游贡献` |
| [compressed-tensors](projects/vllm-project/compressed-tensors/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [dllm-plugin](projects/vllm-project/dllm-plugin/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [guidellm](projects/vllm-project/guidellm/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [llm-compressor](projects/vllm-project/llm-compressor/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [llm-multimodal](projects/vllm-project/llm-multimodal/summary.md) | *待补充* | `上游贡献` |
| [media-kit](projects/vllm-project/media-kit/summary.md) | *待补充* | `上游贡献` |
| [perf-dashboard](projects/vllm-project/perf-dashboard/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [perf-eval](projects/vllm-project/perf-eval/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [production-stack](projects/vllm-project/production-stack/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [recipes](projects/vllm-project/recipes/summary.md) | - JavaScript | `上游贡献` |
| [rfcs](projects/vllm-project/rfcs/summary.md) | *待补充* | `上游贡献` |
| [router](projects/vllm-project/router/summary.md) | *待补充* | `上游贡献` |
| [semantic-router](projects/vllm-project/semantic-router/summary.md) | - Go · Git · Docker · CI/CD | `上游贡献` |
| [speculators](projects/vllm-project/speculators/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [tpu-inference](projects/vllm-project/tpu-inference/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vime](projects/vllm-project/vime/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vllm](projects/vllm-project/vllm/summary.md) | - **大模型推理服务部署**：一键启动 OpenAI 兼容的 API Server，支持 200+ 模型架构 | `continuous-batching` `pagedattention` `vllm` `上游贡献` `推理` |
| [vllm-ascend](projects/vllm-project/vllm-ascend/summary.md) | - C++ · Git · Docker · CI/CD | `ascend` `npu` `vllm` `上游贡献` |
| [vllm-bench](projects/vllm-project/vllm-bench/summary.md) | *待补充* | `上游贡献` |
| [vllm-bnb-plugin](projects/vllm-project/vllm-bnb-plugin/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vllm-daily](projects/vllm-project/vllm-daily/summary.md) | *待补充* | `上游贡献` |
| [vllm-dashboard](projects/vllm-project/vllm-dashboard/summary.md) | - TypeScript | `上游贡献` |
| [vllm-docs](projects/vllm-project/vllm-docs/summary.md) | - TypeScript | `上游贡献` |
| [vllm-gaudi](projects/vllm-project/vllm-gaudi/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vllm-gguf-plugin](projects/vllm-project/vllm-gguf-plugin/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vLLM-in-PyTorch-Conference-2025](projects/vllm-project/vLLM-in-PyTorch-Conference-2025/summary.md) | *待补充* | `上游贡献` |
| [vllm-metal](projects/vllm-project/vllm-metal/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vllm-nccl](projects/vllm-project/vllm-nccl/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vllm-neuron](projects/vllm-project/vllm-neuron/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vllm-omni](projects/vllm-project/vllm-omni/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vllm-openvino](projects/vllm-project/vllm-openvino/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [vllm-project.github.io](projects/vllm-project/vllm-project.github.io/summary.md) | *待补充* | `上游贡献` |
| [vllm-project.github.io-static](projects/vllm-project/vllm-project.github.io-static/summary.md) | *待补充* | `上游贡献` |
| [vllm-skills](projects/vllm-project/vllm-skills/summary.md) | *待补充* | `上游贡献` |
| [vllm-xpu-kernels](projects/vllm-project/vllm-xpu-kernels/summary.md) | - C++ · Git · Docker · CI/CD | `上游贡献` |

## ⚡ SGL Project (上游)

*22 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [ci-data](projects/sgl-project/ci-data/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [cuLA](projects/sgl-project/cuLA/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [genai-bench](projects/sgl-project/genai-bench/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [mini-sglang](projects/sgl-project/mini-sglang/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [ome-crd](projects/sgl-project/ome-crd/summary.md) | *待补充* | `上游贡献` |
| [rbg](projects/sgl-project/rbg/summary.md) | - Go · Git · Docker · CI/CD | `上游贡献` |
| [rbg-api](projects/sgl-project/rbg-api/summary.md) | - Go · Git · Docker · CI/CD | `上游贡献` |
| [sgl-cookbook](projects/sgl-project/sgl-cookbook/summary.md) | - JavaScript | `上游贡献` |
| [sgl-docs](projects/sgl-project/sgl-docs/summary.md) | *待补充* | `上游贡献` |
| [sgl-eval](projects/sgl-project/sgl-eval/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [sgl-kernel-npu](projects/sgl-project/sgl-kernel-npu/summary.md) | - C++ · Git · Docker · CI/CD | `ascend` `npu` `sglang` `上游贡献` |
| [sgl-kernel-xpu](projects/sgl-project/sgl-kernel-xpu/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [sgl-learning-materials](projects/sgl-project/sgl-learning-materials/summary.md) | *待补充* | `上游贡献` |
| [sgl-project.github.io](projects/sgl-project/sgl-project.github.io/summary.md) | - Jupyter | `上游贡献` |
| [sgl-test-files](projects/sgl-project/sgl-test-files/summary.md) | *待补充* | `上游贡献` |
| [sgl-whl](projects/sgl-project/sgl-whl/summary.md) | *待补充* | `上游贡献` |
| [sglang](projects/sgl-project/sglang/summary.md) | - Python · Git · Docker · CI/CD | `radix-attention` `sglang` `structured-generation` `上游贡献` `推理` |
| [sglang-ci-stats](projects/sgl-project/sglang-ci-stats/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [sglang-jax](projects/sgl-project/sglang-jax/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [sglang-omni](projects/sgl-project/sglang-omni/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [SpecForge](projects/sgl-project/SpecForge/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [whl](projects/sgl-project/whl/summary.md) | *待补充* | `上游贡献` |

## 🔺 Triton Lang (上游)

*5 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [kernels](projects/triton-lang/kernels/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [triton](projects/triton-lang/triton/summary.md) | - MLIR/LLVM | `compiler` `gpu` `mlir` `triton` `上游贡献` |
| [triton-ascend](projects/triton-lang/triton-ascend/summary.md) | - MLIR/LLVM | `ascend` `compiler` `npu` `triton` `上游贡献` |
| [triton-ext](projects/triton-lang/triton-ext/summary.md) | - Python · Git · Docker · CI/CD | `上游贡献` |
| [Triton-to-tile-IR](projects/triton-lang/Triton-to-tile-IR/summary.md) | - MLIR/LLVM | `上游贡献` |

## 🔥 PyTorch (上游)

*18 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [ao](projects/pytorch/ao/summary.md) | Python, CUDA, Triton | `pytorch` `训练` `推理` `上游贡献` |
| [audio](projects/pytorch/audio/summary.md) | Python, C++, CUDA, sox | `pytorch` `训练` `推理` `上游贡献` |
| [executorch](projects/pytorch/executorch/summary.md) | C++, Python, ARM NEON, XNNPACK | `pytorch` `训练` `推理` `上游贡献` |
| [extension-cpp](projects/pytorch/extension-cpp/summary.md) | C++, CUDA, CMake, Python | `pytorch` `训练` `推理` `上游贡献` |
| [FBGEMM](projects/pytorch/FBGEMM/summary.md) | C++, x86 AVX2/AVX512, ARM NEON | `pytorch` `训练` `推理` `上游贡献` |
| [gloo](projects/pytorch/gloo/summary.md) | C++, MPI, TCP/IP, InfiniBand | `pytorch` `训练` `推理` `上游贡献` |
| [helion](projects/pytorch/helion/summary.md) | Python, CUDA | `pytorch` `训练` `推理` `上游贡献` |
| [ignite](projects/pytorch/ignite/summary.md) | Python, PyTorch | `pytorch` `训练` `推理` `上游贡献` |
| [kineto](projects/pytorch/kineto/summary.md) | C++, CUDA, CUPTI | `pytorch` `训练` `推理` `上游贡献` |
| [ort](projects/pytorch/ort/summary.md) | Python, C++, ONNX | `pytorch` `训练` `推理` `上游贡献` |
| [pytorch](projects/pytorch/pytorch/summary.md) | Python(主体), C++(core/ATen), CUDA, Triton, CMake | `pytorch` `训练` `推理` `上游贡献` |
| [rl](projects/pytorch/rl/summary.md) | Python, PyTorch | `pytorch` `训练` `推理` `上游贡献` |
| [tensordict](projects/pytorch/tensordict/summary.md) | Python, PyTorch | `pytorch` `训练` `推理` `上游贡献` |
| [tensorpipe](projects/pytorch/tensorpipe/summary.md) | C++, CUDA, InfiniBand | `pytorch` `训练` `推理` `上游贡献` |
| [TensorRT](projects/pytorch/TensorRT/summary.md) | Python, C++, CUDA, TensorRT | `pytorch` `训练` `推理` `上游贡献` |
| [torchtitan](projects/pytorch/torchtitan/summary.md) | Python, PyTorch FSDP2, NCCL | `pytorch` `训练` `推理` `上游贡献` |
| [vision](projects/pytorch/vision/summary.md) | Python, C++, CUDA | `pytorch` `训练` `推理` `上游贡献` |
| [xla](projects/pytorch/xla/summary.md) | C++, Python, XLA | `pytorch` `训练` `推理` `上游贡献` |

## 🧩 Tile-AI (上游)

*6 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [tilelang](projects/tile-ai/tilelang/summary.md) | Python, C++, MLIR, CUDA, TVM | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tilelang-ascend](projects/tile-ai/tilelang-ascend/summary.md) | Python, C++, CANN, Ascend NPU | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tilelang-metax](projects/tile-ai/tilelang-metax/summary.md) | Python, C++, Metax SDK | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tilelang-mlir-ascend](projects/tile-ai/tilelang-mlir-ascend/summary.md) | MLIR, C++, Python, CANN | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tilelang-musa](projects/tile-ai/tilelang-musa/summary.md) | Python, C++, MUSA SDK | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tvm](projects/tile-ai/tvm/summary.md) | C++, Python, MLIR, CUDA, ROCm | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |

## 📚 References — 参考文献

| 引用 | 组织 | 关联项目 |
|------|------|----------|
| [firecracker-microvm--firecracker](references//firecracker-microvm--firecracker/summary.md) | - | - |
| [milvus-io--milvus](references//milvus-io--milvus/summary.md) | - | - |
| [sgl-project--sglang](references//sgl-project--sglang/summary.md) | - | - |
| [triton-lang--triton](references//triton-lang--triton/summary.md) | - | - |
| [vllm-project--pagedattention](references//vllm-project--pagedattention/summary.md) | - | - |

---

> 🤖 本文件由 KG Agent 自动维护。每次 `/kg-add`、`/kg-refresh` 后自动重建。
> 📋 操作日志见 [kg-log.md](kg-log.md) · 质量检查见 `/kg-lint`