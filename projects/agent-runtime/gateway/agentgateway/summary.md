# agentgateway

> [`agentgateway/agentgateway`](https://github.com/agentgateway/agentgateway) · 上游贡献 · 基于 Rust 的高性能 Agent 通信网关，以 A2A 协议为核心实现 Agent 发现、路由和负载均衡

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Rust · 21,945n/105,213e  
<!-- END AUTO -->

---

## 定位
> AgentGateway 是 Agent Mesh 架构中的「API 网关」——类比微服务中的 Kong/APISIX，但专门为 Agent 间通信（A2A 协议）设计。在 Multi-Agent 架构中，AgentGateway 解决 Agent 发现（哪个 Agent 能处理这个任务）、路由（请求转发到最合适的 Agent）和认证（谁有权调用哪个 Agent）三个核心问题。

## 项目介绍
> **Agent 之间的 API 网关——Agent 只需对网关说话，网关负责发现、路由和认证其他 Agent。**

核心场景：
- **Agent 注册与发现**：Agent 启动时注册到网关，声明能力和端点
- **Agent-to-Agent 路由**：主 Agent 通过网关统一调用子 Agent，网关负载均衡
- **A2A 协议标准化接入**：支持 A2A 协议 Agent 的透明接入和管理

## 技术要点
- **Rust 实现**：单二进制，内存 <50MB，10K+ 并发连接
- **A2A 协议原生**：基于 Agent Card 的注册中心和路由逻辑
- **插件架构**：认证/限流/日志以插件形式扩展
- **多协议支持**：HTTP/gRPC/A2A 多协议统一接入

## 技术栈
Rust, A2A Protocol, gRPC, HTTP, Apache 2.0

## 关联
- [`a2aproject/A2A`](../../protocol/A2A/) — 底层 A2A 协议标准
- [`modelcontextprotocol/modelcontextprotocol`](../../protocol/modelcontextprotocol/) — MCP 与 A2A 互补协议
- [`kgateway-dev/kgateway`](../kgateway/) — 通用 K8s Gateway，AgentGateway 专注 Agent 场景

## 开放问题
- [ ] 2026-07-02 AgentGateway 是否支持 MCP 协议的 Agent 接入？还是仅限 A2A？
