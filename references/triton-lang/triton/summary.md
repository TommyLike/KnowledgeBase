# Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations

> MAPL@PLDI 2019 (2019) | Philippe Tillet, Hsiang-Tsung Kung, David Cox
> DOI: [10.1145/3315508.3329973](https://doi.org/10.1145/3315508.3329973)
> 关联项目: triton-lang--triton, triton-lang--triton-ascend

## Abstract (EN)

Triton is a language and compiler for GPU kernel programming centered around the concept of tiles. It provides a C-based language and LLVM-based IR for expressing tensor programs on parametric tile variables, with novel tile-level optimization passes. Demonstrates performance on par with hand-tuned cuBLAS/cuDNN for matrix multiply and convolution.

## 摘要 (中文)

Triton 是面向 GPU kernel 编程的语言与编译器，核心概念是基于 tile（分块）的计算。提供 C 风格语言和基于 LLVM 的中间表示，通过参数化的 tile 变量表达张量程序，并包含新颖的分块级优化 pass。在矩阵乘法和卷积上性能媲美手写 cuBLAS/cuDNN。

## Tags
triton, compiler, mlir, gpu, tile

## 详细中文导读

### 1. 问题背景
GPU kernel 编程极其复杂：
- CUDA 编程需要深入理解 GPU 架构（shared memory、寄存器、warp）
- 手写 kernel 性能优化耗时且不可移植
- 现有 DSL（如 Halide、TVM）面向 CPU，不适用 GPU

### 2. 核心创新: Tile-based 编程模型

**Triton 语言**
- C 风格语法，基于 **tile**（分块）的编程抽象
- 用户只需定义 tile 级别的操作，编译器处理底层优化
- 参数化 tile 变量，自动适应不同硬件

**Triton 编译器**
- 基于 MLIR/LLVM 的中间表示
- tile-level 优化 pass：自动内存合并、共享内存分配、延迟隐藏
- 生成 PTX/CUDA 代码

### 3. 实验结果
- 矩阵乘法: 性能媲美 cuBLAS（差距 <5%）
- 卷积: 性能媲美 cuDNN
- 代码量: 通常 <25 行 Python，vs 数百行 CUDA
- 可在 NVIDIA/AMD/Intel GPU 上运行
- 后衍生为 triton-lang 开源社区项目
