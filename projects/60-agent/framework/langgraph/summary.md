# langgraph

> [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) · 上游贡献 · 用状态图 StateGraph 编排 Agent 循环与分支，支持持久化检查点和人机协作的 Agent 控制面

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `` · Python · 8,888n/53,042e  
<!-- END AUTO -->

---

## 定位
> LangGraph 是 LangChain 团队推出的低层级 Agent 编排引擎，解决传统 Chain 抽象无法表达循环、条件分支、状态共享和人机协作的问题。在 Agent 生态中，LangGraph 是「Agent 的调度器」——用 StateGraph 有向图决定 Agent 何时调用 LLM、何时使用 Tool、何时等待人类审批。团队将其作为 Agent 架构演进的核心关注对象。

## 项目介绍
> **Agent 编排的控制面——用有向状态图让 Agent 在多轮推理、工具调用和人工审批之间自由流转。**

核心场景：
- **ReAct Agent 循环**：Think → Act → Observe 经典循环，LLM 自主决定停止/调工具/求助
- **Multi-Agent 协作**：多个 Agent 通过子图嵌套和共享状态协作，每个 Agent 是独立节点
- **Human-in-the-Loop**：关键节点暂停等待人工审批，支持超时自动通过和条件审批策略
- **长时间运行工作流**：检查点持久化支持持续数小时甚至数天的 Agent 任务

## 技术要点
- **StateGraph 核心模型**：所有工作流以 `StateGraph<State>` 定义，State 是共享 Pydantic 对象。节点接收 State 返回更新，边定义流转，编译后生成 CompiledGraph
- **条件边动态路由**：根据 State 内容决定下一步（`next == "tool"` → 工具节点），这是 Agent 自主决策的基础机制
- **消息归并 Reducer**：`add_messages` reducer 实现消息追加而非覆盖，解决 LLM 上下文的增量更新
- **子图嵌套 Subgraph**：一个 StateGraph 可作为另一个图的节点，实现 Agent 层级的模块化复用
- **检查点持久化**：每个 super-step 自动创建检查点，支持 MemorySaver / SqliteSaver / PostgresSaver
- **streaming 多模式**：values / updates / messages / debug 等流式消费模式，适应不同场景需求
- **LangGraph Platform**：部署层（Server/API/Studio），将 Graph 作为 HTTP API 暴露，支持水平扩展和 A/B 测试

## 技术栈
Python, TypeScript, Pydantic, langchain-core, SQLite/Postgres, FastAPI

## 关联
- [`langchain-ai/langchain`](../langchain/) — 同一团队，LangChain 提供基础抽象，LangGraph 提供编排层
- [`microsoft/autogen`](../autogen/) — Multi-Agent 编排，与 LangGraph 在 Agent 协作场景竞争
- [`crewAIInc/crewAI`](../crewAI/) — Multi-Agent 框架，更高层抽象

## 开放问题
- [ ] 2026-07-02 检查点系统在大规模并发（1000+ threads）时的性能瓶颈？PostgresSaver 写入吞吐是否成为限制？
