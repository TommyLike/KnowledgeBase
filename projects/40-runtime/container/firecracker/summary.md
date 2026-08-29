# firecracker

> [`firecracker-microvm/firecracker`](https://github.com/firecracker-microvm/firecracker) · 上游贡献 · AWS 开源的轻量级 microVM 引擎，通过 KVM 在 125ms 内启动安全隔离的微型虚拟机，Agent 沙箱的安全基石

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Rust · 11,803n/50,782e  
<!-- END AUTO -->

---

## 定位
> Firecracker 是 AWS 为 Lambda 和 Fargate 开发的开源 microVM 引擎。在 Agent 基础设施中，Firecracker 扮演安全沙箱的角色——Agent 生成的代码需要在隔离环境中执行，Firecracker 提供了硬件级（KVM）安全隔离，同时在启动速度（125ms）和资源开销（<5MB 内存）上碾压传统 VM。是 Agent 安全执行的最底层防线，被 Fly.io、Koyeb 等广泛采用。

## 项目介绍
> **为无服务器和容器化工作负载设计的轻量级虚拟机——在硬件隔离的安全性和容器的速度之间找到最佳平衡点。**

核心场景：
- **Agent 代码执行沙箱**：Agent 生成的不受信任代码在 Firecracker microVM 中安全运行，即使代码恶意也无法突破 VM 边界
- **Serverless 函数执行**：AWS Lambda / Fargate 的底层引擎，每次函数调用在独立 microVM 中运行
- **多租户隔离**：每个用户/租户分配独立 microVM，共享物理机但彼此零信任
- **CI/CD Job 隔离**：每条 CI pipeline 的构建任务在隔离 microVM 中执行
- **边缘计算**：轻量到可以在边缘设备上运行多个隔离 microVM

## 技术要点
- **极速启动 125ms**：通过精简的 device model（仅 5 个模拟设备：virtio-net/block/rng/vsock/serial），microVM 从冷启动到可接收请求 <125ms
- **极小内存开销 <5MB**：Firecracker 进程本身占用 <5MB 内存，加上 guest kernel 和 rootfs 仍远低于传统 VM
- **硬件虚拟化 KVM**：利用 Linux KVM 的硬件辅助虚拟化实现真正的 CPU/内存/IO 隔离，非容器级别的 namespace 隔离
- **精简设备模型**：移除 BIOS、VGA、USB、PCI 等传统 VM 组件，仅保留 5 个 virtio 设备，攻击面极小
- **Rate Limiter**：内置 disk/network IOPS 和带宽限速器，防止单 VM 资源滥用影响共驻的其他 VM
- **Rust 实现**：用 Rust 重写自 Google crosvm，内存安全 + 零成本抽象，避免 C 代码的缓冲区溢出等安全问题
- **Snapshot/Restore**：支持 VM 状态的快照保存和快速恢复，实现毫秒级的 microVM 克隆和迁移
- **Jailer 沙箱**：Firecracker 进程通过 Jailer 二进制在严格 chroot + cgroup + seccomp 三明治中运行，即使 VMM 本身被攻破也有额外防线

## 技术栈
Rust, KVM, Linux Kernel, virtio, seccomp, cgroup, OpenAPI (API 规范)

## 关联
- [`e2b-dev/infra`](../../agent-runtime/sandbox/infra/) — E2B 使用 Firecracker 提供 Agent 安全代码执行沙箱
- [Kata Containers](https://github.com/kata-containers/kata-containers) — 同类项目，轻量级 VM 容器运行时
- [gVisor](https://github.com/google/gvisor) — 竞品，用户态内核实现容器隔离

## 开放问题
- [ ] 2026-07-02 Firecracker microVM 的快照恢复速度能否支撑 Agent 函数的毫秒级弹性伸缩（scale-to-zero + cold start）？
