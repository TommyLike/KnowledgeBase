# litellm

> [`BerriAI/litellm`](https://github.com/BerriAI/litellm) · 上游贡献 · 业界最全的 LLM API 统一网关，100+ Provider 通过一个 OpenAI 兼容接口访问，内置负载均衡、速率限制和成本追踪

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Python · 167,017n/931,973e  
<!-- END AUTO -->

---

## 定位
> LiteLLM 是 Agent 生态中「模型访问层」的事实标准——在 Agent 和 LLM Provider 之间提供一个兼容 OpenAI API 格式的统一代理层。对 Agent 开发者来说，LiteLLM 解决了三个核心痛点：(1) 多模型切换——一行代码从 GPT-4o 切换到 Claude，Agent 代码不用改；(2) API 负载均衡——多个 API Key 轮换，绕过速率限制；(3) 成本追踪——每个 Agent 调用的 token 成本和延迟实时可见。167k nodes 的超大规模代码库体现了其 Provider 集成的广度。

## 项目介绍
> **100+ LLM Provider 的统一 API 网关——用标准 OpenAI 格式调用任何模型，内置成本追踪、负载均衡和速率限制。**

核心场景：
- **Agent 多模型切换**：Agent 代码只写一次，通过修改 `model` 参数在 GPT-4o / Claude / Gemini / DeepSeek 间自由切换
- **API 负载均衡**：配置多个 API Key 的轮询/权重/故障转移策略，Agent 在高并发下稳定运行
- **成本追踪与管理**：每个 API 调用的 token 用量和成本实时记录，按 `user` / `team` 维度的成本报表
- **速率限制与排队**：按 RPM/TPM 自动限流和请求排队，保护 API budget
- **自建 AI Gateway**：企业部署 LiteLLM Proxy 作为内部 AI Gateway，统一管理和鉴权所有 LLM 调用

## 技术要点
- **100+ Provider 覆盖**：从 OpenAI/Anthropic/Google/Azure 等主流到 Ollama/vLLM/HuggingFace 等自建方案，覆盖 LLM + Embedding + Image + Audio
- **OpenAI 兼容 API**：输入输出严格遵守 OpenAI ChatCompletion API 格式，任何使用 OpenAI SDK 的代码都无缝切换
- **LiteLLM Proxy (AI Gateway)**：独立部署的 HTTP 代理服务器，提供负载均衡（轮询/权重/最少延迟）、速率限制（RPM/TPM）、成本追踪和 API Key 管理
- **Virtual Key 体系**：管理员创建虚拟 Key 分配给团队/项目，每个 Key 有独立预算、速率限制和过期时间
- **Spend/Budget 追踪**：PostgreSQL 持久化每次调用的 token 用量和成本，按 user/team/tag 维度汇总报表
- **异常检测与告警**：配置延迟/错误率/成本阈值，触发时通过 Slack/Email/Webhook 发送告警
- **Guardrails 集成**：API 调用前后可插入内容过滤、安全检测和输出校验逻辑

## 技术栈
Python, OpenAI SDK, FastAPI (Proxy), PostgreSQL, Redis, 100+ Provider SDKs, MIT

## 关联
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — LangChain 使用 LiteLLM 作为模型统一调用层 (`ChatOpenAI` 内部使用的适配器)
- [`envoyproxy/ai-gateway`](../ai-gateway/) — Envoy 层面的 AI Gateway，与 LiteLLM Proxy 在网关层竞争
- [`higress-group/higress`](../higress/) — 阿里云 AI Gateway，K8s 环境下与 LiteLLM Proxy 竞争
- [`langfuse/langfuse`](../../observability/langfuse/) — LLM 追踪平台，与 LiteLLM 集成实现调用链追踪

## 开放问题
- [ ] 2026-07-02 LiteLLM Proxy 在极高并发（100K+ RPM）下的性能瓶颈在哪里？是否有集群水平扩展方案？
