# Authenticated Workflows 论文分析

> [Archived] 2026-08-14 | 来源: arxiv read + translate 脚本（论文 2602.10465）
> 涉及资源: 论文 [Authenticated Workflows](https://arxiv.org/abs/2602.10465)（IEEE S&P 2026 投稿版）
> 本页为时间点快照，知识可能已过时。

## 核心结论

**论文**: Authenticated Workflows: A Systems Approach to Protecting Agentic AI
**作者**: Mohan Rajagopalan (MACAW Security), Vinay Rao (ROOST.tools)

1. **四个控制面完备且最小**：prompt / tool / data / context 是所有 agent 资源访问的必经边界（Lemma 6 枚举证明）。保护这四个面即可覆盖所有攻击入口，无需枚举攻击模式。
2. **确定性安全替代概率检测**：现有 guardrails/语义过滤器是概率性的（60-80% 检出率且可绕过）；认证工作流通过密码学签名实现"操作要么携带有效证明，要么被拒绝"——174 测试用例 100% 召回率、0 误报。
3. **By-design + By-policy 双重防御**：密码学消除（by-design）处理身份伪造、重放、策略替换；运行时策略执行（by-policy）处理权限提升、数据泄露。两者互补，单独使用均不充分。
4. **MAPL 策略语言将规模从 O(M×N) 降至 O(log M + N)**：通过层级继承（交集语义）+ 运行时动态主体解析 + 密码学证言（attestation）实现工作流时序依赖。
5. **9 框架零协议修改集成**：MCP/A2A/OpenAI/Claude/LangChain/CrewAI/AutoGen/LlamaIndex/Haystack 通过 200-500 行薄适配器接入，验证了抽象层次正确性。
6. **性能开销可忽略**：密码学操作 <0.2ms，PEP 端到端验证 <1ms（不含 LLM verifier），相对网络延迟（50-500ms）可忽略。

## 分析过程

1. `read-arxiv-paper` skill：下载 TeX 源 → 通读主文件 + 11 个章节文件 → 产出摘要
2. `arxiv-paper-translator` skill：4 个并行子智能体翻译全部 15 个 .tex 文件 → 审核（文件完整性/CJK catcode/命令拼写）→ 添加 xeCJK + Fandol 字体 → Docker XeLaTeX 编译 → 15 页中文 PDF
3. 编译修复：verbatim 框图制表符在 lmmono 缺失 → `\setmonofont{DejaVu Sans Mono}`

## 与 KG 的关联

- **agent-runtime 安全方向**：四控制面模型可作为 agent-runtime/{sandbox,tool,memory,security} 子类的安全参考架构
- **MCP/A2A 协议项目**：论文的协议级集成验证（MCP server→agent、A2A delegation→signed token）对 KG 中 MCP 相关项目有直接参考价值
- **策略语言设计**：MAPL 的层级组合 + attestation 模式可借鉴到团队 agent 平台（OpenShell 等）的权限设计
- **LLM API 安全**：one-sided / two-sided wrapping 模式对 API 网关类项目有借鉴意义

## 来源

- 论文 TeX 源: `arXiv_2602.10465/paper_source/`（本地缓存）
- 中文翻译: `arXiv_2602.10465/paper_cn/`（含编译后 15 页 PDF）
- arXiv: https://arxiv.org/abs/2602.10465
