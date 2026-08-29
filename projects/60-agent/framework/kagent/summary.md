# kagent

> [`kagent-dev/kagent`](https://github.com/kagent-dev/kagent) · 上游贡献 · CNCF 旗下的 Kubernetes 原生 Agent 框架，将 Agent 定义为 CRD 用 `kubectl` 在 K8s 生态中声明式管理

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Kagent 是 Agent 框架中的「Kubernetes 原住民」——在 CNCF 生态中将 Agent 作为一等 K8s 资源（CRD）管理，支持 `kubectl apply -f agent.yaml` 声明式部署。它填补了 Agent 框架与云原生运维之间的鸿沟：DevOps/SRE 团队用熟悉的 kubectl/YAML 范式管理 AI Agent，Agent 原生访问 K8s 集群内的 Prometheus/Grafana/Istio/Helm 等工具。CNCF 关联项目，团队关注云原生 Agent 运维这一新兴方向。

## 项目介绍
> **用 Kubernetes 的方式管理 AI Agent——Agent 是 CRD，工具是 CRD，用 `kubectl apply` 部署，用 GitOps 管理 Agent 生命周期。**

核心场景：
- **K8s 集群运维 Agent**：Agent 自动巡检集群健康、响应 Prometheus 告警、执行 Helm 部署
- **声明式 Agent 部署**：`kubectl apply -f agent.yaml` 定义 Agent 的 system prompt、工具集、LLM 配置
- **GitOps Agent 管理**：Agent 定义纳入 Git 仓库，通过 Argo CD 自动同步和部署
- **MCP 工具编排**：内置 K8s/Istio/Helm/Prometheus/Grafana/Cilium 等云原生 MCP Server
- **多云 Agent Mesh**：多个 Agent 跨集群协作，Agent 间通过 MCP/A2A 协议通信

## 技术要点
- **Agent CRD**：Agent 通过 Kubernetes Custom Resource 定义——spec 包含 system prompt、工具列表和 LLM 配置，完全声明式
- **ToolServer CRD**：工具也作为 K8s 自定义资源管理，支持 `kubectl get toolservers`
- **四大组件**：Controller（K8s 调和循环）+ Engine（Google ADK Agent 运行时）+ UI（Web 管理面板）+ CLI（kagentctl 命令行）
- **K8s 深度集成 MCP**：内置 Kubernetes/Istio/Helm/Argo/Prometheus/Grafana/Cilium 等 MCP Server，Agent 可操作整个集群
- **ModelConfig 资源**：统一管理多 LLM 后端的 API Key 和连接配置，支持 OpenAI / Anthropic / Vertex AI / Ollama
- **OpenTelemetry 可观测性**：内建 Agent 活动追踪，兼容 Jaeger / Grafana Tempo
- **Helm Chart 部署**：标准 Helm chart 一键安装整个 Kagent 系统（Controller + Engine + UI）

## 技术栈
Go (52.4%), TypeScript (24.9%), Python (18.1%), Google ADK, Kubernetes CRD, Helm, OpenTelemetry, MCP, Apache 2.0

## 关联
- [CNCF](https://www.cncf.io) — CNCF 关联项目
- [Google ADK](https://github.com/google/adk-python) — Agent 运行时引擎依赖
- [`modelcontextprotocol/modelcontextprotocol`](../../agent-runtime/protocol/modelcontextprotocol/) — MCP 协议，Agent 工具接入标准
- [`kubernetes-sigs/agent-sandbox`](../../agent-runtime/sandbox/agent-sandbox/) — 同生态，K8s 上 Agent 安全沙箱

## 开放问题
- [ ] 2026-07-02 CRD 定义 Agent 的粒度如何选择？一个 Agent CRD 对应一个独立 Agent，还是支持 Agent 团队（Crew）的 CRD 定义？
