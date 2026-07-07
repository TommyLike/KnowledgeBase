# Agent Runtime -- 执行隔离与安全 (Sandbox)

## 关键问题

Agent 沙箱子领域要解决一个核心矛盾：**AI Agent 需要执行不可信代码（LLM 生成、用户提交、第三方插件），但执行环境必须与宿主机和其他 Agent 安全隔离**。这个矛盾在 Agent 场景下尤其尖锐 -- Agent 不是被动 API 调用者，而是**主动生成和执行代码的自主实体**，它可能安装依赖、读写文件、发起网络请求、启动子进程。沙箱的挑战不是「能不能隔离」，而是如何在**隔离强度、启动延迟、运维成本、功能完整性**四者之间找到对应场景的最优解。

---

## 技术方向分类

### 方向 1：MicroVM 硬件级隔离 -- 安全优先，牺牲启动速度

**核心思路**：每个 Agent 沙箱是一个独立的轻量级虚拟机（Firecracker / Kata / gVisor），利用硬件虚拟化实现最强的安全边界。Agent 在 VM 内可以拥有完整的 Linux 环境，但无法逃逸到宿主机。VM 销毁后所有状态清零。

**代表项目**：
- `e2b-dev/infra` (E2B, ~7.5k stars)：Agent 沙箱领域的事实标杆。基于 Firecracker microVM，<200ms 冷启动，API-first（`sandbox.create()` / `sandbox.runCode()`），提供 Python/Node.js/Go 等多语言预构建环境模板和 TypeScript/Python/Go SDK。
- `NVIDIA/OpenShell` (~20k stars)：Rust 编写的多后端沙箱运行时。microVM 只是其四种驱动之一（另有 Podman/Docker/K8s），核心差异化在于**凭据代理出口网关** -- Agent 的 LLM API key 在网络边界注入，Agent 本身看不到原始凭据。还包括 GPU VFIO 直通、OPA 策略引擎和 OCSF 审计。
- `opensandbox-group/OpenSandbox`：协议驱动的通用沙箱平台。支持 gVisor（约 550ms 冷启动）、Kata Containers（QEMU VM）和 Firecracker（约 625ms）三种增强隔离模式。控制面/数据面分离的三层架构，提供 5 种语言 SDK 和 MCP Server 原生集成，是开源社区中覆盖面最广的 Agent Sandbox 方案。

**适用场景**：
- 多租户 SaaS 平台（每个用户/Agent 获得独立 VM）
- 金融、医疗等高合规要求场景
- 执行来自外部的不受信任代码（如用户提交的脚本、第三方 Agent 插件）

**局限**：
- 冷启动延迟即使优化到 <200ms，仍高于容器/进程方案
- 大规模并发（1000+沙箱）下的资源碎片化和调度延迟是未解决的工程难题
- VM 级隔离的运维复杂度显著高于容器方案

---

### 方向 2：容器级隔离 -- 主流平衡点，生态成熟

**核心思路**：利用 Docker / Kubernetes / Podman 等成熟容器技术实现沙箱。相比 MicroVM，容器共享宿主机内核因此启动更快（秒级）；相比进程级隔离，文件系统、网络、cgroup 资源限制更完整。这是目前采用最广泛的路线。

**代表项目**：
- `kubernetes-sigs/agent-sandbox` (Kubernetes SIG)：定义 Agent 沙箱的 K8s 原生 CRD 规范。通过 Sandbox CRD 声明沙箱的运行时类型（container/vm/microvm）和安全策略，利用 RuntimeClass 集成 Kata/gVisor/Firecracker。代表了 K8s 社区对 Agent 沙箱标准化的官方态度。
- `openkruise/agents`：K8s Operator 模式的 Agent 沙箱。通过 Sandbox CRD 管理沙箱完整生命周期（Create -> Ready -> Running -> Idle -> Terminated），自动回收空闲沙箱。支持 GPU/NPU（昇腾 Ascend）资源声明，内置 seccomp/AppArmor/SELinux 安全策略模板。
- `coder/coder` (~8.5k stars)：开发环境即代码平台，以 Terraform 模板定义工作空间，在 K8s/Docker/VM 上按需创建隔离 Agent 执行环境。支持 VS Code/JetBrains/SSH 接入，空闲自动休眠。冷启动约 30s-2min（偏重，非为 Agent 场景优化）。
- `cohere-ai/cohere-terrarium` (~300 stars)：轻量 Python 代码沙箱，双运行时架构（Docker + Pyodide 浏览器端）。专为 LLM Data Agent 设计，提供 `/run` HTTP API，Agent POST 代码获取 stdout/stderr。代码精简，部署门槛极低。
- `volcano-sh/agentcube`：基于 CNCF Volcano 批量调度系统的 Agent 沙箱。差异化在于 GPU/CPU 混合资源管控和批量 Agent 任务优先级调度。
- `TencentCloud/CubeSandbox`：腾讯云的 Agent 安全沙箱方案。容器安全增强 + seccomp/AppArmor + 可插拔运行时（Python/Node.js/Go 模板）。与腾讯云基础设施有潜在绑定。
- `NVIDIA/NemoClaw` (~21.5k stars)：OpenShell 容器之上的安全 Agent 运行时封装。细粒度权限控制（文件路径 + 网络地址 + 系统调用白名单），凭证通过加密通道注入沙箱且不落盘。
- `anthropics/cwc-long-running-agents`：Anthropic 的长时间运行 Agent 参考实现，Docker 沙箱 + Claude Computer Use 协议。核心价值在于任务中断恢复、检查点管理和 Human-in-the-Loop 审查模式。
- `strands-agents/shell`：沙箱化 Shell 执行组件，遵循 strands-agents 统一的 Tool 接口规范。容器内执行任意 Shell 命令，支持临时会话（用完即毁）和持久化会话。
- `agentscope-ai/agentscope-runtime`：Python 的 Agent 运行时框架，Docker/nsjail 双沙箱引擎。OpenTelemetry 全链路可观测，中间件链模式（鉴权/限流/审计）。
- `agentscope-ai/agentscope-runtime-java` (~167 stars)：Java 版 AgentScope 运行时。基于 Java SecurityManager + 自定义 ClassLoader 隔离（但 SecurityManager 在 JDK 17+ 已 deprecated），gRPC 通信层，面向企业 Spring Boot 集成。

**适用场景**：
- 绝大多数 Agent 代码执行场景（Coding Agent、数据分析、自动化脚本）
- 已有 K8s 基础设施的团队
- 需要在隔离性和启动速度之间取得工程平衡的中等安全需求

**局限**：
- 共享宿主机内核，容器逃逸漏洞历史上屡见不鲜
- K8s 方案的冷启动（Pod 调度 + 镜像拉取）往往在数秒到数十秒，对亚秒级交互式 Agent 不够友好
- 多运行时后端的统一抽象层稳定性和行为一致性是普遍的工程难题

---

### 方向 3：进程级轻量隔离 -- 速度优先，零基础设施依赖

**核心思路**：利用 OS 原生安全基元（macOS Seatbelt / Linux bubblewrap / seccomp）或语言级沙箱（WASM / V8 isolates）实现隔离。不需要 Docker，不需要 VM，不需要 K8s -- 直接包装任意进程。启动延迟接近零，是最好的开发者体验方案，但隔离强度也是最低的。

**代表项目**：
- `anthropic-experimental/sandbox-runtime` (~2k stars)：Anthropic 为 Claude Code 开发的进程级沙箱。macOS 使用 `sandbox-exec` 动态生成 Seatbelt 配置文件，Linux 使用 `bubblewrap` + 网络命名空间。HTTP + SOCKS5 双代理网络过滤，TLS Termination（实验性 MITM 解密），npm 全局安装即用。安全默认策略（网络/文件写入全部拒绝，allow-only 模式）。代表了「不需要容器」路线的最高工程水平。
- `DTVMStack/DTVM` (~158 stars)：面向 AI Agent 的确定性虚拟机。以 WASM 为字节码格式，利用 WASM 的沙箱隔离和确定性执行语义。核心创新在于「确定性系统接口 (DSI)」-- 封装文件系统、时钟、随机数等非确定性系统调用，提供确定性替代实现，确保 Agent 操作可审计、可复现。支持 VM 状态快照与回滚。
- `cloudflare/sandbox-sdk`：Cloudflare 的边缘沙箱 SDK。基于 Cloudflare Workers 的 V8 isolates 机制，毫秒级启动，全球 330+ 边缘节点部署。每个沙箱运行在独立 isolate 中。与 Cloudflare 生态深度绑定，适合已使用 CF 的团队。

**适用场景**：
- 本地开发者 Agent（Claude Code、Cursor、Copilot 等编码助手）
- MCP Server 的安全包装（一行命令 `srt` 即沙箱化）
- 边缘计算场景（Cloudflare Workers）
- 对启动延迟敏感（<100ms）且不需要 root 权限的 Agent

**局限**：
- 隔离强度显著低于 VM 和容器：macOS Seatbelt 和 Linux bubblewrap 的设计目标不是防御恶意代码，而是防御意外操作
- 不支持需要内核模块或特权操作的 Agent 工作负载
- WASM 路线（DTVM）的 GPU 推理和部分 C 扩展包支持受限
- Cloudflare sandbox-sdk 锁定 CF 生态，非 CF 用户无法使用

---

### 方向 4：安全策略、标准化与平台托管 -- 不造轮子，用现成的

**核心思路**：不直接提供沙箱执行环境，而是在现有沙箱之上提供安全策略、标准化接口或全托管平台。这是 Agent 沙箱生态的「上层建筑」。

**代表项目**：
- `antgroup/agent-aegis`：Agent 全生命周期安全防护插件。以轻量级插件形式嵌入 Agent 框架，覆盖 prompt 注入检测 -> 工具调用拦截 -> 输出内容过滤。TypeScript 实现，针对金融场景定制。与底层沙箱互补 -- aegis 管「Agent 行为安全性」，沙箱管「代码执行安全性」。
- `agent-infra/sandbox`：社区驱动的 Agent 沙箱 API 标准化尝试。定义 `sandbox.create` / `sandbox.run` / `sandbox.destroy` 的通用接口规范（类似 OCI 之于容器），目标是「Agent 框架和沙箱实现的解耦」。目前共识程度有限，主要沙箱厂商（E2B/腾讯/K8s）尚未明确表态采纳。
- **AWS Bedrock AgentCore 生态**（3 个项目）：
  - `aws/agentcore-cli`：新一代 CLI 工具，本地 `agentcore dev` -> 云端 `agentcore deploy` 一条命令
  - `awslabs/agentcore-samples`：官方示例集，覆盖代码执行沙箱、多工具编排、可观测性等最佳实践
  - `aws/bedrock-agentcore-starter-toolkit`：旧版 Python CLI 工具包，项目脚手架 + 本地调试 + CI/CD
  三者共同构成 AWS 的 Agent 托管平台入口，底层基于 Firecracker microVM，但用户无需关心 -- 全托管。
- `volcengine/agentkit-sdk-python`：火山引擎的 Agent 开发工具包。CLI 脚手架 + `@tool` 装饰器工具注册 + Docker/进程级沙箱执行 + OpenTelemetry 可观测。MCP 协议兼容。定位面向 Python 开发者的 Agent 快速启动体验。
- `google/ax`：Google 的分布式 Agent 运行时。将 Agent 抽象为可分布执行的单元，每个 Agent 在独立沙箱中运行，通过 gRPC 通信。基于 DAG 的任务依赖管理，支持多执行后端（本地进程/容器/云端）。可插拔架构。
- `microsoft/WindowsAgentArena`：微软研究院的 Windows Agent 评测平台。在 Azure Windows VM 中运行 Agent，通过磁盘快照回滚保证测试隔离。150+ 预定义任务，规模化并行测试（数百个 VM 实例）。本质是特殊用途的沙箱 -- 评测而非生产执行。
- `agentscope-ai/AgentTeams`：协作式多智能体操作系统。核心不在沙箱本身，而是多 Agent 协作协议和 Human-in-the-Loop 机制。每个 Agent 在隔离上下文中执行，但隔离策略由平台统一管理。

**适用场景**：
- 不想自建基础设施、愿意使用云厂商托管方案的团队
- 需要在现有沙箱之上增加安全策略层（Agent 行为安全 vs. 代码执行安全）
- 需要标准化接口以实现沙箱厂商可替换的 Agent 框架开发者

**局限**：
- 云厂商方案（AWS/火山引擎/Cloudflare）的供应商锁定风险
- Agent 沙箱 API 标准化（agent-infra/sandbox）的社区共识远未形成
- 安全策略层（agent-aegis）无法替代底层沙箱隔离，只能作为补充

---

## 当前趋势与开放争议

### 趋势

1. **凭据管理与沙箱解耦**：OpenShell 的出口网关注入、OpenSandbox 的 Credential Vault MITM 代理、NemoClaw 的加密凭证注入 -- 多个项目不约而同地把「Agent 不应该看到 API key」作为核心设计约束。这正在成为 Agent 沙箱的标配能力，而不仅是安全加固选项。

2. **多后端可插拔成为共识**：OpenShell（microVM/Podman/Docker/K8s 四后端）、OpenSandbox（Docker+K8s 双重后端）、kubernetes-sigs/agent-sandbox（RuntimeClass 集成 gVisor/Kata/Firecracker）-- 同一个沙箱接口支持不同隔离等级的后端切换，正在成为主流架构模式。

3. **从「能隔离」到「可观测」**：OpenTelemetry 集成几乎成为标配（ax、agentscope-runtime、AgentScope Runtime Java、agentkit-sdk-python、OpenSandbox），沙箱不仅要安全执行，还要让 Agent 的每一步操作可追踪、可审计。

4. **边缘 + 沙箱的融合**：Cloudflare sandbox-sdk 把代码执行推到了 CDN 边缘节点，Terrarium 的 Pyodide 模式在浏览器内运行 Python -- 沙箱不一定是后端服务，也可以是前端能力。

### 争议

1. **隔离强度 vs. 启动速度的不可调和矛盾**：MicroVM（E2B <200ms 冷启动）和进程级（sandbox-runtime 零启动）之间存在本质性的安全/速度权衡。争议在于：对于编码 Agent（最主流的沙箱使用场景），是否真的需要 VM 级隔离？还是容器级甚至进程级就足够？目前没有行业共识。

2. **标准化 vs. 碎片化**：agent-infra/sandbox 试图定义统一的 Sandbox API，但 E2B 有自己的 API，OpenSandbox 有自己的 OpenAPI 规范，K8s 有自己的 Sanbbox CRD。Agent 框架开发者面临「选哪个沙箱后端」的碎片化困境。标准化成功与否取决于大厂（E2B/Anthropic/K8s社区）是否愿意妥协采纳统一接口。

3. **GPU 沙箱的工程挑战**：AgentCube 和 OpenShell 都在尝试 GPU 沙箱（GPU 显存分配、VFIO 直通、MIG 隔离），但 GPU 虚拟化的粒度远不如 CPU/内存。多租户 GPU 集群中的安全隔离（防止显存侧信道攻击、GPU 时间片公平分配）仍是开放问题。

4. **确定性的价值与代价**：DTVM 提出「Agent 代码执行应该确定性可复现」，这对审计和调试极具吸引力。但确定性意味着要裁剪掉大量非确定性系统调用（时钟、随机数、某些网络 I/O 模式），这在实际 Agent 场景中可能严重限制功能。确定性沙箱是未来方向还是过度设计，尚无定论。

5. **安全策略的边界划分**：Agent 安全应该由沙箱底层保证（隔离执行），还是由策略插件保证（行为审计），还是两者兼有？agent-aegis（策略层）和 sandbox-runtime（隔离层）代表了两种不同的安全哲学。实际生产中，两者不是互斥而是互补，但「谁该负责什么」的边界共识正在形成中。

---

## 项目全景表

| 项目 | Stars | 隔离层级 | 核心差异 | 活跃度 |
|------|-------|---------|---------|--------|
| `NVIDIA/OpenShell` | ~20k | MicroVM/Container 多后端 | 凭据代理出口网关 + GPU VFIO 直通 + OPA 策略引擎 | 高 (Rust 多 crate 工作区，15+ 模块) |
| `NVIDIA/NemoClaw` | ~21.5k | Container (OpenShell) | OpenShell 之上的安全封装，细粒度权限白名单，凭证不落盘 | 中 |
| `e2b-dev/infra` | ~7.5k | MicroVM (Firecracker) | <200ms 冷启动，API-first，Agent 沙箱的事实标杆 | 高 (Go, ~94k 行代码) |
| `coder/coder` | ~8.5k | Container/VM (Terraform) | 开发环境即代码，Terraform 模板化工作空间 | 高 |
| `opensandbox-group/OpenSandbox` | ~1k+ | Container + 增强隔离 (gVisor/Kata/Firecracker) | 协议驱动，5 语言 SDK + MCP 原生集成，Credential Vault | 中高 |
| `kubernetes-sigs/agent-sandbox` | ~500+ | Container/VM (K8s RuntimeClass) | K8s 原生的 Agent Sandbox CRD 规范，社区标准化方向 | 中 |
| `openkruise/agents` | ~300+ | Container (K8s Operator) | Sandbox CRD 生命周期自动化，GPU/NPU 支持，seccomp/AppArmor | 中 |
| `anthropic-experimental/sandbox-runtime` | ~2k | 进程级 (OS 原生) | 零容器零 VM，macOS Seatbelt + Linux bubblewrap，Claude Code 安全底座 | 中高 (TypeScript+Rust) |
| `cloudflare/sandbox-sdk` | ~500+ | V8 Isolates (边缘) | 全球 330+ 边缘节点，毫秒级启动，Cloudflare 生态绑定 | 中 |
| `DTVMStack/DTVM` | ~158 | WASM 字节码 | 确定性执行，状态快照与回滚，跨语言 WASM 统一抽象 | 低 (早期) |
| `cohere-ai/cohere-terrarium` | ~300 | Container (Docker) + 浏览器 (Pyodide) | 双运行时架构，轻量极简，专为 LLM Data Agent 设计 | 低 |
| `TencentCloud/CubeSandbox` | ~200+ | Container (腾讯云增强) | 腾讯云容器安全增强方案，可插拔运行时模板 | 低 |
| `volcano-sh/agentcube` | ~100+ | Container (K8s Volcano) | GPU/CPU 混合资源管控，批量 Agent 任务优先级调度 | 低 |
| `antgroup/agent-aegis` | ~300+ | 安全策略层 (插件式) | Agent 全生命周期安全防护，prompt 注入检测 + 工具调用审计 + 输出过滤 | 低 |
| `anthropics/cwc-long-running-agents` | ~500+ | Container (Docker) | 长时间运行 Agent 参考实现，任务中断恢复 + HITL | 低 |
| `aws/agentcore-cli` | ~100+ | 平台托管 (Firecracker) | AWS Bedrock AgentCore CLI 入口，本地开发 + 云端部署 | 中 |
| `awslabs/agentcore-samples` | ~100+ | 平台托管 (Firecracker) | AWS Bedrock AgentCore 官方示例和最佳实践 | 低 |
| `aws/bedrock-agentcore-starter-toolkit` | ~50+ | 平台托管 (Firecracker) | AWS Bedrock AgentCore Python CLI 工具包（旧版） | 低 |
| `volcengine/agentkit-sdk-python` | ~500+ | Container/进程级 | 火山引擎 Agent SDK，CLI 脚手架 + 工具注册 + MCP 兼容 | 中 |
| `google/ax` | ~1k+ | Container/进程/云 | Google 分布式 Agent 运行时，DAG 任务调度 + 可插拔后端 | 中 |
| `agentscope-ai/agentscope-runtime` | ~200+ | Container (Docker/nsjail) | Python Agent 运行时，OpenTelemetry 全链路可观测 | 低 |
| `agentscope-ai/agentscope-runtime-java` | ~167 | JVM 级 (SecurityManager) | Java 企业版 Agent 运行时，Spring Boot 集成 + gRPC | 低 |
| `agentscope-ai/AgentTeams` | ~500+ | 平台管理 (隔离上下文) | 多 Agent 协作 OS，Human-in-the-Loop 深度集成 | 低 |
| `microsoft/WindowsAgentArena` | ~500+ | VM (Azure Windows + 快照回滚) | Windows Agent 基准评测平台，150+ 任务，规模化并行测试 | 低 |
| `agent-infra/sandbox` | ~100+ | API 规范层 | Agent 沙箱标准化接口规范，可插拔后端设计 | 极低 |
| `strands-agents/shell` | ~50+ | Container (Docker) | 沙箱化 Shell 执行组件，Tool 接口标准化 | 极低 |
| `NVIDIA/OpenShell-Community` | ~50+ | Container (Docker) | OpenShell 社区发行版，更快的更新节奏 | 极低 |

*注：Star 数量为近似值，部分低星项目的精确数字需从 GitHub 实时获取。活跃度基于代码 commit 频率、社区参与度和项目阶段综合判断。*

---

## 按场景的选型建议

| 场景 | 推荐技术方向 | 首选项目 | 备选 |
|------|------------|---------|------|
| 本地编码 Agent (Claude Code 等) | 进程级轻量隔离 | `sandbox-runtime` | -- |
| 生产多租户 SaaS (强安全) | MicroVM 硬件隔离 | `e2b-dev/infra` | `OpenSandbox` (gVisor/Firecracker) |
| K8s 集群 Agent 沙箱 | 容器级 (K8s 原生) | `kubernetes-sigs/agent-sandbox` | `openkruise/agents` |
| GPU Agent 沙箱 | MicroVM + GPU 直通 | `NVIDIA/OpenShell` | `volcano-sh/agentcube` |
| 企业级 Java Agent | JVM 容器级 | `agentscope-runtime-java` | `coder/coder` |
| 轻量 Python 数据分析 Agent | 容器级 | `cohere-terrarium` | `agentscope-runtime` |
| 边缘计算 Agent | 进程级 (V8/WASM) | `cloudflare/sandbox-sdk` | `DTVM` |
| Agent 安全审计 (已有沙箱) | 安全策略插件 | `antgroup/agent-aegis` | -- |
| 不想运维基础设施 | 平台托管 | AWS Bedrock AgentCore | 火山引擎 AgentKit |
| Agent 评测 | VM 快照回滚 | `WindowsAgentArena` (Windows) | -- |
