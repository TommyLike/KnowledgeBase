# agent-aegis

> [`antgroup/agent-aegis`](https://github.com/antgroup/agent-aegis) · 上游贡献 · 蚂蚁集团开源的 Agent 全生命周期轻量级安全防护插件

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> AgentAegis 是蚂蚁集团推出的 Agent 运行时安全防护插件，在 Agent 生态中聚焦「Agent 全生命周期运行时保护」——从 prompt 注入检测到工具调用拦截再到输出过滤，以轻量级插件形式嵌入 Agent 框架。

## 项目介绍
> **Agent 的安全防护盾——轻量插件式集成，覆盖 prompt→工具调用→输出的全链路安全检测。**

核心场景：
- **Prompt Injection 防护**：检测并拦截恶意 prompt 注入攻击
- **工具调用安全审计**：Agent 调用工具的权限校验和行为日志
- **输出内容过滤**：生成内容的敏感信息检测和合规过滤
- **金融场景 Agent 安全**：为风控/投研等金融 Agent 场景定制的安全策略

## 技术要点
- **全生命周期防护**：从 prompt 输入到工具调用再到输出，覆盖 Agent 运行的完整链路
- **轻量插件式集成**：以插件形式嵌入主流 Agent 框架，对业务代码侵入最小
- **金融场景定制**：针对蚂蚁内部金融场景（风控、客服、投研）的 Agent 安全需求优化
- **TypeScript 实现**：前端/Node.js Agent 安全检测，支持低延迟场景

## 技术栈
TypeScript, Node.js, Apache 2.0

## 关联
- [`protectai/llm-guard`](../../protectai/llm-guard/) — 竞品，LLM-Guard 是通用 LLM 安全方案
- [蚂蚁集团](https://www.antgroup.com) — 发起方

## 开放问题
- [ ] 2026-07-05 AgentAegis 的金融场景安全策略是否可以抽象为通用 Agent 安全标准？
