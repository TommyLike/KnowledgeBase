# vllm

> [`vllm-project/vllm`](https://github.com/vllm-project/vllm) · 上游贡献 · LLM 推理引擎

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `aab7af0b` · Python/C++/CUDA · 84,148n  
**入口** `vllm/entrypoints/` (OpenAI-compatible API, gRPC) · `vllm/v1/` (新一代引擎核心)  
**架构** API Server → Scheduler(continuous batching) → Worker(PagedAttention) → GPU/NPU/CPU  
**热点** `FlatLogprobs.append`(×1,926) · `StandaloneCompiledArtifacts.get`(×921) · `SubprocessWrapper.join`(×722) · `init_logger`(×722)  
<!-- END AUTO -->

---

## 定位
> vLLM 是当前最活跃的开源 LLM 推理引擎，由 UC Berkeley Sky Computing Lab 发起，超过 2000 位贡献者维护。SOSP 2023 论文提出 PagedAttention 算法。团队在 Ascend NPU 后端插件和 CI 基础设施上向上游贡献代码，目标是确保 vLLM 在华为 Ascend 硬件上的推理性能和兼容性。

## 项目介绍
> **高性能 LLM 推理引擎**，通过 PagedAttention 实现 KV cache 近零浪费（96%+ 利用率），吞吐量 2-4× 超越传统系统。

核心场景：
- **大模型推理服务部署**：一键启动 OpenAI 兼容的 API Server，支持 200+ 模型架构
- **KV Cache 高效管理**：PagedAttention 消除内存碎片，相同显存下支持更大 batch 和更长序列
- **多 GPU 分布式推理**：支持 TP/PP/DP/EP/CP 五种并行策略，单卡装不下的模型也能跑
- **结构化输出与工具调用**：JSON Schema 约束解码、Function Calling、推理链解析
- **Ascend NPU 推理**：通过 vllm-ascend 插件在华为 Ascend 硬件上运行 LLM

## 技术要点
- **PagedAttention**：将 KV cache 按固定 block 分页管理，消除内部和外部碎片，利用率从 20-40% 提升至 96%+
- **Continuous Batching**：iteration-level 调度，请求随时加入/退出 batch，不等整批完成
- **Prefix Caching**：自动检测和复用跨请求的相同前缀 KV cache（system prompt、few-shot examples）
- **Chunked Prefill**：将长 prompt 分块处理，避免 prefill 阶段阻塞 decode
- **Disaggregated Serving**：将 prefill 和 decode 分离到不同 GPU 节点，各自独立扩缩容
- **Speculative Decoding**：用小模型"猜"后续 token，大模型验证，2-3× decode 加速
- **FP8/MXFP4/NVFP4 量化**：多种低精度量化方案，减少显存占用 50%+ 同时保持精度
- **Multi-LoRA**：同时服务数百个 LoRA adapter，每个请求独立选择，Adapter 动态加载卸载

## 技术栈
Python · PyTorch（主力框架）· CUDA/ROCm（GPU kernel）· CUTLASS/Triton（GEMM/MoE kernel）
xFormers/FlashAttention（高效 attention）· Ray（分布式调度）· NCCL（GPU 通信）
Huawei Ascend CANN（NPU 后端）· Intel Gaudi · Google TPU

## 关联
- [`vllm-project/pagedattention`](../../references/vllm-project/pagedattention/) — 奠基论文 (SOSP 2023)
- [`vllm-project/vllm-ascend`](../../projects/vllm-project/vllm-ascend/) — 官方 Ascend NPU 后端
- [`cosdt/vllm-ascend`](../../projects/cosdt/vllm-ascend/) — 团队维护版 Ascend 后端
- [`sgl-project/sglang`](../../projects/sgl-project/sglang/) — 竞品（推理框架，RadixAttention vs PagedAttention）

## 开放问题
- [ ] 2026-06-30 v0.24.0 新架构 v1 engine 对 Ascend 后端的兼容性影响？
- [ ] 2026-06-30 SGLang 在结构化输出场景的优势是否会蚕食 vLLM 的传统市场？
