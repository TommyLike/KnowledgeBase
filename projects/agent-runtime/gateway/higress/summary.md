# higress

> [`higress-group/higress`](https://github.com/higress-group/higress) · 上游贡献 · 基于 Istio+Envoy 的 AI 原生 API 网关，统一 LLM 模型接入、MCP Server 托管与流量治理

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> Higress 是阿里巴巴开源的新一代云原生 API 网关，基于 Istio 和 Envoy 构建，已在阿里生产环境承载数十万 QPS 的流量验证。它从解决传统 Nginx reload 对长连接服务的损伤出发，逐步演进为以 AI 为「一等公民」的 AI 原生网关 —— 不仅提供多模型统一接入、Token 级流控、AI 安全防护等大模型网关能力，还内建 MCP Server 托管机制，可作为 Agent 工具调用的统一治理入口。我们跟踪 Higress 是因为它代表了「API 网关 + AI 网关 + MCP 网关」三合一的演进方向，对团队理解 Agent 基础设施网关层的技术趋势有重要参考价值。

## 项目介绍
> **Higress 是一个将流量网关、微服务网关、安全网关和 AI 网关融为一体的云原生网关，用 Wasm 插件机制实现 AI 场景下的协议转换、模型路由、内容安全和可观测性。**

核心场景：
- **AI 模型统一接入**：作为企业内所有 LLM 调用（OpenAI、通义千问、DeepSeek、vLLM、Ollama 等 100+ 提供商）的统一入口，提供 OpenAI 兼容协议转换、多模型负载均衡与故障切换、Token 消耗限流和全链路可观测。
- **MCP Server 托管与治理**：将 MCP Server 作为 Wasm 插件部署在网关中，为 Agent 工具调用提供统一认证、限流、审计日志和动态热更新，配套 `openapi-to-mcp` 工具可将已有 OpenAPI 接口自动转为 MCP Server。
- **Kubernetes Ingress 替代**：兼容 K8s Nginx Ingress 主流注解，路由变更速度提升十倍，资源开销显著降低，无 reload 中断。
- **微服务网关**：支持从 Nacos、ZooKeeper、Consul、Eureka 发现服务，深度集成 Dubbo、Nacos、Sentinel，HTTP 到 Dubbo 协议转换。
- **安全防护网关**：内建 WAF、IP/Cookie CC 防护、Bot 检测、JWT/OIDC/OAuth2/OPA 认证策略，以及针对 AI 场景的 Prompt 注入检测和敏感内容识别。

## 技术要点
- **Envoy 数据面 + Istio 控制面**：数据面基于 Envoy C++ 代理，控制面通过 Higress Controller 将 K8s Ingress/CRD 转为 Istio API，再经 Pilot 组件生成 xDS 推送至 Envoy。相比传统 Nginx 网关，配置变更毫秒级生效且无流量抖动，连接池复用避免长连接中断。
- **Wasm 多语言插件体系**：插件可用 Go、Rust、JavaScript 编写并编译为 WebAssembly，遵循 Proxy-Wasm 规范。沙箱隔离保证内存安全，插件可独立版本升级、无流量损失热更新。200+ 预置插件覆盖 AI、流量管理、安全和可观测性场景。
- **真正的流式处理**：网关对请求/响应体进行增量流式处理而非全量缓冲，使 Wasm 插件可原生处理 SSE 等流式协议。在 AI 大带宽场景下显著降低内存开销，这是传统 API 网关不具备的能力。
- **AI 专属插件矩阵**：提供 `ai-proxy`（多模型协议转换）、`ai-load-balancer`（FNV-1a 一致性哈希）、`ai-security-guard`（Prompt 注入检测 + Embedding API 内容检测）、`ai-cache`（语义缓存）、`ai-statistics`（Token 消耗与延迟可观测）、`ai-context-limit`（上下文窗口强制限制）、`model-router`（语义路由）等一整套 AI 生命周期插件。
- **Token 粒度流控**：区别于传统 QPS 限流，支持基于 Token 消耗量的配额管理和速率限制，配合 API Key 池轮转机制，适合大模型调用场景的成本控制和多租户隔离。
- **多注册中心混合支持**：同时对接 Nacos、ZooKeeper、Consul、Eureka 四种注册中心，允许混合服务网格场景下无需统一注册中心即可互通。
- **零外部依赖部署**：配置通过 K8s CRD 存储在 etcd 中，无外部数据库依赖。支持单 Docker 命令一键启动 All-in-One 镜像，同时提供 Helm 部署和阿里云计算巢托管方案。
- **MCP Bridge 机制**：通过专用配置面（Mcp Bridge Configuration）将 MCP 工具调用接入网关治理平面，每个工具调用经过 Higress 即获得企业级认证、限流、审计能力，实现「AI 的 USB-C 接口」角色。

## 技术栈
Go, C++ (Envoy), Java (Console 后端), TypeScript/Node.js (Console 前端), Rust (Wasm 插件 SDK), WebAssembly, Istio, Kubernetes CRD, xDS, SSE, gRPC, Dubbo, Nacos

## 关联
- [`envoyproxy/ai-gateway`](../ai-gateway/) — Envoy 官方推出的 AI 网关，同基于 Envoy 数据面，功能侧重不同，可对比参考 AI 网关的两种设计路线
- [`agentgateway/agentgateway`](../agentgateway/) — Agent 网关项目，同为 Agent 调用入口的网关方案
- [`kgateway-dev/kgateway`](../kgateway/) — Kubernetes Gateway API 实现，同为云原生网关领域项目
- [`agentic-community/mcp-gateway-registry`](../mcp-gateway-registry/) — MCP 治理中枢，Higress 的 MCP Server 托管与之形成互补
- [`opensourceways/MCP-gateway`](../../../opensourceways/MCP-gateway/) — 团队自研 MCP 网关，可与 Higress 的 MCP 托管方案对比参考
- [`opensourceways/istio-demo`](../../../opensourceways/istio-demo/) — 团队 Istio 学习项目，Higress 的控制面基于 Istio 衍化，有技术关联

## 开放问题
- [ ] 2026-07-02 Higress 的 Wasm 插件体系与 Envoy 社区 Proxy-Wasm 标准的兼容程度如何？是否存在 Higress 特有的 ABI 扩展导致插件无法跨网关复用？
- [ ] 2026-07-02 Higress 的 MCP Server 托管方案与 Anthropic MCP 官方参考实现（如 Python/TypeScript SDK）在协议兼容性上的差异点有哪些？
- [ ] 2026-07-02 Higress v2.3.0 规划的 WebRTC 实时 AI 能力是否会对 Agent 实时交互场景（如语音 Agent）带来网关层的新范式？
- [ ] 2026-07-02 Higress 在阿里云 MSE 云原生网关产品中使用的是共享内核还是定制分支？社区版与企业版的功能差异对开源生态的长期影响如何评估？
