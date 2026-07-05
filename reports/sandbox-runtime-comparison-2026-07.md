# Anthropic Sandbox Runtime (srt) vs. 其他 Agent Sandbox 方案对比

> 基于项目代码、README 和 GitHub 数据分析

---

## 一、根本差异：srt 是什么（不是什么）

**srt 是进程级 OS 原生沙箱，不是容器/VM 沙箱。**

```
                   srt                          其他 6 个项目
             ┌──────────────┐           ┌──────────────────────────┐
隔离层级      │   OS 进程级    │           │  VM / 容器 / K8s 基础设施  │
             │ sandbox-exec  │           │  Firecracker / Docker / │
             │ bubblewrap    │           │  Kubernetes / containerd │
             └──────────────┘           └──────────────────────────┘
启动方式      npm install -g               docker pull / kubectl apply
使用方式      srt <任意命令>                API 调用或 K8s CRD 创建
目标场景      Claude Code 本地开发           Agent 云平台 / 企业级部署
分发方式      npm 包 (TypeScript)           容器镜像 / Helm Chart
开发方        Anthropic                     独立公司/云厂商/SIG
```

---

## 二、核心差异矩阵

| 维度 | srt | E2B infra | k8s-sigs agent-sandbox | CubeSandbox | OpenSandbox | coder | agent-infra sandbox |
|------|-----|-----------|----------------------|-------------|-------------|-------|-------------------|
| **隔离层级** | OS 进程级 | VM 级 (Firecracker) | 容器级 (K8s) | 容器级 (腾讯) | 容器级 (Docker/K8s) | 容器/VM | 规范层 |
| **安全模型** | OS 原生 (Seatbelt + bubblewrap) | KVM 硬件虚拟化 | K8s RuntimeClass | 腾讯云安全策略 | Docker/K8s 安全 | 混合 | API 接口定义 |
| **冷启动** | **<1ms** (进程包装) | **<200ms** (microVM 快照) | **秒级** (Pod + Warm Pool) | 秒级 | 秒级 | 30s-2min | N/A |
| **隔离强度** | 中 (OS 级别) | 高 (硬件虚拟化) | 中-高 (取决于 Runtime) | 中-高 | 中-高 | 中-高 | N/A |
| **无特权要求** | ✅ 是 | ❌ 需要 KVM | ❌ 需要 K8s 集群 | ❌ 需要 K8s/容器 | ❌ 需要 Docker/K8s | ❌ 需要基础设施 | N/A |
| **本地开发** | ✅✅ 完美 | ⚠️ 需要 KVM | ❌ 需要 K8s | ❌ 需要容器 | ⚠️ 需要 Docker | ⚠️ 需要基础设施 | N/A |
| **部署模型** | npm 全局安装 | SaaS API + 自建 | K8s 集群内 | 腾讯云/K8s | Docker/K8s | 自建平台 | N/A |
| **语言** | TypeScript | Go | Go | Go | TypeScript/Go | Go | TypeScript |
| **网络隔离** | HTTP+SOCKS5 代理 | VM 网络栈 | K8s NetworkPolicy | cubevs 网络策略 | Docker net/iptables | 平台层 | 接口定义 |
| **文件隔离** | OS seatbelt/bwrap | VM 独立磁盘 | Volume/PVC | 容器 overlay FS | Docker volume/bind | 工作空间 | 接口定义 |
| **可观测性** | 违规日志流 (macOS) | OTEL+hugepage 指标 | K8s 原生监控 | K8s 指标 | 内置诊断 | 平台仪表盘 | 接口定义 |
| **生产就绪** | Beta Research Preview | ✅ 商业 SaaS | K8s SIG 孵化 | 腾讯云生产 | 开源生产 | ✅ 商业产品 | 社区规范 |
| **Stars** | 4,579 | 1,211 | 3,062 | 7,298 | 11,817 | 13,705 | 5,337 |

---

## 三、关键差异化特点

### 3.1 srt 独占优势

**1. 零基础设施依赖**

```
其他方案：需要 Docker daemon / K8s 集群 / KVM 内核模块 / Firecracker 二进制
srt：    npm install -g @anthropic-ai/sandbox-runtime，然后 srt <cmd>
```

这是 srt 最核心的差异化——不需要任何基础设施。一个 Node.js 开发者 `npm install` 后就能用。E2B 需要 Firecracker 和 KVM，k8s-sigs 需要完整的 Kubernetes 集群，CubeSandbox 需要容器运行时。

**2. 进程级包装的零成本启动**

`srt curl https://example.com` —— 包装一个进程的开销几乎为零。没有 VM 创建、没有容器镜像拉取、没有 Pod 调度。对于 Agent 在本地执行 `cat` / `curl` / `npm` / `git` 等日常命令的场景，VM 或容器级别的隔离是过度的。

**3. macOS + Linux 双平台原生**

macOS 上使用 Apple Seatbelt（与 macOS 系统完整性保护相同的框架），Linux 上使用 bubblewrap（Flatpak 使用的容器技术）。没有跨平台兼容性问题。

**4. 为 Claude Code / Agent 场景深度定制**

- MCP Server 沙箱化：`.mcp.json` 中将 command 改为 `srt` 即可
- 违规实时告警：通过 macOS `log stream` 实时监控被拦截的沙箱违规
- TLS Termination：可选的 HTTPS 流量内容检查（实验性）
- 安全默认策略：网络默认全禁，写操作默认全禁

### 3.2 srt 的局限性

**1. 隔离强度不如 VM**

```
VM 级 (E2B Firecracker): 恶意代码无法突破 KVM → 即使 srt 内的进程被攻破，
                          也无法突破到 Host 内核
OS 级 (srt):             依赖 macOS/Linux 内核的沙箱机制 →
                          历史上有 Seatbelt 逃逸和 bwrap 提权漏洞
```

**2. 不适用于多租户场景**

srt 设计用于**单用户本地开发**（Claude Code 用户在自己的机器上运行），不支持多租户隔离、资源配额、计费等 SaaS 运营能力。E2B 的 per-team TTL 和 tier+addons 是 srt 完全不具备的。

**3. Linux 平台依赖 bubblewrap**

macOS 的 Seatbelt 是系统级框架（成熟稳定），但 Linux 依赖 bubblewrap（用户态工具），存在系统兼容性问题（某些 Linux 发行版不预装或版本过旧）。

**4. 没有分布式/集群场景**

srt 完全是本地工具。Agent 要在云端跑？要跨多台机器？srt 不是答案。

---

## 四、选型决策树

```
你要运行 Agent 的环境？
├── 本地开发机器 (macOS/Linux) —— 个人使用
│   └── → srt ✅ (最简单、最轻量)
│
├── 团队共享的云环境 —— 多用户
│   ├── 安全隔离是最高优先级 (不可信代码)
│   │   └── → E2B ✅ (Firecracker VM 隔离)
│   ├── 已有 K8s 基础设施
│   │   └── → k8s-sigs agent-sandbox ✅
│   ├── 在腾讯云上
│   │   └── → CubeSandbox ✅
│   └── 需要通用、可移植方案
│       └── → OpenSandbox ✅
│
└── 完整 Agent 工作空间平台 (IDE + Terminal + Agent)
    └── → coder ✅
```

---

## 五、补充说明

### srt 与 E2B 不是零和竞争

两者解决不同层的问题：

```
srt (本地开发)          E2B (云端生产)
    │                       │
用户笔记本                 云端 K8s 集群
npm install srt            API 调用 E2B Cloud
srt curl ...               sandbox.create()
                           sandbox.runCode("print(1)")
                           sandbox.destroy()
```

一个合理的架构可能是：**本地用 srt 做开发和测试，生产用 E2B/k8s-sigs 做部署和运营**。

### srt 对其他项目的影响

srt 的出现（4,579 stars in 8 months）验证了 **"Agent 安全需要分层——不是所有场景都需要 VM 级隔离"** 这一命题。这可能会推动其他 sandbox 项目增加更轻量的本地执行模式。
