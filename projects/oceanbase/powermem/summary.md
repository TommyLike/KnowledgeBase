# PowerMem

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

PowerMem 是 OceanBase 开源的 AI Memory 插件，属于 agent-runtime 生态中的记忆管理组件。本项目为上游贡献关注，团队关注其在 AI Agent 记忆管理领域的技术方案和工程实践，评估其在多 Agent 协作和长上下文场景中的适用性。

## 项目介绍

PowerMem 是一个面向 AI Agent 的精准记忆插件，核心理念是"Accurate, Agile, Affordable"——提供准确、敏捷且低成本的内存管理能力。它将传统数据库的存储引擎能力引入 AI Agent 的记忆管理，解决大模型上下文窗口有限、跨会话状态丢失、记忆检索精度不足等核心痛点。PowerMem 在 OceanBase 数据库团队的工程基因下构建，强调数据可靠性和查询效率。

## 核心场景

- **Agent 长期记忆管理**：为 AI Agent 提供跨会话的持久化记忆能力，支持记忆的存储、检索、更新和遗忘，使 Agent 在多次交互中保持上下文连续性。
- **多 Agent 共享记忆**：在多个 Agent 协作场景中，提供共享记忆空间，支持 Agent 之间的信息传递和知识共享，避免重复上下文注入。
- **精准语义检索**：基于向量索引和混合检索策略，从大规模记忆中快速召回与当前对话最相关的上下文片段，提升 Agent 回复的准确性和连贯性。
- **记忆生命周期管理**：支持记忆的自动衰减、重要性评分、冲突检测与去重，确保记忆库在持续增长时保持高质量和低冗余。

## 技术要点

- **存储引擎设计**：借鉴 OceanBase 数据库的存储技术，采用日志结构合并树（LSM-Tree）等高效数据结构管理记忆，兼顾写入吞吐和查询性能。
- **向量索引与混合检索**：集成向量数据库能力，支持 dense embedding + sparse keyword 的混合检索，通过 rerank 策略提升 top-K 记忆的召回精度。
- **记忆分层架构**：将记忆分为工作记忆（Working Memory）、短期记忆（Short-term Memory）和长期记忆（Long-term Memory）三层，不同层级采用不同的存储策略和检索优先级。
- **插件化集成**：以插件形式集成到主流 AI Agent 框架（如 LangChain、LlamaIndex）中，提供统一的 Memory 接口，降低接入成本。
- **记忆压缩与摘要**：支持对历史对话进行自动摘要和关键信息提取，在上下文窗口受限时用压缩表示替代原始对话，提升 token 利用率。
- **可观测性与评估**：内置记忆命中率、检索延迟、存储规模等指标，支持对记忆系统的效果评估和调优。

## 技术栈

- 语言：Python（主要）、Rust（存储引擎核心）
- LLM 框架：LangChain、LlamaIndex
- 向量数据库：Chroma / Milvus / FAISS
- 存储引擎：自研 LSM-Tree 存储
- 嵌入模型：OpenAI Embedding / 本地 Embedding 模型

## 关联

- 上游依赖：LLM 服务（OpenAI / 本地模型）、向量数据库
- 同类项目：Mem0、MemGPT、Cognee、Zep
- 所属组织：OceanBase（蚂蚁集团旗下分布式数据库团队）

## 开放问题

- PowerMem 在超大规模记忆（千万级以上）下的检索性能是否满足实时对话需求？
- 记忆压缩策略是否会导致关键信息的丢失，尤其在需要精确引用的场景中？
- 与 Mem0、MemGPT 等竞品相比，在记忆准确率和召回率上有无量化对比数据？
- 存储引擎的 Rust 核心与 Python 生态的 FFI 边界是否引入稳定性风险？
