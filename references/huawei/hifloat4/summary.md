# HiFloat4 Format for Language Model Inference

> Yuanyong Luo, Jing Huang, Yu Cheng 等（华为）· 2026 · arXiv:2602.11287v2 · 8 页 · [本地 PDF](paper.pdf) · [全文 markdown](paper.md)

## 中文摘要
本文提出 **HiFloat4（HiF4）**，一种面向大模型推理的 4 位块浮点（BFP）格式，是 HiFloat 项目 8 位以下成果的公开披露。每个 HiF4 单元打包 64 个 4 位元素 + 32 位共享缩放元数据，**平均 4.5 bit/值**（与 NVFP4 持平）。元数据实现**三级层次缩放**：L1 全局基缩放 E6M2（8 位，偏置 48，全局动态范围 69 个 binade，NVFP4 的 E4M3 仅 22 个）→ L2 8 路 1 位微指数 → L3 16 路 1 位微指数，逐级细化组内指数差异、抑制异常值影响。4 位元素为符号-幅值 S1P2（等价 E1M2），**有效精度 3 位**（NVFP4 的 E2M1 仅 2 位）。由于组大小 64 恰好匹配 64 长点积的 PE 输入宽度，矩阵乘可以高度定点化执行：一个 HiF4 单元对即可喂满 PE，而 NVFP4（组 16）需要 4 对；64 长点积下 HiF4 增量面积仅为 NVFP4 的约 1/3、功耗低约 10%。论文回顾了 4 位 BFP 三条路线（MX4 被 AMD 放弃、MXFP4 仅限 weight-only、NVFP4 用 E4M3 缩放），并给出 BF16→HiF4 转换算法与硬件建议。实验在 LLaMA、Qwen、Mistral、DeepSeek-V3.1、LongCat 等模型上，HiF4 直接转换即**全面超越 NVFP4 直接转换与 NVFP4+PTS**，是更精确的 4 位 BFP 格式。

## English Abstract
This paper introduces HiFloat4 (HiF4), a 4-bit block floating-point (BFP) format for LLM inference, disclosing the sub-8-bit achievement of the HiFloat project. Each HiF4 unit packs 64 4-bit elements with 32 bits of shared scaling metadata, averaging 4.5 bits/value (same as NVFP4). The metadata implements a three-level scaling hierarchy: L1 global base scale E6M2 (8-bit, bias 48, 69 binades global dynamic range vs NVFP4's 22 with E4M3) → L2 8-way 1-bit micro-exponents → L3 16-way 1-bit micro-exponents, refining intra-group exponent differences and suppressing outliers. The 4-bit element is sign-magnitude S1P2 (equivalent E1M2) with 3-bit significand precision (NVFP4's E2M1 has only 2). The 64-element group matches the 64-length dot-product PE input width exactly, enabling highly fixed-point matrix multiplication: one HiF4 unit pair feeds a PE, versus 4 pairs for NVFP4 (group 16); incremental area ≈1/3 of NVFP4 and ~10% lower power for 64-length dot products. The paper reviews three 4-bit BFP lineages (MX4 abandoned by AMD, MXFP4 weight-only, NVFP4 E4M3 scale), presents the BF16→HiF4 conversion algorithm and hardware guidance. On LLaMA, Qwen, Mistral, DeepSeek-V3.1 and LongCat, HiF4 direct-cast consistently surpasses both NVFP4 direct-cast and NVFP4+PTS — a more accurate 4-bit BFP format.

## 技术要点
- **三级层次缩放（three-level scaling hierarchy）**：L1 E6M2 全局基缩放（连接所有微指数）+ L2 8 路 E1（每个连接两个相邻 L3）+ L3 16 路 E1 微指数——全局/组间/组内动态范围分而治之，用 1 位粒度细粒度表达组内变化
- **组大小 64 的硬件动机**：Tensor Core/Cube Core 的 64 长点积 PE 要求下，HiF4 一对单元即可匹配 PE 输入宽度，NVFP4（组 16）需四对；E6M2/E4M3 浮点元数据在累加树里引入乘加器，HiF4 增量面积约为 NVFP4 的 1/3、功耗低约 10%
- **有效精度 3 位 vs 2 位**：S1P2（符号-幅值，等价 E1M2）比 NVFP4 的 E2M1 多 1 位有效精度；本地动态范围 4.81 vs 3.58 binade
- **与 MXFP4 路线对比**：MXFP4 组 32 元数据 4.25 bit/值，但组内仅 E2M1 且无层次缩放，精度退化被业界公认（仅 weight-only，如 GPT-OSS）；HiF4 用层级缩放解决了 4 位 BFP 的精度崩溃问题
- **直接转换即最优**：HiF4 direct-cast 全面超越 NVFP4 direct-cast 与 NVFP4+PTS——缩放机制内化进格式本身，推理框架无需额外校准管线

## 关联项目
- [`sgl-project--sgl-kernel-npu`](../../projects/sgl-project/sgl-kernel-npu/summary.md) — HiF4 面向 Cube Core 64 长点积设计，是昇腾 kernel 适配的格式背景
- [`vllm-project--vllm-ascend`](../../projects/vllm-project/vllm-ascend/summary.md) — vLLM 昇腾适配的低精度格式背景
- [`huawei--hifloat8`](../hifloat8/summary.md) — 同系列 8 位格式论文（姊妹篇，白皮书结论预告本文）
