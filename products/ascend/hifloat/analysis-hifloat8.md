# Ascend HiFloat8 — 关键设计分析

> 来源: Ascend HiFloat8 Format for Deep Learning (arXiv:2409.16626, docling 转换)
> 日期:2026-07-07

---

## 一、定位

华为海思自研 8 位浮点格式。核心目标:**用一个格式(E4M3+E5M2 需要两个)同时覆盖训练的前向和后向传播**,在 8bit 极限下实现精度与动态范围的最佳平衡。

## 二、格式定义

HiF8 = Sign(1b) + Dot(2-4b) + Exponent(Db) + Mantissa([1,3]b)

| 字段 | 设计 |
|------|------|
| **Sign** | 1 bit,标准符号位 |
| **Dot** | 变长前缀码,显式指示阶码位宽(D=0-4)和 Denormal 标志(DML)。**大宽度编码小值,小宽度编码大值**,实现锥形精度 |
| **Exponent** | D bits,原码(符号+数值)编码,隐藏 MSB=1。D=0 时阶码为 0 |
| **Mantissa** | 1-3 bits,隐藏 leading 1 |

### 锥形精度分布

```
D=4(宽码): 16 个阶码值,1-bit mantissa → 低精度高动态
D=3:        8 个阶码值,2-bit mantissa
D=2:        7 个阶码值,3-bit mantissa → 高精度近 1.0
D=1:        1 个阶码值,3-bit mantissa
D=0+Denormal: +7 个阶码值(-22到-16),3-bit mantissa
```

**综合阶码 38 binades** (FP16=40,FP8-E4M3 仅 15)。

## 三、关键设计决策

### Dot 域(锥形精度的核心)

- **为什么不用 Posit 的 unary 编码**:不够灵活,无法精细控制 significand 在 exponent 上的分布
- **前缀码设计**:4 位编码 0/DML,3 位编码 1,2 位编码 2/3/4。保证 mantissa 宽度不跳变超过 1 bit,精度变化平滑

### Exponent 域(避免编码冗余)

- 原码+隐藏 MSB=1,不同 D 值指向的阶码范围不重叠
- 比 IEEE 754 的 offset-binary 和 Posit 的 regime 更好地实现了非冗余编码

### Denormal 扩展

- 将 D=0 时的 4-bit mantissa 缩减为 3-bit,腾出的编码空间直接扩展 7 个额外 binades(-22到-16)
- Binades 从 31→38,非常接近 FP16 的 40

## 四、舍入方法

| 方法 | 适用场景 | 特点 |
|------|---------|------|
| **TA(Round-half-to-away)** | 前向(默认)+后向 | 硬件最简单;TE 特殊案例概率极低(2^-20),TA 略高于 TE 精度 |
| **Hybrid Rounding(HR)** | 后向(备选) | 高精度区用 TA,低精度区用简化 SR。Yolo-V3-Tiny 从-1.67%恢复到+0.06% |

HR 是简化版随机舍入:利用 FP32 低 14 位作阈值、高 14 位作分数,避免真随机数生成瓶颈。FP16/BF16 源用特殊 2 位阈值(SR2)。

## 五、实验结果

### 传统网络训练(21 模型,含 CNN/Transformer)

HiF8 训练精度与 FP16 baseline 差异 ≤±0.35%,收敛速度一致。无需像 FP8 那样做 per-tensor scaling——因为 HiF8 动态范围足够大(接近 FP16)。

### LLM 训练(GPT3/LLaMA/T5)

| 训练策略 | 开销 | 覆盖范围 |
|---------|------|---------|
| BLS(向后全局 loss-scaling) | 几乎零额外开销 | 多数 LLM |
| ALS(自适应 loss-scaling) | 同 BLS | 解决超参调优困难 |
| PTS(per-tensor scaling) | 每 10 iter 算 Amax | 少数敏感模型(精度可超 baseline) |

### 推理(PTQ)

- **Transformer 类**:直接 cast 即可用,无需校准
- **CNN 类**:per-tensor scaling 后可用(敏感层留 FP16/BF16)
- **LLM**:LLaMA 直接 cast 可用;OPT 需 SmoothQuant/PTS

## 六、与 FP8/MXFP8/Posit8 对比

| | HiF8 | FP8(E4M3+E5M2) | MXFP8 | Posit(8,2) |
|---|---|---|---|---|
| 格式数 | **1** | 2 | 1(+MX scale) | 1 |
| Binades | 38 | 15+16 | 31+ | 24(≥1b mantissa) |
| 同时覆盖前向+后向 | ✅ | ❌(需两个格式) | 部分 | ❌ |
| 训练精度 vs FP16 | ±0.35% | 需 per-tensor scaling | 需 per-tensor scaling | 精度不足 |
