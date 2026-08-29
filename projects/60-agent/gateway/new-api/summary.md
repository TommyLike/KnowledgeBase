# new-api

> [`QuantumNous/new-api`](https://github.com/QuantumNous/new-api) · 上游贡献 · 统一大模型 API 网关与聚合分发平台，基于 One API 二次开发，提供多厂商模型接入、格式互转、用量计费与智能路由

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> New API 是当前国内最活跃的 LLM API 网关开源项目（GitHub 40.9k Stars），基于已停止维护的 One API 演进而来。团队跟踪此项目以观察 AI 网关领域的技术演进趋势，关注其 API 格式互转中继层、多租户计费模型和信道路由策略等架构设计。在 Agent 生态中，API 网关是连接模型提供商与上层 Agent 应用的关键基础设施，New API 的格式互转能力和多厂商适配经验对团队构建 Agent 编排平台具有参考价值。

## 项目介绍
> **New API 是 One API 的下一代演进版本，为个人和企业提供统一的 AI 模型接入入口，支持 OpenAI、Claude、Gemini 等主流模型厂商的聚合管理与 API 格式双向转换。**

核心场景：
- **多模型统一接入**：通过单一 API 入口管理 OpenAI、Claude、Gemini、Midjourney、Suno 等多个厂商的模型，无需在各平台分别申请 Key
- **API 格式互转**：OpenAI 与 Claude Messages、Google Gemini 之间的双向格式转换，客户端只需使用 OpenAI 格式即可调用所有模型
- **多租户用量计费**：按请求粒度实时统计 Token 消耗，支持预充值额度分配、缓存命中独立计价（cache_creation / cache_read）、多币种分列显示
- **团队协作与权限管控**：支持 OIDC、Discord、Telegram、LinuxDO 等多渠道登录，可按 Token 分组并限制可用模型范围
- **智能路由与高可用**：加权随机选择可用信道、失败自动重试、速率限制，保障模型调用的稳定性和负载均衡

## 技术要点
- **基于 One API 演进**：完全兼容 One API 数据库，支持无缝迁移。前端为原创开发，受 AGPLv3+ 额外条款保护，商业使用需联系官方获取授权
- **多格式 API 互转中继层（relay）**：核心创新在于实现 OpenAI ↔ Claude Messages、OpenAI ↔ Gemini、Gemini ↔ OpenAI 等跨格式中继，客户端无需感知后端模型厂商的 API 差异
- **智能化信道路由**：支持加权随机选择、失败自动重试、速率限制，可按模型粒度为每个信道独立配置权重和并发上限，实现精细化流量调度
- **Reasoning Effort 配置机制**：通过模型名称后缀（如 `o3-mini-high`、`claude-3-7-sonnet-thinking`、`gemini-2.5-pro-thinking-128`）控制推理深度，无需修改请求参数即可切换推理模式
- **灵活的数据存储**：支持 SQLite（默认本地部署）、MySQL ≥ 5.7.8、PostgreSQL ≥ 9.6 三种数据库，适应从个人开发到企业部署的不同场景
- **可选的性能增强组件**：Redis 用于缓存和会话管理，Pyroscope 用于性能剖析，支持环境变量灵活配置流式超时和请求体大小限制
- **多语言国际化 UI**：内置英文、简体中文、繁体中文、法文、日文等多语言界面，配套独立文档站 docs.newapi.pro

## 技术栈
Go, 自研 Web 框架（controller/middleware/router/service/model 分层）, 自研前端（AGPLv3+）, SQLite / MySQL / PostgreSQL, Redis（可选）, Docker / Docker Compose, Pyroscope（可选）

## 关联
- [`BerriAI/litellm`](../litellm) — 主要竞品，Python 生态的 LLM 代理，支持 100+ 模型提供商，功能定位高度重叠
- [One API](https://github.com/songquanpeng/one-api)（上游基础，MIT 协议）— New API 的代码基础，已停止活跃维护
- [new-api-key-tool](https://github.com/Calcium-Ion/new-api-key-tool) — 生态配套工具，提供配额查询功能
- [new-api-horizon](https://github.com/Calcium-Ion/new-api-horizon) — 高性能优化版，针对大规模部署场景

## 开放问题
- [ ] 2026-07-02 One API 原版已停止维护，New API 在 AGPLv3+ 额外条款下的商业化路径和社区治理模式如何演进？是否有被上游继承 / fork 回社区主线的可能？
- [ ] 2026-07-02 New API 的中继层格式转换主要覆盖 OpenAI、Claude、Gemini 三大厂商，对新兴模型协议（如 MCP、Agent-to-Agent）的适配能力如何？是否需要团队关注其扩展性设计？
