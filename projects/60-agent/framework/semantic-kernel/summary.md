# semantic-kernel

> [`microsoft/semantic-kernel`](https://github.com/microsoft/semantic-kernel) · 上游贡献 · 微软的模型无关 AI 编排 SDK，将 LLM 作为「内核」通过 Plugin 机制连接企业现有系统与服务

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Semantic Kernel 是微软在 AI 编排领域的企业级 SDK，核心理念是将 LLM 视为操作系统的「内核」（Kernel），通过 Plugin 机制连接各种企业服务和数据源。与 LangChain 的「组件市场」定位不同，SK 更强调与企业现有微软技术栈（Azure、.NET、M365）的深度整合。已有官方继任者 Microsoft Agent Framework。团队将其作为企业级 AI 编排 SDK 的架构参考。

## 项目介绍
> **将 AI 融入企业应用的编排 SDK——以 Kernel 为核心，Plugin 为扩展，让 LLM 无缝调用企业现有 API、数据库和工作流。**

核心场景：
- **企业 AI 聊天机器人**：将 LLM 与企业客服系统、工单系统连接，Agent 自动分类和处理工单
- **Plugin 生态扩展**：原生代码 Plugin / Prompt 模板 Plugin / OpenAPI Plugin / MCP 协议 Plugin 四种方式接入外部能力
- **多 Agent 委派（Triage-Agent 模式）**：分诊 Agent 分析请求 → 按专业路由到账单/退款/技术支持等专业 Agent
- **RAG 应用**：集成 Azure AI Search、Elasticsearch、Chroma 等向量数据库实现知识库问答
- **本地推理**：兼容 Ollama、LM Studio、ONNX，支持离线/边缘场景

## 技术要点
- **Kernel-Plugin-Agent-Service 四层架构**：Kernel 为核心编排器，Plugin 提供可扩展能力，Agent 为智能体单元，Service 连接底层 AI 服务
- **模型无关设计**：不绑定特定 LLM 提供商，一套代码适配 OpenAI / Azure OpenAI / HuggingFace / NVIDIA / Google 等
- **四种 Plugin 扩展方式**：Native Code（直接写代码）、Prompt Template（模板化提示）、OpenAPI（导入 API 规范）、MCP 协议
- **Process Framework**：面向复杂业务流程的结构化工作流框架，支持确定性的步骤编排和条件分支
- **Triage-Agent 委派模式**：入口 Agent 按请求类型路由到多个专业 Agent，每个专业 Agent 独立完成子任务
- **多模态支持**：同时处理文本、视觉、音频输入，通过统一接口访问多模态模型
- **多语言 SDK**：C#（66%）+ Python（32%）+ Java，满足不同技术栈企业需求
- **企业级特性**：内置可观测性、安全过滤、速率限制、审计追踪

## 技术栈
C#, Python, Java, OpenAI, Azure OpenAI, HuggingFace, Ollama, ONNX, Azure AI Search, Elasticsearch, Chroma

## 关联
- [`microsoft/autogen`](../autogen/) — 同为微软出品，AutoGen 偏多 Agent 对话协作，SK 偏企业服务编排
- [`langchain-ai/langchain`](../langchain/) — 竞品，LangChain 偏组件生态，SK 偏企业集成
- Microsoft Agent Framework — 官方继任者，整合 AutoGen + SK
- Azure AI Foundry — 微软 AI 平台，SK 的一级部署目标

## 开放问题
- [ ] 2026-07-02 Microsoft Agent Framework 整合 AutoGen + SK 后，Process Framework 的确定性编排与对话式 Agent 的动态决策如何统一？
