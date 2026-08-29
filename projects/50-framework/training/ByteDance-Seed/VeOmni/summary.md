# VeOmni

> [`ByteDance-Seed/VeOmni`](https://github.com/ByteDance-Seed/VeOmni) · 字节 Seed 任意模态模型训练框架(Model-Centric Distributed Recipe Zoo)

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `32d537db5eeca24a67a4bc90d4827e2d80391293` · Python · 609文件/25M · nodes 待 codebase-memory 索引
**入口** · `veomni/` 主包 · `train.sh` · `tasks/` · `configs/`
**架构** · Trainer-free 线性训练脚本 + FSDP2/SP(Ulysses)/EP 分布式后端 + GroupGemm kernel(Liger) + Torch Distributed Checkpoint
**热点** · `veomni/`(×609) · `tasks/` · `configs/`
<!-- END AUTO -->

---

## 定位
> 字节 Seed 开源的任意模态模型训练框架,论文 *OmniScale*(arXiv:2508.02317)已被 AAAI 2026 接收。团队关注点:① 它是少见的**声明支持昇腾 NPU** 的通用训练框架(NVIDIA/AMD/昇腾三平台),与团队昇腾生态与训练底座方向强相关;② "Trainer-free" 设计与 Torch native 路线是训练框架架构演进的参考样本。团队暂无上游贡献记录。

## 项目介绍
> 面向单模态与多模态模型的预训练与后训练的统一框架——"seamlessly scale models of any modality across various accelerators"。

核心场景:
- **文本/多模态模型预训练与后训练**:DeepSeek 2.5/3/R1(236B/671B)、DeepSeek-V4、Llama3、Qwen2-3 全系
- **大规模 MoE 训练**:Qwen3-MoE、Qwen3-VL MoE(30BA3B/235BA22B),Experts Parallelism
- **图像/视频生成模型(DiT)训练**:Wan2.1-I2V-14B、LTX-2.3
- **Omni 模型训练**:Qwen2-3 Omni(7B/30BA3B)
- **RL 后训练**:内置 rl trainer,支持作为 RL 框架的 trainer backend

## 技术要点
- **Trainer-free 设计**:线性训练脚本替代 PyTorch-Lightning / HF Trainer 类"刚性结构化 trainer",训练逻辑完全透明可改;另提供 basic trainer(text/VLM/omni)与 rl trainer
- **FSDP2 后端** + **Sequence Parallelism**(DeepSpeed Ulysses,async/non-async)+ **Experts Parallelism**(Qwen3-MoE 规模验证)
- **GroupGemm kernel**(基于 Liger-Kernel):MoE 场景高效分组 GEMM
- **Torch Distributed Checkpoint**:原生分布式 checkpoint,非 HF save 格式
- **跨加速器**:NVIDIA GPU / AMD ROCm / **Ascend NPU**;Dynamic batching、Omnidata 数据处理、wandb 追踪
- 生态:已被 UI-TARS、dFactory、LMMs-Engine、OpenHA 等外部项目采用

## 技术栈
- Python · PyTorch(原生最大化利用) · FSDP2 · DeepSpeed Ulysses(SP) · Liger-Kernel(GroupGemm) · Torch Distributed Checkpoint · wandb
- 致谢/借鉴:ByteCheckpoint、veScale、LLaMA-Factory、torchtitan、torchtune

## 关联
- [vllm-project/vllm-omni](../vllm-project/vllm-omni/) — **无直接关系**。同名"Omni"属命名巧合:VeOmni 是**训练侧**框架(ByteDance-Seed),vllm-omni 是**推理/服务侧**框架(vllm-project);VeOmni README 未提及 vllm-omni
- [verl-project/verl-omni](https://github.com/verl-project/verl-omni) — **规划中关联**:VeOmni Upcoming Features 计划支持 "RL post training for omni-modality models with VeRL"(issue #262,未实现);若落地,可能形成"训练(VeOmni)→ RL(VeRL-Omni)→ 推理 rollout(vLLM-Omni)"链路
- 同类竞品参照:torchtitan、veScale、LLaMA-Factory

## 开放问题
- [ ] 2026-08-26 VeOmni 与 vllm-omni 命名易混,团队内部口径需区分(训练框架 vs 推理框架)
- [ ] 2026-08-26 昇腾 NPU 支持的实际成熟度(配置可用 vs 生产验证)待核实;与 CANN 版本矩阵的兼容性待查
