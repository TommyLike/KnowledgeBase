# kgateway

> [`kgateway-dev/kgateway`](https://github.com/kgateway-dev/kgateway) · 上游贡献 · CNCF 旗下的 Kubernetes 原生 AI Gateway，将 Envoy 代理与 K8s Gateway API 融合为统一的 AI 流量管理平面

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Go · 14,657n/42,592e  
<!-- END AUTO -->

---

## 定位
> Kgateway (前 Gloo) 是 Solo.io 捐献给 CNCF 的 Kubernetes 原生 API 网关，在 K8s Gateway API 基础上扩展了 AI 流量管理能力。在 Agent 基础设施中，kgateway 填补了「Kubernetes 层面的 AI 网关」这一缺口——在 K8s 集群内运行的 Agent 服务，通过 Kgateway 获得统一的 LLM API 路由、认证和流量控制。与 LiteLLM（应用层）和 Envoy AI Gateway（C++ Filter 层）不同，kgateway 是 K8s-native CRD 驱动方案。

## 项目介绍
> **Kubernetes Gateway API 的 AI 扩展——用 K8s 原生 CRD 管理 LLM API 流量的路由、安全和观测。**

核心场景：
- **K8s 集群内 AI 流量管理**：Agent 微服务通过 kgateway 访问外部 LLM API，统一鉴权和速率控制
- **多模型路由**：根据请求特征将流量路由到不同 LLM Provider 或不同的模型版本
- **AI 服务暴露与保护**：内部 Agent 服务通过 Gateway API 安全暴露，支持 mTLS + OIDC 认证
- **Canary 部署**：A/B 测试不同模型版本或 Prompt 版本，渐进式发布

## 技术要点
- **K8s Gateway API 实现**：实现 K8s Gateway API 规范，支持 HTTPRoute/TCPRoute 等标准资源
- **Envoy 代理引擎**：底层使用 Envoy xDS 协议动态配置代理规则
- **AI Extension**：AI 流量感知的 BackendTrafficPolicy，支持 LLM 专用路由和转换
- **声明式 CRD 管理**：全部配置通过 kubectl apply 管理，支持 GitOps（Argo/Flux）
- **多级认证**：支持 API Key / OIDC / OAuth2 / mTLS 等多级认证链

## 技术栈
Go, Kubernetes Gateway API, Envoy Proxy, xDS, CRD, Apache 2.0

## 关联
- [`envoyproxy/ai-gateway`](../ai-gateway/) — 同族，Envoy 层面的 AI Gateway Filter
- [`higress-group/higress`](../higress/) — 竞品，阿里云 K8s AI Gateway
- [`BerriAI/litellm`](../litellm/) — 竞品/互补，应用层 AI Proxy
- [CNCF](https://www.cncf.io) — CNCF 项目

## 开放问题
- [ ] 2026-07-02 kgateway 的 AI 流量管理能力与 K8s Gateway API 标准演进如何同步？Gateway API 是否会原生支持 AI 流量语义？
