# pytorch/executorch

> [`pytorch/executorch`](https://github.com/pytorch/executorch) · 上游贡献 · PyTorch 移动端与边缘设备推理引擎

## 定位
> PyTorch 的"小兄弟",专为移动端/嵌入式/边缘设备打造的推理运行时。与主仓库的 torch.compile 共享前端,但生成更轻量的运行时。

## 项目介绍
> **手机和 IoT 设备上的 PyTorch 推理。** 支持 iOS/Android/嵌入式 Linux,通过 Ahead-of-Time 编译将 PyTorch 模型转为高度优化的 C++ 代码,运行时体积可小至几百 KB。

## 技术栈
C++, Python, ARM NEON, XNNPACK
## 关联
- [pytorch/pytorch](../pytorch/) — 核心框架,共享 torch.export 前端
- [pytorch/ao](../ao/) — 量化加速
