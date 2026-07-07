# openkruise/agents

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

OpenKruise 团队推出的 Agent 沙箱 Operator，为 Kubernetes 上运行 AI Agent 所需的代码执行沙箱提供快速、低成本的部署与管理方案。本项目属于上游贡献范畴，团队主要关注其沙箱生命周期管理、多沙箱类型支持（Docker/containerd/VM）以及在昇腾等国产硬件平台上的适配潜力。

## 项目介绍

`openkruise/agents` 是一个 Kubernetes Operator，专注于为 AI Agent 提供可靠的代码执行沙箱环境。它将沙箱的创建、健康检查、生命周期管理、资源回收等操作抽象为 Kubernetes 自定义资源（CRD），让 Agent 应用可以像管理 Pod 一样管理沙箱实例，无需自行处理沙箱编排的复杂性。

## 核心场景

- **AI Agent 代码执行隔离**：Agent 需要在受控环境中执行不可信代码（如 LLM 生成的 Python 脚本），沙箱提供文件系统、网络、进程级别的隔离。
- **多租户沙箱管理**：在共享 Kubernetes 集群中为不同 Agent 或不同用户提供独立的沙箱实例，支持配额和资源限制。
- **批量沙箱编排**：一次性创建大量沙箱用于并行任务（如批量代码评测、自动化测试），Operator 负责调度和资源优化。
- **沙箱镜像预热与缓存**：通过镜像预拉取和快照机制缩短沙箱启动时间，提升 Agent 响应速度。

## 技术要点

- **自定义沙箱运行时抽象**：通过 `Sandbox` CRD 定义沙箱规格，解耦上层 Agent 逻辑和底层容器运行时，支持 Docker、containerd 及轻量级 VM（如 Kata Containers、Firecracker）等多种后端。
- **沙箱生命周期自动化**：Operator 管理沙箱的完整生命周期（Create → Ready → Running → Idle → Terminated），自动回收空闲沙箱以控制成本。
- **GPU 与 NPU 资源支持**：沙箱可声明 GPU/NPU 资源（如 NVIDIA GPU、昇腾 Ascend NPU），为 AI Agent 提供硬件加速的推理环境。
- **安全加固**：内置 seccomp、AppArmor、SELinux 策略模板，限制沙箱内进程的 syscall 行为；支持非 root 运行和只读根文件系统。
- **可观测性集成**：暴露 Prometheus 指标，记录沙箱创建耗时、活跃数量、错误率等运维关键数据。
- **与 Kruise 生态协同**：可配合 OpenKruise 的 CloneSet、SidecarSet 等高级工作负载实现更精细的沙箱编排，如原地升级、Sidecar 注入等。

## 技术栈

- **语言**：Go
- **框架**：Kubernetes controller-runtime / Kubebuilder
- **容器运行时**：Docker、containerd、Kata Containers
- **监控**：Prometheus metrics
- **平台**：Kubernetes 1.22+

## 关联

- **上游**：无直接上游依赖，基于 Kubernetes 原生 API 和 controller-runtime 构建
- **关联项目**：`openkruise/kruise`（OpenKruise 主项目，提供 CloneSet 等工作负载）、`openkruise/kruise-game`（游戏服务器沙箱管理）
- **同类项目**：`e2b-dev/infra`（E2B 云沙箱）、`codesandbox/codesandbox-operator`、`flyteorg/flyte`（ML 工作流沙箱执行）

## 开放问题

- 沙箱冷启动延迟如何收敛到 < 1s？镜像预热 + 快照方案的实际效果有待在大规模集群中验证。
- 多运行时后端的统一抽象层是否足够稳定？VM 级沙箱和容器级沙箱在安全性和性能上的取舍需要明确指引。
- Ascend NPU 虚拟化切分与沙箱绑定的方案尚未成熟，如何在沙箱内实现细粒度 NPU 分配是待探索方向。
