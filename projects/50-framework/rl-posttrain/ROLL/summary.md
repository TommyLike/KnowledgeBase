# ROLL

> [`alibaba/ROLL`](https://github.com/alibaba/ROLL) · 上游贡献

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-07-10T08:11:40Z · Python · 358 files · 4985n/23201e  
**入口** `roll/pipeline/rlvr/` (RLVR) · `roll/pipeline/agentic/` (Agent RL) · `roll/distributed/` (分布式)  
**架构** Pipeline → Scheduler (generate/rollout/reward) → Executor (FSDP2/Megatron/HF) → Platform (CUDA/NPU/ROCm)  
**热点** `BatchProxy.items`(×211) · `transfer_backend.get`(×205) · `ItemsGroup.info`(×180)  
<!-- END AUTO -->


---

## 定位
> 阿里 RL for LLM 框架，20+ RL 算法(PPO/GRPO/Reinforce++/GSPO)，支持 Ascend NPU

## 项目介绍
> LLM 强化学习后训练框架。

## 技术栈
- Python · Megatron-LM / SGLang / vLLM / Ray

## 关联
> _待补充_

## 开放问题
> _随 delta 追加_
