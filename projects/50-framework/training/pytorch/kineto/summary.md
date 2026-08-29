# pytorch/kineto

> [`pytorch/kineto`](https://github.com/pytorch/kineto) · 上游贡献 · PyTorch 的性能 Profiling 基础设施

## 定位
> PyTorch 的 GPU/CPU Profiler 底层库,负责收集 CUDA kernel 执行时间线、内存分配追踪和算子调用堆栈。

## 项目介绍
> **GPU/CPU 性能剖析库。** 与 NVIDIA CUPTI/ROCm roctracer 对接,捕获 GPU kernel 执行时间线,生成 Chrome Tracing 可读的时间线文件。torch.profiler 的用户界面底层由 kineto 驱动。

## 技术栈
C++, CUDA, CUPTI
## 关联
- [pytorch/pytorch](../pytorch/) — 核心框架的 profiler 后端
