# tile-ai/tilelang-ascend

> [`tile-ai/tilelang-ascend`](https://github.com/tile-ai/tilelang-ascend) · 上游贡献 · TileLang 昇腾 NPU 后端适配:算子库与硬件特定优化

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

## 定位
> TileLang 在华为昇腾 NPU 上的后端适配层。将 TileLang IR 编译到 Ascend 可执行算子,是 TileLang 支持国产芯片的关键组件。

## 项目介绍
> **TileLang→Ascend NPU 的后端。** 提供昇腾硬件专用的算子实现、内存布局优化、CANN 集成和性能调优。

## 技术栈
Python, C++, CANN, Ascend NPU
## 关联
- [tile-ai/tilelang](../tilelang/) — 上游 DSL
- [tile-ai/tilelang-mlir-ascend](../tilelang-mlir-ascend/) — MLIR 昇腾后端
