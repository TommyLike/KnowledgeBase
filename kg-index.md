# KG 全局索引

> 自动生成于 2026-07-10 08:15 UTC · 621 projects · 11 references

## 快速导航

- [🎯 Agent 开发框架](#agent-framework) (19 projects)
- [⚙️ Agent 运行时](#agent-runtime) (72 projects)
  - [🛡️ 沙箱](#agent-runtime-sandbox) (27)
  - [🧠 记忆层](#agent-runtime-memory) (14)
  - [🚪 网关](#agent-runtime-gateway) (10)
  - [📊 可观测性](#agent-runtime-observability) (10)
  - [🔧 工具](#agent-runtime-tool) (7)
  - [📡 协议](#agent-runtime-protocol) (2)
  - [🗺️ 规划器](#agent-runtime-planner) (1)
  - [🔒 安全](#agent-runtime-security) (1)
- [💾 Agent 存储](#agent-storage) (7 projects)
- [🏗️ Agent 基础设施](#agent-infra) (11 projects)
- [☁️ 多云](#multi-cloud) (2 projects)
- [🏢 OpenSourceWay](#opensourceways) (397 projects)
- [🔬 COSDT](#cosdt) (23 projects)
- [🚀 vLLM Project](#vllm-project) (39 projects)
- [⚡ SGL Project](#sgl-project) (22 projects)
- [🔺 Triton Lang](#triton-lang) (5 projects)
- [🔥 PyTorch](#pytorch) (18 projects)
- [🧩 Tile-AI](#tile-ai) (6 projects)
- [📚 References](#references) (11 papers)

---

## 🎯 Agent 开发框架
*19 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [adk-python](projects/agent-framework/adk-python/summary.md) | Python, Java, A2A Protocol, Google Cloud | `agent` `framework` `上游贡献` |
| [agent-framework](projects/agent-framework/agent-framework/summary.md) | Python, C#, Azure, Durable Functions | `agent` `framework` `上游贡献` |
| [agno](projects/agent-framework/agno/summary.md) | Python, OpenTelemetry, MCP, A2A, Docker, PostgreSQL, Apache 2.0 | `agent` |
| [autogen](projects/agent-framework/autogen/summary.md) | Python (61.7%), C# (25.1%), TypeScript (12.4%), OpenAI GPT-4o, gRPC, MCP, Docker | `agent` |
| [camel](projects/agent-framework/camel/summary.md) | Python (95.9%), TypeScript, uv, OpenAI API, Apache 2.0 | `agent` |
| [crewAI](projects/agent-framework/crewAI/summary.md) | Python (98.7%), UV, OpenAI API, Ollama, LM Studio, Pydantic, MCP, A2A | `agent` |
| [dify](projects/agent-framework/dify/summary.md) | Python(后端), TypeScript(前端), PostgreSQL, Redis | `agent` `framework` `上游贡献` |
| [Flowise](projects/agent-framework/Flowise/summary.md) | TypeScript, Node.js, LangChain.js | `agent` `framework` `上游贡献` |
| [harness-sdk](projects/agent-framework/harness-sdk/summary.md) | Python, Strands Agent Framework, MIT | `agent` |
| [kagent](projects/agent-framework/kagent/summary.md) | Go (52.4%), TypeScript (24.9%), Python (18.1%), Google ADK, Kubernetes CRD, Helm, OpenTelemetry, MCP | `agent` |
| [langchain](projects/agent-framework/langchain/summary.md) | Python, TypeScript (LangChain.js), OpenAI/Anthropic SDK, Pydantic, LangSmith (observability), LangGr | `agent` |
| [langgraph](projects/agent-framework/langgraph/summary.md) | Python, TypeScript, Pydantic, langchain-core, SQLite/Postgres, FastAPI | `agent` |
| [llama_index](projects/agent-framework/llama_index/summary.md) | Python, TypeScript, 向量数据库 | `agent` `framework` `上游贡献` |
| [mastra](projects/agent-framework/mastra/summary.md) | TypeScript, Node.js | `agent` `framework` `上游贡献` |
| [NeMo-Agent-Toolkit](projects/agent-framework/NeMo-Agent-Toolkit/summary.md) | Python, NVIDIA NIM, CUDA | `agent` `framework` `上游贡献` |
| [openai-agents-python](projects/agent-framework/openai-agents-python/summary.md) | Python, OpenAI API | `agent` `framework` `上游贡献` |
| [pydantic-ai](projects/agent-framework/pydantic-ai/summary.md) | Python, Pydantic, OpenTelemetry, Logfire, uv, MkDocs, MIT | `agent` |
| [semantic-kernel](projects/agent-framework/semantic-kernel/summary.md) | C#, Python, Java, OpenAI, Azure OpenAI, HuggingFace, Ollama, ONNX, Azure AI Search, Elasticsearch, C | `agent` |
| [smolagents](projects/agent-framework/smolagents/summary.md) | Python, HuggingFace Transformers, LiteLLM, Docker, E2B | `agent` |

## ⚙️ Agent 运行时

### agent-runtime › sandbox
*🛡️ 沙箱 — 27 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [agent-aegis](projects/agent-runtime/sandbox/agent-aegis/summary.md) | TypeScript, Node.js, Apache 2.0 | `agent` `sandbox` `security` `上游贡献` |
| [agent-sandbox](projects/agent-runtime/sandbox/agent-sandbox/summary.md) | Go, Kubernetes CRD, RuntimeClass, Kata Containers/gVisor, Apache 2.0 | `agent` |
| [agentcore-cli](projects/agent-runtime/sandbox/agentcore-cli/summary.md) | TypeScript, Node.js, AWS Bedrock SDK, Apache 2.0 | `agent` `runtime` `aws` `cli` `上游贡献` |
| [agentcore-samples](projects/agent-runtime/sandbox/agentcore-samples/summary.md) | Amazon Bedrock Agentcore 的官方示例和参考实现仓库，由 AWS 实验室（awslabs）维护。展示如何利用 Bedrock Agentcore 平台将 AI Agent 从原型 | `agent` `runtime` `aws` `上游贡献` |
| [agentcube](projects/agent-runtime/sandbox/agentcube/summary.md) | Go, Kubernetes, Volcano, Apache 2.0 | `agent` `sandbox` `kubernetes` `上游贡献` |
| [agentkit-sdk-python](projects/agent-runtime/sandbox/agentkit-sdk-python/summary.md) | AgentKit 是火山引擎（Volcengine）开源的 AI Agent 开发与部署工具包，提供 Python SDK 和 CLI 脚手架工具。团队以**上游贡献**方式参与，关注其在 Agent | `agent` `runtime` `sdk` `上游贡献` |
| [agents](projects/agent-runtime/sandbox/agents/summary.md) | OpenKruise 团队推出的 Agent 沙箱 Operator，为 Kubernetes 上运行 AI Agent 所需的代码执行沙箱提供快速、低成本的部署与管理方案。本项目属于上游贡献范畴，团 | `agent` `sandbox` `kubernetes` `上游贡献` |
| [agentscope-runtime](projects/agent-runtime/sandbox/agentscope-runtime/summary.md) | AgentScope-Runtime 是 AgentScope 生态中的生产级 Agent 应用运行时框架，专注于为 AI Agent 提供安全的工具执行沙箱和全链路可观测性。本项目属于**上游贡献* | `agent` `runtime` `sandbox` `上游贡献` |
| [agentscope-runtime-java](projects/agent-runtime/sandbox/agentscope-runtime-java/summary.md) | agentscope-runtime-java 是 AgentScope 生态的 Java 运行时组件，定位为 AI Agent 的部署执行环境和工具沙箱。项目属于上游贡献范畴，团队关注其在 Java | `agent` `runtime` `java` `上游贡献` |
| [AgentTeams](projects/agent-runtime/sandbox/AgentTeams/summary.md) | AgentTeams 是 agentscope-ai 组织下的开源协作式多智能体操作系统（Collaborative Multi-Agent OS），面向需要透明编排、人机协同的多智能体场景。项目在知 | `agent` `runtime` `multi-agent` `上游贡献` |
| [ax](projects/agent-runtime/sandbox/ax/summary.md) | Google 开源的分布式 Agent 运行时，属于 agent-runtime/sandbox 类别。团队以**上游贡献**方式参与，关注分布式 Agent 编排、沙箱执行环境、以及多 Agent  | `agent` `runtime` `distributed` `上游贡献` |
| [bedrock-agentcore-starter-toolkit](projects/agent-runtime/sandbox/bedrock-agentcore-starter-toolkit/summary.md) | Amazon Bedrock AgentCore 的官方 CLI 启动工具包，属于 AWS 团队的上游贡献项目。提供一套标准化的 Python 命令行工具，帮助开发者在本地快速创建、配置、测试和部署  | `agent` `runtime` `aws` `上游贡献` |
| [coder](projects/agent-runtime/sandbox/coder/summary.md) | Go, TypeScript, Terraform, K8s/Docker, code-server, PostgreSQL, AGPL/Enterprise | `agent` |
| [cohere-terrarium](projects/agent-runtime/sandbox/cohere-terrarium/summary.md) | Terrarium 是 Cohere 开源的一个轻量级 Python 代码沙箱，专为 LLM 数据 Agent 场景设计。在我们的知识图谱中归类为 agent-runtime/sandbox，属于上游 | `agent` `sandbox` `上游贡献` |
| [CubeSandbox](projects/agent-runtime/sandbox/CubeSandbox/summary.md) | Go, Kubernetes, Containerd, Apache 2.0 | `agent` |
| [cwc-long-running-agents](projects/agent-runtime/sandbox/cwc-long-running-agents/summary.md) | Anthropic 官方发布的长时间运行 Agent 参考实现，基于 Claude Computer Use (CWC) 能力构建。该项目展示了如何在沙箱环境中让 Agent 持续工作数小时甚至数天， | `agent` `runtime` `long-running` `上游贡献` |
| [DTVM](projects/agent-runtime/sandbox/DTVM/summary.md) | DTVM（DeTerministic Virtual Machine）是一个面向 AI Agent 的确定性虚拟机项目，由 DTVMStack 组织维护。本项目在知识图谱中标记为**上游贡献**，团队 | `agent` `runtime` `vm` `上游贡献` |
| [infra](projects/agent-runtime/sandbox/infra/summary.md) | Go, Firecracker microVM, KVM, REST API, TypeScript/Python SDK, Docker | `agent` |
| [NemoClaw](projects/agent-runtime/sandbox/NemoClaw/summary.md) | NVIDIA 开源的 Agent 安全运行时环境，用于在 NVIDIA OpenShell 内安全运行 Hermes、OpenClaw 等 AI Agent。属于团队上游贡献范畴，关注其 sandbo | `agent` `runtime` `security` `上游贡献` |
| [OpenSandbox](projects/agent-runtime/sandbox/OpenSandbox/summary.md) | Python (FastAPI), Go (Gin, execd/ingress/egress), Kotlin, C# (.NET), TypeScript, Java, Docker, Kuber | `agent` |
| [OpenShell](projects/agent-runtime/sandbox/OpenShell/summary.md) | ┌──────────────────────────────────────┐ | `agent` `sandbox` `runtime` `上游贡献` |
| [OpenShell-Community](projects/agent-runtime/sandbox/OpenShell-Community/summary.md) | Rust, Docker, Apache 2.0 | `agent` `runtime` `community` `上游贡献` |
| [sandbox](projects/agent-runtime/sandbox/sandbox/summary.md) | TypeScript, Docker, Kubernetes, MIT | `agent` |
| [sandbox-runtime](projects/agent-runtime/sandbox/sandbox-runtime/summary.md) | TypeScript, Node.js, macOS sandbox-exec (Seatbelt Scheme), Linux bubblewrap, HTTP Proxy, SOCKS5 Prox | `agent` `sandbox` `上游贡献` |
| [sandbox-sdk](projects/agent-runtime/sandbox/sandbox-sdk/summary.md) | Cloudflare Sandbox SDK 是 Cloudflare 开源的边缘沙箱运行环境方案，团队以**上游贡献**方式参与。该 SDK 允许开发者在 Cloudflare 全球边缘网络上创建和 | `agent` `sandbox` `边缘计算` `上游贡献` |
| [shell](projects/agent-runtime/sandbox/shell/summary.md) | shell 是 strands-agents 生态中的沙箱化 Shell 执行组件，为 AI Agent 提供受控的命令行环境。项目在 KG 中的定位为**上游贡献**——团队关注其沙箱隔离机制和 A | `agent` `sandbox` `上游贡献` |
| [WindowsAgentArena](projects/agent-runtime/sandbox/WindowsAgentArena/summary.md) | Windows Agent Arena 是微软研究院推出的面向 Windows 操作系统的 AI Agent 基准测试与可扩展沙盒平台。该项目在知识图谱中归类为 agent-runtime/sandb | `agent` `runtime` `windows` `上游贡献` |

### agent-runtime › memory
*🧠 记忆层 — 14 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [beads](projects/agent-runtime/memory/beads/summary.md) | Go, HNSW, 倒排索引, 图数据库引擎, Apache 2.0 | `agent` |
| [hindsight](projects/agent-runtime/memory/hindsight/summary.md) | Python, Event Sourcing, Apache 2.0 | `agent` |
| [letta](projects/agent-runtime/memory/letta/summary.md) | Python, FastAPI, REST/WebSocket, LLM APIs, PostgreSQL, Apache 2.0 | `agent` |
| [mem0](projects/agent-runtime/memory/mem0/summary.md) | Python, Qdrant/Chroma/Weaviate (向量), Neo4j (图), OpenAI/Anthropic API, Apache 2.0 | `agent` |
| [mempalace](projects/agent-runtime/memory/mempalace/summary.md) | Python 3.9+, ChromaDB, SQLite, embeddinggemma-300m / all-MiniLM-L6-v2, gRPC, numpy, Docker (CPU/GPU) | `agent` |
| [memU](projects/agent-runtime/memory/memU/summary.md) | Python 3.13+ (含 Rust 扩展), uv 包管理, asyncio 异步框架, SQLite / PostgreSQL + pgvector, OpenAI / DeepSeek /  | `agent` |
| [NoKV](projects/agent-runtime/memory/NoKV/summary.md) | Rust, MIT | `agent` |
| [OpenViking](projects/agent-runtime/memory/OpenViking/summary.md) | OpenViking 是字节跳动/火山引擎开源的面向 AI Agent 的上下文数据库，为团队在上游 Agent 基础设施层的关注项目。我们关注其在高性能向量检索、混合存储引擎、以及 Agent 记忆 | `agent` `memory` `context` `上游贡献` |
| [powermem](projects/agent-runtime/memory/powermem/summary.md) | PowerMem 是 OceanBase 开源的 AI Memory 插件，属于 agent-runtime 生态中的记忆管理组件。本项目为上游贡献关注，团队关注其在 AI Agent 记忆管理领域的 | `agent` `memory` `上游贡献` |
| [ragflow](projects/agent-runtime/memory/ragflow/summary.md) | Python, TypeScript, DeepDoc (CV+OCR), Infinity (Rust 向量数据库), Elasticsearch, Redis, PostgreSQL | `agent` |
| [ReMe](projects/agent-runtime/memory/ReMe/summary.md) | ReMe 是 AgentScope 团队开源的 Agent 记忆管理工具包，为 LLM Agent 提供可扩展的长期记忆能力。团队将其纳入知识图谱作为上游贡献项目，关注其在记忆检索、记忆总结和跨会话上 | `agent` `memory` `上游贡献` |
| [seekdb](projects/agent-runtime/memory/seekdb/summary.md) | C++, SQL, OceanBase, HNSW, Paxos, Apache 2.0 | `agent` |
| [supabase](projects/agent-runtime/memory/supabase/summary.md) | TypeScript, PostgreSQL, pgvector, PostgREST, GoTrue (auth), Elixir (realtime), MIT + EE | `agent` |
| [TencentDB-Agent-Memory](projects/agent-runtime/memory/TencentDB-Agent-Memory/summary.md) | Python, Vector Database (ChromaDB / Milvus / FAISS), Embedding Models, LangChain / LlamaIndex 集成, SQ | `agent` `memory` `上游贡献` |

### agent-runtime › gateway
*🚪 网关 — 10 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [agentgateway](projects/agent-runtime/gateway/agentgateway/summary.md) | Rust, A2A Protocol, gRPC, HTTP, Apache 2.0 | `agent` |
| [ai-gateway](projects/agent-runtime/gateway/ai-gateway/summary.md) | C++ (Envoy), Go, Protobuf/gRPC, xDS, Envoy Filter API, Apache 2.0 | `agent` |
| [cc-switch](projects/agent-runtime/gateway/cc-switch/summary.md) | Rust 61.5%, TypeScript 36.9%, React 18, Vite, TailwindCSS 3.4, Tauri 2.8, TanStack Query v5, shadcn/ | `agent` |
| [CLIProxyAPI](projects/agent-runtime/gateway/CLIProxyAPI/summary.md) | Go, HTTP, OpenAI API, MIT | `agent` |
| [higress](projects/agent-runtime/gateway/higress/summary.md) | Go, C++ (Envoy), Java (Console 后端), TypeScript/Node.js (Console 前端), Rust (Wasm 插件 SDK), WebAssembly | `agent` |
| [kgateway](projects/agent-runtime/gateway/kgateway/summary.md) | Go, Kubernetes Gateway API, Envoy Proxy, xDS, CRD, Apache 2.0 | `agent` |
| [litellm](projects/agent-runtime/gateway/litellm/summary.md) | Python, OpenAI SDK, FastAPI (Proxy), PostgreSQL, Redis, 100+ Provider SDKs, MIT | `agent` |
| [mcp-gateway-registry](projects/agent-runtime/gateway/mcp-gateway-registry/summary.md) | Python / FastAPI（后端 API），Nginx（反向代理），MongoDB CE / Amazon DocumentDB / MongoDB Atlas（数据存储），sentence-t | `agent` |
| [new-api](projects/agent-runtime/gateway/new-api/summary.md) | Go, 自研 Web 框架（controller/middleware/router/service/model 分层）, 自研前端（AGPLv3+）, SQLite / MySQL / Postgr | `agent` |
| [rtk](projects/agent-runtime/gateway/rtk/summary.md) | Rust (93.1%), Shell (4.6%), TypeScript (1.5%), SQLite (rusqlite), Clap, serde, regex, Rust 标准库 I/O | `agent` |

### agent-runtime › observability
*📊 可观测性 — 10 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [deepeval](projects/agent-runtime/observability/deepeval/summary.md) | Python, PyTest, LangChain/LlamaIndex, OpenAI/Anthropic API, Apache 2.0 | `agent` |
| [langfuse](projects/agent-runtime/observability/langfuse/summary.md) | TypeScript, Next.js, ClickHouse, PostgreSQL, Prisma, OpenTelemetry, MIT (core) + EE | `agent` |
| [lm-evaluation-harness](projects/agent-runtime/observability/lm-evaluation-harness/summary.md) | Python, PyTorch, HuggingFace Transformers/Datasets, Accelerate, vLLM, SGLang, llama.cpp, ONNX Runtim | `agent` |
| [openlit](projects/agent-runtime/observability/openlit/summary.md) | Python, OpenTelemetry, NVIDIA DCGM, Grafana, Apache 2.0 | `agent` |
| [openllmetry](projects/agent-runtime/observability/openllmetry/summary.md) | Python, OpenTelemetry, LangChain/OpenAI SDK, Apache 2.0 | `agent` |
| [opik](projects/agent-runtime/observability/opik/summary.md) | Python, Java, OpenTelemetry, ClickHouse, MySQL, React, Apache 2.0 | `agent` |
| [phoenix](projects/agent-runtime/observability/phoenix/summary.md) | Python (45.7%), TypeScript/React (39.2%), Jupyter Notebook (13.8%), OpenTelemetry Protocol (OTLP), O | `agent` |
| [promptfoo](projects/agent-runtime/observability/promptfoo/summary.md) | TypeScript, YAML, OpenAI/Anthropic API, MIT | `agent` |
| [ragas](projects/agent-runtime/observability/ragas/summary.md) | Python, LangChain/LlamaIndex, OpenAI/Anthropic API, Apache 2.0 | `agent` |
| [trulens](projects/agent-runtime/observability/trulens/summary.md) | Python, OpenTelemetry, Streamlit, SQLite/PostgreSQL/Snowflake, Poetry, Azure Pipelines, MkDocs | `agent` |

### agent-runtime › tool
*🔧 工具 — 7 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [agent-browser](projects/agent-runtime/tool/agent-browser/summary.md) | TypeScript, Puppeteer, Vercel AI SDK, MIT | `agent` |
| [browser-harness](projects/agent-runtime/tool/browser-harness/summary.md) | Python, Playwright, MIT | `agent` |
| [browser-use](projects/agent-runtime/tool/browser-use/summary.md) | Python, Playwright, LangChain, OpenAI/Anthropic API, Chromium/Firefox/WebKit, MIT | `agent` |
| [composio](projects/agent-runtime/tool/composio/summary.md) | TypeScript, Python, OAuth2, 200+ SaaS API 集成, PostgreSQL, Apache 2.0 | `agent` |
| [firecrawl](projects/agent-runtime/tool/firecrawl/summary.md) | TypeScript, Rust (部分模块), Puppeteer/Playwright, Redis, PostgreSQL, Markdown, MIT + EE | `agent` |
| [page-agent](projects/agent-runtime/tool/page-agent/summary.md) | Python, DOM Parser, LLM APIs, Apache 2.0 | `agent` |
| [reader](projects/agent-runtime/tool/reader/summary.md) | TypeScript, civkit, tsyringe, Puppeteer, curl-impersonate, PDF.js, LibreOffice, Turndown, Koa, Docke | `agent` |

### agent-runtime › protocol
*📡 协议 — 2 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [A2A](projects/agent-runtime/protocol/A2A/summary.md) | Python, TypeScript, HTTP/JSON, SSE, JWT/OAuth, Apache 2.0 | `agent` |
| [modelcontextprotocol](projects/agent-runtime/protocol/modelcontextprotocol/summary.md) | TypeScript, Python, JSON-RPC 2.0, JSON Schema, SSE, HTTP, MIT (spec) | `agent` |

### agent-runtime › planner
*🗺️ 规划器 — 1 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [gpt-researcher](projects/agent-runtime/planner/gpt-researcher/summary.md) | Python ≥ 3.11, FastAPI + Uvicorn（后端）, LangChain + LangGraph（Agent 编排）, AG2 可选（第二多 Agent 框架）, LiteLLM | `agent` |

### agent-runtime › security
*🔒 安全 — 1 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [llm-guard](projects/agent-runtime/security/llm-guard/summary.md) | Python, HuggingFace Transformers, ONNX, OpenAI Moderation API, Apache 2.0 | `agent` |

## 💾 Agent 存储
*7 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [chroma](projects/agent-storage/chroma/summary.md) | Rust (core engine), Python (SDK), TypeScript (client), HNSW, SQLite, Apache 2.0 | `agent` |
| [lancedb](projects/agent-storage/lancedb/summary.md) | Rust (核心引擎), Lance (自研列式存储格式), Apache Arrow, Apache DataFusion (SQL 引擎), Python/Typescript/Java (SDK | `agent` |
| [marqo](projects/agent-storage/marqo/summary.md) | Python, PyTorch, ONNX, CLIP/BERT, Vespa (底层搜索引擎), Docker, Apache 2.0 | `agent` |
| [milvus](projects/agent-storage/milvus/summary.md) | Go, C++, Python SDK, gRPC, MinIO/S3, Pulsar/Kafka, etcd, Apache 2.0, CNCF Graduated | `agent` |
| [opensearch](projects/agent-storage/opensearch/summary.md) | Java, Lucene, k-NN Plugin, ML Commons, OpenSearch Dashboard, Apache 2.0 | `agent` |
| [qdrant](projects/agent-storage/qdrant/summary.md) | Rust, gRPC, REST API, RocksDB, HNSW, Raft, Apache 2.0 | `agent` |
| [weaviate](projects/agent-storage/weaviate/summary.md) | Go, GraphQL, HNSW, BM25, OpenAI/HuggingFace/Cohere, Apache 2.0 | `agent` |

## 🏗️ Agent 基础设施
*11 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [AReaL](projects/agent-infra/AReaL/summary.md) | *待补充* | `rl` `rlhf` `post-training` `llm` |
| [firecracker](projects/agent-infra/firecracker/summary.md) | Rust, KVM, Linux Kernel, virtio, seccomp, cgroup, OpenAPI (API 规范) | `agent` |
| [inngest](projects/agent-infra/inngest/summary.md) | TypeScript, Go (executor), Python, Vercel/Netlify, AWS Lambda, Event Store | `agent` |
| [miles](projects/agent-infra/miles/summary.md) | *待补充* | `rl` `rlhf` `post-training` `llm` |
| [nats-server](projects/agent-infra/nats-server/summary.md) | Go, Go Modules, GoReleaser, Docker, Helm, 自定义文本协议, 自研文件存储引擎, Raft, TLS, JWT | `agent` |
| [redpanda](projects/agent-infra/redpanda/summary.md) | C++, Seastar, Raft, Bazel, Go (rpk CLI), Go (Redpanda Connect / Benthos), WebAssembly (WASM), Python | `agent` |
| [restate](projects/agent-infra/restate/summary.md) | Rust, TypeScript/Java/Kotlin/Python/Go SDK, gRPC, HTTP, RocksDB (storage) | `agent` |
| [ROLL](projects/agent-infra/ROLL/summary.md) | *待补充* | `rl` `rlhf` `post-training` `llm` |
| [slime](projects/agent-infra/slime/summary.md) | *待补充* | `rl` `rlhf` `post-training` `llm` |
| [temporal](projects/agent-infra/temporal/summary.md) | Go, Protocol Buffers, gRPC, Cassandra, MySQL/PostgreSQL | `agent` |
| [trigger.dev](projects/agent-infra/trigger.dev/summary.md) | TypeScript, Next.js, Zod, Vercel, OpenAI/Anthropic SDK, PostgreSQL | `agent` |

## ☁️ 多云
*2 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [karmada](projects/multi-cloud/karmada/summary.md) | *待补充* | `上游贡献` `multi-cluster` `kubernetes` `scheduling` `cncf` |
| [liqo](projects/multi-cloud/liqo/summary.md) | *待补充* | `上游贡献` `multi-cluster` `kubernetes` `scheduling` |

## 🏢 OpenSourceWay
*397 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [2022shanghai-covid](projects/opensourceways/2022shanghai-covid/summary.md) | *待补充* | `ai-agent` `community` `python` `团队主导` |
| [agent-development-specification](projects/opensourceways/agent-development-specification/summary.md) | *待补充* | `ai-agent` `ci-cd` `shell` `团队主导` |
| [agent-framwork](projects/opensourceways/agent-framwork/summary.md) | *待补充* | `ai-agent` `python` `团队主导` |
| [agent-skills](projects/opensourceways/agent-skills/summary.md) | *待补充* | `ai-agent` `python` `团队主导` |
| [ai-auto-test](projects/opensourceways/ai-auto-test/summary.md) | *待补充* | `ai-agent` `shell` `团队主导` |
| [ai-native-develop-infra](projects/opensourceways/ai-native-develop-infra/summary.md) | *待补充* | `ai-agent` `shell` `团队主导` |
| [ai-proxy](projects/opensourceways/ai-proxy/summary.md) | *待补充* | `ai-agent` `python` `团队主导` |
| [aibrix-deploy](projects/opensourceways/aibrix-deploy/summary.md) | *待补充* | `ai-agent` `deploy` `团队主导` |
| [aidigest](projects/opensourceways/aidigest/summary.md) | *待补充* | `ai-agent` `python` `团队主导` |
| [apig-discovery-service](projects/opensourceways/apig-discovery-service/summary.md) | *待补充* | `backend` `python` `团队主导` |
| [apig-openapi-registry](projects/opensourceways/apig-openapi-registry/summary.md) | *待补充* | `backend` `团队主导` |
| [apig-registry-tools](projects/opensourceways/apig-registry-tools/summary.md) | *待补充* | `backend` `cli` `python` `团队主导` |
| [APIMagic](projects/opensourceways/APIMagic/summary.md) | *待补充* | `backend` `团队主导` |
| [app-bot](projects/opensourceways/app-bot/summary.md) | *待补充* | `团队主导` |
| [app-bugzilla](projects/opensourceways/app-bugzilla/summary.md) | *待补充* | `community` `docker` `团队主导` |
| [app-cla-server](projects/opensourceways/app-cla-server/summary.md) | *待补充* | `auth` `backend` `go` `repo-management` `团队主导` |
| [app-cla-signing](projects/opensourceways/app-cla-signing/summary.md) | *待补充* | `auth` `go` `团队主导` |
| [app-cla-stat](projects/opensourceways/app-cla-stat/summary.md) | *待补充* | `auth` `data` `go` `团队主导` |
| [app-cla-webui](projects/opensourceways/app-cla-webui/summary.md) | *待补充* | `auth` `frontend` `javascript` `团队主导` |
| [app-community-metadata](projects/opensourceways/app-community-metadata/summary.md) | *待补充* | `community` `data` `go` `团队主导` |
| [app-cve-backend](projects/opensourceways/app-cve-backend/summary.md) | *待补充* | `backend` `java` `security` `团队主导` |
| [app-cve-frontend](projects/opensourceways/app-cve-frontend/summary.md) | *待补充* | `css` `frontend` `security` `团队主导` |
| [app-jenkins](projects/opensourceways/app-jenkins/summary.md) | *待补充* | `ci-cd` `团队主导` |
| [app-kubernetes-maintenance](projects/opensourceways/app-kubernetes-maintenance/summary.md) | *待补充* | `ai-agent` `docker` `frontend` `kubernetes` `repo-management` `团队主导` |
| [app-mailman](projects/opensourceways/app-mailman/summary.md) | *待补充* | `ai-agent` `email` `frontend` `kubernetes` `python` `团队主导` |
| [app-meeting-server](projects/opensourceways/app-meeting-server/summary.md) | *待补充* | `backend` `community` `python` `团队主导` |
| [app-meetingbot](projects/opensourceways/app-meetingbot/summary.md) | *待补充* | `community` `docker` `团队主导` |
| [app-patchtracking](projects/opensourceways/app-patchtracking/summary.md) | *待补充* | `community` `docker` `团队主导` |
| [app-pkgmanage](projects/opensourceways/app-pkgmanage/summary.md) | *待补充* | `python` `团队主导` |
| [app-publish](projects/opensourceways/app-publish/summary.md) | *待补充* | `java` `团队主导` |
| [app-repo](projects/opensourceways/app-repo/summary.md) | *待补充* | `backend` `css` `repo-management` `团队主导` |
| [app-robot-server](projects/opensourceways/app-robot-server/summary.md) | *待补充* | `backend` `bot` `团队主导` |
| [app-robot-webui](projects/opensourceways/app-robot-webui/summary.md) | *待补充* | `bot` `frontend` `团队主导` |
| [app-ssh-tunnel](projects/opensourceways/app-ssh-tunnel/summary.md) | *待补充* | `docker` `kubernetes` `团队主导` |
| [argocd-application](projects/opensourceways/argocd-application/summary.md) | *待补充* | `ci-cd` `deploy` `团队主导` |
| [argus-controller](projects/opensourceways/argus-controller/summary.md) | *待补充* | `ci-cd` `git-platform` `go` `workflow` `团队主导` |
| [argus-worker](projects/opensourceways/argus-worker/summary.md) | *待补充* | `ci-cd` `git-platform` `go` `kubernetes` `workflow` `团队主导` |
| [argus-workflow-demo](projects/opensourceways/argus-workflow-demo/summary.md) | *待补充* | `git-platform` `go` `workflow` `团队主导` |
| [ascend-ci-argocd](projects/opensourceways/ascend-ci-argocd/summary.md) | *待补充* | `ascend` `ci-cd` `git-platform` `团队主导` |
| [ascend-ci-deployment](projects/opensourceways/ascend-ci-deployment/summary.md) | *待补充* | `ascend` `ci-cd` `deploy` `kubernetes` `shell` `团队主导` |
| [ascend-ci-permission](projects/opensourceways/ascend-ci-permission/summary.md) | *待补充* | `ascend` `ci-cd` `团队主导` |
| [ascend-ci-project](projects/opensourceways/ascend-ci-project/summary.md) | *待补充* | `ai-agent` `ascend` `ci-cd` `deploy` `repo-management` `团队主导` |
| [ascend-runner-onboarding](projects/opensourceways/ascend-runner-onboarding/summary.md) | *待补充* | `ascend` `go` `团队主导` |
| [ascend_optimization_scripts](projects/opensourceways/ascend_optimization_scripts/summary.md) | *待补充* | `ascend` `community` `python` `团队主导` |
| [audit-lib](projects/opensourceways/audit-lib/summary.md) | *待补充* | `observability` `sdk` `团队主导` |
| [auth-center](projects/opensourceways/auth-center/summary.md) | *待补充* | `auth` `java` `团队主导` |
| [backlog](projects/opensourceways/backlog/summary.md) | Markdown（文档模板）· Python · Shell · Jenkins（流水线）· Kubernetes（预览集群）· Vault（配置管理）· GitHub Actions | `python` `团队主导` |
| [benchmark_llm](projects/opensourceways/benchmark_llm/summary.md) | *待补充* | `llm` `python` `团队主导` |
| [bigfiles-lfs-all](projects/opensourceways/bigfiles-lfs-all/summary.md) | *待补充* | `团队主导` |
| [calculator-umbrella](projects/opensourceways/calculator-umbrella/summary.md) | *待补充* | `ai-agent` `makefile` `repo-management` `团队主导` |
| [cdn-check](projects/opensourceways/cdn-check/summary.md) | *待补充* | `go` `团队主导` |
| [cdn-cronjob](projects/opensourceways/cdn-cronjob/summary.md) | *待补充* | `go` `团队主导` |
| [cdn-nginx](projects/opensourceways/cdn-nginx/summary.md) | *待补充* | `docker` `团队主导` |
| [certification-all](projects/opensourceways/certification-all/summary.md) | *待补充* | `团队主导` |
| [certification-server](projects/opensourceways/certification-server/summary.md) | *待补充* | `backend` `java` `团队主导` |
| [certification-website](projects/opensourceways/certification-website/summary.md) | *待补充* | `frontend` `vue` `团队主导` |
| [China-CID](projects/opensourceways/China-CID/summary.md) | *待补充* | `ci-cd` `vue` `团队主导` |
| [ci-all](projects/opensourceways/ci-all/summary.md) | *待补充* | `ci-cd` `团队主导` |
| [cla](projects/opensourceways/cla/summary.md) | *待补充* | `auth` `团队主导` |
| [cla-all](projects/opensourceways/cla-all/summary.md) | *待补充* | `auth` `团队主导` |
| [code-server-operator](projects/opensourceways/code-server-operator/summary.md) | *待补充* | `backend` `go` `kubernetes` `团队主导` |
| [codearts-CI](projects/opensourceways/codearts-CI/summary.md) | *待补充* | `ci-cd` `python` `团队主导` |
| [codearts-ci-config](projects/opensourceways/codearts-ci-config/summary.md) | *待补充* | `ci-cd` `shell` `团队主导` |
| [codearts-workflow-image](projects/opensourceways/codearts-workflow-image/summary.md) | *待补充* | `shell` `workflow` `团队主导` |
| [cola-golang](projects/opensourceways/cola-golang/summary.md) | *待补充* | `团队主导` |
| [community-health](projects/opensourceways/community-health/summary.md) | *待补充* | `cli` `community` `observability` `python` `repo-management` `团队主导` |
| [community-robot-lib](projects/opensourceways/community-robot-lib/summary.md) | *待补充* | `bot` `community` `go` `sdk` `团队主导` |
| [community-robots](projects/opensourceways/community-robots/summary.md) | *待补充* | `bot` `community` `shell` `团队主导` |
| [community-sig-monitor](projects/opensourceways/community-sig-monitor/summary.md) | *待补充* | `community` `frontend` `git-platform` `observability` `python` `团队主导` |
| [compass-ci](projects/opensourceways/compass-ci/summary.md) | *待补充* | `ci-cd` `deploy` `团队主导` |
| [copr_design](projects/opensourceways/copr_design/summary.md) | *待补充* | `html` `团队主导` |
| [copr_docker](projects/opensourceways/copr_docker/summary.md) | *待补充* | `docker` `团队主导` |
| [cora](projects/opensourceways/cora/summary.md) | Go · Cobra（CLI 框架）· OpenAPI 3.0（Spec 驱动）· YAML（配置/视图定义）· Makefile + Docker | `cli` `community` `go` `团队主导` |
| [cve-manager](projects/opensourceways/cve-manager/summary.md) | *待补充* | `go` `security` `团队主导` |
| [cve-manager-ng](projects/opensourceways/cve-manager-ng/summary.md) | *待补充* | `go` `security` `团队主导` |
| [cve-sa-backend](projects/opensourceways/cve-sa-backend/summary.md) | *待补充* | `backend` `go` `security` `团队主导` |
| [dataarts_tasks](projects/opensourceways/dataarts_tasks/summary.md) | *待补充* | `data` `团队主导` |
| [DataMagic](projects/opensourceways/DataMagic/summary.md) | *待补充* | `data` `java` `团队主导` |
| [datastat-manage-website](projects/opensourceways/datastat-manage-website/summary.md) | *待补充* | `data` `frontend` `vue` `团队主导` |
| [datastat-server](projects/opensourceways/datastat-server/summary.md) | *待补充* | `backend` `data` `java` `团队主导` |
| [defect-manager](projects/opensourceways/defect-manager/summary.md) | *待补充* | `go` `团队主导` |
| [deploy](projects/opensourceways/deploy/summary.md) | *待补充* | `deploy` `团队主导` |
| [design-workflow](projects/opensourceways/design-workflow/summary.md) | *待补充* | `workflow` `团队主导` |
| [discourse-analytics](projects/opensourceways/discourse-analytics/summary.md) | *待补充* | `data` `javascript` `团队主导` |
| [discourse-audit-cronjob](projects/opensourceways/discourse-audit-cronjob/summary.md) | *待补充* | `observability` `python` `团队主导` |
| [discourse-easecheck](projects/opensourceways/discourse-easecheck/summary.md) | *待补充* | `ruby` `团队主导` |
| [discourse_config](projects/opensourceways/discourse_config/summary.md) | *待补充* | `python` `团队主导` |
| [discourse_theme](projects/opensourceways/discourse_theme/summary.md) | *待补充* | `javascript` `团队主导` |
| [doc-search-input](projects/opensourceways/doc-search-input/summary.md) | *待补充* | `ai-agent` `ascend` `auth` `python` `团队主导` |
| [docs](projects/opensourceways/docs/summary.md) | *待补充* | `frontend` `javascript` `repo-management` `团队主导` |
| [docs-archived](projects/opensourceways/docs-archived/summary.md) | *待补充* | `团队主导` |
| [easy-editor-website](projects/opensourceways/easy-editor-website/summary.md) | *待补充* | `frontend` `vue` `团队主导` |
| [easyeditor-server](projects/opensourceways/easyeditor-server/summary.md) | *待补充* | `backend` `java` `团队主导` |
| [easymodel-plugins](projects/opensourceways/easymodel-plugins/summary.md) | *待补充* | `llm` `python` `团队主导` |
| [easypackages](projects/opensourceways/easypackages/summary.md) | *待补充* | `shell` `团队主导` |
| [EasySearch](projects/opensourceways/EasySearch/summary.md) | *待补充* | `elasticsearch` `java` `团队主导` |
| [EasySearch-RAGSearch](projects/opensourceways/EasySearch-RAGSearch/summary.md) | *待补充* | `elasticsearch` `python` `团队主导` |
| [EasySearch-RAGSearch-frontend](projects/opensourceways/EasySearch-RAGSearch-frontend/summary.md) | *待补充* | `elasticsearch` `frontend` `javascript` `团队主导` |
| [EasySearchImport](projects/opensourceways/EasySearchImport/summary.md) | *待补充* | `elasticsearch` `java` `团队主导` |
| [EasySoftware-autorepair](projects/opensourceways/EasySoftware-autorepair/summary.md) | *待补充* | `ai-agent` `团队主导` |
| [easysoftware-autoupgrade](projects/opensourceways/easysoftware-autoupgrade/summary.md) | *待补充* | `java` `团队主导` |
| [easysoftware-pr-autohandle](projects/opensourceways/easysoftware-pr-autohandle/summary.md) | *待补充* | `java` `团队主导` |
| [EasySoftwareInput](projects/opensourceways/EasySoftwareInput/summary.md) | *待补充* | `ascend` `java` `团队主导` |
| [EasySoftwareService](projects/opensourceways/EasySoftwareService/summary.md) | *待补充* | `java` `团队主导` |
| [easywhisperx](projects/opensourceways/easywhisperx/summary.md) | *待补充* | `python` `团队主导` |
| [easywhisperx-website](projects/opensourceways/easywhisperx-website/summary.md) | *待补充* | `css` `frontend` `团队主导` |
| [etherpad-lite](projects/opensourceways/etherpad-lite/summary.md) | *待补充* | `typescript` `团队主导` |
| [eur-build-all](projects/opensourceways/eur-build-all/summary.md) | *待补充* | `frontend` `团队主导` |
| [flexcompute-sdk](projects/opensourceways/flexcompute-sdk/summary.md) | *待补充* | `go` `sdk` `团队主导` |
| [flexcompute-server](projects/opensourceways/flexcompute-server/summary.md) | *待补充* | `backend` `go` `团队主导` |
| [forum-reply-robot](projects/opensourceways/forum-reply-robot/summary.md) | *待补充* | `bot` `community` `python` `团队主导` |
| [foundation-model-server](projects/opensourceways/foundation-model-server/summary.md) | *待补充* | `backend` `go` `llm` `团队主导` |
| [geo-develop-workflow](projects/opensourceways/geo-develop-workflow/summary.md) | *待补充* | `javascript` `workflow` `团队主导` |
| [geo-question-sets](projects/opensourceways/geo-question-sets/summary.md) | *待补充* | `团队主导` |
| [geo-workflow](projects/opensourceways/geo-workflow/summary.md) | *待补充* | `python` `workflow` `团队主导` |
| [git-access-sdk](projects/opensourceways/git-access-sdk/summary.md) | *待补充* | `go` `sdk` `团队主导` |
| [gitcode-ascend-trans](projects/opensourceways/gitcode-ascend-trans/summary.md) | *待补充* | `ascend` `git-platform` `python` `团队主导` |
| [gitcode-migrate-script](projects/opensourceways/gitcode-migrate-script/summary.md) | *待补充* | `git-platform` `python` `团队主导` |
| [go-atomgit](projects/opensourceways/go-atomgit/summary.md) | *待补充* | `go` `团队主导` |
| [go-ddd-framework](projects/opensourceways/go-ddd-framework/summary.md) | *待补充* | `go` `sdk` `团队主导` |
| [go-gitcode](projects/opensourceways/go-gitcode/summary.md) | *待补充* | `backend` `git-platform` `go` `sdk` `团队主导` |
| [go-gitee](projects/opensourceways/go-gitee/summary.md) | *待补充* | `git-platform` `go` `sdk` `团队主导` |
| [go-github-adapter](projects/opensourceways/go-github-adapter/summary.md) | *待补充* | `git-platform` `go` `团队主导` |
| [golang-ddd-framework](projects/opensourceways/golang-ddd-framework/summary.md) | *待补充* | `go` `sdk` `团队主导` |
| [happy-new-year](projects/opensourceways/happy-new-year/summary.md) | *待补充* | `vue` `团队主导` |
| [hdc-task-manager](projects/opensourceways/hdc-task-manager/summary.md) | *待补充* | `go` `团队主导` |
| [helm-chart-value](projects/opensourceways/helm-chart-value/summary.md) | *待补充* | `deploy` `kubernetes` `团队主导` |
| [helm-charts](projects/opensourceways/helm-charts/summary.md) | *待补充* | `deploy` `kubernetes` `团队主导` |
| [hifloat-website](projects/opensourceways/hifloat-website/summary.md) | *待补充* | `frontend` `团队主导` |
| [hot-topic-website-backend](projects/opensourceways/hot-topic-website-backend/summary.md) | *待补充* | `backend` `frontend` `go` `团队主导` |
| [hotopic-all](projects/opensourceways/hotopic-all/summary.md) | *待补充* | `shell` `团队主导` |
| [hotopic-data-clean](projects/opensourceways/hotopic-data-clean/summary.md) | *待补充* | `community` `data` `python` `团队主导` |
| [hotopic-mining](projects/opensourceways/hotopic-mining/summary.md) | *待补充* | `community` `python` `团队主导` |
| [hwid-website](projects/opensourceways/hwid-website/summary.md) | *待补充* | `css` `frontend` `团队主导` |
| [image-scanning](projects/opensourceways/image-scanning/summary.md) | *待补充* | `go` `团队主导` |
| [inference-perf-dashboard](projects/opensourceways/inference-perf-dashboard/summary.md) | *待补充* | `frontend` `python` `团队主导` |
| [inference-platform](projects/opensourceways/inference-platform/summary.md) | *待补充* | `python` `团队主导` |
| [infra-audit-service](projects/opensourceways/infra-audit-service/summary.md) | *待补充* | `go` `observability` `团队主导` |
| [infra-common](projects/opensourceways/infra-common/summary.md) | *待补充* | `python` `repo-management` `团队主导` |
| [infra-community](projects/opensourceways/infra-community/summary.md) | *待补充* | `community` `python` `repo-management` `团队主导` |
| [infra-landscape](projects/opensourceways/infra-landscape/summary.md) | *待补充* | `docker` `团队主导` |
| [infra-mindspore](projects/opensourceways/infra-mindspore/summary.md) | *待补充* | `community` `mindspore` `repo-management` `shell` `团队主导` |
| [infra-openeuler](projects/opensourceways/infra-openeuler/summary.md) | *待补充* | `community` `openeuler` `repo-management` `团队主导` |
| [infra-openfuyao](projects/opensourceways/infra-openfuyao/summary.md) | *待补充* | `community` `团队主导` |
| [infra-opengauss](projects/opensourceways/infra-opengauss/summary.md) | *待补充* | `community` `opengauss` `repo-management` `团队主导` |
| [infra-openlookeng](projects/opensourceways/infra-openlookeng/summary.md) | *待补充* | `community` `团队主导` |
| [infra-openmind](projects/opensourceways/infra-openmind/summary.md) | *待补充* | `团队主导` |
| [infra-openubmc](projects/opensourceways/infra-openubmc/summary.md) | *待补充* | `openubmc` `团队主导` |
| [infra-pytorch](projects/opensourceways/infra-pytorch/summary.md) | *待补充* | `pytorch` `团队主导` |
| [infra-radar](projects/opensourceways/infra-radar/summary.md) | *待补充* | `ci-cd` `go` `observability` `团队主导` |
| [infraAIService](projects/opensourceways/infraAIService/summary.md) | *待补充* | `ai-agent` `python` `团队主导` |
| [infrastructure](projects/opensourceways/infrastructure/summary.md) | *待补充* | `python` `团队主导` |
| [insights](projects/opensourceways/insights/summary.md) | *待补充* | `data` `团队主导` |
| [integration-tests](projects/opensourceways/integration-tests/summary.md) | *待补充* | `ai-agent` `python` `repo-management` `团队主导` |
| [ip-geo-fastapi](projects/opensourceways/ip-geo-fastapi/summary.md) | *待补充* | `backend` `ci-cd` `python` `团队主导` |
| [issue-cli](projects/opensourceways/issue-cli/summary.md) | *待补充* | `cli` `团队主导` |
| [issue_pr_board](projects/opensourceways/issue_pr_board/summary.md) | *待补充* | `go` `团队主导` |
| [issue_state_monitor](projects/opensourceways/issue_state_monitor/summary.md) | *待补充* | `data` `go` `observability` `团队主导` |
| [istio-demo](projects/opensourceways/istio-demo/summary.md) | *待补充* | `python` `团队主导` |
| [jenkins-log-scanner](projects/opensourceways/jenkins-log-scanner/summary.md) | *待补充* | `ci-cd` `cli` `community` `frontend` `go` `团队主导` |
| [kafka-lib](projects/opensourceways/kafka-lib/summary.md) | *待补充* | `go` `messaging` `sdk` `团队主导` |
| [keycloak-social-gitee](projects/opensourceways/keycloak-social-gitee/summary.md) | *待补充* | `auth` `ci-cd` `git-platform` `html` `团队主导` |
| [lfs-website](projects/opensourceways/lfs-website/summary.md) | *待补充* | `css` `frontend` `团队主导` |
| [lingqu-website](projects/opensourceways/lingqu-website/summary.md) | *待补充* | `css` `frontend` `团队主导` |
| [llm-wiki](projects/opensourceways/llm-wiki/summary.md) | *待补充* | `llm` `团队主导` |
| [lxc-launcher](projects/opensourceways/lxc-launcher/summary.md) | *待补充* | `go` `团队主导` |
| [maillist-templates](projects/opensourceways/maillist-templates/summary.md) | *待补充* | `ai-agent` `email` `repo-management` `团队主导` |
| [mailman](projects/opensourceways/mailman/summary.md) | *待补充* | `ai-agent` `docker` `email` `frontend` `python` `团队主导` |
| [MCP-gateway](projects/opensourceways/MCP-gateway/summary.md) | *待补充* | `backend` `mcp` `typescript` `团队主导` |
| [meeting-cann-website](projects/opensourceways/meeting-cann-website/summary.md) | *待补充* | `community` `frontend` `typescript` `团队主导` |
| [meeting-center](projects/opensourceways/meeting-center/summary.md) | *待补充* | `ci-cd` `community` `frontend` `python` `团队主导` |
| [meeting-mcp](projects/opensourceways/meeting-mcp/summary.md) | *待补充* | `community` `mcp` `团队主导` |
| [meeting-platform](projects/opensourceways/meeting-platform/summary.md) | *待补充* | `community` `python` `团队主导` |
| [meeting-server](projects/opensourceways/meeting-server/summary.md) | *待补充* | `backend` `community` `shell` `团队主导` |
| [meeting-website](projects/opensourceways/meeting-website/summary.md) | *待补充* | `community` `frontend` `vue` `团队主导` |
| [message-bus-all](projects/opensourceways/message-bus-all/summary.md) | *待补充* | `messaging` `团队主导` |
| [message-collect](projects/opensourceways/message-collect/summary.md) | *待补充* | `go` `messaging` `团队主导` |
| [message-collect-cron](projects/opensourceways/message-collect-cron/summary.md) | *待补充* | `go` `messaging` `团队主导` |
| [message-collect-githook](projects/opensourceways/message-collect-githook/summary.md) | *待补充* | `go` `messaging` `团队主导` |
| [message-manager](projects/opensourceways/message-manager/summary.md) | Go · Gin（Web 框架）· GORM · PostgreSQL · Cassandra · Redis | `go` `messaging` `团队主导` |
| [message-manager-website](projects/opensourceways/message-manager-website/summary.md) | *待补充* | `frontend` `html` `messaging` `团队主导` |
| [message-push](projects/opensourceways/message-push/summary.md) | *待补充* | `go` `messaging` `团队主导` |
| [message-transfer](projects/opensourceways/message-transfer/summary.md) | *待补充* | `go` `messaging` `团队主导` |
| [mindspore-jenkins-repo](projects/opensourceways/mindspore-jenkins-repo/summary.md) | *待补充* | `ci-cd` `community` `html` `mindspore` `repo-management` `团队主导` |
| [mongodb-lib](projects/opensourceways/mongodb-lib/summary.md) | *待补充* | `go` `sdk` `团队主导` |
| [om-check](projects/opensourceways/om-check/summary.md) | *待补充* | `python` `团队主导` |
| [om-collection](projects/opensourceways/om-collection/summary.md) | *待补充* | `python` `团队主导` |
| [om-dataarts](projects/opensourceways/om-dataarts/summary.md) | Python · PostgreSQL（主存储）· psycopg2 · GitHub/Gitee/GitCode API · Jenkins（调度）· Docker | `data` `python` `团队主导` |
| [om-dataarts-back](projects/opensourceways/om-dataarts-back/summary.md) | *待补充* | `data` `python` `团队主导` |
| [om-dataarts-deployment](projects/opensourceways/om-dataarts-deployment/summary.md) | *待补充* | `data` `deploy` `python` `团队主导` |
| [om-datacenter](projects/opensourceways/om-datacenter/summary.md) | *待补充* | `data` `shell` `团队主导` |
| [om-deployment](projects/opensourceways/om-deployment/summary.md) | *待补充* | `deploy` `团队主导` |
| [om-kafka](projects/opensourceways/om-kafka/summary.md) | *待补充* | `java` `messaging` `团队主导` |
| [om-magicai](projects/opensourceways/om-magicai/summary.md) | *待补充* | `ai-agent` `java` `团队主导` |
| [om-search](projects/opensourceways/om-search/summary.md) | *待补充* | `团队主导` |
| [om-webserver](projects/opensourceways/om-webserver/summary.md) | *待补充* | `backend` `frontend` `java` `团队主导` |
| [oneid-all](projects/opensourceways/oneid-all/summary.md) | *待补充* | `ai-agent` `auth` `repo-management` `shell` `团队主导` |
| [oneid-server](projects/opensourceways/oneid-server/summary.md) | *待补充* | `auth` `backend` `java` `团队主导` |
| [oneid-website](projects/opensourceways/oneid-website/summary.md) | *待补充* | `auth` `frontend` `vue` `团队主导` |
| [oneid-workbench](projects/opensourceways/oneid-workbench/summary.md) | *待补充* | `auth` `java` `团队主导` |
| [oneid-workbench-website](projects/opensourceways/oneid-workbench-website/summary.md) | *待补充* | `auth` `frontend` `vue` `团队主导` |
| [openApiTest](projects/opensourceways/openApiTest/summary.md) | *待补充* | `backend` `python` `团队主导` |
| [OpenDesignPlus](projects/opensourceways/OpenDesignPlus/summary.md) | *待补充* | `团队主导` |
| [openeuler-images](projects/opensourceways/openeuler-images/summary.md) | *待补充* | `openeuler` `团队主导` |
| [openeuler-jenkins-repo](projects/opensourceways/openeuler-jenkins-repo/summary.md) | *待补充* | `ci-cd` `community` `openeuler` `repo-management` `团队主导` |
| [openeuler-sig-info-check](projects/opensourceways/openeuler-sig-info-check/summary.md) | *待补充* | `openeuler` `团队主导` |
| [openeuler-website-v2](projects/opensourceways/openeuler-website-v2/summary.md) | *待补充* | `frontend` `javascript` `openeuler` `团队主导` |
| [opengauss-jenkins-repo](projects/opensourceways/opengauss-jenkins-repo/summary.md) | *待补充* | `ci-cd` `community` `html` `opengauss` `repo-management` `团队主导` |
| [opengauss_infra](projects/opensourceways/opengauss_infra/summary.md) | *待补充* | `html` `opengauss` `团队主导` |
| [opengecko](projects/opensourceways/opengecko/summary.md) | *待补充* | `ai-agent` `python` `团队主导` |
| [openlookeng-jenkins-repo](projects/opensourceways/openlookeng-jenkins-repo/summary.md) | *待补充* | `ci-cd` `community` `html` `repo-management` `团队主导` |
| [opensource-radar-web](projects/opensourceways/opensource-radar-web/summary.md) | *待补充* | `frontend` `javascript` `observability` `团队主导` |
| [opensource101](projects/opensourceways/opensource101/summary.md) | *待补充* | `团队主导` |
| [opensourceway](projects/opensourceways/opensourceway/summary.md) | *待补充* | `html` `团队主导` |
| [opensourceways-repo-monitor](projects/opensourceways/opensourceways-repo-monitor/summary.md) | *待补充* | `observability` `python` `repo-management` `团队主导` |
| [openUBMC-portal](projects/opensourceways/openUBMC-portal/summary.md) | *待补充* | `css` `openubmc` `团队主导` |
| [ops-mgmt](projects/opensourceways/ops-mgmt/summary.md) | *待补充* | `security` `团队主导` |
| [osi-task-manager](projects/opensourceways/osi-task-manager/summary.md) | *待补充* | `go` `团队主导` |
| [osinfra-jenkins-repo](projects/opensourceways/osinfra-jenkins-repo/summary.md) | *待补充* | `ci-cd` `html` `repo-management` `团队主导` |
| [patch-manager](projects/opensourceways/patch-manager/summary.md) | *待补充* | `go` `团队主导` |
| [patch-manager-website](projects/opensourceways/patch-manager-website/summary.md) | *待补充* | `frontend` `团队主导` |
| [patchwork](projects/opensourceways/patchwork/summary.md) | *待补充* | `python` `团队主导` |
| [permission-manage-website](projects/opensourceways/permission-manage-website/summary.md) | *待补充* | `frontend` `团队主导` |
| [playground-app](projects/opensourceways/playground-app/summary.md) | *待补充* | `vue` `团队主导` |
| [playground-courses](projects/opensourceways/playground-courses/summary.md) | *待补充* | `团队主导` |
| [playground-images](projects/opensourceways/playground-images/summary.md) | *待补充* | `团队主导` |
| [playground-manager](projects/opensourceways/playground-manager/summary.md) | *待补充* | `go` `团队主导` |
| [pod_exporter_monitoring](projects/opensourceways/pod_exporter_monitoring/summary.md) | *待补充* | `observability` `python` `团队主导` |
| [portal-mcp-servers](projects/opensourceways/portal-mcp-servers/summary.md) | *待补充* | `backend` `javascript` `mcp` `团队主导` |
| [portal-workflow](projects/opensourceways/portal-workflow/summary.md) | *待补充* | `javascript` `workflow` `团队主导` |
| [postgresql-lib](projects/opensourceways/postgresql-lib/summary.md) | *待补充* | `sdk` `团队主导` |
| [pr-issue-report](projects/opensourceways/pr-issue-report/summary.md) | *待补充* | `ai-agent` `community` `python` `repo-management` `团队主导` |
| [public_issue](projects/opensourceways/public_issue/summary.md) | *待补充* | `团队主导` |
| [python-gitee](projects/opensourceways/python-gitee/summary.md) | *待补充* | `git-platform` `python` `团队主导` |
| [QA](projects/opensourceways/QA/summary.md) | *待补充* | `团队主导` |
| [rag-ci-deploy](projects/opensourceways/rag-ci-deploy/summary.md) | *待补充* | `ci-cd` `deploy` `python` `团队主导` |
| [redis-lib](projects/opensourceways/redis-lib/summary.md) | *待补充* | `go` `sdk` `团队主导` |
| [release-mgmt](projects/opensourceways/release-mgmt/summary.md) | *待补充* | `deploy` `python` `团队主导` |
| [repo-file-cache](projects/opensourceways/repo-file-cache/summary.md) | *待补充* | `go` `repo-management` `团队主导` |
| [repo-owners-cache](projects/opensourceways/repo-owners-cache/summary.md) | *待补充* | `go` `repo-management` `团队主导` |
| [reproducible-backend](projects/opensourceways/reproducible-backend/summary.md) | *待补充* | `backend` `ci-cd` `java` `团队主导` |
| [reproducible-builds-libfaketime](projects/opensourceways/reproducible-builds-libfaketime/summary.md) | *待补充* | `ci-cd` `frontend` `sdk` `团队主导` |
| [reproducible-website](projects/opensourceways/reproducible-website/summary.md) | *待补充* | `ci-cd` `frontend` `团队主导` |
| [RM-Check](projects/opensourceways/RM-Check/summary.md) | *待补充* | `python` `团队主导` |
| [robot-framework-lib](projects/opensourceways/robot-framework-lib/summary.md) | *待补充* | `bot` `go` `sdk` `团队主导` |
| [robot-gitcode-hook-delivery](projects/opensourceways/robot-gitcode-hook-delivery/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitcode-software-package](projects/opensourceways/robot-gitcode-software-package/summary.md) | *待补充* | `bot` `community` `git-platform` `go` `团队主导` |
| [robot-gitee-access](projects/opensourceways/robot-gitee-access/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-approve](projects/opensourceways/robot-gitee-approve/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-assign](projects/opensourceways/robot-gitee-assign/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-assign-issue](projects/opensourceways/robot-gitee-assign-issue/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-associate](projects/opensourceways/robot-gitee-associate/summary.md) | *待补充* | `bot` `ci-cd` `git-platform` `go` `团队主导` |
| [robot-gitee-checkpr](projects/opensourceways/robot-gitee-checkpr/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-cla](projects/opensourceways/robot-gitee-cla/summary.md) | *待补充* | `auth` `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-cve-issue-suspending-check](projects/opensourceways/robot-gitee-cve-issue-suspending-check/summary.md) | *待补充* | `bot` `git-platform` `go` `security` `团队主导` |
| [robot-gitee-hook-delivery](projects/opensourceways/robot-gitee-hook-delivery/summary.md) | *待补充* | `bot` `frontend` `git-platform` `go` `messaging` `团队主导` |
| [robot-gitee-hook-dispatcher](projects/opensourceways/robot-gitee-hook-dispatcher/summary.md) | *待补充* | `bot` `frontend` `git-platform` `go` `messaging` `团队主导` |
| [robot-gitee-keeper-approve](projects/opensourceways/robot-gitee-keeper-approve/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-label](projects/opensourceways/robot-gitee-label/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-lgtm](projects/opensourceways/robot-gitee-lgtm/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-lib](projects/opensourceways/robot-gitee-lib/summary.md) | *待补充* | `bot` `git-platform` `go` `sdk` `团队主导` |
| [robot-gitee-lifecycle](projects/opensourceways/robot-gitee-lifecycle/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-openeuler-responsible-guide](projects/opensourceways/robot-gitee-openeuler-responsible-guide/summary.md) | *待补充* | `bot` `frontend` `git-platform` `openeuler` `团队主导` |
| [robot-gitee-openeuler-review](projects/opensourceways/robot-gitee-openeuler-review/summary.md) | *待补充* | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-gitee-openeuler-upstream-monitor](projects/opensourceways/robot-gitee-openeuler-upstream-monitor/summary.md) | *待补充* | `bot` `git-platform` `java` `observability` `openeuler` `团队主导` |
| [robot-gitee-openeuler-welcome](projects/opensourceways/robot-gitee-openeuler-welcome/summary.md) | *待补充* | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-gitee-opengauss-review](projects/opensourceways/robot-gitee-opengauss-review/summary.md) | *待补充* | `bot` `git-platform` `go` `opengauss` `团队主导` |
| [robot-gitee-opengauss-sigguide](projects/opensourceways/robot-gitee-opengauss-sigguide/summary.md) | *待补充* | `bot` `frontend` `git-platform` `opengauss` `团队主导` |
| [robot-gitee-owners-monitor](projects/opensourceways/robot-gitee-owners-monitor/summary.md) | *待补充* | `bot` `git-platform` `observability` `团队主导` |
| [robot-gitee-python-lib](projects/opensourceways/robot-gitee-python-lib/summary.md) | *待补充* | `bot` `git-platform` `python` `sdk` `团队主导` |
| [robot-gitee-repo-watcher](projects/opensourceways/robot-gitee-repo-watcher/summary.md) | *待补充* | `bot` `git-platform` `go` `repo-management` `团队主导` |
| [robot-gitee-review-trigger](projects/opensourceways/robot-gitee-review-trigger/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-scavenger](projects/opensourceways/robot-gitee-scavenger/summary.md) | *待补充* | `bot` `data` `git-platform` `go` `团队主导` |
| [robot-gitee-size](projects/opensourceways/robot-gitee-size/summary.md) | *待补充* | `bot` `git-platform` `团队主导` |
| [robot-gitee-software-package](projects/opensourceways/robot-gitee-software-package/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-sweepstakes](projects/opensourceways/robot-gitee-sweepstakes/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-synchronizer](projects/opensourceways/robot-gitee-synchronizer/summary.md) | *待补充* | `bot` `git-platform` `go` `observability` `repo-management` `团队主导` |
| [robot-gitee-tech4dx-label](projects/opensourceways/robot-gitee-tech4dx-label/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-gitee-tide](projects/opensourceways/robot-gitee-tide/summary.md) | *待补充* | `bot` `git-platform` `团队主导` |
| [robot-gitee-version-freezer](projects/opensourceways/robot-gitee-version-freezer/summary.md) | *待补充* | `bot` `git-platform` `团队主导` |
| [robot-gitee-welcome](projects/opensourceways/robot-gitee-welcome/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-github-access](projects/opensourceways/robot-github-access/summary.md) | *待补充* | `bot` `git-platform` `go` `团队主导` |
| [robot-github-cla](projects/opensourceways/robot-github-cla/summary.md) | *待补充* | `auth` `bot` `git-platform` `go` `团队主导` |
| [robot-github-hook-delivery](projects/opensourceways/robot-github-hook-delivery/summary.md) | *待补充* | `bot` `frontend` `git-platform` `go` `messaging` `团队主导` |
| [robot-github-hook-dispatcher](projects/opensourceways/robot-github-hook-dispatcher/summary.md) | *待补充* | `bot` `ci-cd` `frontend` `git-platform` `go` `messaging` `团队主导` |
| [robot-github-lib](projects/opensourceways/robot-github-lib/summary.md) | *待补充* | `bot` `git-platform` `go` `sdk` `团队主导` |
| [robot-github-openeuler-assign](projects/opensourceways/robot-github-openeuler-assign/summary.md) | *待补充* | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-github-openeuler-label](projects/opensourceways/robot-github-openeuler-label/summary.md) | *待补充* | `bot` `git-platform` `openeuler` `团队主导` |
| [robot-github-openeuler-lifecycle](projects/opensourceways/robot-github-openeuler-lifecycle/summary.md) | *待补充* | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-github-openeuler-repo-watcher](projects/opensourceways/robot-github-openeuler-repo-watcher/summary.md) | *待补充* | `bot` `git-platform` `go` `openeuler` `repo-management` `团队主导` |
| [robot-github-openeuler-review](projects/opensourceways/robot-github-openeuler-review/summary.md) | *待补充* | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-github-openeuler-welcome](projects/opensourceways/robot-github-openeuler-welcome/summary.md) | *待补充* | `bot` `git-platform` `go` `openeuler` `团队主导` |
| [robot-github-synchronizer](projects/opensourceways/robot-github-synchronizer/summary.md) | *待补充* | `bot` `git-platform` `go` `observability` `repo-management` `团队主导` |
| [robot-gitlab-access](projects/opensourceways/robot-gitlab-access/summary.md) | *待补充* | `bot` `go` `团队主导` |
| [robot-gitlab-label](projects/opensourceways/robot-gitlab-label/summary.md) | *待补充* | `bot` `团队主导` |
| [robot-gitlab-lib](projects/opensourceways/robot-gitlab-lib/summary.md) | *待补充* | `bot` `go` `sdk` `团队主导` |
| [robot-gitlab-repo-watcher](projects/opensourceways/robot-gitlab-repo-watcher/summary.md) | *待补充* | `bot` `go` `repo-management` `团队主导` |
| [robot-gitlab-review](projects/opensourceways/robot-gitlab-review/summary.md) | *待补充* | `bot` `go` `团队主导` |
| [robot-gitlab-sync-repo](projects/opensourceways/robot-gitlab-sync-repo/summary.md) | *待补充* | `bot` `go` `repo-management` `团队主导` |
| [robot-gitlab-welcome](projects/opensourceways/robot-gitlab-welcome/summary.md) | *待补充* | `bot` `go` `团队主导` |
| [robot-hook-dispatcher](projects/opensourceways/robot-hook-dispatcher/summary.md) | *待补充* | `bot` `go` `团队主导` |
| [robot-issue-manage](projects/opensourceways/robot-issue-manage/summary.md) | *待补充* | `bot` `community` `git-platform` `python` `workflow` `团队主导` |
| [robot-openeuler-ci-tools](projects/opensourceways/robot-openeuler-ci-tools/summary.md) | *待补充* | `bot` `ci-cd` `cli` `openeuler` `python` `团队主导` |
| [robot-plugin-syncfile](projects/opensourceways/robot-plugin-syncfile/summary.md) | *待补充* | `bot` `repo-management` `团队主导` |
| [robot-tools](projects/opensourceways/robot-tools/summary.md) | *待补充* | `ai-agent` `bot` `cli` `data` `deploy` `git-platform` `python` `workflow` `团队主导` |
| [robot-universal-access](projects/opensourceways/robot-universal-access/summary.md) | *待补充* | `bot` `community` `go` `团队主导` |
| [robot-universal-agreements](projects/opensourceways/robot-universal-agreements/summary.md) | *待补充* | `bot` `go` `团队主导` |
| [robot-universal-assign](projects/opensourceways/robot-universal-assign/summary.md) | *待补充* | `bot` `community` `go` `团队主导` |
| [robot-universal-associate](projects/opensourceways/robot-universal-associate/summary.md) | *待补充* | `bot` `ci-cd` `community` `go` `团队主导` |
| [robot-universal-cache](projects/opensourceways/robot-universal-cache/summary.md) | *待补充* | `bot` `community` `团队主导` |
| [robot-universal-ci-tools](projects/opensourceways/robot-universal-ci-tools/summary.md) | *待补充* | `bot` `ci-cd` `cli` `python` `团队主导` |
| [robot-universal-cla](projects/opensourceways/robot-universal-cla/summary.md) | *待补充* | `auth` `bot` `community` `go` `团队主导` |
| [robot-universal-comment](projects/opensourceways/robot-universal-comment/summary.md) | *待补充* | `bot` `community` `go` `团队主导` |
| [robot-universal-hook-delivery](projects/opensourceways/robot-universal-hook-delivery/summary.md) | *待补充* | `bot` `frontend` `go` `messaging` `团队主导` |
| [robot-universal-issue-workflow](projects/opensourceways/robot-universal-issue-workflow/summary.md) | *待补充* | `bot` `go` `workflow` `团队主导` |
| [robot-universal-label](projects/opensourceways/robot-universal-label/summary.md) | *待补充* | `bot` `community` `go` `团队主导` |
| [robot-universal-lifecycle](projects/opensourceways/robot-universal-lifecycle/summary.md) | *待补充* | `bot` `community` `go` `团队主导` |
| [robot-universal-quality-gate-trigger](projects/opensourceways/robot-universal-quality-gate-trigger/summary.md) | *待补充* | `bot` `ci-cd` `cli` `community` `go` `repo-management` `团队主导` |
| [robot-universal-repo-watcher](projects/opensourceways/robot-universal-repo-watcher/summary.md) | *待补充* | `bot` `community` `go` `repo-management` `团队主导` |
| [robot-universal-review](projects/opensourceways/robot-universal-review/summary.md) | *待补充* | `bot` `community` `go` `团队主导` |
| [robot-universal-scavenger](projects/opensourceways/robot-universal-scavenger/summary.md) | *待补充* | `bot` `go` `observability` `团队主导` |
| [robot-universal-welcome](projects/opensourceways/robot-universal-welcome/summary.md) | *待补充* | `bot` `community` `go` `团队主导` |
| [sbom-deploy](projects/opensourceways/sbom-deploy/summary.md) | *待补充* | `deploy` `docker` `团队主导` |
| [sbom-repo-service](projects/opensourceways/sbom-repo-service/summary.md) | *待补充* | `java` `repo-management` `团队主导` |
| [sbom-service](projects/opensourceways/sbom-service/summary.md) | *待补充* | `java` `团队主导` |
| [sbom-tools](projects/opensourceways/sbom-tools/summary.md) | *待补充* | `cli` `团队主导` |
| [sbom-website](projects/opensourceways/sbom-website/summary.md) | *待补充* | `frontend` `vue` `团队主导` |
| [search-all](projects/opensourceways/search-all/summary.md) | *待补充* | `团队主导` |
| [security-cve-all](projects/opensourceways/security-cve-all/summary.md) | *待补充* | `security` `shell` `团队主导` |
| [server-common-lib](projects/opensourceways/server-common-lib/summary.md) | *待补充* | `backend` `go` `sdk` `团队主导` |
| [sig-miniprogram](projects/opensourceways/sig-miniprogram/summary.md) | *待补充* | `javascript` `团队主导` |
| [smart_tools](projects/opensourceways/smart_tools/summary.md) | *待补充* | `cli` `python` `团队主导` |
| [software-package-all](projects/opensourceways/software-package-all/summary.md) | *待补充* | `团队主导` |
| [software-package-gateway](projects/opensourceways/software-package-gateway/summary.md) | *待补充* | `backend` `go` `团队主导` |
| [software-package-github-server](projects/opensourceways/software-package-github-server/summary.md) | *待补充* | `backend` `git-platform` `go` `团队主导` |
| [software-package-server](projects/opensourceways/software-package-server/summary.md) | *待补充* | `backend` `go` `团队主导` |
| [software-package-sync-pr](projects/opensourceways/software-package-sync-pr/summary.md) | *待补充* | `go` `repo-management` `团队主导` |
| [software-package-sync-repo](projects/opensourceways/software-package-sync-repo/summary.md) | *待补充* | `go` `repo-management` `团队主导` |
| [software-package-website](projects/opensourceways/software-package-website/summary.md) | *待补充* | `frontend` `vue` `团队主导` |
| [space-k8s-operator](projects/opensourceways/space-k8s-operator/summary.md) | *待补充* | `go` `kubernetes` `团队主导` |
| [space-server](projects/opensourceways/space-server/summary.md) | *待补充* | `backend` `go` `团队主导` |
| [space-server-monitor](projects/opensourceways/space-server-monitor/summary.md) | *待补充* | `backend` `go` `observability` `团队主导` |
| [study](projects/opensourceways/study/summary.md) | *待补充* | `团队主导` |
| [sync-agent](projects/opensourceways/sync-agent/summary.md) | *待补充* | `ai-agent` `backend` `git-platform` `go` `repo-management` `团队主导` |
| [sync-bot](projects/opensourceways/sync-bot/summary.md) | *待补充* | `go` `repo-management` `团队主导` |
| [sync-file-server](projects/opensourceways/sync-file-server/summary.md) | *待补充* | `backend` `go` `repo-management` `团队主导` |
| [sync-mirror-repos](projects/opensourceways/sync-mirror-repos/summary.md) | *待补充* | `git-platform` `python` `repo-management` `团队主导` |
| [sync-model-openpangu](projects/opensourceways/sync-model-openpangu/summary.md) | *待补充* | `llm` `python` `repo-management` `团队主导` |
| [sync-repo-file](projects/opensourceways/sync-repo-file/summary.md) | *待补充* | `go` `repo-management` `团队主导` |
| [sync-repo-file-job](projects/opensourceways/sync-repo-file-job/summary.md) | *待补充* | `repo-management` `团队主导` |
| [sync-repository-file](projects/opensourceways/sync-repository-file/summary.md) | *待补充* | `go` `repo-management` `团队主导` |
| [test](projects/opensourceways/test/summary.md) | *待补充* | `团队主导` |
| [test-infra](projects/opensourceways/test-infra/summary.md) | *待补充* | `go` `kubernetes` `团队主导` |
| [test-pub](projects/opensourceways/test-pub/summary.md) | *待补充* | `团队主导` |
| [test1](projects/opensourceways/test1/summary.md) | *待补充* | `团队主导` |
| [tools-collection](projects/opensourceways/tools-collection/summary.md) | *待补充* | `cli` `shell` `团队主导` |
| [translator](projects/opensourceways/translator/summary.md) | *待补充* | `cli` `python` `repo-management` `团队主导` |
| [ttfhw](projects/opensourceways/ttfhw/summary.md) | *待补充* | `python` `团队主导` |
| [ttfhw-backup](projects/opensourceways/ttfhw-backup/summary.md) | *待补充* | `python` `团队主导` |
| [uvp](projects/opensourceways/uvp/summary.md) | *待补充* | `java` `security` `团队主导` |
| [uvp-website](projects/opensourceways/uvp-website/summary.md) | *待补充* | `frontend` `security` `vue` `团队主导` |
| [vLLM-dashboard-website](projects/opensourceways/vLLM-dashboard-website/summary.md) | *待补充* | `frontend` `llm` `vllm` `vue` `团队主导` |
| [vscode-doc-tools](projects/opensourceways/vscode-doc-tools/summary.md) | *待补充* | `cli` `typescript` `团队主导` |
| [vscode-portal-cms](projects/opensourceways/vscode-portal-cms/summary.md) | *待补充* | `vue` `团队主导` |
| [whitebox](projects/opensourceways/whitebox/summary.md) | *待补充* | `python` `团队主导` |
| [workflow-control-tower](projects/opensourceways/workflow-control-tower/summary.md) | *待补充* | `ai-agent` `repo-management` `shell` `workflow` `团队主导` |
| [xihe-aicc-finetune](projects/opensourceways/xihe-aicc-finetune/summary.md) | *待补充* | `ai-agent` `go` `xihe` `团队主导` |
| [xihe-all](projects/opensourceways/xihe-all/summary.md) | *待补充* | `shell` `xihe` `团队主导` |
| [xihe-audit-sdk](projects/opensourceways/xihe-audit-sdk/summary.md) | *待补充* | `observability` `sdk` `xihe` `团队主导` |
| [xihe-audit-server](projects/opensourceways/xihe-audit-server/summary.md) | *待补充* | `backend` `go` `observability` `xihe` `团队主导` |
| [xihe-audit-sync-sdk](projects/opensourceways/xihe-audit-sync-sdk/summary.md) | *待补充* | `go` `observability` `repo-management` `sdk` `xihe` `团队主导` |
| [xihe-cronjob](projects/opensourceways/xihe-cronjob/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-docs](projects/opensourceways/xihe-docs/summary.md) | *待补充* | `typescript` `xihe` `团队主导` |
| [xihe-extra-services](projects/opensourceways/xihe-extra-services/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-finetune](projects/opensourceways/xihe-finetune/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-git-access](projects/opensourceways/xihe-git-access/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-git-access-sdk](projects/opensourceways/xihe-git-access-sdk/summary.md) | *待补充* | `go` `sdk` `xihe` `团队主导` |
| [xihe-git-hook-delivery](projects/opensourceways/xihe-git-hook-delivery/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-gitea](projects/opensourceways/xihe-gitea/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-gitea-sdk](projects/opensourceways/xihe-gitea-sdk/summary.md) | *待补充* | `go` `sdk` `xihe` `团队主导` |
| [xihe-gitlab-hook-delivery](projects/opensourceways/xihe-gitlab-hook-delivery/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-grpc-protocol](projects/opensourceways/xihe-grpc-protocol/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-image-build](projects/opensourceways/xihe-image-build/summary.md) | *待补充* | `frontend` `html` `xihe` `团队主导` |
| [xihe-internal-server](projects/opensourceways/xihe-internal-server/summary.md) | *待补充* | `backend` `go` `xihe` `团队主导` |
| [xihe-jupyter-server](projects/opensourceways/xihe-jupyter-server/summary.md) | *待补充* | `backend` `go` `xihe` `团队主导` |
| [xihe-message-server](projects/opensourceways/xihe-message-server/summary.md) | *待补充* | `backend` `go` `messaging` `xihe` `团队主导` |
| [xihe-resource-script](projects/opensourceways/xihe-resource-script/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-script](projects/opensourceways/xihe-script/summary.md) | *待补充* | `go` `xihe` `团队主导` |
| [xihe-sdk](projects/opensourceways/xihe-sdk/summary.md) | *待补充* | `go` `sdk` `xihe` `团队主导` |
| [xihe-server](projects/opensourceways/xihe-server/summary.md) | *待补充* | `backend` `go` `xihe` `团队主导` |
| [xihe-sop](projects/opensourceways/xihe-sop/summary.md) | *待补充* | `xihe` `团队主导` |
| [xihe-statistics](projects/opensourceways/xihe-statistics/summary.md) | *待补充* | `data` `go` `xihe` `团队主导` |
| [xihe-sync-repo](projects/opensourceways/xihe-sync-repo/summary.md) | *待补充* | `go` `repo-management` `xihe` `团队主导` |
| [xihe-training-center](projects/opensourceways/xihe-training-center/summary.md) | *待补充* | `ai-agent` `go` `xihe` `团队主导` |
| [xihe-website](projects/opensourceways/xihe-website/summary.md) | *待补充* | `frontend` `vue` `xihe` `团队主导` |
| [xihe-website-v2](projects/opensourceways/xihe-website-v2/summary.md) | *待补充* | `frontend` `vue` `xihe` `团队主导` |
| [yabot](projects/opensourceways/yabot/summary.md) | *待补充* | `go` `repo-management` `团队主导` |

## 🔬 COSDT
*23 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [ci-infra](projects/cosdt/ci-infra/summary.md) | *待补充* | `ci-cd` `python` `团队主导` |
| [cosdt.github.io](projects/cosdt/cosdt.github.io/summary.md) | *待补充* | `git-platform` `html` `团队主导` |
| [dockerfiles](projects/cosdt/dockerfiles/summary.md) | *待补充* | `docker` `团队主导` |
| [DownStream1](projects/cosdt/DownStream1/summary.md) | *待补充* | `团队主导` |
| [DownStream2](projects/cosdt/DownStream2/summary.md) | *待补充* | `团队主导` |
| [elastic-tool](projects/cosdt/elastic-tool/summary.md) | *待补充* | `cli` `elasticsearch` `python` `团队主导` |
| [llama.cpp](projects/cosdt/llama.cpp/summary.md) | *待补充* | `llm` `shell` `团队主导` |
| [onnxruntime](projects/cosdt/onnxruntime/summary.md) | *待补充* | `onnx` `shell` `团队主导` |
| [op-plugin](projects/cosdt/op-plugin/summary.md) | *待补充* | `ascend` `cpp` `npu` `pytorch` `团队主导` |
| [openeuler-keynote-2020](projects/cosdt/openeuler-keynote-2020/summary.md) | *待补充* | `openeuler` `repo-management` `shell` `团队主导` |
| [oss-map](projects/cosdt/oss-map/summary.md) | *待补充* | `python` `团队主导` |
| [pytorch](projects/cosdt/pytorch/summary.md) | *待补充* | `jupyter` `pytorch` `团队主导` |
| [pytorch-integration-tests](projects/cosdt/pytorch-integration-tests/summary.md) | *待补充* | `python` `pytorch` `团队主导` |
| [PyTorchInsight](projects/cosdt/PyTorchInsight/summary.md) | *待补充* | `community` `data` `python` `pytorch` `团队主导` |
| [skills](projects/cosdt/skills/summary.md) | *待补充* | `ai-agent` `cli` `python` `团队主导` |
| [test-infra](projects/cosdt/test-infra/summary.md) | *待补充* | `typescript` `团队主导` |
| [torch_backend](projects/cosdt/torch_backend/summary.md) | *待补充* | `ascend` `backend` `cpp` `npu` `pytorch` `团队主导` |
| [torchcomms-bak](projects/cosdt/torchcomms-bak/summary.md) | *待补充* | `cpp` `pytorch` `团队主导` |
| [triton-ascend](projects/cosdt/triton-ascend/summary.md) | *待补充* | `ascend` `compiler` `cpp` `npu` `triton` `团队主导` |
| [UpStream](projects/cosdt/UpStream/summary.md) | *待补充* | `团队主导` |
| [vllm-ascend](projects/cosdt/vllm-ascend/summary.md) | *待补充* | `ascend` `ci-cd` `git-platform` `llm` `python` `vllm` `团队主导` |
| [vllm-ascend-integration-ci](projects/cosdt/vllm-ascend-integration-ci/summary.md) | *待补充* | `ascend` `ci-cd` `llm` `python` `vllm` `团队主导` |
| [vllm-benchmarks](projects/cosdt/vllm-benchmarks/summary.md) | *待补充* | `llm` `python` `vllm` `团队主导` |

## 🚀 vLLM Project
*39 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [agentic-api](projects/vllm-project/agentic-api/summary.md) | *待补充* | `上游贡献` |
| [aibrix](projects/vllm-project/aibrix/summary.md) | *待补充* | `上游贡献` |
| [bart-plugin](projects/vllm-project/bart-plugin/summary.md) | *待补充* | `上游贡献` |
| [ci-infra](projects/vllm-project/ci-infra/summary.md) | *待补充* | `上游贡献` |
| [compressed-tensors](projects/vllm-project/compressed-tensors/summary.md) | *待补充* | `上游贡献` |
| [dllm-plugin](projects/vllm-project/dllm-plugin/summary.md) | *待补充* | `上游贡献` |
| [guidellm](projects/vllm-project/guidellm/summary.md) | *待补充* | `上游贡献` |
| [llm-compressor](projects/vllm-project/llm-compressor/summary.md) | *待补充* | `上游贡献` |
| [llm-multimodal](projects/vllm-project/llm-multimodal/summary.md) | *待补充* | `上游贡献` |
| [media-kit](projects/vllm-project/media-kit/summary.md) | *待补充* | `上游贡献` |
| [perf-dashboard](projects/vllm-project/perf-dashboard/summary.md) | *待补充* | `上游贡献` |
| [perf-eval](projects/vllm-project/perf-eval/summary.md) | *待补充* | `上游贡献` |
| [production-stack](projects/vllm-project/production-stack/summary.md) | *待补充* | `上游贡献` |
| [recipes](projects/vllm-project/recipes/summary.md) | *待补充* | `上游贡献` |
| [rfcs](projects/vllm-project/rfcs/summary.md) | *待补充* | `上游贡献` |
| [router](projects/vllm-project/router/summary.md) | *待补充* | `上游贡献` |
| [semantic-router](projects/vllm-project/semantic-router/summary.md) | *待补充* | `上游贡献` |
| [speculators](projects/vllm-project/speculators/summary.md) | *待补充* | `上游贡献` |
| [tpu-inference](projects/vllm-project/tpu-inference/summary.md) | *待补充* | `上游贡献` |
| [vime](projects/vllm-project/vime/summary.md) | *待补充* | `上游贡献` |
| [vllm](projects/vllm-project/vllm/summary.md) | Python · PyTorch（主力框架）· CUDA/ROCm（GPU kernel）· CUTLASS/Triton（GEMM/MoE kernel） | `continuous-batching` `pagedattention` `vllm` `上游贡献` `推理` |
| [vllm-ascend](projects/vllm-project/vllm-ascend/summary.md) | *待补充* | `ascend` `npu` `vllm` `上游贡献` |
| [vllm-bench](projects/vllm-project/vllm-bench/summary.md) | *待补充* | `上游贡献` |
| [vllm-bnb-plugin](projects/vllm-project/vllm-bnb-plugin/summary.md) | *待补充* | `上游贡献` |
| [vllm-daily](projects/vllm-project/vllm-daily/summary.md) | *待补充* | `上游贡献` |
| [vllm-dashboard](projects/vllm-project/vllm-dashboard/summary.md) | *待补充* | `上游贡献` |
| [vllm-docs](projects/vllm-project/vllm-docs/summary.md) | *待补充* | `上游贡献` |
| [vllm-gaudi](projects/vllm-project/vllm-gaudi/summary.md) | *待补充* | `上游贡献` |
| [vllm-gguf-plugin](projects/vllm-project/vllm-gguf-plugin/summary.md) | *待补充* | `上游贡献` |
| [vLLM-in-PyTorch-Conference-2025](projects/vllm-project/vLLM-in-PyTorch-Conference-2025/summary.md) | *待补充* | `上游贡献` |
| [vllm-metal](projects/vllm-project/vllm-metal/summary.md) | *待补充* | `上游贡献` |
| [vllm-nccl](projects/vllm-project/vllm-nccl/summary.md) | *待补充* | `上游贡献` |
| [vllm-neuron](projects/vllm-project/vllm-neuron/summary.md) | *待补充* | `上游贡献` |
| [vllm-omni](projects/vllm-project/vllm-omni/summary.md) | *待补充* | `上游贡献` |
| [vllm-openvino](projects/vllm-project/vllm-openvino/summary.md) | *待补充* | `上游贡献` |
| [vllm-project.github.io](projects/vllm-project/vllm-project.github.io/summary.md) | *待补充* | `上游贡献` |
| [vllm-project.github.io-static](projects/vllm-project/vllm-project.github.io-static/summary.md) | *待补充* | `上游贡献` |
| [vllm-skills](projects/vllm-project/vllm-skills/summary.md) | *待补充* | `上游贡献` |
| [vllm-xpu-kernels](projects/vllm-project/vllm-xpu-kernels/summary.md) | *待补充* | `上游贡献` |

## ⚡ SGL Project
*22 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [ci-data](projects/sgl-project/ci-data/summary.md) | *待补充* | `上游贡献` |
| [cuLA](projects/sgl-project/cuLA/summary.md) | *待补充* | `上游贡献` |
| [genai-bench](projects/sgl-project/genai-bench/summary.md) | *待补充* | `上游贡献` |
| [mini-sglang](projects/sgl-project/mini-sglang/summary.md) | *待补充* | `上游贡献` |
| [ome-crd](projects/sgl-project/ome-crd/summary.md) | *待补充* | `上游贡献` |
| [rbg](projects/sgl-project/rbg/summary.md) | *待补充* | `上游贡献` |
| [rbg-api](projects/sgl-project/rbg-api/summary.md) | *待补充* | `上游贡献` |
| [sgl-cookbook](projects/sgl-project/sgl-cookbook/summary.md) | *待补充* | `上游贡献` |
| [sgl-docs](projects/sgl-project/sgl-docs/summary.md) | *待补充* | `上游贡献` |
| [sgl-eval](projects/sgl-project/sgl-eval/summary.md) | *待补充* | `上游贡献` |
| [sgl-kernel-npu](projects/sgl-project/sgl-kernel-npu/summary.md) | *待补充* | `ascend` `npu` `sglang` `上游贡献` |
| [sgl-kernel-xpu](projects/sgl-project/sgl-kernel-xpu/summary.md) | *待补充* | `上游贡献` |
| [sgl-learning-materials](projects/sgl-project/sgl-learning-materials/summary.md) | *待补充* | `上游贡献` |
| [sgl-project.github.io](projects/sgl-project/sgl-project.github.io/summary.md) | *待补充* | `上游贡献` |
| [sgl-test-files](projects/sgl-project/sgl-test-files/summary.md) | *待补充* | `上游贡献` |
| [sgl-whl](projects/sgl-project/sgl-whl/summary.md) | *待补充* | `上游贡献` |
| [sglang](projects/sgl-project/sglang/summary.md) | *待补充* | `radix-attention` `sglang` `structured-generation` `上游贡献` `推理` |
| [sglang-ci-stats](projects/sgl-project/sglang-ci-stats/summary.md) | *待补充* | `上游贡献` |
| [sglang-jax](projects/sgl-project/sglang-jax/summary.md) | *待补充* | `上游贡献` |
| [sglang-omni](projects/sgl-project/sglang-omni/summary.md) | *待补充* | `上游贡献` |
| [SpecForge](projects/sgl-project/SpecForge/summary.md) | *待补充* | `上游贡献` |
| [whl](projects/sgl-project/whl/summary.md) | *待补充* | `上游贡献` |

## 🔺 Triton Lang
*5 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [kernels](projects/triton-lang/kernels/summary.md) | *待补充* | `上游贡献` |
| [triton](projects/triton-lang/triton/summary.md) | *待补充* | `compiler` `gpu` `mlir` `triton` `上游贡献` |
| [triton-ascend](projects/triton-lang/triton-ascend/summary.md) | *待补充* | `ascend` `compiler` `npu` `triton` `上游贡献` |
| [triton-ext](projects/triton-lang/triton-ext/summary.md) | *待补充* | `上游贡献` |
| [Triton-to-tile-IR](projects/triton-lang/Triton-to-tile-IR/summary.md) | *待补充* | `上游贡献` |

## 🔥 PyTorch
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

## 🧩 Tile-AI
*6 projects*

| 项目 | 摘要 | 标签 |
|------|------|------|
| [tilelang](projects/tile-ai/tilelang/summary.md) | Python, C++, MLIR, CUDA, TVM | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tilelang-ascend](projects/tile-ai/tilelang-ascend/summary.md) | Python, C++, CANN, Ascend NPU | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tilelang-metax](projects/tile-ai/tilelang-metax/summary.md) | Python, C++, Metax SDK | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tilelang-mlir-ascend](projects/tile-ai/tilelang-mlir-ascend/summary.md) | MLIR, C++, Python, CANN | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tilelang-musa](projects/tile-ai/tilelang-musa/summary.md) | Python, C++, MUSA SDK | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |
| [tvm](projects/tile-ai/tvm/summary.md) | C++, Python, MLIR, CUDA, ROCm | `tilelang` `compiler` `dsl` `gpu` `上游贡献` |

## 📚 References
*11 papers*

| 引用 | 标题 | 年份 |
|------|------|------|
| [areal](references/antgroup/areal/summary.md) | 2505.24298 | 2025 |
| [dapo](references/bytedance/dapo/summary.md) | 2410.06584 | 2025 |
| [deepseek-r1](references/deepseek/deepseek-r1/summary.md) | 2501.12948 | 2025 |
| [deepseekmath](references/deepseek/deepseekmath/summary.md) | 2402.03300 | 2024 |
| [firecracker](references/firecracker-microvm/firecracker/summary.md) | - | - |
| [milvus](references/milvus-io/milvus/summary.md) | - | - |
| [rl-llm-survey](references/misc/rl-llm-survey/summary.md) | 2407.16216 | 2024 |
| [sglang](references/sgl-project/sglang/summary.md) | - | - |
| [dpo](references/stanford/dpo/summary.md) | 2305.18290 | 2023 |
| [triton](references/triton-lang/triton/summary.md) | - | - |
| [pagedattention](references/vllm-project/pagedattention/summary.md) | - | - |

---
> 🤖 本文件由 KG Agent 自动维护。操作日志见 [kg-log.md](kg-log.md) · 质检见 `/kg-lint`