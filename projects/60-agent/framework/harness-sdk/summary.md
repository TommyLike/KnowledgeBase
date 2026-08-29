# harness-sdk

> [`strands-agents/harness-sdk`](https://github.com/strands-agents/harness-sdk) · 上游贡献 · Strands Agents 的 Agent 评估与测试 SDK，为 AI Agent 提供标准化的性能基准和行为验证工具

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> Harness SDK 是 Strands Agents 推出的 Agent 评估 SDK，专注于 Agent 行为的可重复测试——与通用 LLM 评估框架（DeepEval/RAGAS）不同，Harness SDK 更关注 Agent 的端到端行为验证：给定输入，Agent 是否正确完成了多步骤任务。在 Agent 测试生态中，Harness SDK 填补了「Agent 行为基准测试」这一细分领域。

## 项目介绍
> **Agent 的行为测试 SDK——用标准化的测试用例验证 Agent 端到端任务的执行正确性。**

核心场景：
- **Agent 回归测试**：代码变更后自动验证 Agent 行为是否退化
- **多步骤任务验证**：验证 Agent 能否完整执行 search→analyze→write 的端到端流程
- **Agent 性能基准**：标准化测试套件衡量 Agent 在不同任务上的表现

## 技术要点
- **端到端行为测试**：测试的不是单一 LLM 调用，而是 Agent 的完整任务执行结果
- **声明式测试定义**：测试用例以结构化格式定义输入、预期行为和成功标准
- **可重复执行**：相同输入产生相同测试结果，适合 CI/CD 集成
- **Strands Agents 生态**：与 Strands 的 Agent 框架深度集成

## 技术栈
Python, Strands Agent Framework, MIT

## 关联
- [`strands-agents`](https://github.com/strands-agents) — 同一团队
- [`confident-ai/deepeval`](../../agent-runtime/observability/deepeval/) — 通用 LLM 评估框架，Harness 更偏 Agent 行为测试

## 开放问题
- [ ] 2026-07-02 Agent 行为测试的「正确性」标准如何定义？多步任务的成功判断是否依赖 LLM-as-Judge 的主观性？
