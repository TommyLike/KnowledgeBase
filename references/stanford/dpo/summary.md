# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

> Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn (Stanford) · 2023 · arXiv:2305.18290

## 中文摘要
DPO 解决了 RLHF 需要显式训练 reward model 的问题。核心发现：Bradley-Terry 偏好模型下的最优策略有一个闭式解，可以直接从偏好数据优化策略，把 reward model 消掉。比 RLHF+PPO 更简单、更稳定，但不适合需要探索的推理场景（被 GRPO 补充）。NeurIPS 2023。

## 技术要点
> _待补充_

## 关联项目
['alignment', 'llm', 'rl', 'rlhf']

## 关联
> _待补充_
