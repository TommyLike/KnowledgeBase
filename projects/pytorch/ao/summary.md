# pytorch/ao

> [`pytorch/ao`](https://github.com/pytorch/ao) · 上游贡献 · PyTorch 原生量化与稀疏化训练推理库

## 定位
> PyTorch 的模型压缩引擎。提供 INT4/INT8/FP8/FP4 等多精度量化方案,以及稀疏化训练/推理加速。前身是 torch.quantization,独立为 torchao 后迭代更快。

## 项目介绍
> **PyTorch 模型的量化与稀疏化加速。** 支持 QAT(量化感知训练)、PTQ(后训练量化)、weight-only 量化等,覆盖 NVIDIA/AMD/CPU 多后端。与 torch.compile 紧密集成。

## 技术栈
Python, CUDA, Triton
## 关联
- [pytorch/pytorch](../pytorch/) — 核心框架
- [pytorch/executorch](../executorch/) — 移动端量化推理
