# llm-guard

> [`protectai/llm-guard`](https://github.com/protectai/llm-guard) · 上游贡献 · LLM 安全防护工具包，提供 Prompt 注入检测、PII 脱敏、有害内容过滤和输出净化等安全组件

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> LLM-Guard 是 Protect AI 开源的 LLM 安全防护方案，在 Agent 安全生态中填补「输入输出安全网关」这一关键环节。Agent 在接收用户输入和生成输出时，需要通过安全检测防止 Prompt Injection、数据泄露和有害内容生成。LLM-Guard 提供了开箱即用的安全扫描 Pipeline，可以嵌入 Agent 的输入/输出通道中。

## 项目介绍
> **LLM 的安全防火墙——在 Agent 的输入输出通道中插入安全检测，过滤注入攻击、敏感信息和有害内容。**

核心场景：
- **Prompt Injection 检测**：识别用户输入中的恶意注入指令，防止绕过 Agent 的 system prompt
- **PII 脱敏**：检测并脱敏输入输出中的手机号/邮箱/身份证/地址/信用卡号
- **有害内容过滤**：检测暴力/色情/仇恨言论/自残等不安全内容
- **输出净化**：对 LLM 输出进行最后一道安全扫描，过滤不安全回答

## 技术要点
- **分类器 Pipeline**：输入→Anonymize(脱敏)→Ban Topics(话题检测)→Prompt Injection(注入检测)→Toxicity(毒性)→PII(隐私)等串行扫描
- **多模型后端**：支持 HuggingFace 分类模型、OpenAI Moderation API、本地 ONNX 模型
- **可配置阈值**：每种检测器独立配置敏感度和处理策略（flag/warn/block）
- **Python 库集成**：`from llm_guard import scan_prompt, scan_output` 两行代码完成安全检测
- **LLM-as-Judge 检测**：部分检测器使用 LLM 本身判断内容安全性

## 技术栈
Python, HuggingFace Transformers, ONNX, OpenAI Moderation API, Apache 2.0

## 关联
- [Protect AI](https://protectai.com) — 同团队，AI 安全企业
- [`langchain-ai/langchain`](../../../agent-framework/langchain/) — 可作为 LangChain Agent 的安全中间件

## 开放问题
- [ ] 2026-07-02 Prompt Injection 检测的准确率在新型攻击向量（multi-turn inject / image-based inject）下是否仍然可靠？
