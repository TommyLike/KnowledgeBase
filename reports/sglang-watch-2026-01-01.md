# sgl-project/sglang 技术动态摘要

> 周期: 2026-01-01 ~ 2026-06-30 | 数据源: Releases / Issues / PRs / Discussions

---

## 版本变化

| 版本 | 日期 | 类型 | 间隔 |
|------|------|------|------|
| v0.5.14 | 06-26 | stable | 13 天 |
| v0.5.13 | 06-13 | stable | 18 天 |
| v0.5.12.post1 | 05-26 | stable | 10 天 |
| v0.5.12 | 05-16 | stable | 11 天 |
| v0.5.11 | 05-05 | stable | — |

**发版节奏**：约 **11-18 天一个 stable release**，2026 年上半年保持高频迭代。

---

## PR 方向聚类 (上周, 50 PRs 采样)

| 方向 | PR 数 | 占比 | 趋势 |
|------|-------|------|------|
| CI/测试 | 30 | 60% | 🔥 最高 |
| 文档 | 11 | 22% | |
| DeepSeek 适配 | 6 | 12% | ⬆️ 上升 |
| Diffusion 模型 | 5 | 10% | ⬆️ 新增方向 |
| NPU 支持 | 4 | 8% | ⬆️ Ascend |
| AMD GPU | 3 | 6% | |
| Blackwell (NVFP4) | 3 | 6% | 🆕 |
| 量化 | 3 | 6% | |
| 多模态 | 2 | 4% | |

**本周特征**：
- CI/测试占主导（60%），说明处于**质量加固期**
- DeepSeek 适配和 Diffusion 是增长方向
- NPU (Ascend) 和 AMD 的硬件适配活跃
- Blackwell NVFP4 是新出现的硬件支持方向

---

## 社区热点 (Issues)

Discussions 活跃度较低（👍 均为 0），Issue 按 reactions 排序无高热度结果。说明 SGLang 社区的讨论主要在 PR review 中发生，而非独立的 Issue/Discussion 线程。

---

## 竞争分析: SGLang vs vLLM

| 维度 | vLLM | SGLang |
|------|------|--------|
| 最新版本 | v0.24.0 (06-29) | v0.5.14 (06-26) |
| 发版节奏 | ~14 天 | ~13 天 |
| 硬件支持 | NVIDIA CUDA + Ascend + Intel | NVIDIA CUDA + AMD + NPU + Blackwell |
| 差异化 | PagedAttention (SOSP 2023) | RadixAttention + 压缩 FSM (NeurIPS 2024) |
| 亮点趋势 | 版本号跳变大 (v0.23→v0.24) | DeepSeek/Diffusion 新方向 |

**差距变化**：
- vLLM 在推理吞吐量上仍有文章优势（2-4× baseline），SGLang 在结构化输出（JSON/Regex 约束解码）和 Agent 多轮推理场景有 6.4× 优势
- SGLang 发版节奏与 vLLM 基本持平（~2 周），社区活跃度相当
- SGLang 近期在 **Diffusion 模型** 和 **多模态** 方向投入增加，可能是新的差异化点
- vLLM 版本号从 v0.23→v0.24 跳变大，暗示有较大架构变更

---

## 结论

1. **高频迭代稳定**：SGLang 保持 ~2 周一版的节奏，v0.5.x 系列趋于成熟
2. **质量加固期**：本周 60% PR 为 CI/测试，可能为 v0.6 大版本做准备
3. **DeepSeek 战略投入**：连续多周有 DeepSeek 相关 PR，说明团队重点适配国产大模型
4. **竞争格局**：vLLM 和 SGLang 在各自优势领域保持领先，尚未出现一方全面压倒另一方的趋势

---

*KG System | 2026-06-30 | /kg-watch sgl-project--sglang*
