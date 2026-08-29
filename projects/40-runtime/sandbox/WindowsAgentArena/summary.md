# Windows Agent Arena (WAA)

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

Windows Agent Arena 是微软研究院推出的面向 Windows 操作系统的 AI Agent 基准测试与可扩展沙盒平台。该项目在知识图谱中归类为 agent-runtime/sandbox，标签为「上游贡献」——团队关注其作为 Windows 桌面 Agent 评测基础设施的价值，可用于参考其沙盒架构设计、任务定义方法论及规模化评测实践。

## 项目介绍

Windows Agent Arena 提供了一个可复现、可扩展的 Windows Agent 评测框架，在真实的 Windows 虚拟机中运行 AI Agent 完成一系列桌面操作任务，并通过标准化指标评估 Agent 的能力。项目解决了 Windows 平台 Agent 评测缺乏统一基准的核心痛点，使不同 Agent 实现可以在相同环境下公平对比。

## 核心场景

- **Agent 基准评测**：在统一的 Windows 环境中对多个 AI Agent（如多模态模型 + 桌面操作框架）进行横向对比，覆盖 150+ 真实 Windows 任务。
- **规模化并行测试**：通过 Azure 云上虚拟机集群，支持同时运行数百个 Agent 实例，显著缩短评测周期。
- **Agent 能力分析**：从任务完成率、操作步数、成功率、时间效率等多个维度量化 Agent 在 Windows 桌面环境中的表现。
- **沙盒安全隔离**：每个 Agent 在独立 Windows VM 中运行，通过重置快照确保任务间互不干扰，避免 Agent 操作对宿主机产生影响。

## 技术要点

- **Windows 虚拟化沙盒**：基于 Azure Windows VM + 磁盘快照回滚机制，每次任务完成后自动将 VM 恢复到干净状态，保证测试隔离性和可复现性。
- **150+ 预定义任务集**：涵盖文件管理、浏览器操作、系统设置、Office 文档编辑、命令行操作、多媒体处理等多类 Windows 典型工作负载，难度分级（easy/medium/hard）。
- **多 Agent 框架适配**：通过统一的任务接口和观察空间（截图 + 可访问性树 + OCR 文本），支持接入不同 Agent 后端（如 GPT-4V、Claude Computer Use 等）。
- **评估指标体系**：包含任务成功率（Success Rate）、首次尝试通过率（Pass@1）、平均完成时间、平均操作步数等，提供多维度能力雷达图。
- **Azure 云原生编排**：利用 Azure VM Scale Sets 实现弹性伸缩，支持按需启动/销毁 Windows VM，降低大规模评测的基础设施成本。
- **安全边界设计**：VM 网络隔离、快照自动回滚、任务超时熔断（默认 120 秒），确保 Agent 的任意操作不会逃逸沙盒。

## 技术栈

- **语言**: Python（核心调度与评估逻辑）、PowerShell（Windows 自动化脚本）、TypeScript（部分 Web 相关工具）
- **虚拟化**: Azure Virtual Machines (Windows 10/11)、磁盘快照
- **Agent 框架**: 兼容多种框架（UFO、OS-Copilot、Claude Computer Use、自定义 Agent）
- **可观测性**: Azure Monitor、自定义遥测管道
- **编排**: Azure VM Scale Sets、Docker（管理节点）
- **评估**: 自定义评估 pipeline + 指标可视化（matplotlib/seaborn）

## 关联

- **上游**: 无直接上游依赖，设计理念受 OSWorld、WebArena 等 Agent 评测基准启发
- **同类项目**: OSWorld（Ubuntu 桌面 Agent 评测）、WebArena（Web Agent 评测）、SWE-bench（代码 Agent 评测）、AndroidWorld（Android Agent 评测）
- **Agent 框架生态**: UFO（微软 Windows Agent）、Claude Computer Use（Anthropic）、OS-Copilot
- **潜在关联**: 团队主导的 Agent 相关项目（如 agent-runtime 类别下的其他项目）可参考 WAA 的评测方法论和沙盒架构

## 开放问题

- WAA 当前仅支持 Windows，跨平台（Linux/macOS）扩展方案待探索
- 任务集偏向 GUI 操作，对 CLI 和编程类 Agent 任务的覆盖有限
- 评测成本较高（Windows VM 许可 + Azure 计算资源），小团队使用门槛偏高
- Agent 观察空间是否应增加更丰富的上下文（如窗口层次结构、应用状态）尚在讨论中
