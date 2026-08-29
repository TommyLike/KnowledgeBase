# 10-compiler · 编译器与代码生成


> **MOC 导览页** · 本层 11 个项目 · [↑ 返回栈总览](../README.md)

把高层张量程序**下降（lower）**到具体硬件能执行的核函数。上承框架的算子调用，下接芯片的指令集——决定"同一段模型代码能不能高效跑在 GPU/NPU/多种加速器上"。本层是 AI 栈里离硬件最近、又直接影响上层性能天花板的一环。

## 项目（11）

- [`tile-ai--tilelang`](tile-ai/tilelang/) — tilelang、compiler、dsl
- [`tile-ai--tilelang-ascend`](tile-ai/tilelang-ascend/) — tilelang、compiler、dsl
- [`tile-ai--tilelang-metax`](tile-ai/tilelang-metax/) — tilelang、compiler、dsl
- [`tile-ai--tilelang-mlir-ascend`](tile-ai/tilelang-mlir-ascend/) — tilelang、compiler、dsl
- [`tile-ai--tilelang-musa`](tile-ai/tilelang-musa/) — tilelang、compiler、dsl
- [`tile-ai--tvm`](tile-ai/tvm/) — tilelang、compiler、dsl
- [`triton-lang--Triton-to-tile-IR`](triton-lang/Triton-to-tile-IR/) — 上游贡献
- [`triton-lang--kernels`](triton-lang/kernels/) — 上游贡献
- [`triton-lang--triton`](triton-lang/triton/) — compiler、gpu、mlir
- [`triton-lang--triton-ascend`](triton-lang/triton-ascend/) — ascend、compiler、npu
- [`triton-lang--triton-ext`](triton-lang/triton-ext/) — 上游贡献

## 关联论文

- [`huawei--hifloat4`](../../references/huawei/hifloat4/summary.md) — `quantization, ascend, npu`
- [`huawei--hifloat8`](../../references/huawei/hifloat8/summary.md) — `quantization, ascend, npu`
- [`triton-lang--triton`](../../references/triton-lang/triton/summary.md) — `read`
