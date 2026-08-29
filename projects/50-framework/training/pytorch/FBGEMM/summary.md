# pytorch/FBGEMM

> [`pytorch/FBGEMM`](https://github.com/pytorch/FBGEMM) · 上游贡献 · Meta 开源的高性能矩阵乘法与量化推理库

## 定位
> PyTorch 的量化推理后端引擎。提供 x86 和 ARM 平台上的 INT8/INT4 矩阵乘法加速,是 PyTorch 默认的 CPU 量化推理后端。

## 项目介绍
> **通用矩阵乘法(GEMM)加速库。** 最初为 Facebook 推荐系统设计,现已扩展到支持多种量化格式和稀疏矩阵运算。torch.ao 的量化模型在 CPU 上推理时底层调用 FBGEMM。

## 技术栈
C++, x86 AVX2/AVX512, ARM NEON
## 关联
- [pytorch/pytorch](../pytorch/) — 核心框架的量化后端
- [pytorch/ao](../ao/) — 量化前端
