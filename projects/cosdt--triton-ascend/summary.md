# triton-ascend — 项目摘要
> [https://github.com/cosdt/triton-ascend](https://github.com/cosdt/triton-ascend)

> cosdt | Ascend NPU 适配版 Triton 编译器，C++/Python MLIR 编译框架
> Python | 1548 文件 | 18MB | commit: 617b5cc3
> Codebase: 5,017 nodes / 22,919 edges

## 入口
python/triton/__init__.py, lib/

## 架构
Python DSL → Triton IR → TritonGPU IR → LLVM IR (MLIR 编译流水线)

## 热点模块
DFSSubgraphState.empty(116), arange(93), zeros(92), store(86), load(83)

