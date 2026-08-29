# deepseek-harness

> [`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness) · DeepSeek 官方 agent harness，一切皆插件

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-08-13 · commit `47f9438` · TypeScript · 2319文件/~497K行 · 42465n/92315e  
**入口** · `packages/core/agent-loop/src/agent.ts`(ReactLoopAgent.step 主循环) · `packages/interaction/commands/src/index.ts`(CommandRuntime) · `packages/boot/app-boot`(profile 组合启动)  
**架构** · Cordis 插件树：54 个插件包按子系统分组（core/client/session/llm/tools 类），无特权核心；`core/agent-loop` 实现 React 式 agent loop，`interaction/commands` 提供用户命令运行时，profile/bundle 分层组合（dsh-base → dsh-web-app/dsh-headless）  
**热点** · `agent-loop`(ReactLoopAgent) · `interaction/commands`(CommandRuntime) · `session`(append-only event log) · `llm`(adapter seam) · `client`(2813 nodes 最大包)
<!-- END AUTO -->

---

## 定位
> DeepSeek AI 于 2026-08-13 发布的官方开源 agent harness（`dsh`），核心理念 "Everything is a Plugin"。团队作为观察者关注：Cordis 插件化 agent 架构范式（无特权核心、全部能力可替换）、DeepSeek 模型生态的原生 agent 运行时形态，以及对现有 agent-framework 竞争格局的影响。

## 项目介绍
> DeepSeek Harness (`dsh`) — DeepSeek AI 开发的智能体脚手架，提供 Web UI 和 headless 两种运行形态，上线即 42k+ stars。

核心场景：
- **Web UI 交互**：`npx @deepseek-ai/dsh web` 启动浏览器界面，与 agent 多轮协作
- **Headless 一次性运行**：`dsh-headless` bundle 提供无服务器的一次性任务执行
- **插件化扩展**：通过 `dsh-plugin` 生态（Cordis 插件）扩展模型适配、工具、持久化等全部能力
- **Profile 组合**：声明式 profile（bundle 有序堆叠 + patch 覆盖）定义定制化 agent 运行时

## 技术要点
- **Cordis 插件架构**：一切皆插件——模型适配器、工具注册表、会话日志、agent loop 本身都是插件，可在配置层替换；无特权核心，插件卸载时注册效果自动回滚（reversible effects）
- **Profile/Bundle 分层组合**：profile = 有序 bundle 列表 + `cordis.patch.yml` 覆盖层；`dsh-base` 提供基础层（模型/工具/持久化/沙箱/审批策略），`dsh-web-app`/`dsh-headless` 提供运行形态层
- **事件驱动扩展点**：三类事件——Session events（持久事实，可重放）、Agent events（在途工作流观察/拦截）、Capability events（向 seam 注入策略和适配器，无需导入 loop）
- **Scoped 注册原语**：`core/scope` 提供 per-agent 的注册作用域，实现 agent 间能力隔离

## 技术栈
- TypeScript · Node.js · Cordis（插件框架）· pnpm workspace monorepo · Vitest（测试）

## 关联
- [cordiverse/cordis](https://github.com/cordiverse/cordis) — 上游依赖，插件框架（时空可组合性编程范式）
- [Koishi 生态](https://koishi.chat) — Cordis 源自 Koishi 聊天机器人框架生态
- 竞品关系：Claude Code / Codex CLI 类 agent harness 的直接竞品
- 📄 [时空可组合性论文](../../../references/cordiverse/spatiotemporal-composability/summary.md) — Cordis 设计论文（PKU×DeepSeek，88页），dsh 插件架构的理论底座，已在 KG 归档

## 开放问题
> _随 delta 追加_
