# triton

> [`triton-lang/triton`](https://github.com/triton-lang/triton) · 上游贡献

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `285de7a1` · MLIR · 1668文件/? · 11,747n/70,050e  
<!-- END AUTO -->

---

## 定位
> GPU Kernel 编程语言和编译器，通过 tile 级编程抽象让开发者无需手写 CUDA 即可获得接近手写优化的 GPU 性能。MAPL@PLDI 2019 论文支撑，AI 编译器领域基础项目。

## 项目介绍
> GPU Tile 级编程语言和编译器。核心场景：(1) 用 Python-like 语法编写 GPU kernel，无需手写 CUDA (2) 通过 MLIR 编译优化自动适配不同 GPU 硬件 (3) 在 PyTorch 2.0 中作为默认 GPU 后端（torch.compile）。

## 技术栈
- MLIR/LLVM

## 关联
- [`triton-lang/triton`](../../references/triton-lang/triton/) — 奠基论文 (MAPL@PLDI 2019)
- [`cosdt/triton-ascend`](../../cosdt/triton-ascend/) — 团队维护版 Ascend 后端
- [`triton-lang/triton-ascend`](../../triton-lang/triton-ascend/) — 上游 Ascend 后端

## 开放问题
> _随 delta 追加_

