# 60-agent · 智能体层


> **MOC 导览页** · 本层 70 个项目 · [↑ 返回栈总览](../README.md)

把 LLM 的"单次生成"封装成**能感知、能记忆、能调工具、能协作**的自主体。按能力域拆：框架（编排）、记忆、网关（多模型路由）、可观测、工具、协议（MCP/A2A）、规划、安全、编码 Agent。

## 编码 Agent（2）

- [`anomalyco--opencode`](coding/opencode/) — coding-agent、ai、上游贡献
- [`xai-org--grok-build`](coding/grok-build/) — coding-agent、ai、上游贡献

## 框架 / 编排（20）

- [`NVIDIA--NeMo-Agent-Toolkit`](framework/NeMo-Agent-Toolkit/) — agent、framework、上游贡献
- [`agno-agi--agno`](framework/agno/) — agent
- [`camel-ai--camel`](framework/camel/) — agent
- [`crewAIInc--crewAI`](framework/crewAI/) — agent
- [`deepseek-ai--deepseek-harness`](framework/deepseek-harness/) — DeepSeek 官方 agent harness，一切皆插件（Cordis）
- [`flowiseai--Flowise`](framework/Flowise/) — agent、framework、上游贡献
- [`google--adk-python`](framework/adk-python/) — agent、framework、上游贡献
- [`huggingface--smolagents`](framework/smolagents/) — agent
- [`kagent-dev--kagent`](framework/kagent/) — agent
- [`langchain-ai--langchain`](framework/langchain/) — agent
- [`langchain-ai--langgraph`](framework/langgraph/) — agent
- [`langgenius--dify`](framework/dify/) — agent、framework、上游贡献
- [`mastra-ai--mastra`](framework/mastra/) — agent、framework、上游贡献
- [`microsoft--agent-framework`](framework/agent-framework/) — agent、framework、上游贡献
- [`microsoft--autogen`](framework/autogen/) — agent
- [`microsoft--semantic-kernel`](framework/semantic-kernel/) — agent
- [`openai--openai-agents-python`](framework/openai-agents-python/) — agent、framework、上游贡献
- [`pydantic--pydantic-ai`](framework/pydantic-ai/) — agent
- [`run-llama--llama_index`](framework/llama_index/) — agent、framework、上游贡献
- [`strands-agents--harness-sdk`](framework/harness-sdk/) — agent

## 网关 / 路由（13）

- [`BerriAI--litellm`](gateway/litellm/) — agent
- [`Cmochance--codex-app-transfer`](gateway/codex-app-transfer/) — agent、gateway、上游贡献
- [`MetaFARS--codex-relay`](gateway/codex-relay/) — agent、gateway、上游贡献
- [`QuantumNous--new-api`](gateway/new-api/) — agent
- [`agentgateway--agentgateway`](gateway/agentgateway/) — agent
- [`agentic-community--mcp-gateway-registry`](gateway/mcp-gateway-registry/) — agent
- [`envoyproxy--ai-gateway`](gateway/ai-gateway/) — agent
- [`farion1231--cc-switch`](gateway/cc-switch/) — agent
- [`higress-group--higress`](gateway/higress/) — agent
- [`kgateway-dev--kgateway`](gateway/kgateway/) — agent
- [`lightseekorg--smg`](gateway/smg/) — agent、gateway、上游贡献
- [`router-for-me--CLIProxyAPI`](gateway/CLIProxyAPI/) — agent
- [`rtk-ai--rtk`](gateway/rtk/) — agent

## 记忆（14）

- [`NevaMind-AI--memU`](memory/memU/) — agent
- [`NoKV-Lab--NoKV`](memory/NoKV/) — agent
- [`TencentCloud--TencentDB-Agent-Memory`](memory/TencentDB-Agent-Memory/) — agent、memory、上游贡献
- [`agentscope-ai--ReMe`](memory/ReMe/) — agent、memory、上游贡献
- [`gastownhall--beads`](memory/beads/) — agent
- [`infiniflow--ragflow`](memory/ragflow/) — agent
- [`letta-ai--letta`](memory/letta/) — agent
- [`mem0ai--mem0`](memory/mem0/) — agent
- [`mempalace--mempalace`](memory/mempalace/) — agent
- [`oceanbase--powermem`](memory/powermem/) — agent、memory、上游贡献
- [`oceanbase--seekdb`](memory/seekdb/) — agent
- [`supabase--supabase`](memory/supabase/) — agent
- [`vectorize-io--hindsight`](memory/hindsight/) — agent
- [`volcengine--OpenViking`](memory/OpenViking/) — agent、memory、context

## 可观测 / 评测（10）

- [`EleutherAI--lm-evaluation-harness`](observability/lm-evaluation-harness/) — agent
- [`arize-ai--phoenix`](observability/phoenix/) — agent
- [`comet-ml--opik`](observability/opik/) — agent
- [`confident-ai--deepeval`](observability/deepeval/) — agent
- [`langfuse--langfuse`](observability/langfuse/) — agent
- [`openlit--openlit`](observability/openlit/) — agent
- [`promptfoo--promptfoo`](observability/promptfoo/) — agent
- [`traceloop--openllmetry`](observability/openllmetry/) — agent
- [`truera--trulens`](observability/trulens/) — agent
- [`vibrantlabsai--ragas`](observability/ragas/) — agent

## 规划（1）

- [`assafelovic--gpt-researcher`](planner/gpt-researcher/) — agent

## 协议（2）

- [`a2aproject--A2A`](protocol/A2A/) — agent
- [`modelcontextprotocol--modelcontextprotocol`](protocol/modelcontextprotocol/) — agent

## 安全（1）

- [`protectai--llm-guard`](security/llm-guard/) — agent

## 工具（7）

- [`ComposioHQ--composio`](tool/composio/) — agent
- [`alibaba--page-agent`](tool/page-agent/) — agent
- [`browser-use--browser-harness`](tool/browser-harness/) — agent
- [`browser-use--browser-use`](tool/browser-use/) — agent
- [`firecrawl--firecrawl`](tool/firecrawl/) — agent
- [`jina-ai--reader`](tool/reader/) — agent
- [`vercel-labs--agent-browser`](tool/agent-browser/) — agent

## 关联论文

- [`cordiverse--spatiotemporal-composability`](../../references/cordiverse/spatiotemporal-composability/summary.md) — `plugin-architecture, composability, cordis, agent-harness`
