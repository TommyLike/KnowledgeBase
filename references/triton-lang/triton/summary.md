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
