# HiFloat4 — 关键设计分析

> 来源:HiFloat4 Format for Language Model Inference(docling 转换)
> 日期:2026-07-07

---

## 一、定位

华为自研 4-bit Block Floating-Point(BFP)格式,面向**大模型推理**。核心目标:**精度超 NVFP4,硬件面积仅 1/3,功耗低 10%**。

## 二、格式定义

每个 HiF4 单元 = **32-bit 缩放元数据 + 64×4-bit 元素**,平均 4.5 bit/value。

### 三级缩放层次

```
Level 1(E6M2): 全局 base scale(8-bit unsigned FP)
  └─ Level 2(E1_8): 8-way 1-bit micro-exponent
       └─ Level 3(E1_16): 16-way 1-bit micro-exponent
            └─ S1P2 ×64: 4-bit sign-magnitude 元素
```

| 属性 | HiF4 | NVFP4 |
|------|------|-------|
| 平均存储 | 4.5 bit/value | 4.5 bit/value |
| 组大小 | **64** | 16 |
| 元素格式 | S1P2(E1M2),3-bit significand | E2M1,2-bit significand |
| 全局基尺度 | **E6M2**(unsigned FP8) | E4M3(float) |
| 全局动态范围 | **69 binades** [-50,18] | 22 binades [-10,11] |
| 局部动态范围 | **4.81 binades** | 3.58 binades |
| 微指数 | 两级共享(8+16) | 单个独立 2-bit |

## 三、关键设计决策

### 为什么选 S1P2(E1M2)而非 E2M1

- S1P2 = 3-bit significand(**精度上限更高**)
- E2M1 = 2-bit significand(动态范围稍大但精度损失严重)
- HiF4 通过两级微指数补足了 S1P2 的动态范围短板,同时保留了 3-bit 精度优势

### 为什么组大小为 64

- 元数据开销随组大小均摊:64 元素/32-bit 元数据 = 0.5 bit/value overhead
- 关键收益:**64 长度点积 = 1 对 HiF4 单元刚好填满一个 PE 输入宽度**,无需多对单元拼接
- NVFP4 组大小 16→需要 4 对单元填同一 PE→积累树需要 6 个额外乘法器

### 为什么 E6M2 做全局尺度

- E6M2(unsigned FP8,48 bias):动态范围 [-48,15]=69 binades → **无需 PTS**(NVFP4 的 E4M3 仅 22 binades,必须额外 per-tensor scaling)
- 训练场景也可直接用,不用像 NVFP4 那样需要 PTS 额外开销

### 硬件点积优势

64 长度点积中:
- HiF4:微指数被吸收为左移→乘法器输入 S2P2(5-bit 整数)→纯整数积累树→仅末端 1 个浮点乘法器+1 个大整数乘法器
- NVFP4:E2M1→S3P1(5-bit 整数)→4 个浮点乘法器+4 个大整数乘法器→浮点累加
- **HiF4 省 6 个乘法器,增量面积≈NVFP4 的 1/3,功耗低约 10%**

## 四、量化误差

高斯分布数据,MSE 比例:HiF4 : MXFP4 : NVFP4 ≈ 1 : 1.5 : 2.5

NVFP4 在数据接近边界时溢出/下溢导致误差暴涨(需 PTS 挽救)。HiF4 和 MXFP4 不需要 PTS,无额外量化开销。

## 五、实验结果

### Small LLMs(7-14B,8 benchmarks)

| 格式 | 4 模型平均 Acc | Acc Drop |
|------|-------------|----------|
| BF16 | 72.99 | baseline |
| NVFP4(direct) | 61.42 | **Crash(Mistral-7B)** |
| NVFP4+PTS | 71.38 | -1.61 |
| HiF4(direct) | 71.87 | **-1.12** |
| HiF4+HiGPTQ | 72.23 | -0.76 |

### Large LLMs(DeepSeek-V3.1 671B + LongCat 560B,10 benchmarks)

| 格式 | DeepSeek-V3.1 Acc Drop | LongCat Acc Drop |
|------|----------------------|------------------|
| NVFP4(direct) | -0.63 | **-3.84(MMLU -20)** |
| NVFP4+PTS | -0.20 | -3.51 |
| HiF4(direct) | **+0.98**(超 BF16!) | **+0.48** |

关键发现:
- **NVFP4 在 Mistral-7B 和 LongCat 上直接崩溃**(精度退化为随机猜测)
- HiF4 在所有模型上 stable,且 DeepSeek-V3.1 上 HiF4 direct-cast **超越 BF16 baseline**
- **Qwen2.5-14B 上 HiF4+HiGPTQ 超越 BF16 baseline**

## 六、与 NVFP4 对比总结

| 维度 | HiF4 | NVFP4 | 差异原因 |
|------|------|-------|---------|
| 精度 | ✅ 全模型碾压 | ❌ 敏感模型崩溃 | 更大全局+局部动态范围,更大组大小 |
| PTS 需求 | ❌ 不需要 | ✅ 必须 | E6M2 69 binades vs E4M3 22 binades |
| 硬件面积 | 1× | **3×** | 组大小 64→1 对填 PE vs 4 对 |
| 功耗 | 低 10% | — | 纯整数积累树 vs 多浮点乘法器 |
| 训练潜力 | 已论证 | 需 PTS 额外开销 | E6M2 动态范围足够 |
