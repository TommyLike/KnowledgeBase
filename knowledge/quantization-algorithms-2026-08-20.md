# 量化算法：历史演进与主要技术方向

> [Archived] 2026-08-20 | 来源: /kg-topic
> 涉及项目: vllm-project--vllm, vllm-project--llm-compressor, vllm-project--compressed-tensors, vllm-project--vllm-bnb-plugin, vllm-project--vllm-gguf-plugin, sgl-project--sglang, sgl-project--sgl-kernel-npu, vllm-project--vllm-ascend, radixark--miles
> 本页为时间点快照，知识可能已过时。

## 核心结论

1. **量化已从"部署优化手段"升级为"训练-推理全生命周期的精度工程"**：2015 年的 Deep Compression 只为压缩 CNN 体积，2024 年 DeepSeek-V3 用 FP8 完成了 671B 参数模型的全量预训练，量化正式进入训练主流程。
2. **演进主轴是"比特宽度下探"**：FP16/INT8 → INT8 W8A8 → INT4 W4A16 → FP8（E4M3/E5M2）→ FP4（MXFP4/NVFP4）→ 2-bit/1.58-bit 三元。每降一档，异常值处理与纠错机制就复杂一层。
3. **2025-2026 的主线趋势是"硬件-算法协同设计"**：Blackwell 的 NVFP4/MXFP4 把 FP4 算力变成免费午餐，但纯算法 PTQ（如旋转、分组量化）在新格式上的收益规律完全不同——MR-GPTQ 甚至证明了 Hadamard 旋转对 NVFP4 有害。量化方法的优劣从此必须放在具体硬件格式下讨论。
4. **推理框架层已收敛**：vLLM/SGLang 都把 GPTQ/AWQ/FP8 作为一等公民，kernel 层（Marlin/Machete/DeepGEMM/FlashInfer）决定实际速度，格式层（compressed-tensors/llm-compressor）决定模型可携带性。
5. **昇腾另立格式路线**：华为 HiFloat 系列（HiF8/HiF4）用变长点位域编码让 8 比特自带近 FP16 的动态范围，摆脱了 FP8 对细粒度缩放的依赖，Ascend 950PR 将原生支持——国产硬件在低精度格式上从"跟随 FP8/MX"转为"自定标准 + 捐献开源联盟（GCC）"。

---

## 一、背景：为什么需要量化

大模型的部署受三道墙约束：

| 墙 | 表现 | 量化收益 |
|---|---|---|
| **显存墙** | 671B 参数 FP16 权重 ≈ 1.3TB，单卡放不下 | INT8 减半，INT4 减 3/4 |
| **带宽墙** | 解码阶段每 token 都要读一遍全部权重，受限于 HBM 带宽 | 权重越小，每 token 搬运字节越少 |
| **算力墙** | 低精度矩阵乘在专用单元上吞吐更高 | H100 FP8 Tensor Core 是 FP16 的 2 倍 |

对**解码阶段**（每个 token 读一遍所有权重）而言，量化主要是**带宽优化**：W4A16 把每 token 的权重搬运量从 2 字节/参数降到 0.5 字节，理论吞吐上限直接翻 4 倍——这就是推理框架（vLLM/SGLang）把权重压缩而非激活压缩作为主战场的原因。

## 二、历史演进时间线

### 2.1 前 LLM 时代（2015–2021）：CNN 的 INT8 成熟期

| 时间 | 工作 | 贡献 |
|---|---|---|
| 2015 | **Deep Compression**（Han et al.） | 剪枝+量化+霍夫曼编码三件套，AlexNet/VGG 压缩 35–49×，确立"量化=部署优化"范式 |
| 2018 | **QAT INT8**（Jacob et al.） | 训练时插入伪量化节点模拟量化误差，梯度用 STE 直通估计器回传，INT8 推理精度无损 |
| 2020 | **AdaRound**（Nagel et al.） | 发现四舍五入不是最优舍入：逐权重自适应选择向上/向下舍入，重建误差显著下降 |
| 2020 | TensorRT 校准 | 工业界固化 PTQ 流程：MinMax/MSE/Entropy(KL 散度) 三种校准器 |

这一时期的共识：**CNN 的 INT8 问题基本解决**，量化是"即插即用"的部署工具。但这个共识在 LLM 上被彻底打破。

### 2.2 LLM 时代第一次浪潮（2022–2023）：异常值是核心敌人

LLM 的激活存在**异常值**：某些固定通道的激活幅度比其他通道大 100 倍以上（Llama 系列尤其明显）。对激活做 INT8 量化时，量程被这几个异常通道撑爆，其余通道的有效精度被稀释。

| 时间 | 工作 | 核心思路 | 比特 | 方案类型 |
|---|---|---|---|---|
| 2022.08 | **LLM.int8()** | 把 MatMul 拆成两路：异常列保留 FP16，正常列走 INT8；运行时动态检测 | W8A8 混合 | PTQ（免校准） |
| 2022.10 | **GPTQ**（Frantar et al., ICLR'23） | 逐层最小化重建误差 + 二阶 Hessian 信息逐权重补偿误差（源自 OBS 剪枝理论） | W4A16 | PTQ（需校准） |
| 2022.11 | **SmoothQuant**（ICML'23） | 用数学等价变换 `W·diag(s)·diag(s)⁻¹·X` 把量化的难度从激活迁移到权重，激活变平滑 | W8A8 | PTQ（需校准） |
| 2023.05 | **QLoRA**（Dettmers） | NF4（正态分布拟合的 4-bit 格式）+ 双重量化，微调 65B 模型仅需 48GB | W4A16 | 微调侧 |
| 2023.06 | **AWQ**（MLSys'24） | 激活感知：只保护约 1% 的显著权重通道（per-channel 缩放），其余通道量化为 INT4 | W4A16 | PTQ（需校准） |

三种应对异常值的路线在此定型，后续几乎所有工作都是它们的变体：

1. **躲**（LLM.int8）：异常值不量化，保持 FP16，代价是两路 MatMul、3 个 kernel/层；
2. **迁**（SmoothQuant）：数学等价变换把异常值从激活"赶"到权重里；
3. **保**（AWQ）：异常值对应的权重通道给更高的缩放精度，其余照常量化。

GPTQ 与 AWQ 后来成为推理框架的**事实标准**：vLLM/SGLang/TensorRT-LLM 全部支持，W4A16 成为消费级 GPU 跑大模型的默认配置。

### 2.3 低比特与浮点分叉（2023–2024）：两条路

**路 A：继续往整数低比特走**

| 时间 | 工作 | 思路 |
|---|---|---|
| 2023-24 | QuIP / QuIP# | 先做非相干处理（旋转矩阵）让权重分布均匀，再用 2-bit 格子量化，理论保证 |
| 2023-24 | BitNet 1.58 | 权重三值化 {-1, 0, +1}，训练从零开始，推理退化为加法 |
| 2024 | T-MAC 等 | 查表法（LUT）把 1-2 bit 反量化变成位运算查表，CPU 上极快 |
| 2024 | KVQuant / KIVI | KV cache 单独量化（key 逐通道、value 逐 token 的混合粒度） |

**路 B：浮点低精度成为主线（硬件驱动）**

| 时间 | 事件 |
|---|---|
| 2022 | FP8 格式 E4M3/E5M2 提出（Micikevicius et al.），H100 原生支持 FP8 Tensor Core |
| 2023 | OCP 发布 **Microscaling (MX) 格式族**：MXFP8/MXFP6/MXFP4，用 E8M0 指数作为块共享缩放因子 |
| 2024.12 | **DeepSeek-V3** 用 FP8 混合精度完成 671B/14.8T tokens 预训练，证明 FP8 训练工程可行 |
| 2025 | **Blackwell 原生 FP4**：NVFP4（全局 FP32 scale + 每 16 元素 E4M3 二级 scale）与 MXFP4 硬件支持，FP4 算力免费 |
| 2024.09 | **HiFloat8 提出**（Luo et al., arXiv:2409.16626） | 华为：变长点位域编码，8 比特综合阶码 -22~+15（38 个，FP16 为 40 个） |
| 2025.09 | **HC 2025 发布 HiFloat 系列**（HiF8/HiF4）并捐献 GCC | 启动《HiF8 团体标准》与"HiFloat 大模型共创行动" |
| 2026 Q1 | **Ascend 950PR 原生支持 HiF8** | 编解码入硬件，HiF8 算力 919 TFLOPS 高于 MXFP8/FP8 的 804（Cube+Vector 合计） |

浮点低精度（FP8/FP4）相比整数低比特的关键优势：**动态范围靠指数位天然覆盖**，对异常值远不如 INT 格式敏感——INT8 最怕的激活异常值问题，在 E4M3 下大幅缓解。这是 FP8 能同时用于训练和推理、而 INT4 只能权重-only 的根本原因。

### 2.4 当前格局（2025–2026）：硬件-算法协同设计

ICLR 2026 的量化论文全景调研（91 篇接收论文、13 个研究方向）给出的核心判断：**纯算法 PTQ 时代结束，硬件-算法协同成为主线**。具体信号：

- **格式选择本身成为研究问题**：MXFP4 vs NVFP4 的缩放因子精度（E8M0 vs E4M3 二级 scale）对精度影响巨大（arXiv:2507.17417 综合评测的结论之一）；
- **旋转法在新格式下失灵**：Hadamard 旋转对 INT4 有效，但 MR-GPTQ 证明它对 NVFP4（group=16）**有害**——INT 时代的经验不能直接迁移到 FP4；
- **混合精度组合**：NVIDIA MicroMix 提出 MXFP4+MXFP6+MXFP8 混合，因为 INT4 kernel 无法完全利用 Blackwell 的 FP4 Tensor Core；
- **FP4 训练探索**：Metis（低秩谱分解+稀疏采样）把 FP4 训练损失差距从 3-4% 收窄到 0.4%；随机舍入保证反向传播无偏是关键；
- **优化器量化理论**：Adam 二阶矩对量化极敏感（要求 q_V = O(1/T²)），Muon 优化器没有二阶矩所以容忍宽松得多的量化。

## 三、核心原理基础

### 3.1 量化公式

仿射量化：`r = s·(q − z)`，反量化：`q = round(r/s + z)`
- `s`（scale，步长）决定精度粒度，`z`（zero point，零点）处理非对称分布；
- 对称量化 `z=0`，实现更简单，INT8 常用；FP 格式天然对称。

### 3.2 量化粒度（精度与开销的权衡）

| 粒度 | scale 数量 | 精度 | 典型用途 |
|---|---|---|---|
| per-tensor | 1 个/张量 | 最粗 | 早期 INT8 |
| per-channel | 1 个/输出通道 | 中 | SmoothQuant、AWQ 保护通道 |
| per-group | 每 128 权重一组 | 细 | GPTQ/AWQ W4A16 标配 |
| per-block | 每 16-128 元素 | 最细 | FP8 blockwise（DeepGEMM 128×128）、NVFP4（16） |

粒度越细精度越高，但反量化开销越大——所以分组大小成为硬件-算法协同的焦点（Blackwell 上 group=16/32 与 E8M0/E4M3 scale 的组合决定实际性能）。

### 3.3 校准方法（PTQ 的输入）

MinMax（量程截断）、MSE（最小化重建误差）、Percentile（截断长尾）、KL 散度（TensorRT 默认）。校准数据集规模一般只需几百条样本。

### 3.4 为什么权重可以 INT4、激活不行

- 权重分布均匀、无异常值 → INT4 + per-group scale 就能保住精度；
- 激活有异常值 + 每个 token 都变 → 静态量化极易被撑爆，要么动态量化（运行时算 scale，开销大），要么保持 FP16（即 W4A16 的 A16）；
- 结论：**W4A16 是当前推理性价比甜点**，W8A8（FP8/INT8）是训练与高端推理的选择，W4A4 及以上仍主要停留在研究。

## 四、主要技术方向地图

### 方向 1：PTQ vs QAT vs 低精度训练

| 路线 | 时机 | 成本 | 精度下限 | 代表 |
|---|---|---|---|---|
| PTQ | 训练后，无需重训 | 几百条校准样本 | INT4 可用 | GPTQ/AWQ |
| QAT | 训练中模拟量化 | 完整训练预算 | INT4 更强 | LLM-QAT、Kimi K2 的 INT4 QAT |
| 低精度训练 | 从零用低精度训练 | 完整训练预算 | FP8 已生产验证 | DeepSeek-V3（FP8）、Metis（FP4） |

趋势：模型厂商开始把 QAT 下沉——Kimi K2 直接发布原生 INT4 QAT 权重（W4A16 免校准），vLLM/SGLang 都要专门适配。量化从"下游的部署技巧"变成"上游的训练决策"。

### 方向 2：权重-only（W4A16）vs 权重+激活（W8A8）

- W4A16：只量化权重，激活保持 FP16。推理带宽优化为主，kernel 相对简单（在线反量化后走 FP16 GEMM），是消费级部署的主流；
- W8A8：权重和激活都量化，能吃低精度算力单元（INT8/FP8 Tensor Core）。FP8 W8A8 在 H100+ 是默认选择，吞吐是 W4A16 方案的近 2 倍——高端硬件上 FP8 正在取代 INT4 权重-only。

### 方向 3：异常值处理（INT 路线的核心矛盾）

见 §2.2 的三路线（躲/迁/保）+ 2024 年的旋转法（QuaRot/SpinQuant 用旋转矩阵把异常值打散）。注意：旋转法在 FP4 硬件格式上失效（MR-GPTQ 结论），是"算法红利随硬件演进过期"的典型案例。

### 方向 4：浮点低精度格式

- **FP8 E4M3/E5M2**：E4M3 精度高（推理首选），E5M2 动态范围大（梯度场景）；
- **MX 家族（Microscaling）**：块共享一个 8-bit 指数（E8M0），元素只留尾数——MXFP8/MXFP6/MXFP4。优势是 scale 开销极小，被 AMD/ARM/Intel/NVIDIA 共同推进为开放标准；
- **NVFP4**：Blackwell 原生，两级缩放（全局 FP32 + 每 16 元素 E4M3 scale），评测显示精度普遍优于 MXFP4。

**HiFloat（华为/GCC，变长编码路线）**——与上面所有格式的根本差异是放弃了"固定指数/尾数切分"：

- **HiF8**：引入点位域（Dot）变长前缀码，数值靠近 0 时多分位给尾数、远离 0 时多分位给指数，8 比特达到 38 个综合阶码（-22~+15），逼近 FP16 的 40 个——动态范围靠编码本身，不靠缩放；
- **训练**：Delayed Scaling 策略下与 BF16 收敛相当（DeepSeek-3B 15B tokens、Olmo-1B 80B tokens 预训练验证，平均任务精度差 <1%）；显存较 BF16 省 50-75%，矩阵乘算力提升 2-8×；
- **推理**：动态范围自足，多数任务 per-tensor 甚至 scale-free 量化即可，简化框架与硬件设计；
- **HiF4**：三级层次缩放（64 元素块共享 E6M2 scale + 8 元素子块与 4 元素微块的 1-bit 细化），规避 4-bit 整数格式的精度崩溃；
- **生态**：捐献全球计算联盟（GCC）共建，量化算法在 CANN amct 开源（gitcode.com/cann/amct）；A2/A3 平台已有 LUT 实现的 HiFloat8 cast 算子；昇腾 HiFloat 综合评测见 arXiv:2602.12635；
- **与 FP8 路线对比**：FP8 是"固定切分 + 缩放补偿"（复杂度转移到缩放机制），HiF8 是"变长切分自带动态范围"（复杂度转移到编解码硬件）。两者在 950PR 上并存。

### 方向 5：KV Cache 量化

长上下文 + 高并发的关键优化：KV 占显存的比例随上下文长度线性增长。FP8 E4M3 是 vLLM/SGLang 的标准选择；研究侧（KVQuant/KIVI）发现 key 适合逐通道量化、value 适合逐 token 量化，需分而治之。

### 方向 6：极低比特（≤2 bit）

三元（BitNet 1.58）到查表反量化（T-MAC）。目前主要用于 CPU/边缘推理，GPU 上收益被 Marlin/FP4 压制；但作为"权重近乎免费"的极限形态，值得长期跟踪。

### 方向 7：硬件-算法协同（当前主线）

- **Kernel 层**：Marlin（Ampere+ INT4，cp.async 流水）、Machete（Hopper，TMA + 混合输入 W4A16）、DeepGEMM（FP8 128×128 块缩放）、FlashInfer（运行时 JIT 生成最优 kernel）；
- **格式层**：compressed-tensors（稀疏+量化的 safetensors 扩展格式）、llm-compressor（压缩算法库）——模型格式与压缩算法的标准化；
- **硬件层**：Blackwell FP4 Tensor Core 强制 block=16/32 与 scale 格式的适配，量化算法必须"为格式而设计"。

## 五、推理框架落地现状（关联 KG 项目）

### 5.1 vLLM

- **kernel 后端**：Marlin 系（GPTQ/AWQ/FP8/FP4，NVIDIA Ampere 起步）、Machete（Hopper W4A16）、DeepGEMM（DeepSeek FP8 blockwise）；
- **生态插件**（KG 内项目）：`vllm-bnb-plugin`（bitsandbytes 动态量化）、`vllm-gguf-plugin`（GGUF 格式）、`llm-compressor`（压缩算法库）、`compressed-tensors`（压缩张量存储格式）；
- **硬件覆盖面**：Marlin 为 NVIDIA 独占；FP8 W8A8 需 Ada/Hopper/AMD/Neuron；INT8 W8A8 覆盖面最广（Turing→Hopper + x86 CPU + TPU）。

### 5.2 SGLang

- 量化支持维度更细：FP8 原生（H100+ 默认）、FP8 Block（B200）、ModelOpt FP8/FP4（NVIDIA 动态量化工具链）、AWQ/GPTQ/Marlin INT4、W4AFP8（MoE 混合精度）、GGUF（CPU）；
- AMD 侧：`quark_int4fp8_moe`（CDNA3/4）、`petit_nvfp4`（ROCm 上的 NVFP4 移植）；
- kernel 层以 FlashInfer JIT 编译 + CUTLASS 为主。

### 5.3 昇腾侧（KG 内 `sgl-kernel-npu`、`vllm-ascend`、`triton-lang`）

昇腾 NPU 的低精度算力单元与 CUDA 生态不同，量化 kernel（INT8/FP8 GEMM 及反量化）是这两条适配线的核心攻坚点。量化格式本身是平台无关的（FP8 E4M3、per-group INT4 都是开放的），真正的适配工作量在 **kernel 重写与精度对齐**上——这也是 KG 内 sgl-kernel-npu 定位为"SGLang 昇腾算子库"的原因。量化算法知识是理解这两条适配线工作内容的前置背景。

**HiF8 使昇腾的低精度路线与 CUDA 生态分叉**：950PR 原生 HiF8（919 TFLOPS，高于 MXFP8/FP8 的 804），量化算法（amct）已在 gitcode 开源，A2/A3 平台有 LUT cast 算子兜底——sgl-kernel-npu/vllm-ascend 未来可能需要同时适配 FP8/MX、HiF8 与 INT 系列多套格式。

### 5.4 训练侧（KG 内 `radixark--miles`）

Miles 的 FP8 全栈训练与 INT4 QAT 属于方向 1 的训练侧路线，与 DeepSeek-V3 的 FP8 工程一脉相承。

## 六、关键论文清单

| 论文 | 年份 | 贡献 |
|---|---|---|
| Deep Compression (Han et al.) | 2015 | 压缩三件套，量化进入主流 |
| Quantization and Training of NNs (Jacob et al.) | 2018 | QAT INT8 奠基 |
| AdaRound (Nagel et al.) | 2020 | 自适应舍入 |
| FP8 Formats for Deep Learning (Micikevicius et al.) | 2022 | E4M3/E5M2 格式定义 |
| LLM.int8() (Dettmers et al.) | 2022 | 异常值分解，W8A8 混合 |
| GPTQ (Frantar et al., ICLR'23) | 2022 | 二阶逐层纠错，W4A16 标准 |
| SmoothQuant (Xiao et al., ICML'23) | 2022 | 异常值迁移，W8A8 |
| QLoRA (Dettmers et al.) | 2023 | NF4+双重量化 |
| AWQ (Lin et al., MLSys'24) | 2023 | 激活感知保护显著通道 |
| QuIP# / QuaRot / SpinQuant | 2023-24 | 旋转+非相干处理，2-bit |
| DeepSeek-V3 Technical Report | 2024 | FP8 大规模训练生产验证 |
| KVQuant (NeurIPS'24) | 2024 | KV cache 量化 |
| Ascend HiFloat8 Format for Deep Learning ([本地](../references/huawei/hifloat8/summary.md)) | 2024 | HiF8 格式定义 + 点位域变长编码 |
| A Comprehensive Evaluation on Quantization for LLMs (arXiv:2507.17417) | 2025 | FP4/MX 格式系统评测 |
| HiFloat4 Format for Language Model Inference ([本地](../references/huawei/hifloat4/summary.md)) | 2026 | HiF4 三级层次缩放，精度超 NVFP4 |
| Unleashing Low-Bit Inference on Ascend NPUs (arXiv:2602.12635) | 2026 | 昇腾 HiFloat 格式推理综合评测 |
| Metis（ICLR'26） | 2026 | FP4 训练差距收窄到 0.4% |

## 七、开放问题

1. **FP4 训练的稳定性边界**：随机舍入保无偏是必要条件，但优化器（尤其 Adam 二阶矩）的量化敏感度上限在哪？
2. **旋转法的适用范围**：对 INT4 有效的旋转/非相干处理，在 MX/NVFP4 上被证明有害——新格式需要新的一阶/二阶纠错理论；
3. **昇腾低精度生态的量化完备度**：FP8/INT4 kernel 的精度对齐与性能差距，是 KG 内昇腾适配线值得持续跟踪的量化侧指标；
4. **QAT 下沉**：Kimi K2 原生 INT4 QAT 权重若成为模型厂商标配，PTQ 工具的定位将被重塑；
5. **HiFloat16 的公开信息缺失**：截至 2026-08，公开渠道仅有 HiF8/HiF4；若存在 HiFloat16，其定位（对标 BF16 的训练格式？）尚待资料确认。

## 来源

- [A Comprehensive Evaluation on Quantization Techniques for Large Language Models (arXiv:2507.17417)](https://arxiv.org/abs/2507.17417)
- [ICLR 2026 模型量化论文全景调研（Awesome-Model-Quantization）](https://kai-liu.cn/Awesome-Model-Quantization/)
- [A Survey on Model Compression for Large Language Models (arXiv:2308.07633)](https://ar5iv.labs.arxiv.org/html/2308.07633)
- [清华/浪潮 JCST 2026 综述：大语言模型量化技术](https://zhuanlan.zhihu.com/p/2042564257594725208)
- [Efficient-LLMs-Survey (AIoT-MLSys-Lab)](https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey)
- [vLLM Quantization 官方文档](https://docs.vllm.ai/en/v0.14.0/features/quantization/)
- [SGLang Quantization Techniques (DeepWiki)](https://deepwiki.com/sgl-project/sglang/4.6-quantization-techniques)
- [LLM Quantization Formats Compared (D-Central)](https://d-central.tech/llm-quantization-formats/)
- [Ascend HiFloat8 Format for Deep Learning (arXiv:2409.16626)](https://arxiv.org/abs/2409.16626) · [KG 本地归档](../../references/huawei/hifloat8/summary.md)（含全文 markdown 提取版）
- [HiFloat4 Format for Language Model Inference (arXiv:2602.11287)](https://arxiv.org/abs/2602.11287) · [KG 本地归档](../../references/huawei/hifloat4/summary.md)（含全文 markdown 提取版）
- [Unleashing Low-Bit Inference on Ascend NPUs (arXiv:2602.12635)](https://arxiv.org/abs/2602.12635)
- [HiFloat 官网（GCC 共建）](https://hifloat.gccorg.com/zh)
- [GCC 承接新一代低精度数据格式](https://www.gccorg.com/article/18/418.html)

## KG 关联

- [vllm-project--vllm](../../projects/vllm-project/vllm/summary.md) — 量化 kernel 主战场
- [vllm-project--llm-compressor](../../projects/vllm-project/llm-compressor/summary.md) — 压缩算法库
- [vllm-project--compressed-tensors](../../projects/vllm-project/compressed-tensors/summary.md) — 压缩张量格式
- [vllm-project--vllm-bnb-plugin](../../projects/vllm-project/vllm-bnb-plugin/summary.md) — bitsandbytes 插件
- [vllm-project--vllm-gguf-plugin](../../projects/vllm-project/vllm-gguf-plugin/summary.md) — GGUF 插件
- [sgl-project--sglang](../../projects/sgl-project/sglang/summary.md) — SGLang 量化支持矩阵
- [sgl-project--sgl-kernel-npu](../../projects/sgl-project/sgl-kernel-npu/summary.md) — 昇腾算子库（量化 kernel 攻坚点）
- [vllm-project--vllm-ascend](../../projects/vllm-project/vllm-ascend/summary.md) — vLLM 昇腾适配
- [radixark--miles](../../projects/agent-infra/miles/summary.md) — FP8 全栈/INT4 QAT 训练侧
- [huawei--hifloat8](../../references/huawei/hifloat8/summary.md) — 昇腾 8 位格式论文（本地 PDF + 全文 markdown）
- [huawei--hifloat4](../../references/huawei/hifloat4/summary.md) — 昇腾 4 位块浮点论文（本地 PDF + 全文 markdown）
