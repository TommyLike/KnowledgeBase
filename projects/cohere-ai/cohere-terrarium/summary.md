# cohere-terrarium

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

Terrarium 是 Cohere 开源的一个轻量级 Python 代码沙箱，专为 LLM 数据 Agent 场景设计。在我们的知识图谱中归类为 agent-runtime/sandbox，属于上游贡献项目。它为 LLM Agent 提供安全隔离的 Python 执行环境，支撑代码生成、数据分析和自动化工作流等场景。

## 项目介绍

Terrarium 提供了一个简单、安全的 Python 沙箱执行环境，允许 LLM Agent 在隔离容器中运行任意 Python 代码。它基于 Docker 容器技术实现进程级隔离，支持 Pyodide（浏览器端 Python）和 Docker 两种运行时后端，兼顾安全性与灵活性。项目定位为"helpful LLM data agents"的基础设施组件，让 Agent 能够安全地执行数据分析、文件处理和代码生成任务。

## 核心场景

- **LLM Agent 代码执行**：Agent 生成 Python 代码后，在 Terrarium 沙箱中安全执行，获取运行结果返回给 Agent，避免对宿主环境造成影响。
- **数据分析 Agent**：LLM 驱动的数据分析场景中，Agent 编写 pandas/numpy 数据处理脚本，在沙箱中执行并获取分析结果。
- **多语言数据 Agent**：Terrarium 不仅限于 Python，还支持通过不同基础镜像扩展到其他语言运行时，满足多语言数据处理需求。
- **浏览器端沙箱**：通过 Pyodide 后端，Terrarium 可以在浏览器中直接运行 Python 代码，无需后端服务，适用于纯前端 Agent 场景。

## 技术要点

- **双重运行时架构**：支持 Docker 容器隔离和 Pyodide（WebAssembly Python）两种执行后端。Docker 提供强隔离，Pyodide 提供零服务端依赖的浏览器内执行能力。
- **安全隔离机制**：基于 Docker 容器的网络隔离、资源限制（CPU/内存）、文件系统隔离和超时控制，防止恶意代码逃逸或资源滥用。
- **镜像定制能力**：支持自定义 Docker 基础镜像，用户可通过提供自定义 Dockerfile 预装特定 Python 包（如 pandas、numpy、matplotlib），满足不同 Agent 场景的依赖需求。
- **异步执行模式**：提供异步代码提交和执行接口，支持 Agent 并行提交多个代码片段，提高数据处理吞吐量。
- **HTTP API 接口**：提供简洁的 REST API（`/run` 端点），Agent 可通过 HTTP POST 提交代码并获取 stdout/stderr 和执行结果。
- **轻量化设计**：代码库精简易读，核心逻辑集中在少数几个 Python 文件中，部署门槛低，适合快速集成到 Agent 框架中。

## 技术栈

- **语言**：Python（核心运行时 + HTTP 服务）
- **容器**：Docker（生产级隔离后端）
- **浏览器运行时**：Pyodide / WebAssembly
- **Web 框架**：FastAPI（HTTP API 层）
- **异步**：Python asyncio

## 关联

- **上游依赖**：Docker Engine、Pyodide
- **同类项目**：OpenAI Code Interpreter、E2B Sandbox、aigem/agent-sandbox（Codebox）、rayonapp/rayon-code-interpreter
- **下游集成**：可集成到 LangChain、LlamaIndex、CrewAI 等 Agent 框架中作为代码执行后端

## 开放问题

- 相比 E2B 等商业沙箱方案，Terrarium 的安全隔离粒度是否足够应对生产环境中的对抗性攻击？
- Pyodide 后端在浏览器环境中执行 Python 代码时，对第三方 C 扩展包的支持有限，如何覆盖更多数据分析依赖？
- Terrarium 目前缺少对执行结果的结构化数据回传（如 DataFrame 序列化）的内置支持，Agent 集成时需要额外封装。
- 项目的社区活跃度和维护频率相对较低（~300 stars），长期可持续性需要关注。
