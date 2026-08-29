# tile-ai/tilelang

> [`tile-ai/tilelang`](https://github.com/tile-ai/tilelang) · 上游贡献 · Pincent VanGogh(PVG)发起的高性能张量计算 DSL,类 Triton 语法,面向多后端代码生成

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

## 定位
> TileLang 是一个类 Triton 的张量计算 DSL,提供 Python 原生编程体验,通过多级 IR 编译到 CUDA/ROCm/Musa/Ascend 等多种 GPU 后端。团队关注其作为昇腾 NPU 编译栈的关键上游——昇腾适配(tilelang-ascend)和 MLIR 后端(tilelang-mlir-ascend)均依赖 TileLang 核心。

## 项目介绍
> **Python 原生、多后端的 GPU 张量 DSL。** 语法类似 Triton,自动将高层张量操作编译为目标 GPU 代码。支持的性能关键特性包括:硬件感知的 Tiling 自动搜索、Shared Memory 管理、Warp 级优化、自动混合精度。

## 技术栈
Python, C++, MLIR, CUDA, TVM
## 关联
- [tile-ai/tilelang-ascend](../tilelang-ascend/) — 昇腾后端适配
- [tile-ai/tilelang-mlir-ascend](../tilelang-mlir-ascend/) — MLIR 昇腾后端
- [tile-ai/tvm](../tvm/) — 上游 TVM Fork
- [triton-lang/triton](../../triton-lang/triton/) — 竞品(Triton)
