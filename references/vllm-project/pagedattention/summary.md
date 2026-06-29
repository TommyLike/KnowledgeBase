# Efficient Memory Management for Large Language Model Serving with PagedAttention

> SOSP 2023 (2023) | Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, Ion Stoica
> arXiv: [2309.06180](https://arxiv.org/abs/2309.06180)
> DOI: [10.1145/3600006.3613165](https://doi.org/10.1145/3600006.3613165)
> 关联项目: vllm-project--vllm, vllm-project--vllm-ascend

## Abstract (EN)

LLM serving suffers from inefficient KV cache memory management. This paper proposes PagedAttention, inspired by OS virtual memory paging, to manage KV cache in fixed-size blocks. The vLLM system built on it achieves near-zero memory waste (96%+ utilization) and 2-4x throughput improvement over prior systems like FasterTransformer and Orca.

## 摘要 (中文)

大语言模型推理面临 KV cache 内存管理低效问题。本文受操作系统虚拟内存分页机制启发，提出 PagedAttention 算法，将 KV cache 按固定大小块管理，消除了内部和外部内存碎片。基于此构建的 vLLM 推理引擎实现了近零内存浪费（96%+ 利用率）和 2-4× 吞吐量提升。

## Tags
vllm, 推理, 内存管理, kv-cache, pagedattention

## 详细中文导读

### 1. 问题背景
LLM 推理服务的核心瓶颈是 **KV cache 内存管理**。以 13B 参数模型在 A100 (40GB) 上为例：
- 65% 显存被模型权重占用（静态）
- 30% 显存用于 KV cache（动态增长/收缩）
- 现有系统仅 20-38% 的 KV cache 内存被有效利用，其余浪费在碎片和冗余上

### 2. 核心创新: PagedAttention
受操作系统虚拟内存分页机制启发：
- **分块管理**: KV cache 按固定大小 block 分配，不再要求连续内存
- **按需分配**: 消除内部碎片（不再预分配最大长度）
- **等大小块**: 消除外部碎片（所有 block 相同大小）
- **块级共享**: 同一请求的多个序列（beam search/parallel sampling）可共享 KV cache block

### 3. vLLM 系统设计
- **Block-level 内存管理器**: 与 PagedAttention 协同设计
- **抢占式调度**: 支持请求级别的抢占和恢复
- **分布式**: 支持单卡装不下的超大模型
- 实现: ~8K 行 Python + ~2K 行 C++/CUDA

### 4. 实验结果
- KV cache 内存利用率: 20-40% → **96%+**
- 吞吐量: **2-4×** 提升（vs FasterTransformer/Orca）
- 长序列、大模型、复杂解码算法下优势更明显
- 开源地址: https://github.com/vllm-project/vllm
