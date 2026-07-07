# Agent Runtime 技术全景 — 目录索引

> 2026-07-07 | 覆盖 72 开源项目 / 8 子领域 | [GitHub](https://github.com/TommyLike/KnowledgeBase)

---

| 编号 | 文件 | 子领域 | 项目数 | 内容概要 |
|------|------|--------|--------|---------|
| 00 | [00-overview.md](00-overview.md) | **全景观** | 72 | 背景、8 关键问题全景、技术方向总览、72 项目速查表、交叉分析、选型指南 |
| 01 | [01-sandbox.md](01-sandbox.md) | Sandbox 执行隔离 | 27 | MicroVM/容器/进程级/策略层 4 方向、10 场景选型、凭据解耦趋势 |
| 02 | [01-memory.md](01-memory.md) | Memory 状态记忆 | 14 | 7 技术方向(API 框架/有状态 Agent/混合引擎/RAG/事件溯源/原文/后端)、LongMemEval |
| 03 | [01-gateway.md](01-gateway.md) | Gateway 模型治理 | 10 | LLM 路由/协议转换/认证流控/MCP 注册 4 方向、LiteLLM vs Higress vs New API |
| 04 | [01-observability.md](01-observability.md) | Observability 可观测 | 10 | 追踪平台/评估框架/安全评估/OTel SDK 5 方向、评估指标体系全景 |
| 05 | [01-tool.md](01-tool.md) | Tool 工具集成 | 7 | 浏览器自动化/网页提取/工具平台 3 方向、竞合关系矩阵 |
| 06 | [01-protocol.md](01-protocol.md) | Protocol 通信协议 | 2 | MCP vs A2A 分工、Task 状态机、6 协议对比、统一治理 |
| 07 | [01-planner.md](01-planner.md) | Planner 规划推理 | 1 | 6 范式+GPT-Researcher 代码级、与 Sandbox/Memory/Gateway 交叉 |
| 08 | [01-security.md](01-security.md) | Security 内容安全 | 1 | LLM-Guard 代码级、OWASP Top 10(2025)、三层防御、RL 攻击趋势 |

## 阅读路径

- **快速了解** → 先读 `00-overview.md` 前两节(背景+关键问题全景),再扫项目全景表
- **选型决策** → 读完 00-overview 第七节(选型指南)+ 对应子领域的 01-*.md
- **深度研究** → 按编号顺序逐个子领域精读,关注交叉分析(第五节)

## 文件清单

```
reports/agent-landscape/
├── INDEX.md                  ← 本文件
├── 00-overview.md            ← 总览报告
├── 00-overview.pdf
├── 01-sandbox.md             ← Sandbox 深度
├── 01-sandbox.pdf
├── 01-memory.md              ← Memory 深度
├── 01-memory.pdf
├── 01-gateway.md             ← Gateway 深度
├── 01-gateway.pdf
├── 01-observability.md       ← Observability 深度
├── 01-observability.pdf
├── 01-tool.md                ← Tool 深度
├── 01-tool.pdf
├── 01-protocol.md            ← Protocol 深度
├── 01-protocol.pdf
├── 01-planner.md             ← Planner 深度
├── 01-planner.pdf
├── 01-security.md            ← Security 深度
└── 01-security.pdf
```
