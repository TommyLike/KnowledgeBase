# openlit

> [`openlit/openlit`](https://github.com/openlit/openlit) · 上游贡献 · 基于 OpenTelemetry 的 LLM 应用性能监控平台，自动插桩 OpenTelemetry 收集 GPU/LLM/Agent 的全栈性能指标

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 待 /kg-refresh  
<!-- END AUTO -->

---

## 定位
> OpenLIT 是 LLM 可观测性领域注重 GPU/基础设施监控的方案——与 Langfuse（偏 Trace 和 Prompt 管理）不同，OpenLIT 同时关注 GPU 利用率、VRAM、推理延迟等硬件指标和 LLM token 成本。在 Agent 基础设施可观测中，OpenLIT 填补了「GPU 资源管理」这一缺口。

## 项目介绍
> **GPU + LLM 全栈可观测——不仅追踪 API 调用，更监控底层的 GPU 利用率和推理成本。**

核心场景：
- **GPU 资源监控**：实时追踪 Agent 推理时的 GPU 利用率、显存、温度
- **LLM 调用可观测**：Token 成本、延迟、错误率的全链路追踪
- **成本分摊**：按 Team/Project/Model 维度分析 GPU 和 API 成本

## 技术要点
- **OpenTelemetry 自动插桩**：基于 OTel 标准，自动收集 Trace 和 Metric
- **GPU 指标采集**：NVIDIA DCGM / NVML 采集 GPU 指标
- **可视化 Dashboard**：内置 Grafana 风格的可视化面板

## 技术栈
Python, OpenTelemetry, NVIDIA DCGM, Grafana, Apache 2.0

## 关联
- [`langfuse/langfuse`](../langfuse/) — 竞品/互补，Langfuse 偏 Trace+Prompt，OpenLIT 偏 GPU 监控
- [`traceloop/openllmetry`](../openllmetry/) — 同为 OTel 标准，OpenLLMetry 是 SDK，OpenLIT 是平台

## 开放问题
- [ ] 2026-07-02 GPU 指标的采集频率和精度是否能满足实时 Agent 推理的调度决策需求？
