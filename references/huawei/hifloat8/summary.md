# Ascend HiFloat8 Format for Deep Learning

> Yuanyong Luo 等（华为海思/中央硬件/计算产品线）· 2024 · arXiv:2409.16626v2 · 13 页白皮书 · [本地 PDF](paper.pdf) · [全文 markdown](paper.md)

## 中文摘要
本文是华为 HiFloat 项目的首篇公开白皮书，提出新型 8 位浮点格式 **HiFloat8（HiF8）**。HiF8 在 IEEE 754 基础上增加了一个 **点位域（dot field）**，用非传统前缀码实现**锥形精度（tapered precision）**：常规数编码中，7 个指数值配 3 位尾数、8 个指数值配 2 位尾数、16 个指数值配 1 位尾数；非常规数（denormal）编码额外扩展 7 个 2 的幂次，动态范围从 31 个 binade 扩到 38 个（FP16 为 40 个）。格式由四字段构成：符号（1 位）+ 点位（2-4 位前缀码）+ 指数（D 位符号-幅值码，隐含最高位）+ 尾数（1-3 位）。支持全部特殊值（Inf/NaN/Zero，正负零合并）。由于精度与动态范围取得更好平衡，HiF8 可同时用于训练的前向与反向。论文给出舍入方法（TA/混合舍入）、三种训练策略（BLS 反向损失缩放 / ALS 自适应损失缩放 / PTS 逐张量缩放）与三种推理方案（直接转换 / PTS / SmoothQuant）。实验：传统网络（ResNet/ViT/YoLo/DeepLab 等 20 个模型）HiF8 与 FP16 损失曲线高度重合、验证精度差 ±0.4% 内；LLM（T5-11B、LLaMA-7B、GPT3-6.7B/13B，Book3+OpenWebText2+Wikipedia 数据）训练 PPL 与 FP16 相当（如 12.05→12.20），推理 PTQ 三种方案均近无损。

## English Abstract
This preliminary white paper proposes HiFloat8 (HiF8), a novel 8-bit floating-point format for deep learning featuring tapered precision. HiF8 adds a dot field to IEEE 754, using unconventional prefix codes: normal values get 7 exponent values with 3-bit mantissa, 8 with 2-bit, 16 with 1-bit; denormal values extend the dynamic range by 7 extra powers of two (31→38 binades; FP16 covers 40). Four fields: sign (1 bit), dot (2-4 bit prefix code), exponent (D-bit sign-magnitude with hidden MSB), mantissa (1-3 bits). All special values supported (pos/neg zero merged). Thanks to the better precision/dynamic-range balance, HiF8 works in both forward and backward passes. The paper describes rounding methods (TA / hybrid), three training strategies (BLS backward loss-scaling / ALS adaptive loss-scaling / PTS per-tensor scaling) and three inference schemes (direct-cast / PTS / SmoothQuant). Experiments: 20+ traditional networks (ResNet/ViT/YoLo/DeepLab) show HiF8 loss curves highly overlapping FP16, validation accuracy within ±0.4%; LLM training (T5-11B, LLaMA-7B, GPT3-6.7B/13B on Book3+OpenWebText2+Wikipedia) matches FP16 PPL (e.g. 12.05→12.20); LLM PTQ inference near-lossless with all three schemes.

## 技术要点
- **点位域（Dot Field）+ 锥形精度**：指数/尾数切分不固定——大数值多分位给指数（动态范围），小数值多分位给尾数（精度）。点位用非传统前缀码（小值 4 位、中值 3 位、大值 2 位编码），即时可译
- **动态范围对比**（含 denormal）：HiF8 [-22,15] vs FP16 [-24,15] vs E4M3 [-9,8] vs E5M2 [-16,15]——HiF8 以 8 比特逼近 FP16 的 40 个 binade，是 E4M3 的近 4 倍
- **训练策略**：BLS（继承 FP16 混合精度）→ ALS（scale window 按 {1,20,...,1000} 列表自适应升降，解决 LLM 早期梯度剧变）→ PTS（逐张量 2 的幂缩放，类似 Transformer Engine 但无需每迭代算 Amax）
- **推理优势**：动态范围自足，直接转换（direct-cast）即近无损；SmoothQuant 可作为异常值兜底
- **单一格式覆盖训推**：这是 HiF8 相对 FP8 双格式（E4M3 前向/E5M2 梯度）的定位差异；结论预告了 HiFloat 8 位以下的后续成果（即 HiF4）

## 关联项目
- [`sgl-project--sgl-kernel-npu`](../../projects/sgl-project/sgl-kernel-npu/summary.md) — HiF8 是昇腾 NPU 的低精度主线格式，kernel 适配需考虑
- [`vllm-project--vllm-ascend`](../../projects/vllm-project/vllm-ascend/summary.md) — vLLM 昇腾适配的量化格式背景
- [`cosdt--vllm-ascend`](../../projects/cosdt/vllm-ascend/summary.md) — 团队 vllm-ascend fork 的量化侧背景
- [`huawei--hifloat4`](../hifloat4/summary.md) — 同系列 4 位格式论文（姊妹篇）
