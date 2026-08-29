# sandbox

> [`agent-infra/sandbox`](https://github.com/agent-infra/sandbox) · 上游贡献 · Agent 基础设施社区的通用沙箱接口规范，定义 Agent 代码执行的标准化 API 和运行时抽象

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Agent Infra Sandbox 是一个社区驱动的沙箱接口标准化尝试——不提供具体的沙箱实现，而是定义 Agent 代码执行的通用 API 规范（类似 OCI 之于容器）。在 Agent 沙箱生态中，Sandbox 规范的愿景是「Agent 框架和沙箱实现的解耦」。

## 项目介绍
> **Agent 沙箱的标准化接口——定义 `sandbox.create`/`sandbox.run`/`sandbox.destroy` 的通用 API。**

核心场景：
- **沙箱实现可替换**：Agent 框架按标准接口调用，底层沙箱可切换 E2B/Firecracker/Docker
- **沙箱互操作性**：不同厂商的沙箱实现同一个规范

## 技术要点
- **通用 Sandbox API**：`create`/`run`/`destroy`/`upload`/`download` 标准操作
- **可插拔后端**：支持 Docker/K8s/Firecracker 等多种运行时
- **社区驱动**：Agent Infra 社区维护

## 技术栈
TypeScript, Docker, Kubernetes, MIT

## 关联
- [`e2b-dev/infra`](../../sandbox/infra/) / [`coder/coder`](../../sandbox/coder/) — 沙箱实现
- [agent-infra](https://github.com/agent-infra) — 同一社区组织

## 开放问题
- [ ] 2026-07-02 沙箱标准化的社区共识程度？主要沙箱厂商（E2B/腾讯云/K8s）是否愿意采纳？
