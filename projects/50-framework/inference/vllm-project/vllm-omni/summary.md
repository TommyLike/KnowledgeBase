# vllm-omni

> [`vllm-project/vllm-omni`](https://github.com/vllm-project/vllm-omni) · 上游贡献

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-08-08 · commit 待 /kg-refresh · Python 2227 files / ~737K lines · nodes 待 codebase-memory 索引  
**入口** · `vllm_omni/` 主包 · `apps/` 服务入口 · `docs/design/architecture_overview.md` 架构文档  
**架构** · Stage-based Pipeline 架构：AR Stage（Thinker/Talker）→ Diffusion Stage（DiT）→ Decoder Stage（VAE/Code2Wav），通过 OmniConnector 实现跨阶段数据传输，支持全分离（fully disaggregated）部署  
**热点** · `vllm_omni/stage_runtime/` 阶段运行时 · `vllm_omni/diffusion/` DiT 推理加速 · `vllm_omni/connector/` 跨阶段通信 · `vllm_omni/models/` 模型适配层  
<!-- END AUTO -->

---

## 定位
> vllm-project 组织的上游项目。vLLM 社区的全模态推理引擎，将 vLLM 从纯文本自回归推理扩展到支持文本、图像、音频、视频和动作（action）的全模态模型服务。团队作为上游贡献者参与，关注其在多模态推理、分离式部署、Diffusion Transformer 加速等方面的架构演进。

## 项目介绍
> 面向全模态（omni-modality）模型的高效推理与服务框架——"Easy, fast, and cheap omni-modality model serving for everyone"。

核心场景：
- **全模态对话服务**：Qwen3-Omni、MiniCPM-o 4.5 等模型的实时多模态对话
- **语音合成（TTS）**：Qwen3-TTS、CosyVoice3、VoxCPM2 等语音生成模型的高吞吐服务
- **图像/视频/音频生成**：HunyuanImage、MiniMax H3、Wan2.2、FLUX 等 Diffusion 模型的推理加速
- **机器人策略推理**：GR00T-N1.7、DreamZero-DROID、InternVLA-A1 等具身智能模型
- **全分离（disaggregated）部署**：通过 OmniConnector 将 AR 理解阶段、DiT 生成阶段、VAE 解码阶段拆分到不同 GPU 集群，按需独立扩缩容

## 技术要点
- **Stage-based Pipeline 抽象**：将复杂多模态模型拆解为独立的 Stage（如 Qwen3-Omni 的 Thinker → Talker → Code2Wav），每个 Stage 有独立的 batching 策略、并行策略和部署位置，Stage 间通过 OmniConnector 异步传输
- **OmniConnector 分离式通信**：支持 Mooncake Store/Transfer Engine、Mori、Yuanyong、共享内存等多种传输后端，实现跨节点零拷贝数据传输和动态资源分配
- **Diffusion Continuous Batching**：将 vLLM 的 continuous batching 扩展到 DiT 模型，请求级动态组批，结合 CFG-Parallel / Sequence Parallel / VAE Patch Parallel 等并行策略，提升图像/视频生成吞吐
- **Cache-DiT / TeaCache / Skip-Softmax**：针对 DiT 的注意力计算优化，通过缓存中间特征和跳过冗余 softmax 减少计算量，加速扩散去噪过程
- **Distributed Layerwise Offload**：支持将 DiT 层按策略卸载到 CPU/远程存储，降低显存峰值，使大分辨率生成可在有限 GPU 上运行
- **全双工实时推理（experimental）**：MiniCPM-o 4.5 支持流式音频输入输出，实现端到端实时语音对话

## 技术栈
- Python · PyTorch · vLLM（自回归引擎内核）· CUDA/ROCm/MUSA/NPU/XPU · NCCL/Mooncake（跨节点通信）· FlashAttention/xFormers · ModelOpt/AutoRound（量化）

## 关联
- **上游依赖**: [vllm-project/vllm](../vllm/) — 复用 vLLM 的 KV cache 管理、continuous batching、分布式调度等核心能力
- **RL 集成**: [VeRL-Omni](https://github.com/verl-project/verl-omni) — 基于 vLLM-Omni 的 RL 训练框架
- **社区生态**: [recipes](https://recipes.vllm.ai) — 社区维护的模型部署配方

## 开放问题
> _随 delta 追加_
