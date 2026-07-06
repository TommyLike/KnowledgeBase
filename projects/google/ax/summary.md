# google/ax

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

Google 开源的分布式 Agent 运行时，属于 agent-runtime/sandbox 类别。团队以**上游贡献**方式参与，关注分布式 Agent 编排、沙箱执行环境、以及多 Agent 协作的工程落地。

## 项目介绍

ax（Agent eXecution）是 Google 推出的开源分布式 Agent 运行时，为构建和运行多 Agent 系统提供基础设施。它将 Agent 抽象为可分布执行的单元，支持任务分解、并行执行、状态管理，让开发者像编写单 Agent 应用一样自然地开发多 Agent 系统。

核心场景：
- **分布式 Agent 编排**：将复杂任务自动分解到多个 Agent 实例并行执行，支持跨节点调度和结果聚合
- **多 Agent 协作**：多个 Agent 之间通过消息传递进行通信与协作，实现复杂工作流的协同处理
- **沙箱执行环境**：每个 Agent 运行在隔离的沙箱中，提供安全的代码执行和工具调用能力
- **可观测性与调试**：内置追踪、日志和监控能力，便于开发者观察和调试分布式 Agent 系统

## 技术要点

- **分布式任务调度**：基于 DAG 的任务依赖管理，支持 Agent 任务的拓扑排序和并行调度，自动处理任务间的数据传递
- **Agent 生命周期管理**：统一的 Agent 创建、执行、监控、销毁生命周期，支持状态恢复和断点续传
- **沙箱隔离**：每个 Agent 运行在独立沙箱中，通过 gRPC/HTTP 进行跨进程通信，确保故障隔离和安全边界
- **可插拔后端**：支持多种执行后端（本地进程、容器、云端），可根据场景灵活切换
- **声明式配置**：通过 YAML/Protobuf 声明 Agent 拓扑和工作流，降低编排复杂度
- **OpenTelemetry 集成**：内置分布式追踪和指标导出，与现有可观测性生态无缝对接

## 技术栈

- 语言：Go（核心运行时）、Python（SDK 和工具链）
- 通信：gRPC、Protocol Buffers
- 容器化：Docker、Kubernetes
- 可观测性：OpenTelemetry

## 关联

- 上游：Google 内部 Agent 基础设施（具体代号未公开）
- 同类项目：LangGraph、CrewAI、AutoGen（均为 Agent 编排框架，ax 侧重分布式运行时层面）
- 依赖：gRPC、Protocol Buffers、OpenTelemetry SDK

## 开放问题

- ax 与 Google 内部 Agent 运行时的具体关系及开源策略路线图
- 分布式场景下的状态一致性和故障恢复策略的成熟度
- 与主流 LLM 框架（LangChain、LlamaIndex）的集成深度
- 社区治理模式：Google 主导的开源项目中社区贡献的实际影响力
