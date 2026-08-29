# A Programming Paradigm for Spatiotemporal Composability

> Yifan Shi, Wei Zhang (Peking University), Tianyi Cui (DeepSeek-AI) · 2026 · [PDF](https://github.com/cordiverse/paper/blob/main/paper.pdf) · 88 pages

## 中文摘要
现代软件——从插件系统到自进化智能体脚手架——越来越需要**动态组合**，但其形式化基础仍不成熟。本文识别出动态组合的两个正交维度：**时间可组合性**（组件卸载时其副作用能被完全安全地撤销）和**空间可组合性**（组件间依赖能被声明式地响应式管理）。论文将经典 effect/coeffect 概念提升到运行时机制：形式化了**可逆效应**（每次上下文变换携带逆变换并由运行时追踪）与**响应式共效应**（上下文每次变化按组件声明通知其激活/停用/中性）。两者统一到单一 Context 类型，构成一个编程范式；再组合为组件概念，给出动态组合演算（calculus），其元理论将时空可组合性从单个组件推广到整个交错组件系统。论文在 **Cordis** 中实现了这些思想——一个提供效应追踪与共效应解析核心库、声明式组件加载器（配置调和 + 热模块替换）的元框架。案例研究：Koishi。

## English Abstract
Modern software—from plugin systems to self-evolving agent harnesses—increasingly requires dynamic composition, yet its formal foundations remain underdeveloped. Two orthogonal dimensions: temporal composability (completely revert a component's side effects upon removal) and spatial composability (declare and reactively manage inter-component dependencies). The authors lift classical effect/coeffect concepts to runtime mechanisms: revertible effects (every context transformation carries an inverse tracked by the runtime) and reactive coeffects (each context change notifies a component against its coeffect specification). Unified into a single context type, constituting a programming paradigm; combined into the notion of a component with a calculus of dynamic composition whose metatheory carries spatiotemporal composability from a single component to whole interleaved systems. Implemented in Cordis—a meta-framework with effect tracking, coeffect resolution, declarative component loader with configuration reconciliation and hot module replacement. Case study: Koishi.

## 技术要点
- **Revertible Effects（可逆效应）**：每次上下文变换携带显式逆变换，运行时追踪；组件卸载时按序回滚全部副作用（资源分配、事件注册、状态变更）——解决 VSCode 类插件系统"卸载需重启"的时间维度问题
- **Reactive Coeffects（响应式共效应）**：组件以声明式规范描述所需依赖；上下文每次变化（服务出现/消失/被替换）自动通知受影响组件——解决插件间无结构契约的空间维度问题
- **Unified Context（统一上下文）**：效应上下文与共效应上下文合并为单一 Context 类型；共效应上的观察等价为效应提供独立性——构成编程范式
- **Calculus of Dynamic Composition（动态组合演算）**：组件生命周期（装载/卸载/迭代/异步/失败）的操作语义；元理论证明 Preservation、Temporal/Spatial Composability、Progress、Confluence
- **Cordis 元框架**：核心库（效应追踪 + 共效应解析）+ 声明式组件加载器（配置调和 + HMR）；Koishi 聊天机器人框架作为生产案例（累计装机数千万）

## 关联项目
- [`deepseek-ai--deepseek-harness`](../../projects/agent-framework/deepseek-harness/summary.md) — Cordis 是 dsh 的底座框架；论文 §1.2.2 明确以 self-evolving agent harnesses 为核心动机场景，dsh 是首个大规模应用
- [`anomalyco--opencode`](../../projects/coding-agent/opencode/summary.md) — 同类 agent harness 的竞品参照系（传统分层架构 vs Cordis 插件树）

## 关联
- **上游来源**：北京大学（Yifan Shi, Wei Zhang）+ DeepSeek-AI（Tianyi Cui）联合研究
- **下游实现**：cordiverse/cordis（元框架）、deepseek-ai/deepseek-harness（dsh）
- **理论渊源**：effect systems（Haskell IO monad 谱系）、coeffect systems（contextual typing 谱系）

## 备注
- 无 arXiv 版本；官方渠道为 GitHub cordiverse/paper 仓库（paper.pdf, 88 页）
- 📄 **中文全译本已归档**：[paper-zh.pdf](paper-zh.pdf)（30 页，pandoc/Docker XeLaTeX 编译）+ [paper-zh.tex](paper-zh.tex) 源文件。散文全译、数学符号保留原文、7 个定理/引理/推论编号沿用原文、图 1/图 2 以占位符指向原 PDF 第 29/34 页
- 数据引用：2026-06-09 VSCode Marketplace Top 100 扩展中 87 个含可执行代码需重启卸载、仅 7 个声明 extensionDependencies
- 论文 §6 讨论：系统边界、服务多路复用、访问控制与沙箱、语言无关性、相互依赖与组件粒度、依赖类型化与版本化、与语言/OS 协同设计
- 📄 配套前身文章已本地归档：[可逆的插件系统（Koishi 官方设计文档，2023，中文原文）](disposable-plugin-system-koishi-2023.md) + [PDF 版](disposable-plugin-system-koishi-2023.pdf)——Shigma 在论文前三年撰写的工程设计文章，含 effect 函子数学推导（幺半群→群→同态证明）与「逻辑/时间/空间三维可组合性」的最初表述
