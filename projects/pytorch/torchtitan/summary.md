# pytorch/torchtitan

> [`pytorch/torchtitan`](https://github.com/pytorch/torchtitan) · 上游贡献 · PyTorch 原生大模型训练平台

## 定位
> PyTorch 团队官方出品的 LLM 预训练参考实现,展示如何用纯 PyTorch 原生 API(FSDP/TP/PP)高效训练 GPT-like 模型。

## 项目介绍
> **PyTorch 原生大模型训练最佳实践。** 用 FSDP2 + Tensor Parallel + Pipeline Parallel 训练 Llama 3 架构模型,支持 FP8 训练、异步检查点、数据加载优化。目标是证明 PyTorch 原生分布式 API 已足够成熟。

## 技术栈
Python, PyTorch FSDP2, NCCL
## 关联
- [pytorch/pytorch](../pytorch/) — 核心框架
- [pytorch/ao](../ao/) — FP8 量化训练
