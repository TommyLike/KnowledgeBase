# vllm-report

> [`vllm-ascend/vllm-report`](https://github.com/vllm-ascend/vllm-report)

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> vllm-ascend 的日常提交监控与 AI 分析工具。每日自动拉取 vllm/vllm-ascend 新提交并做 AI 分析，为 vllm-ascend 代码升级和 main2main 适配提供知识库支撑。属于 vllm-ascend 生态的辅助工具。

## 项目介绍
> vllm-ascend 社区的提交监控和 AI 分析工具。核心场景：(1) 每日 GitHub Actions 拉取 vllm + vllm-ascend 最新提交及完整 diff (2) 两阶段 AI 分析：DeepSeek 批量分析提交意图/风险/影响，Claude Code Agent 深度分析涉及 Ascend 的关键变更 (3) 架构知识库覆盖 vllm (~70KB) 和 vllm-ascend (~90KB) 共 11 个维度 (4) 提供 25 个 MCP 工具的 stdio MCP Server，支持渐进式加载 (5) 邮件报告 + 暗色主题 Web Dashboard (6) 适配状态跟踪（pending / adapted）。

## 技术要点
- **两阶段 AI 分析流水线**：Phase 1 DeepSeek 批量分析 + 路径过滤跳过非 Ascend 相关提交，Phase 2 Claude Code Agent 深度分析受影响的接口和适配工作量
- **架构知识库**：覆盖模块、关键抽象、接口面、硬件抽象、跨项目关系等 11 维度，每周自动刷新
- **MCP Server**：25 个工具，4 个类别（架构分析、适配管理、变更分析、工程支持）
- **适配状态管理**：提交分为 pending（待适配）和 adapted（已覆盖）两态

## 技术栈
- Python · GitHub Actions · DeepSeek API · Claude Code · MCP

## 关联
- [`vllm-project/vllm-ascend`](../vllm-ascend/) — 主要服务目标，vLLM 昇腾 NPU 后端
- [`vllm-project/vllm`](../vllm/) — 上游 vLLM 引擎，监控其变更

## 开放问题
> _随 delta 追加_
