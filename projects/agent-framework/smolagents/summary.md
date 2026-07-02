# smolagents

> [`huggingface/smolagents`](https://github.com/huggingface/smolagents) · 上游贡献 · Hugging Face 出品的轻量级代码执行型 AI Agent 框架，核心逻辑仅约一千行代码

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh
<!-- END AUTO -->

---

## 定位
> smolagents 是 Hugging Face 官方推出的极简 Agent 框架，在 Agent 框架生态中占据"轻量但可用生产"的独特定位。其核心差异化在于 **Code-as-Action 范式**——Agent 不输出 JSON 工具调用，而是直接生成并执行 Python 代码片段，将控制流（循环、条件分支）与多工具调用融合在单次生成中，相比传统 JSON-based 方案减少约 30% 的 LLM 调用步数。作为模型无关框架，它向上对接 HuggingFace Hub 模型生态和 LiteLLM 多提供商支持，向下提供 E2B/Docker 沙箱安全执行，是研究 Agent 代码执行范式和快速构建 Agent 原型的理想选择。

## 项目介绍
> **一个让 AI Agent "用代码思考"的极简框架：Agent 不再输出工具调用 JSON，而是直接写 Python 代码来完成任务。**

核心场景：
- **Agent 原型快速构建**：核心逻辑仅约 1000 行 Python 代码，开发者可在极短时间内理解并扩展 Agent 行为，适合研究和快速实验
- **多模型 Agent 评测对比**：支持 HuggingFace Hub 模型、OpenAI、Anthropic、Amazon Bedrock、本地 Transformers 模型等，同一套 Agent 逻辑可无缝切换底层 LLM 进行 benchmark
- **代码生成 + 执行一体化工作流**：Agent 在 ReAct 循环中生成 Python 代码并立即执行，适合需要多步推理、数据计算、文件操作等复杂任务
- **多智能体协作系统**：内置多 Agent 层级编排能力，可将复杂任务分解给多个子 Agent 协同完成
- **安全沙箱化 Agent 部署**：通过 E2B、Docker 等沙箱环境执行不可信代码，兼顾 Agent 能力和安全性

## 技术要点
- **Code-as-Action 范式**：smolagents 的核心创新。传统 Agent 框架要求 LLM 输出 JSON 结构来描述工具调用（如 `{"tool": "search", "args": {"query": "..."}}`），解析后再执行；而 CodeAgent 直接让 LLM 生成 Python 代码（如 `results = web_search(query="...")`），工具就是 Python 函数，代码即动作。这种方式天然支持循环、条件判断、变量赋值，一次生成可完成多步操作，大幅减少 LLM 往返次数。
- **ReAct 循环架构**：Agent 遵循 `Task → Memory → Model generates code → Execute → Loop until final_answer()` 的标准 ReAct 模式。`final_answer()` 是终止信号，Agent 调用它即表示任务完成并将结果返回给用户。每一步的代码执行结果和中间变量都会被记录到 Agent Memory 中供后续步骤参考。
- **两种 Agent 类型**：`CodeAgent` 生成并执行 Python 代码，是框架的主推模式；`ToolCallingAgent` 采用传统 JSON/text 工具调用方式，兼容现有依赖工具调用 API 的 LLM（如原生支持 function calling 的模型）。两者共享相同的 Tool 和 Memory 抽象。
- **模型无关的 LlmEngine 抽象**：通过统一的模型接口层对接多种后端——`InferenceClientModel` 对接 HuggingFace 推理服务、`LiteLLMModel` 通过 LiteLLM 支持 100+ LLM 提供商、`TransformersModel` 加载本地 HuggingFace 模型、`OpenAIModel` 兼容 OpenAI API 协议的服务（如 Together AI、OpenRouter），以及 `AzureOpenAIModel` 和 `AmazonBedrockModel` 覆盖企业部署场景。
- **多模态输入支持**：Agent 可接收文本、图像、视频、音频等多种模态的输入。工具可以返回富媒体内容，Agent 在生成代码时可引用这些多模态数据，使 Agent 能够处理视觉推理、视频理解等任务。
- **沙箱化代码执行**：代码执行安全是 Code-as-Action 范式的核心挑战。smolagents 提供分层安全方案——托管云沙箱（E2B、Blaxel、Modal）提供开箱即用的隔离环境；自托管方案支持 Docker 容器隔离；`LocalPythonExecutor` 提供本地执行但明确标注不构成安全边界，仅适用于可信代码。
- **HuggingFace Hub 深度集成**：工具和 Agent 可作为 Hub 仓库进行版本管理、分享和复用。`push_to_hub()` / `pull_from_hub()` 简化了 Agent 和 Tool 的分发流程。社区可贡献自定义 Tool 到 Hub，其他用户一键加载使用。
- **MCP 协议支持**：工具可从任意 Model Context Protocol (MCP) 服务器获取，使 smolagents 能接入日益增长的 MCP 工具生态。同时支持将 LangChain 工具通过适配器转换为 smolagents Tool，降低迁移成本。
- **CLI 开箱即用**：提供 `smolagent` 和 `webagent` 两个命令行工具。`smolagent` 是通用多步 Agent，`webagent` 是基于 Helium 的网页浏览 Agent，均可通过命令行参数指定模型和工具配置，零代码即可体验 Agent 能力。

## 技术栈
Python, HuggingFace Transformers, LiteLLM, Docker, E2B

## 关联
- [`langchain`](../langchain/) — LangChain 工具可通过适配器在 smolagents 中复用，两者在工具生态层互通
- [`langgraph`](../langgraph/) — LangGraph 提供图结构 Agent 编排，与 smolagents 的层级多 Agent 方案形成互补
- [`crewAI`](../crewAI/) — 同为多 Agent 框架，crewAI 侧重角色扮演式协作，smolagents 侧重代码执行式 Agent
- [`autogen`](../autogen/) — 微软的多 Agent 对话框架，与 smolagents 的代码执行范式形成不同流派
- [`pydantic-ai`](../pydantic-ai/) — Pydantic 出品的 Agent 框架，侧重结构化输出，与 smolagents 的代码执行路径互补
- [`agno`](../agno/) — 同为轻量级 Agent 框架，两者在"极简可 hack"的定位上相近

## 开放问题
- [ ] 2026-07-02 Code-as-Action 范式的安全边界如何形式化？当前沙箱方案（E2B/Docker）提供了进程级隔离，但 Agent 生成的代码仍可能通过工具调用产生副作用（如发送邮件、修改数据库）。是否存在比沙箱更细粒度的权限控制方案？
- [ ] 2026-07-02 开源模型在 CodeAgent 范式下的表现如何？smolagents 声称开源模型（如 DeepSeek-R1）在 agentic workflow 上可与闭源模型竞争，但这需要更大规模的 benchmark 验证，特别是代码生成的正确性和安全性维度。
- [ ] 2026-07-02 与其他 Agent 框架相比，Code-as-Action 在长周期任务中的 token 消耗和可靠性是否有量化对比数据？减少 30% 步数不一定意味着降低 30% 成本，需要端到端评估。
