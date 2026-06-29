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

## 详细中文导读

### 1. 问题背景
LLM 应用越来越复杂，不仅仅是简单的 chat completion，还包括：
- 多轮对话、ReAct agent、多模态推理
- 结构化输出（JSON、代码、特定格式）
- 多个 LLM 调用组成的程序（program-like）

现有系统（vLLM、Guidance、LMQL）在处理这些复杂 LLM program 时效率低下。

### 2. 核心创新

**RadixAttention**
- 基于基数树 (Radix Tree) 的 LRU 缓存
- 自动检测和复用跨调用的 KV cache（如共享前缀的多个生成）
- 无需用户手动指定共享关系

**压缩有限状态机 (FSM)**
- 约束解码场景（如生成 JSON）的加速技术
- 一次解码多个 token，跳过确定性路径
- 大幅降低约束解码的延迟

**API 推测执行**
- 仅 API 可访问的模型（如 GPT-4）的优化
- 推测性并行执行多个调用

### 3. 实验结果
- 吞吐量: **最高 6.4×** 提升 vs vLLM/Guidance/LMQL
- 支持 Llama-7B/70B、Mistral-8x7B、LLaVA 等多模态
- GPU: NVIDIA A10G/A100
