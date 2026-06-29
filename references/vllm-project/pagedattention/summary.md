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
