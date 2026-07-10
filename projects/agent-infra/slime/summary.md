# slime

> [`THUDM/slime`](https://github.com/THUDM/slime) · 上游贡献

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-07-10T08:11:40Z · Python · 268 files · 3425n/12442e  
**入口** `train.py` · `train_async.py` (异步训练) · `slime/backends/megatron_utils/` (Megatron后端)  
**架构** Megatron-LM (训练) ↔ Ray ↔ SGLang (推理) + Data Buffer (rollout_buffer)  
**热点** `BufferQueue.append`(×171) · `TensorBackuper.get`(×127) · `exec_command`(×38)  
<!-- END AUTO -->


---

## 定位
> 智谱/清华 RL post-training 基座框架，Megatron-LM+SGLang+Ray，GLM-4.5/4.6 训练框架

## 项目介绍
> LLM 强化学习后训练框架。

## 技术栈
- Python · Megatron-LM / SGLang / vLLM / Ray

## 关联
> _待补充_

## 开放问题
> _随 delta 追加_
