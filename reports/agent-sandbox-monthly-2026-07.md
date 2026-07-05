# Agent Sandbox 生态月度报告（2026-06-05 ~ 2026-07-05）

> 分析范围：7 个 agent-runtime/sandbox 项目（含新增 anthropic-experimental/sandbox-runtime），基于 GitHub PR、Issue、Commit 数据。

---

## 一、总览

| 项目 | Stars | 30d 提交 | 30d 合并 PR | 核心定位 | 活跃度 |
|------|-------|---------|------------|---------|--------|
| **coder/coder** | 13.7k | 494 | 20+ | 远程开发平台 → Agent 工作空间 | 🔥🔥🔥🔥🔥 |
| **opensandbox-group/OpenSandbox** | 11.8k | 276 | 20+ | 通用 Sandbox 框架（Docker/K8s） | 🔥🔥🔥🔥 |
| **TencentCloud/CubeSandbox** | 7.3k | 195 | 20+ | 腾讯云安全沙箱 | 🔥🔥🔥🔥 |
| **e2b-dev/infra** | 1.2k | 176 | 20+ | Firecracker Agent 沙箱 API | 🔥🔥🔥 |
| **kubernetes-sigs/agent-sandbox** | 3.1k | 80 | 20+ | K8s 原生 Sandbox CRD | 🔥🔥 |
| **agent-infra/sandbox** | 5.3k | 6 | 6 | 沙箱 API 规范 | ⭐ |

---

## 二、各项目详细分析

### 2.1 coder/coder — 开发平台向 Agent 工作空间的战略转型

**本月关键词：Agent UI、Template Builder、移动体验**

coder 是本月最活跃的项目（494 commits），核心动向是**加速从「开发者 IDE 平台」向「Agent 工作空间平台」转型**：

**主要 PR 方向：**

| 方向 | 代表 PR | 说明 |
|------|---------|------|
| Agent 聊天 UI | #26964, #26965 | 移动端 Agent Chat 键盘适配、模型选择器优化 |
| Template Builder | #26938, #26935 | 新建模板页面的 provisioner 警告和禁用逻辑 |
| AI Bridge | #26971 | Bedrock STS assume-role 客户端修复（AWS AI 集成） |
| 聊天后端重构 | #26942 | 移除 chatd 旧的 model-routing dispatch shim |
| 工作空间管理 | #26948 | 自动停止倒计时改用相对时间 |

**讨论方向：**
- 从 Template Builder 和 Agent Page 的频繁 UI 迭代可以看出，coder 正在构建**非开发者的 Agent 工作空间创建体验**
- AI Bridge 组件（对接 Bedrock/Vertex AI 等）持续迭代，表明 coder 正将 AI 能力作为工作空间的一等公民
- 移动端 Agent Chat UI 的专项优化说明团队重视「随时随地与 Agent 交互」的场景

**值得关注的 Issue（推测基于迭代方向）：**
- Agent 工作空间的生命周期管理与普通开发工作空间的差异化
- 多租户 Agent 沙箱的计费和资源配额

---

### 2.2 opensandbox-group/OpenSandbox — 通用沙箱框架的成熟化

**本月关键词：Docker 桥接、K8s 诊断、CI 自动化**

OpenSandbox 是 stars 最多的沙箱项目（11.8k），本月重点在**生产可靠性增强和部署体验优化**：

**主要 PR 方向：**

| 方向 | 代表 PR | 说明 |
|------|---------|------|
| Docker 网络 | #1182 | 新增 bridge-mode 可配置端口范围 |
| Docker 安全 | #1172 | egress ipv6 sysctls 跳过（无 procfs 时） |
| K8s 诊断 | #1151 | 容器日志读取增强（308 行改动） |
| K8s 快照 | #1164 | 回退到已停止的快照容器 |
| 镜像发布 | #1161 | 新增 ghcr 镜像发布支持 |
| 事件循环 | #1171 | 修复 image pull 阻塞事件循环 + 优雅关闭 |
| CI 改进 | #1152 | PR 标签自动应用（替换评论方式） |
| 清理 | #1178 | 移除未使用的 PendingSandbox 机制（-377 行） |

**讨论方向：**
- Docker bridge 模式持续增强说明项目在 Docker 和 K8s 两个 runtime 上都在投入
- 移除 PendingSandbox 等废弃机制表明架构在简化
- ghcr 镜像发布和 CI 改进体现社区协作成熟度在提升
- 诊断能力的增强（容器日志、扩展信息在 lifecycle 响应中返回）表明生产可观测性是重点

---

### 2.3 TencentCloud/CubeSandbox — 多架构 + 性能优化双线推进

**本月关键词：ARM64、网络策略、一键部署**

CubeSandbox 保持高频迭代（195 commits），**腾讯云基础设施深度整合**是其核心特色：

**主要 PR 方向：**

| 方向 | 代表 PR | 说明 |
|------|---------|------|
| 多架构支持 | #720, #715 | 多架构 CI（x86+ARM64）、aarch64 完整构建 |
| 网络性能 | #727 | cubevs 网络策略应用开销优化（-96/+271） |
| Egress 增强 | #726, #723 | 明文 HTTP 凭据注入、路由感知出口 |
| 一键部署 | #720, #725, #731 | 多架构 CI + vmlinux 上传 + Terraform 改进 |
| 调度优化 | #721, #722 | Cubelet 上报间隔调至 1s、打分策略配置 |
| 快照/锁优化 | #749 | 快照运行时活跃绑定表 + MySQL 死锁修复 |
| 文档 | #731, #736, #739 | 路线图、ARM64 安装指南、v0.5.0 中英双语 changelog |

**讨论方向：**
- 多架构（ARM64）支持是本月最明确的战略投入，意味着 CubeSandbox 在拓展非 x86 场景（如 ARM 服务器、边缘设备）
- 网络策略性能优化（271 行改动）说明大规模集群下的网络策略 overhead 是实际瓶颈
- 一键部署 + Terraform 改进是降低接入门槛的关键举措
- 中英双语文档和路线图透明化，表现出社区开放治理的倾向

---

### 2.4 e2b-dev/infra — 生产化打磨：TTL、快照、可观测性

**本月关键词：租户隔离、快照管理、Hugepage 指标**

E2B 本月聚焦**SaaS 平台的多租户运营能力和生产稳定性**：

**主要 PR 方向：**

| 方向 | 代表 PR | 说明 |
|------|---------|------|
| 租户事件 TTL | #3181, #3179 | per-team events TTL 限制（按 tier+addons 分层） |
| 沙箱生命周期 | #3200 | 沙箱 duration 强制 clamp，防止超长运行 |
| 快照过滤 | #3184 | 按名称过滤快照（+410/-197） |
| 编排器指标 | #3182 | 上报 hugepage 指标到 API（+358/-218） |
| 数据修复 | #3203 | 处理沙箱停止时间的损坏数据 |
| 清理维护 | #3183 | 移除 best-of-k 等废弃 feature flag（-82 行） |
| 安全更新 | #3188 | Go 1.26.4 CVE 修复 |
| OTEL 增强 | #3206 | S3 存储客户端增加 OTEL instrumentation |

**讨论方向：**
- per-team TTL 和沙箱 duration clamp 表明 E2B 正在从「技术验证」走向「SaaS 运营」——需要精确的资源生命周期控制和成本核算
- Hugepage 指标上报说明大内存场景（如 LLM 推理沙箱）是用户实际需求
- 快照过滤功能的 400+ 行改动说明快照管理是重点投入方向
- 移除废弃 feature flags 说明产品方向在收敛
- Issue #3193（orchestrator 缺少独立超时执行导致 VM 泄漏）是一个关键可靠性问题

---

### 2.5 kubernetes-sigs/agent-sandbox — 生态建设：示例、文档、依赖升级

**本月关键词：Warm Pool、示例丰富、K8s 版本跟进**

K8s SIG 项目本月重点在**降低用户上手门槛和跟随 K8s 主干版本升级**：

**主要 PR 方向：**

| 方向 | 代表 PR | 说明 |
|------|---------|------|
| Warm Pool | #1053, #1050 | SandboxWarmPool kubectl 输出增强 + metrics label |
| 文档/示例 | #1043, #1040, #1023 | Playwright 示例、Cilium egress 示例、GKE 用户指南 |
| 依赖升级 | #1046, #1036, #1037 | golangci-lint v2、controller-runtime v0.24.1、k8s v0.36.2 |
| Bug 修复 | #1035, #1032, #1027 | AsyncSandboxClient cleanup、race condition 修复 |
| 跨平台 | #1062 | Chrome sandbox 入口跨平台编译修复 |

**讨论方向：**
- Warm Pool 功能的持续投入说明「冷启动延迟」是 Agent 沙箱的核心体验瓶颈
- 大量示例文档（Playwright、Cilium、GKE）说明项目在主动降低接入门槛
- 紧随 K8s 最新版本（v0.36.2）表明项目在 SIG 中有较强的维护力量
- 与 v0.5.0 发布（6/24）同步，功能和示例都在快速补齐

---

### 2.6 agent-infra/sandbox — 文档规范期，代码变动少

**本月关键词：文档、安全示例、版本同步**

agent-infra/sandbox 本月只有 6 个提交，主要是文档和安全示例的补充：

| PR | 说明 |
|-----|------|
| #215 | 安全绑定 Sandbox 示例到 localhost（+443/-74） |
| #212 | v1.11.0 版本同步文档 |
| #207 | Codex 配置文档新增 |
| #217 | docker-compose 内容修正 + 镜像版本固定 |
| #216 | API key 示例补充 |
| #177 | volcengine 错误处理修复 |

**讨论方向：**
- 代码层面变化少表明 API 规范趋于稳定
- `localhost` 安全绑定和 API key 示例说明项目在补安全最佳实践
- 作为规范层项目，低代码变动可视为成熟信号

---

## 三、跨项目趋势分析

### 3.1 六个项目的定位分层

```
        agent-infra/sandbox (API 规范 — 标准制定)
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
OpenSandbox  CubeSandbox  k8s-sigs/agent-sandbox
(Docker/K8s  (腾讯云深度   (K8s 原生 CRD
 通用框架)    集成沙箱)     Warm Pool)
    │          │          │
    └──────────┼──────────┘
               │
               ▼
         e2b-dev/infra (SaaS API — Firecracker 极致性能)
               │
               ▼
         coder/coder (终端用户面 — Agent 工作空间)
```

### 3.2 三大共同趋势

**趋势一：多运行时/多架构成为标配**

CubeSandbox 的 ARM64 完整构建、OpenSandbox 的 Docker+K8s 双运行时、k8s-sigs 的跨平台编译修复——所有项目都在面向多架构和多运行时场景演进。Agent 沙箱不能假定 x86+Docker。

**趋势二：冷启动优化是核心体验瓶颈**

k8s-sigs 的 Warm Pool 功能、CubeSandbox 的 cubelet 上报间隔调至 1s、E2B 的快照过滤和管理功能——都是为了降低「Agent 需要沙箱 → 沙箱就绪」的延迟。这个指标直接决定了 AI Agent 的用户体验。

**趋势三：从「能用」到「可运营」的SaaS化转型**

E2B 的 per-team TTL、CubeSandbox 的一键部署、OpenSandbox 的 ghcr 发布——项目普遍在补**多租户资源管控、部署自动化、成本核算**等 SaaS 运营能力。Agent 沙箱不只是技术问题，更是平台运营问题。

### 3.3 差异化发展方向

| 项目 | 核心差异化方向 |
|------|---------------|
| **coder** | Agent 工作空间的**终端用户体验**——让非开发者也能创建和管理 Agent 环境 |
| **OpenSandbox** | **通用性和社区生态**——支持最多 runtime，降低所有场景的接入门槛 |
| **CubeSandbox** | **腾讯云深度整合**——一键部署、多架构、与腾讯云容器安全体系绑定 |
| **e2b** | **SaaS API + 极致性能**——Firecracker microVM，<200ms 冷启动 |
| **k8s-sigs** | **K8s 标准化**——Sandbox CRD 纳入 K8s 上游标准，Warm Pool 降低冷启动 |
| **agent-infra** | **API 规范共识**——定义沙箱通用接口，与 OCI 之于容器的角色类比 |

---

## 四、需要关注的问题

1. **coder 的 Agent 转型深度**：coder 有 13.7k stars 和最强的开发活跃度，但其 Agent 功能目前主要在 UI 层（Agent Chat）。是否会像 E2B 那样在底层做 Firecracker 级的安全隔离？还是依靠 K8s/Docker 的安全策略？

2. **E2B 的 SaaS 定价模型**：per-team TTL 和 tier+addons 的引入表明 E2B 在建立商业化定价体系。开源版和云服务的功能边界如何划分值得关注。

3. **CubeSandbox 与腾讯云的绑定程度**：一键部署深度集成腾讯云 Terraform，是否支持非腾讯云环境的独立部署对社区采用至关重要。

4. **k8s-sigs Sandbox CRD 的标准化进程**：v0.5.0 的功能已经相当完整（Warm Pool、多运行时、Cilium egress），但能否成为 K8s 上游标准取决于社区共识。agent-infra/sandbox 的规范层也在竞争这个标准定义权。

5. **OpenSandbox 的定位演变**：11.8k stars 但未与特定云厂商绑定，它是在走向「沙箱的 Kubernetes」（通用编排层），还是「被集成的组件」（各云厂商直接使用）？

---

## 五、数据来源

- GitHub PR/Issue 数据：通过 `gh pr list` / `gh issue list` / `gh search commits` 采集
- 统计周期：2026-06-05 ~ 2026-07-05
- 项目列表来源：知识库 `projects/agent-runtime/sandbox/` 目录
