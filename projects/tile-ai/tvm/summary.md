# tile-ai/tvm

> [`tile-ai/tvm`](https://github.com/tile-ai/tvm) · 上游贡献 · Pincent VanGogh 维护的 Apache TVM Fork,作为 TileLang 生态的上游编译器基础设施

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

## 定位
> PVG 维护的 TVM fork,为 TileLang 提供底层编译器支持。TVM 的 Relay/TIR 等编译基础设施是 TileLang IR 降级到各硬件后端的关键通道。

## 项目介绍
> **TVM 的 PVG Fork。** 基于 Apache TVM 开源编译器,增加 TileLang 生态所需的定制优化和 bug 修复。TileLang 的高层 IR 通过 TVM 的 TIR 层最终编译为各 GPU 后端的可执行代码。

## 技术栈
C++, Python, MLIR, CUDA, ROCm
## 关联
- [tile-ai/tilelang](../tilelang/) — TileLang 核心编译器,依赖 TVM
- [triton-lang/triton](../../triton-lang/triton/) — 竞品(Triton,自研编译栈)
