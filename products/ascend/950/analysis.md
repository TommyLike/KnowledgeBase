# 昇腾 950 NPU 关键设计分析

> 来源:昇腾 950 NPU 架构白皮书(docling 转换:index.md)
> 日期:2026-07-07

---

## 一、芯片定位与产品矩阵

面向大模型全生命周期的旗舰 AI 芯片,**Chiplet 多 Die 合封**(2×AI Die + 2×IO Die + HBM 模块),共架构双产品:

| 规格 | 昇腾 950PR | 昇腾 950DT |
|------|-----------|-----------|
| **定位** | 高性能推荐 + 大模型 Prefill + 多模态推理 | 大模型全量训练 + 复杂推理(Decode+Prefill) |
| **片上内存** | 128GB / 1.6TB/s | 144GB / 4TB/s |
| **AI 子系统** | 32-28 Cube Core + 64-56 Vector Core | 36-28 Cube Core + 72-56 Vector Core |
| **L2 Cache** | 128MB(跨 Die UMA 统一地址) | 128MB |
| **MXFP4 峰值** | 1784 TFLOPS | 2007 TFLOPS |
| **HiF8/FP8 峰值** | 919 TFLOPS | 1034 TFLOPS |
| **BF16/FP16 峰值** | 486 TFLOPS | 547 TFLOPS |

---

## 二、第三代 DaVinci Core 架构

### 2.1 分离式 Core 设计

每个 AI 子系统 = **1×Cube Core(矩阵张量) + 2×Vector Core(向量通用)**。分离架构让两类计算独立升级、按需配比。

### 2.2 Cube Core — 张量计算引擎

| 创新点 | 细节 |
|--------|------|
| **低精度格式** | 新增 HiF8 / MXFP8 / MXFP4。MXFP4 算力 = 4× BF16; HiF8/MXFP8 = 2× BF16 |
| **HiF8 自有格式** | 华为自研 8bit 浮点。变长前缀码编码阶码位宽(Dot 域),锥形精度分布(靠近 1 精度高,远离渐降)。综合阶码 [-22,15] 共 38 个 powers of 2,接近 FP16 的 40 个。**无需额外 MX 缩放因子**(MXFP8 需要) |
| **即时量化回写** | L0C Buffer→Unified Buffer 随路量化(FP32→BF16/FP16/FP8/INT8),降核内缓冲占用和核间带宽 |
| **FlashAttention 优化** | 单核性能较上代提升 1.5-2×,结合 CV 融合直通+Vector 算力翻倍+随路量化 |

### 2.3 Vector Core — 向量计算引擎

| 创新点 | 细节 |
|--------|------|
| **算力翻倍** | FP16/FP32 单核 TFLOPS 较上代 +100% |
| **双发射 Register-Based SIMD** | 从传统 SIMD 升级,新增 BF16 原生支持,多种浮点格式转换指令 |
| **新同构 SIMD/SIMT 混合编程** | **以 SIMD 为主、SIMT 为辅**。规则计算走 SIMD(高性能双发 ALU+乱序执行),不规则分支(Gather/Scatter/Hash Insert)走 SIMT(编程灵活)。VF(Vector Function)为基本块,支持 SIMD↔SIMT 快速切换 |
| **软硬件栈优化** | Softmax/GELU 等关键函数微架构优化,减少数据依赖气泡 |

### 2.4 CV 融合直通

Cube L0C Buffer ↔ Vector Unified Buffer 直接数据通道,**不经过 L2 Cache**。

**意义**:FlashAttention 等算子频繁在 Cube(矩阵乘)和 Vector(Softmax 等)间切换,中间结果走 L2 往返延迟高(几十到上百 cycle)、带宽被占用。直通通道将延迟降到几个 cycle,释放 L2 带宽给其他并发 Task,同时大幅降功耗。

配合 Vector 算力翻倍和随路量化,三者叠加使 FlashAttention 单核性能提升 1.5-2×。

### 2.5 NDDMA 指令

硬化地址生成逻辑,最多 5 维数据重排。数据搬运+转置一次完成,内置缓存自动发掘局部性(将多个元素粒度读合并为 128B 读)。降低 Kernel 编程复杂度。

### 2.6 同步机制

新增 BufferID 同步(`get_buf()`/`rel_buf()`),类似互斥锁。替代传统 `set_flag`/`wait_flag`,与流水线解耦,降低并发编程复杂度。

---

## 三、Memory 子系统

```
昇腾 950 Memory 层次:
  L0A/L0B/L0C Buffer (64KB/64KB/256KB per Core)
  └─ Unified Buffer (512KB per Core)
       └─ L2 Cache (128MB, 2-Die UMA 统一地址)
            └─ 片上 HBM (950PR: 128GB / 1.6TB/s | 950DT: 144GB / 4TB/s)
```

### 关键设计

| 特性 | 细节 |
|------|------|
| **Chiplet UMA** | 2×AI Die + 2×IO Die + HBM 通过 D2D+Mem I/F 连接,统一地址空间,硬件维护跨 Die Cache 一致性,软件无感 |
| **128MB L2 Cache** | 多 Bank 分布,512B Cache Line,新增 **128B Sector Cache**(小粒度访问性能 2×+) |
| **L2 Hint** | 算子可控 allocate/non-allocate 策略,跨 Task 数据复用优化。如 Task₀ 输出→Task₁ 输入保留在 L2,短期无用数据直接 bypass |
| **CMO** | SDMA 支持 Prefetch / Writeback / Invalid / Flush,软件可控时机和范围 |
| **RAS** | Online ECC + 巡检发现薄弱点 + 动态行失效隔离(预留行替换,用户无感) |

### Memory 规格表

| Memory 层级 | 容量 |
|------------|------|
| L1 Buffer | 512KB per AI Core |
| L0A/B Buffer | 64KB each per AI Core |
| L0C Buffer | 256KB per AI Core |
| Unified Buffer | 512KB per AI Core |
| CPU L1 Cache | 64KB per CPU Core |
| CPU L2 Cache | 1MB per CPU Core |
| L3 Cache | 4MB per CPU Cluster |
| L2 Cache | Up to 128MB |
| 片上内存 | 950PR: 128GB / 950DT: 144GB |

---

## 四、灵衢(Unified Bus 2.0)互联系统

### 物理规格

| 规格 | 数值 |
|------|------|
| HiLink SerDes | 72 Lane → 18×4 Port,每 Port 最高 4×112Gbps |
| 芯片 IO 带宽 | **2TB/s (2016 GB/s 双向)** |
| PCIe 5.0 | x16, 128GB/s 双向, EP/RC 双模(静态选择) |
| UBoE | 2×400Gbps,与 UB 共用 SerDes 端口,支持 Port Bifurcation |

### 协议栈(三大访问语义)

| 语义 | 模式 | 用途 | 可靠性 |
|------|------|------|--------|
| **URMA** | 异步(队列 SQE/CQE) | Write/Read/Send/Atomic(FetchAdd/CAS) | RTP 可靠传输(端到端重传,4 Port 带宽) \| CTP 简易传输(9 Port 带宽) |
| **UB Memory** | 同步(Load/Store/Atomic) | 跨芯片直接访存,最高 **128TB 共享地址空间**,UMMU 做 VA→PA 翻译+权限控制 | — |
| **UBoE** | UB 协议跑以太网 | 直接接入标准以太网交换机,无需协议转换 | 依赖以太网 |

### CCU 集合通信加速单元

**硬件卸载**集合通信,释放 AI Core 算力。架构:CCUM(Mission 任务编程入口)→CCUA(集成 MemorySlice + Reduce Unit)。支持算法:Broadcast / Reduce Scatter / All Gather / All Reduce / All2All / All2Allv。流程:软件下发 Mission→硬件自主搬运(URMA)或计算(Reduce)→完成上报。

### 超节点能力

| 能力 | 规格 |
|------|------|
| **超节点规模** | **8192 卡**(上代 384 卡) |
| **集群规模** | **128K+ 卡** |
| **组网拓扑** | Full Mesh / Clos / nD-Mesh / 混合 |
| **超大内存池** | UB 直连 CPU 内存,高带宽低延迟,无需协议转换 |
| **超大存储池** | UB 直连存储资源,跳过中间协议层 |
| **UB↔Ethernet** | UB Switch 转换 + UBoE 原生接入 |
| **片内转发** | UB On Chip Switch:单 IO Die 内 9×4 Port 转发,流量不进入计算 Die,不占用 DRAM 带宽 |

---

## 五、STARS 2.0 调度系统

System Task and Resource Scheduler 2.0,芯片全局硬件任务调度器。

### 核心能力

| 能力 | 规格 |
|------|------|
| **Host 下沉** | 2048 条任务流预取→调度→完成上报,软硬协同 |
| **并发调度** | AIC/AIV/VPC/JPEGD/JPEGE + 16 AI CPU Task + 64 Host CPU Task + 64 UB Jetty + 32 CCU + 32 SDMA Channel |
| **HSCB 总线** | 专用高速控制总线,调度延迟 **ns 级**,独立于数据 NoC,支持广播调度 |
| **Group 调度** | 最多 8 Group,按 Die 亲和性分组,充分利用 L2 局部性 |
| **算力切分** | AIC/AIV/SDMA 最多 16 资源池,其他加速器 8 池,支持 VM 绑定隔离 |
| **同步标志** | 128K 单比特或 4096 多比特(32bit)同步标志位 |
| **条件算子** | 支持执行条件算子 |
| **实时 Profiling** | TOP-DOWN 模型:Task 时间轨迹/计算开销/带宽/功耗 |

---

## 六、其他子系统

### AI CPU — Linx816

- 华为自研 ARMv8-A 架构,物理双线程(可独立配置单/双线程)
- 4 Cluster × 2 Core = 8 核,每核 L1 64KB + L2 1MB,每 Cluster L3 4MB
- 职责:(1)通用控制(NPU 侧 OS/页表管理/性能监控/IO 调度)(2)CPU 类算子(补充 AI Core)
- 硬件缓存一致性与 AI Core+L2 子系统互通

### DVPP — 数字视觉预处理

| 模块 | 数量 | 能力 |
|------|------|------|
| VPC | 4 Core | 缩放/裁剪/色彩空间转换/仿射透视变换,对标 OpenCV/TorchVision,1080P@5760FPS |
| JPEGD | 8 Core | 最大 32K×32K, YUV444/422/420/440/400,区域解码 |
| JPEGE | 4 Core | 最大 32K×32K, YUV420/422/444,1024FPS@1080P |
| 调度 | STARS 直接硬件调度 | — |

### 安全引擎

专用安全算法引擎,全链路数据处理安全。

---

## 七、设计哲学总结

| # | 策略主线 | 具体体现 |
|---|---------|---------|
| 1 | **低精度换吞吐** | HiF8/MXFP8/MXFP4 三级低精度 → BF16 的 2-4× 等效算力 |
| 2 | **Chiplet UMA 解耦** | 计算 Die + IO Die + HBM 独立演进,统一地址空间简化编程 |
| 3 | **软硬协同降延迟** | STARS 硬调度(ns 级) + CCU 硬卸载集合通信 + NDDMA 硬地址生成 + HSCB 专用总线 |
| 4 | **SIMD/SIMT 混合** | 以 SIMD 为主力、SIMT 补不规则场景,不做二选一 |
| 5 | **超节点破内存墙** | 8192 卡 UB 直连 → 128TB+ 共享地址空间 + 超大内存/存储池 |
| 6 | **计算通信深度融合** | CCU 硬件卸载 + CV 融合直通 + UB On Chip Switch 片内转发 |

---

## 八、HiF8 数值精度(附录)

HiF8 是华为自研 8bit 浮点格式,关键特征:

- **变长前缀码(Dot 域)**:显式指示阶码存储位宽和 Denormal 标志,实现锥形精度(靠近 1 精度最高,远离渐降)
- **原码编码阶码+隐藏位**:不同位宽阶码表达范围不重复,无冗余编码
- **综合阶码 [-22, 15]**:接近 FP16 的 [-24, 15],共 38 个 powers of 2
- **vs MXFP8**:不需要额外的 8 位 MX 缩放因子,在 8bit 极低开销下兼顾精度和动态范围
- **特殊值编码**:ZERO(0x00)/NAN(0x80)/+INF(0x6F)/-INF(0xEF),不区分正负零
