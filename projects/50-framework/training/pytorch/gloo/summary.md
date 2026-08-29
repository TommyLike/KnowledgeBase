# pytorch/gloo

> [`pytorch/gloo`](https://github.com/pytorch/gloo) · 上游贡献 · 多机训练集合通信库

## 定位
> PyTorch 分布式训练的默认 CPU 通信后端。torch.distributed 在 CPU 上默认使用 gloo 进行 allreduce/broadcast/barrier 等集合通信。

## 项目介绍
> **跨平台集合通信库。** 支持 TCP/IP 和 InfiniBand 传输,提供 allreduce/broadcast/allgather 等通信原语。相比 NCCL(仅 NVIDIA GPU),gloo 支持 CPU 和多种传输方式。

## 技术栈
C++, MPI, TCP/IP, InfiniBand
## 关联
- [pytorch/pytorch](../pytorch/) — 核心框架,CPU 分布式后端
