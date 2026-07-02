# backlog

> [`opensourceways/backlog`](https://github.com/opensourceways/backlog) · 团队主导 · AI 驱动的工作流编排与需求管理

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `?` · Markdown/Python · 10,872n/11,273e  
**入口** `.github/workflows/` → AI orchestrator pipeline  
**架构** Issue 管理 → AI 需求分析 → AI 架构设计 → AI 开发实现 → AI 测试 → 发布部署（全流程自动化）  
**热点** Workflow Requirement / Workflow Develop / Workflow Deploy Test  
<!-- END AUTO -->

---

## 定位
> 社区基础设施团队的需求与交付管理仓库，也是 AI Native 开发流程的核心编排引擎。管理所有社区项目从需求分析到生产发布的全生命周期，通过 AI Agent 自动完成需求文档、架构设计、代码实现、自动测试、预览部署和版本发布。团队自主设计开发的核心项目。

## 项目介绍
> **AI 驱动的全流程需求交付平台**，一条 GitHub Issue 从创建到上线全自动。

核心场景：
- **AI 需求分析**：提交 `[需求]` Issue → AI 自动生成需求分析说明书→ 人评审合入
- **AI 架构设计**：通过评审后 → AI 自动产出架构设计文档和设计 PR
- **AI 开发实现**：打 `accepted` + `project:` 标签 → AI 单命令完成 design + 代码 + 预览 + UT + 开 PR
- **预览环境部署**：每个 issue 分支自动部署到预览集群，真实 Vault 配置 + runtime-clone 源码
- **故障复盘**：`[缺陷]` Issue → AI 辅助根因分析 → 归档经验到 `context/experience/`

## 技术要点
- **Orchestrate Pipeline**：Jenkins + Python 编排的 5 阶段流水线（Requirement → Design → Develop → Deploy Test → Release）
- **预览集群隔离**：独立 K8s 集群 `infra-hk-preview-cluster-003`，per-service namespace，Vault userpass 读配置
- **Runtime Clone**：预览环境不构建镜像，pod 启动时现拉 issue 分支源码 + 装依赖 + 跑
- **确定性门禁**：security-gate + UT 覆盖率 + 格式检查在 PR CI 异步执行，不与 agent 内联阻塞
- **单命令直达**：`/ai-develop-preview` 一条命令完成设计+实现+预览+UT+开PR，面向开发者的最简入口

## 技术栈
Markdown（文档模板）· Python · Shell · Jenkins（流水线）· Kubernetes（预览集群）· Vault（配置管理）· GitHub Actions

## 关联
- [`opensourceways/infra-common`](../../projects/opensourceways/infra-common/) — 部署信息权威源（service.md）
- [`opensourceways/agent-development-specification`](../../projects/opensourceways/agent-development-specification/) — 团队层开发规范

## 开放问题
- [ ] 2026-06-30 preview-only 服务（如 meeting-server）何时推广到所有 umbrella？
