# SGLang: Efficient Execution of Structured Language Model Programs

> NeurIPS 2024 (2024) | Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Sun, Jeff Huang, Cody Hao Yu, Shiyi Cao, Christos Kozyrakis, Ion Stoica, Joseph Gonzalez, Clark Barrett, Ying Sheng
> arXiv: [2312.07104](https://arxiv.org/abs/2312.07104)
> 关联项目: sgl-project--sglang, sgl-project--sgl-kernel-npu

## Abstract (EN)

SGLang combines a frontend language for programming LLM applications with a high-performance runtime. Key innovations: RadixAttention (automatic KV cache reuse via radix tree LRU cache), compressed finite state machines (faster constrained decoding), and API speculative execution. Achieves up to 6.4x throughput improvement over vLLM, Guidance, and LMQL.

## 摘要 (中文)

SGLang 结合了 LLM 应用编程前端语言与高性能运行时。核心创新：RadixAttention（通过基数树 LRU 缓存自动复用 KV cache）、压缩有限状态机（加速约束解码）、API 推测执行。相比 vLLM、Guidance、LMQL 实现最高 6.4× 吞吐量提升。

## Tags
sglang, 推理, structured-generation, kv-cache, radixattention
