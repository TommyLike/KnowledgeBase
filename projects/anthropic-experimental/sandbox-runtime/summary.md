# sandbox-runtime

> [`anthropic-experimental/sandbox-runtime`](https://github.com/anthropic-experimental/sandbox-runtime) · 上游贡献 · Anthropic 开源的进程级轻量沙箱工具，利用 OS 原生安全基元（macOS sandbox-exec / Linux bubblewrap）实现文件系统和网络隔离，无需容器

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `c68d128` · TypeScript + Rust · 132文件/1.9MB · 538n/1341e  
**入口** `src/cli.ts` (main) · `src/sandbox/sandbox-manager.ts` (wrapWithSandbox/initialize/reset)  
**架构** 三平台进程级沙箱：CLI → SandboxManager → 平台适配层 (macOS sandbox-exec / Linux bubblewrap / Windows Sandbox) → 代理层 (HTTP Proxy + SOCKS5 Proxy + MuxProxy + TLS Terminate + Parent Proxy) → 凭据注入 (credential-mask-files)  
**热点** sandbox-manager.ts · http-proxy.ts · macos-sandbox-utils.ts · linux-sandbox-utils.ts · tls-terminate-proxy.ts · credential-mask-files.ts
<!-- END AUTO -->

---

## 定位
> Sandbox Runtime (srt) 是 Anthropic 为 Claude Code 开发的进程级沙箱工具，已开源为社区可用。与 E2B（Firecracker VM 级隔离）、k8s-sigs（CRD 容器沙箱）、CubeSandbox（腾讯云容器沙箱）等「基础设施层」方案不同，srt 采用**OS 原生安全基元（macOS Seatbelt + Linux bubblewrap）+ 代理式网络过滤**实现零容器/零 VM 的轻量进程隔离。在 Agent Sandbox 生态中，srt 是最轻量、最贴近开发者日常使用的方案——不启动容器、不分配 VM，直接包装任意命令行进程。团队关注其作为 Agent 安全工具的 OS 原生路线。

## 项目介绍
> **不需要容器的进程沙箱——用 macOS sandbox-exec 或 Linux bubblewrap 直接隔离任意进程的文件系统和网络访问，Claude Code 的安全底座。**

核心场景：
- **Agent 命令安全执行**：Claude Code 的 Bash 命令、MCP Server 调用自动通过 srt 沙箱化，防止 Agent 读取敏感文件或访问未授权网络
- **MCP Server 沙箱隔离**：在 `.mcp.json` 中将 `command` 改为 `srt`，配置 `~/.srt-settings.json` 即可限制 MCP Server 的文件系统和网络权限
- **任意进程安全包装**：`srt curl example.com` 一行命令即可让 curl 在受限环境中运行
- **开发环境安全**：npm install / git push 等操作自动受沙箱策略保护

## 技术要点
- **macOS + Linux 双平台 OS 原生隔离**：macOS 使用 `sandbox-exec` 动态生成 Seatbelt 配置文件（Apple 官方沙箱框架），Linux 使用 `bubblewrap`（Flatpak 使用的容器技术）配合网络命名空间隔离。不使用 Docker/VM
- **安全默认策略（Secure-by-Default）**：网络默认全部拒绝（allow-only 模式），文件写入默认全部拒绝（allow-only），文件读取默认全部允许但支持 deny-then-allow 模式
- **HTTP + SOCKS5 双代理网络过滤**：所有网络流量经本地 HTTP 代理（HTTP/HTTPS）和 SOCKS5 代理（其他 TCP）路由，代理层执行域名白名单/黑名单检查
- **macOS Seatbelt 动态配置**：运行时根据用户设置动态生成 Sandbox Profile，通过 scheme 语言精确控制文件路径、网络端口、mach port 等权限
- **TLS Termination（实验性）**：可选的 HTTPS MITM 解密，使代理层能检查加密流量内容并执行细粒度请求过滤。排除 mTLS 和证书固定（certificate-pinning）的上游
- **违规实时监控**：macOS 上通过 SandboxViolationStore 接入系统沙箱违规日志（`/usr/bin/log stream`），实时告警被拦截的操作
- **TypeScript npm 包分发**：`npm install -g @anthropic-ai/sandbox-runtime` 全局安装，跨平台 npm 二进制，TypeScript 编写的库和 CLI 双模式

## 技术栈
TypeScript, Node.js, macOS sandbox-exec (Seatbelt Scheme), Linux bubblewrap, HTTP Proxy, SOCKS5 Proxy, npm

## 关联
- [Claude Code](https://claude.com/claude-code) — srt 作为 Claude Code 的安全沙箱底座，所有 Bash 命令和 MCP Server 调用通过 srt 执行
- [`e2b-dev/infra`](../../agent-runtime/sandbox/infra/) — 竞品/互补。E2B 是 Firecracker VM 级隔离（硬件级安全但启动慢），srt 是 OS 级隔离（启动快但隔离度低于 VM）
- [`kubernetes-sigs/agent-sandbox`](../../agent-runtime/sandbox/agent-sandbox/) — 竞品/互补。K8s 容器沙箱（集群环境），srt 是本地进程沙箱（开发者环境）
- [`TencentCloud/CubeSandbox`](../../agent-runtime/sandbox/CubeSandbox/) — 竞品/互补。云厂商容器沙箱，srt 是本地轻量方案
- [`opensandbox-group/OpenSandbox`](../../agent-runtime/sandbox/OpenSandbox/) — 竞品/互补。通用沙箱框架（Docker/K8s），srt 是进程级无容器方案
- [`modelcontextprotocol/modelcontextprotocol`](../../agent-runtime/protocol/modelcontextprotocol/) — MCP 协议，srt 的关键应用场景是 MCP Server 沙箱化

## 开放问题
- [ ] 2026-07-05 srt 的 Linux bubblewrap 方案与 macOS Seatbelt 方案的安全隔离等级差异有多大？
- [ ] 2026-07-05 Anthropic 是否会将 srt 的 OS 原生方案推广为 Agent Sandbox 的行业标准？目前 "anthropic-experimental" 的 org 位置是否暗示正式产品化计划？
