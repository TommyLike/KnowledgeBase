# crewAI

> [`crewAIInc/crewAI`](https://github.com/crewAIInc/crewAI) · 上游贡献 · 面向生产的多 Agent 工作流编排框架，通过 Crews + Flows 双抽象实现从快速原型到企业自动化的全链路

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> CrewAI 是当前增长最快的 Multi-Agent 框架之一，以「角色驱动」和「事件驱动」双引擎覆盖从简单 Agent 团队到复杂企业工作流的全场景。在 Agent 生态中，CrewAI 填补了「开箱即用的角色型多 Agent 协作」这一空白——相比 LangGraph 的底层图编排，CrewAI 提供更高层的 YAML 配置 + 角色定义体验。团队关注其在生产环境中的适用性，以及 Crews+Flows 混合模式在企业自动化中的实践。

## 项目介绍
> **为 AI Agent 赋予角色和团队——用 YAML 定义 Agent 角色和任务，自动编排多 Agent 协同工作。**

核心场景：
- **角色型多 Agent 协作**：定义 Researcher / Writer / Reviewer 等角色，Agent 按角色分工完成研究→撰写→审核流程
- **事件驱动工作流**：通过 `@start`、`@listen`、`@router` 装饰器编排有状态的自动化流程
- **YAML 配置驱动**：`config/agents.yaml` + `config/tasks.yaml` 定义所有 Agent 和任务，代码与配置分离
- **Human-in-the-Loop**：关键步骤暂停等待人工审批，支持条件审批策略
- **企业自动化**：混合使用自主式 Crews 和确定性 Flows，兼顾灵活性与精确控制

## 技术要点
- **Crews 核心抽象**：每个 Crew 由 Role（角色）、Goal（目标）、Tools（工具）、Tasks（任务）四元组定义，Agent 按角色履职
- **Flows 事件驱动**：`@start` → `@listen(condition)` → `@router(condition)` 装饰器链定义状态流转，支持 `or_`/`and_` 条件组合
- **双重执行模式**：Sequential（顺序执行）和 Hierarchical（层级执行，由 Manager Agent 统一调度任务分配）
- **Pydantic 结构化状态**：工作流状态以 Pydantic 模型定义，类型安全 + 自动校验
- **Agent 能力矩阵**：内置 Tool Calling / Memory / Knowledge / Checkpointing / MCP / A2A 协议 / 多 LLM Provider
- **Crew + Flow 融合**：同一应用中混合使用 AutoAgent 自主决策（Crews）和确定性控制流（Flows）
- **商业支持 AMP Suite**：Enterprise 级追踪可观测性 + 统一控制面 + 私有化部署

## 技术栈
Python (98.7%), UV, OpenAI API, Ollama, LM Studio, Pydantic, MCP, A2A

## 关联
- [`langchain-ai/langgraph`](../langgraph/) — 竞品/互补，LangGraph 低层图编排，CrewAI 高层角色型抽象
- [`microsoft/autogen`](../autogen/) — 同为 Multi-Agent 框架，AutoGen 偏研究型对话驱动，CrewAI 偏生产级角色驱动
- [`langchain-ai/langchain`](../langchain/) — 依赖 LangChain 的 LLM/Tool 抽象

## 开放问题
- [ ] 2026-07-02 Crews + Flows 混合模式在大规模 Agent 团队（10+ Agent）时的状态管理和调度复杂性如何控制？
