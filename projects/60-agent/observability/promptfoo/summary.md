# promptfoo

> [`promptfoo/promptfoo`](https://github.com/promptfoo/promptfoo) · 上游贡献 · LLM 红队测试和安全评估框架，系统化测试 Prompt Injection/Jailbreak/PII 泄露等安全风险

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · TypeScript · 21,261n/65,359e  
<!-- END AUTO -->

---

## 定位
> Promptfoo 是 LLM 安全评估领域的红队工具——不做可观测性追踪，不做 RAG 质量评估，专注一件事：找到 Prompt 和模型的安全漏洞。在 Agent 安全生态中，Promptfoo 是安全工程师的瑞士军刀：编写 YAML 测试用例 → 批量对 LLM 执行攻击 → 自动生成漏洞报告。团队关注 LLM 安全测试的自动化方法论。

## 项目介绍
> **LLM 的红队测试框架——用声明式测试用例系统化检测 Prompt 注入、越狱和敏感信息泄露。**

核心场景：
- **Prompt Injection 测试**：批量执行已知注入攻击向量，检测模型是否被 bypass
- **Jailbreak 评估**：用已知越狱 Prompt 测试，评估防护有效性
- **PII/敏感信息泄露检测**：诱导模型输出敏感信息，检测防护机制
- **多模型安全对比**：同时测试 GPT-4o / Claude / Gemini 等模型的安全表现

## 技术要点
- **YAML 声明式测试**：测试用例以 YAML 定义，包含 prompt 变体、断言和预期结果
- **内置攻击库**：预置 100+ 注入攻击和越狱 Prompt 模板
- **多 Provider 支持**：同时测试 50+ LLM Provider，安全对比一目了然
- **CI/CD 集成**：作为 GitHub Actions 安全检查，不通过不部署
- **可视化报告**：Web UI 展示测试结果、漏洞分布和修复建议

## 技术栈
TypeScript, YAML, OpenAI/Anthropic API, MIT

## 关联
- [`protectai/llm-guard`](../../security/llm-guard/) — 互补，LLM-Guard 做运行时安全防护，Promptfoo 做评估期安全测试
- [`confident-ai/deepeval`](../deepeval/) — 互补，DeepEval 做质量评估，Promptfoo 做安全评估

## 开放问题
- [ ] 2026-07-02 Promptfoo 的漏洞检测能否跟上 LLM 安全攻击的进化速度？攻击库的更新机制是社区驱动还是团队维护？
