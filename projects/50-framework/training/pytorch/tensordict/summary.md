# pytorch/tensordict

> [`pytorch/tensordict`](https://github.com/pytorch/tensordict) · 上游贡献 · PyTorch 专用张量字典容器

## 定位
> torchrl 的基础设施,提供类 dict 的 Tensor 容器,支持 GPU 上的高效批量操作,是强化学习和多模态场景的通用数据结构。

## 项目介绍
> **结构化 Tensor 容器。** 类似 Python dict 但 key 映射到 Tensor,支持懒加载、内存映射、NestedTensor 嵌套等,尤其适合 RL 的 (state, action, reward) 三元组存储。

## 技术栈
Python, PyTorch
## 关联
- [pytorch/pytorch](../pytorch/) — 核心框架
- [pytorch/rl](../rl/) — 强依赖
