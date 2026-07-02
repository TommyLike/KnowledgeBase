# mcp-gateway-registry

> [`agentic-community/mcp-gateway-registry`](https://github.com/agentic-community/mcp-gateway-registry) · 上游贡献 · AI 资产统一管控平面：为组织内 MCP 服务器、AI Agent、Skills 技能和自定义实体提供注册发现、访问控制、审计与安全扫描的治理中枢

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> mcp-gateway-registry 是 AI 资产治理领域的核心基础设施，始于 MCP 协议的统一网关，已演进为覆盖多种 AI 资产类型的通用注册中心。团队通过上游贡献参与其生态建设，跟踪 MCP 网关的接入管理、多 IdP 联邦认证以及 Agent 注册发现等能力演进，为内部 AI 资产管控提供参考架构。

## 项目介绍
> **为组织内所有 AI 资产（MCP 服务器、AI Agent、Skills 技能、自定义实体）提供统一的注册发现、访问控制、审计和安全扫描的治理中枢，从 MCP 网关演进为通用 AI 资产注册中心。**

核心场景：
- **企业 MCP 服务器统一接入**：AI 编码助手和 Agent 通过单一 Nginx 网关接入，自动路由到后端多个 MCP 服务器，消除每个 IDE 单独配置 MCP 端点的痛点，集中管理认证和授权。
- **Agent 注册与 A2A 通信**：注册 AI Agent（支持 A2A 协议或自定义协议），Agent 通过注册中心相互发现、认证后建立点对点直连通信，无需经过网关中转。
- **AI 技能（Skills）管理**：注册和版本化管理 SKILL.md 技能文件（托管于 GitHub/GitLab/Bitbucket），自动安全扫描，供 AI 编码助手按需发现和加载。
- **虚拟 MCP 服务器聚合**：将多个后端 MCP 服务器的工具、资源和提示词聚合为一个统一端点，支持版本路由（多版本并行运行、header 驱动测试、即时回滚）。
- **多云部署与安全合规**：支持 Docker Compose / Terraform ECS / Helm EKS 三种部署方式，集成六大企业 IdP，满足 SOC 2 / GDPR 合规审计要求。

## 技术要点
- **Nginx 反向代理层**：TLS 终止 + 认证校验 + 动态路由，支持 SSE 和 Streamable HTTP 双传输协议，SIGHUP 信号限速、错开健康检查以避免重启风暴。
- **混合搜索（RRF）**：采用 Reciprocal Rank Fusion 替代加法评分，融合全文检索和向量相似度，统一入口搜索服务器、工具和 Agent。
- **多嵌入后端**：支持本地 sentence-transformers、OpenAI 以及 LiteLLM 代理的 100+ 模型（Bedrock Titan、Cohere 等），灵活适配不同规模的部署环境。
- **MongoDB/DocumentDB 存储**：唯一存储后端（已移除文件存储），DocumentDB 使用原生 HNSW 向量索引，MongoDB CE 使用应用层向量搜索。
- **注册中心联邦**：支持点对点联邦同步，Fernet 加密凭证传输，路径命名空间隔离；兼容 AWS Bedrock AgentCore 注册中心跨账户/区域导入；支持 ARD v1.0（Agentic Resource Discovery）规范。
- **OAuth2/OIDC 统一认证**：六种 IdP 集成（Keycloak / Entra ID / Okta / Auth0 / Cognito / PingFederate），四种凭证类型并发支持（Session Cookie / IdP JWT / 静态 Token / 联邦静态 Token），多密钥静态 Token 支持按密钥分组和零停机轮换。
- **资产生命周期管理**：自服务工作流 draft → approval → active，支持人工审批或 CI/CD 自动化，注册 Webhook 和 Gate（fail-closed 外部准入控制）。
- **OpenTelemetry 可观测性**：每服务原生 Prometheus /metrics 端点（端口 9464），OTLP 推送至 Datadog / New Relic / Grafana Cloud / Honeycomb，集中审计日志（TTL 保留 + 凭证脱敏 + JSONL/CSV 导出）。

## 技术栈
Python / FastAPI（后端 API），Nginx（反向代理），MongoDB CE / Amazon DocumentDB / MongoDB Atlas（数据存储），sentence-transformers / OpenAI / LiteLLM（嵌入向量），OAuth2 / OIDC（认证），Docker Compose / Terraform ECS / Helm EKS（部署），OpenTelemetry + Prometheus（可观测性），pytest（701+ 测试），GitHub Actions / CodeBuild（CI/CD），Fernet / HMAC（加密）

## 关联
- 上游依赖：MongoDB、Nginx、Keycloak / Cognito 等 IdP、LiteLLM（嵌入代理）、Cisco AI Defense Scanner（安全扫描集成）、GoDaddy ANS（Agent Name Service 域名验证）、AWS Bedrock AgentCore（联邦同步）
- 下游用户：Claude Code / Codex CLI / Kiro CLI（AI 编码助手通过 DCR 集成），各类 MCP 客户端
- 同生态：Anthropic MCP Registry（API 兼容），Model Context Protocol 官方规范

## 开放问题
- [ ] 2026-07-02 ARD v1.0 规范目前的状态和社区采纳进度如何？对现有注册中心联邦机制的影响有多大？
- [ ] 2026-07-02 虚拟 MCP 服务器聚合中的版本路由能力在实际生产环境中的性能瓶颈和最佳实践有哪些？
- [ ] 2026-07-02 与 Anthropic 官方 MCP Registry 的 API 兼容程度如何？是否有迁移路径或互操作方案？
