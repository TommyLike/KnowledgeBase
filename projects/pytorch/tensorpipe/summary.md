# pytorch/tensorpipe

> [`pytorch/tensorpipe`](https://github.com/pytorch/tensorpipe) · 上游贡献 · PyTorch 的张量感知点对点通信原语

## 定位
> PyTorch 分布式通信的传输层抽象。提供张量级别的点对点通信,支持多种传输方式(TCP/SHM/IB)的自动选择。

## 项目介绍
> **张量级别的点对点通信。** 自动根据 tensor 大小和设备选择最优传输方式(小张量用 Unix socket,大张量用共享内存或 InfiniBand),对上层透明。

## 技术栈
C++, CUDA, InfiniBand
## 关联
- [pytorch/pytorch](../pytorch/) — 核心框架的传输层
- [pytorch/gloo](../gloo/) — 集合通信(多对多)
