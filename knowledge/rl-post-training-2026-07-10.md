# RL for LLM 关键论文分析

> [Archived] 2026-07-10 | 来源: 论文调研
> 涉及: 6 篇 2023-2025 关键论文 + 5 个 slime 生态项目
> 本页为时间点快照，知识可能已过时。

## 核心结论

2023-2025 年，RL for LLM 领域经历了从 **RLHF（对齐）→ DPO（简化）→ GRPO（推理）** 的三阶段跃迁。关键转折点是 DeepSeek-R1 证明了纯 RL 能让 LLM 自主涌现推理能力。

## 论文关系图

```
RLHF (InstructGPT, 2022)
  ├─ DPO (Rafailov, 2023) — 消掉 reward model，直接优化偏好
  │   ├─ KTO / SimPO / ORPO — 进一步简化
  │   └─ 局限: 离线训练，不适合推理场景
  │
  └─ GRPO (Shao/DeepSeekMath, 2024) — 消掉 critic network
      ├─ DeepSeek-R1 (Guo, 2025) — GRPO + 可验证奖励 → 推理涌现
      ├─ DAPO (Yu/ByteDance, 2025) — 改进 GRPO 的 vanishing advantage
      ├─ Dr. GRPO / Reinforce++ — 进一步简化
      │
      └─ 系统工程:
          ├─ AReaL (Ant, 2025) — 全异步 RL，2.77× 加速
          ├─ slime (THUDM) — Megatron+SGLang+Ray 基座
          ├─ ROLL (Alibaba) — 20+ 算法，Ascend NPU
          ├─ Miles (RadixArk) — 企业级 fork
          └─ vime (vLLM) — vLLM 后端替代
```

## 论文对比

| 维度 | DPO | GRPO | DAPO |
|------|-----|------|------|
| 需要 reward model? | ❌ (内置) | ✅ (需要可验证奖励) | ✅ |
| 需要 critic? | N/A | ❌ (组内归一化) | ❌ |
| 训练模式 | 离线 (固定偏好数据) | 在线 (rollout→reward→update) | 在线 |
| 推理能力 | 弱 (对齐为主) | ✅ (数学/代码) | ✅ (更强) |
| 显存开销 | 低 | 中 | 中高 (动态采样) |
| 主要用途 | 对齐/安全/风格 | 推理/代码/数学 | 推理/代码/数学 |
| 代表模型 | Zephyr, Llama-3 | DeepSeek-R1, GLM-4.5 | Qwen+DAPO |

## 技术要点

### 1. 为什么 GRPO 取代了 PPO？

PPO 需要 4 个模型同时加载：policy + reference + critic + reward。GRPO 把 critic 消掉（用组内归一化替代），把 reward model 换成可验证函数（数学答案对错/代码pass@k）。从 4 模型 → 2 模型（policy + reference），显存减半。

### 2. DPO 和 GRPO 的分工

- **DPO**: 适合"对齐"场景（让模型更 helpful/harmless）。数据来自人类偏好，离线训练，不需要在训练时生成新数据。
- **GRPO**: 适合"推理"场景（数学/代码）。数据来自可验证奖励（答案对不对），在线训练（模型自己生成→奖励→更新）。GRPO 能让模型学会"试错"，DPO 不能。

### 3. 从同步到异步（AReaL 的创新）

传统 RL：训练等 rollout 结束 → rollout 等训练完成 → GPU 空转。AReaL 将两者完全解耦：rollout loop 持续生成数据写入 buffer，training loop 持续从 buffer 读数据训练，互不等待。在 1000 GPU 上实现了 2.77× 的端到端加速。

### 4. slime 生态的"安卓化"

智谱开源 slime 后：
- 阿里 fork → ROLL（+Ascend NPU 支持 + 20+ 算法）
- 蚂蚁 fork → AReaL（+全异步）
- RadixArk fork → Miles（+FP8/INT4/R3 企业特性）
- vLLM fork → vime（+vLLM 后端替代 SGLang）

这形成了类似 Android 的生态：一个核心框架 + 多个厂商定制版本。RL post-training 基础设施正在标准化。

## 开源项目数据

| 项目 | 组织 | 代码规模 | 关系 | 特色 |
|------|------|---------|------|------|
| slime | 智谱/清华 | 3,425n/12,442e | 基座 | Megatron+SGLang+Ray |
| ROLL | 阿里 | 4,985n/23,201e | fork | 20+算法/FSDP2/Ascend |
| AReaL | 蚂蚁 | 12,134n/63,474e | fork | 全异步RL/NeurIPS |
| Miles | RadixArk | 7,203n/31,721e | fork | FP8/INT4/R3/企业 |
| vime | vLLM | 3,305n/12,642e | fork | vLLM backend |

## 来源

- [DeepSeek-R1](https://arxiv.org/abs/2501.12948) — Guo et al., 2025
- [DeepSeekMath/GRPO](https://arxiv.org/abs/2402.03300) — Shao et al., 2024
- [DPO](https://arxiv.org/abs/2305.18290) — Rafailov et al., 2023
- [RL for LLM Survey](https://arxiv.org/abs/2407.16216) — Wang et al., 2024
- [AReaL](https://arxiv.org/abs/2505.24298) — Ant Group, 2025
- [DAPO](https://arxiv.org/abs/2410.06584) — Yu et al., 2025
- [slime](https://github.com/THUDM/slime) · [ROLL](https://github.com/alibaba/ROLL) · [AReaL](https://github.com/inclusionAI/AReaL) · [Miles](https://github.com/radixark/miles) · [vime](https://github.com/vllm-project/vime)
