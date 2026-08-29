# OpenSandbox

> [`opensandbox-group/OpenSandbox`](https://github.com/opensandbox-group/OpenSandbox) · 上游贡献 · 面向 AI Agent 的通用、可插拔沙箱平台，提供多语言 SDK、统一生命周期 API、网络隔离与凭证注入的一站式安全执行基础设施

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh
<!-- END AUTO -->

---

## 定位
> OpenSandbox 是 AI Agent 生态中承上启下的沙箱基础设施层：向下对接 Docker、Kubernetes 及 gVisor/Kata/Firecracker 等安全容器运行时，向上为 Coding Agent、GUI Agent、Agent 评测框架、RL 训练等场景提供统一的隔离执行环境。它是目前开源社区中覆盖面最广的 Agent Sandbox 方案——同时提供 5 种语言 SDK、MCP 协议集成、以及从本地 Docker 到生产 Kubernetes 的无缝切换能力。我们跟踪该项目是为了理解 Agent 安全执行的最佳实践，以及评估其作为团队 Agent 产品执行后端的可行性。

## 项目介绍
> **OpenSandbox 是一个协议驱动的通用沙箱平台，将容器编排复杂性封装在统一 API 之后，让 AI Agent 开发者无需关心底层基础设施即可安全运行不可信代码。**

核心场景：
- **Coding Agent 代码执行**：为 Claude Code、Gemini CLI、OpenAI Codex CLI、Qwen Code、Kimi CLI 等编程 Agent 提供隔离的代码运行环境，支持命令执行、文件操作、Jupyter 内核集成
- **GUI Agent 浏览器自动化**：在沙箱中运行 Chrome/Playwright，为 Web 操作 Agent 提供安全的浏览器环境，配合 Ingress 网关实现远程 VNC/Web 访问
- **Agent 评测与基准测试**：为 Harbor 等评测框架提供可复现的隔离评测环境，确保每次评测在干净的沙箱中运行
- **AI 代码解释器**：提供与 ChatGPT Code Interpreter 类似的 Jupyter 内核沙箱，支持数据分析、图表生成等交互式编程场景
- **强化学习训练**：为 RL 训练 pipeline 批量创建和销毁沙箱环境，通过 Kubernetes 运行时实现大规模并发调度

## 技术要点
- **控制面/数据面分离的三层架构**：控制面由 Python FastAPI 服务器负责沙箱生命周期管理（创建、启动、暂停、终止、TTL 自动回收），数据面由 Go 编写的 execd/ingress/egress 组件在沙箱内执行实际操作。这种分离使得控制面可独立扩缩容，数据面组件可注入任意沙箱镜像
- **可插拔沙箱运行时**：同一套生命周期 API 支持 Docker 和 Kubernetes 两种后端。Docker 运行时面向本地开发和单机部署，使用 bridge 网络模式并通过 bootstrap 脚本注入 execd；Kubernetes 运行时面向生产环境，基于 BatchSandbox CRD 实现资源池化和快速供给，支持 agent-sandbox provider
- **execd 执行守护进程**：每个沙箱内部运行的 Go/Gin HTTP 守护进程，提供命令执行（SSE 流式输出）、文件操作（上传、下载、搜索、目录列举）、Jupyter 内核代码执行、PTY WebSocket 终端等全部运行时能力，同时暴露 /ping 和 /metrics 健康端点
- **Ingress 网关与网络策略**：统一 HTTP/WebSocket 反向代理，支持 URI、Header、Wildcard Host 多种路由策略，自动生成签名 URL 保障访问安全。在客户端无法直连沙箱时提供 Server Proxy 模式中继流量，并支持按流量自动续期沙箱 TTL
- **Egress 出网策略管控**：Go 实现的网络侧车（sidecar），通过 DNS 拦截 + nftables 规则在沙箱级别实施出网白名单/黑名单策略。支持运行时动态更新策略、FQDN 到 IP 的自动解析与规则下发，以及实验性的 HTTPS MITM 透明 TLS 拦截
- **Credential Vault 凭证安全注入**：平台级定义凭证（API Key、OAuth Token、HTTP Header、Query Param），通过 egress 侧车在请求时以 MITM 代理方式替换占位符，沙箱内用户代码无法接触真实凭证明文。所有 SDK 均已支持，CLI 通过 `osb credential-vault` 管理
- **多级安全隔离**：除默认的 runc 进程级隔离外，支持 gVisor（用户态内核，系统调用拦截，冷启动约 550ms）、Kata Containers（基于 QEMU 的完整 VM 隔离）、Firecracker microVM（轻量级虚拟机，冷启动约 625ms）三种增强隔离模式，按安全等级灵活选用
- **OpenAPI 协议优先设计**：`specs/` 目录中的 OpenAPI 规范是沙箱协议的单一事实来源，第三方可以实现自有沙箱运行时，只要符合协议即可与 OpenSandbox 客户端生态互通。oSEP（OpenSandbox Enhancement Proposal）机制管理协议演进
- **MCP Server 原生集成**：`opensandbox-mcp` 将沙箱创建、命令执行、文件操作暴露为标准 MCP 工具，Claude Code、Cursor 等 MCP 客户端可直接调用。结合 egress 策略和凭证注入，实现了从 Agent 到沙箱的端到端安全链路
- **多语言 SDK 与 CLI**：提供 Python、Java/Kotlin、TypeScript/JavaScript、C#/.NET、Go 五种语言的客户端 SDK，统一封装 `Sandbox.create()` / `run()` / `files` / `kill()` 生命周期。`osb` CLI 支持从终端直接管理沙箱、凭证和网络策略

## 技术栈
Python (FastAPI), Go (Gin, execd/ingress/egress), Kotlin, C# (.NET), TypeScript, Java, Docker, Kubernetes, gVisor, Kata Containers, Firecracker, SQLite, OpenAPI, MCP

## 关联
- [`kubernetes-sigs/agent-sandbox`](../agent-sandbox/) — Kubernetes SIG 的 Agent 沙箱项目，OpenSandbox 的 Kubernetes 运行时支持其作为 provider
- [`firecracker-microvm/firecracker`](../../../agent-infra/firecracker/) — Firecracker microVM，OpenSandbox 的增强隔离后端之一
- [`langchain-ai/langgraph`](../../../agent-framework/langgraph/) — LangGraph Agent 框架，OpenSandbox 官方示例中的集成目标
- [`agent-infra/sandbox`](../sandbox/) — agent-infra 组织的沙箱方案，同赛道竞品/参考

## 开放问题
- [ ] 2026-07-02 OpenSandbox 的 K8s 运行时在大规模（1000+ 并发沙箱）下的调度延迟和资源池化效率如何？冷启动优化（镜像预热、沙箱预热）的具体策略是什么？
- [ ] 2026-07-02 Credential Vault 的 MITM 代理方式在高并发下是否成为瓶颈？是否有计划支持 sidecar 注入之外的无代理模式？
- [ ] 2026-07-02 OpenSandbox 与 kubernetes-sigs/agent-sandbox 的集成深度如何？两者在 K8s 场景下的分工边界是什么？

