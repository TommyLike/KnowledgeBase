# Agent Lightning v1.0: Towards Harnessed Agentic RL

> Zhiyuan He, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Jiahang Xu, Chong Luo（微软）; Siwei Zhang（复旦）; Zhiwen Zhou（浙大）; Tin Yan Tsui（爱丁堡）· 2026 · arXiv:2608.17528 · 技术报告 18 页 · [本地 PDF](paper.pdf) · [中文全译 PDF](paper-zh.pdf) · [全文 markdown](paper.md) · [中文全文](paper-zh.md) · [项目](https://github.com/microsoft/agent-lightning)

## 中文摘要
本文提出 **Harnessed Agentic RL（脚手架驱动的智能体强化学习）** 范式并发布 Agent Lightning v1.0。核心观察：现代智能体运行在管理工具/上下文/控制流的**智能体脚手架（agent harness）**中，部署时的脚手架（而非训练引擎）拥有环境交互循环，训练引擎只能通过 LLM 端点代理观察到一串请求-响应对。将这类调用组装成训练样本带来四个此前被低估的挑战：① **重分词与样本合并**——重分词会破坏 token 前缀连续性（聊天模板非组合性、解码-重分词漂移、推理时输出变换三种机制），框架间的缓冲 token 替换可能引入 off-policy 拼接；② **优势计算**——一次 rollout 产生动态数量样本（实测平均 2.4 个），应在 rollout 级而非样本级计算基线；③ **损失归一化**——rollout 级 token 均值损失优于样本级归一化（seq-mean 让多样本 rollout 权重过大、token-mean 对长负样本敏感）；④ **训练后端调度**——动态样本数映射到固定 GPU worker，须保留 rollout 级统计与更新边界。Agent Lightning v1.0 以 **约 3500 行代码**实现（API 网关 + Rollout 控制器 + 定制化训练器），支持任意脚手架，自托管 Kubernetes（弃用商业沙箱），并引入**共址异步 RL**（rollout 与更新分时共享同一 GPU 池，端到端快约 2 倍且 GPU 更少）。实验：搜索智能体（Search-R1 设置，验证 25.1%→41.7%）、指令遵循（LLM-in-Sandbox，51.9%→70.2%）、编程智能体（SWE-smith 数据清洗 + 防奖励黑客 + **仅 6K 样本将 Qwen3.5-9B 从 SWE-bench Verified 41.8% 提升至 56.4%，+14.6%**）。消融证实 rollout 级优势 + rollout 级归一化最优（38.2% vs 35.0%/33.1%@step128）。

## English Abstract
This paper introduces the paradigm of Harnessed Agentic RL and releases Agent Lightning v1.0. Modern agents run inside agent harnesses managing tools, context, and control flow; in harnessed RL the deploy-time harness — not the training engine — owns the environment interaction loop, so the trainer observes only request–response pairs at an LLM endpoint proxy. Assembling these calls into training samples raises four underappreciated challenges: (1) retokenization and sample merging (token-prefix continuity breaks via chat-template non-compositionality, decode–retokenize drift, and inference-time output transformation; buffered-token replacement can be off-policy stitching); (2) advantage calculation should be rollout-level, not sample-level (a rollout yields a dynamic number of samples, 2.4 on average in practice); (3) loss normalization favors rollout-level token-mean (sample-level seq-mean overweights multi-sample rollouts; token-mean is sensitive to long negative sequences); (4) training backend scheduling must map dynamic sample counts onto fixed GPU workers while preserving rollout provenance. Agent Lightning v1.0 implements these choices in only ~3,500 lines of code (API Gateway + Rollout Controller + Customized Trainer on VERL), supports arbitrary harnesses, runs on self-hosted Kubernetes instead of commercial sandboxes, and introduces collocated async RL sharing one GPU pool between rollout and update (~2× end-to-end speedup with fewer GPUs). Results: search agent (25.1%→41.7%), instruction following (51.9%→70.2%), and coding agent — with a complete SWE-smith data-cleaning pipeline and reward-hacking safeguards, RL alone improves Qwen3.5-9B on SWE-bench Verified from 41.8% to 56.4% (+14.6) with only ~6K training examples. Ablations confirm rollout-level advantage + rollout-level normalization is best (38.2% vs 35.0%/33.1% @ step 128).

## 技术要点
- **HARL 范式定义**：部署时脚手架拥有上下文构建/工具执行/交互循环，训练器只观察 LLM 端点上的请求-响应对；POMDP 潜在状态 = 脚手架状态 + 环境状态；已被 verl Uni-Agent、AReaL 2.0、slime v0.3.0、Polar 采纳
- **重分词破坏 token 前缀连续性**：三种机制（聊天模板非组合性如 Qwen 移除 `<think>`、解码-重分词漂移如 having→h/aving vs hav/ing、推理时输出变换）；缓冲 token 替换（AReaL/verl Uni-Agent）改变实际消耗的 prompt → off-policy 偏差；树形训练代价大；本文选尽力而为序列合并（精确 token 前缀才合并）
- **rollout 级 vs 样本级统计量**：实测仅 36% rollout 保持单样本、平均 2.41 样本/rollout；样本级优势使基线从 1/2 偏到 3/4；rollout 级 token 均值损失（slime 方案）在三种归一化中最稳
- **共址异步 RL**：与 AReaL 异步 RL（双 GPU 池）对比，rollout 与更新分时共享同一 GPU 池，API 网关在相位切换时暂停新请求使切换对脚手架不可见；约 2 倍端到端加速且 GPU 更少
- **防奖励黑客双防护**：禁用 Git 命令 + 隐藏 .git 目录；Kubernetes 网络策略白名单阻断出站网络——堵住 git 历史/wget/pip/urllib 四条偷答案路径

## 关联项目
- [`THUDM--slime`](../../projects/50-framework/rl-posttrain/slime/summary.md) — 论文引用 slime v0.3.0（采纳代理式训练，样本级优势 + rollout 级归一化，本文对其选型的批判对象之一）
- [`inclusionAI--AReaL`](../../projects/50-framework/rl-posttrain/AReaL/summary.md) — 论文引用 AReaL/AReaL 2.0（异步 RL 提出者 + 缓冲 token 替换实现者，共址异步的直接对照）
- [`radixark--miles`](../../projects/50-framework/rl-posttrain/miles/summary.md) — slime 企业级 fork，同受本文 rollout 级归一化设计影响
- [`vllm-project--vime`](../../projects/50-framework/inference/vllm-project/vime/summary.md) — vLLM 原生 RL post-training，verl 系训练后端，与定制化训练器同源
- [`deepseek-ai--deepseek-harness`](../../projects/60-agent/framework/deepseek-harness/summary.md) — 论文定义的 agent harness 概念与 KG 内 harness 项目同源词，可交叉参照
