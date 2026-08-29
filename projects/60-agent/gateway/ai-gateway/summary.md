# ai-gateway

> [`envoyproxy/ai-gateway`](https://github.com/envoyproxy/ai-gateway) · 上游贡献 · Envoy 基金会旗下的 AI API 网关，在 Envoy Proxy 层面提供 LLM 流量的统一接入、速率限制和可观测性

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Envoy AI Gateway 代表「基础设施层 AI 网关」的方向——不同于 LiteLLM/Portkey 等应用层 Proxy，AI Gateway 运行在 Envoy Proxy 层面，与 Service Mesh 和 API Gateway 天然集成。在 Agent 基础设施中，这意味着不需要改变 Agent 代码，网络层的 Envoy Filter 自动接管 LLM API 流量，注入认证/限流/观测/路由逻辑。团队关注 Service Mesh 与 AI 网关的融合趋势。

## 项目介绍
> **Envoy 层面的 AI API 代理——不需要改 Agent 代码，Envoy 自动拦截 LLM 流量，统一认证、限流和观测。**

核心场景：
- **LLM 流量统一网关**：所有服务调用 LLM API 统一通过 Envoy AI Gateway，集中管理 API Key 和审计
- **Service Mesh + AI**：与 Istio/Envoy Mesh 结合，LLM 流量获得与微服务流量同等的治理能力
- **多模型路由**：根据请求特征（成本/延迟/模型）自动路由到不同 LLM Provider
- **速率限制与并发控制**：在 Envoy 层面实施全局 LLM API 限流

## 技术要点
- **Envoy Filter 扩展**：作为 Envoy HTTP Filter 运行，拦截和修改 HTTP 请求/响应
- **Provider 抽象**：将不同 LLM API 的差异封装在 Provider 层（OpenAI/Anthropic/AWS Bedrock/GCP Vertex 等）
- **Token 计数与成本追踪**：在 Envoy 层面实时统计 token 用量和成本
- **声明式配置**：通过 Envoy xDS 协议动态更新网关规则
- **内置可观测性**：Envoy 原生指标和追踪集成（Prometheus/Zipkin/OTel）

## 技术栈
C++ (Envoy), Go, Protobuf/gRPC, xDS, Envoy Filter API, Apache 2.0

## 关联
- [`BerriAI/litellm`](../litellm/) — 竞品，LiteLLM 是应用层 AI Gateway，Envoy AI Gateway 是基础设施层
- [`higress-group/higress`](../higress/) — 同类，阿里云的 K8s AI Gateway
- [Envoy](https://www.envoyproxy.io) — 底层代理引擎
- [Istio](https://istio.io) — 同生态，Service Mesh

## 开放问题
- [ ] 2026-07-02 Envoy 层面的 AI 网关是否过于底层？SSE/Streaming 响应体解析的正确性和完整性在 C++ Filter 层的实现难度如何？
