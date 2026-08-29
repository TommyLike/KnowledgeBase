# pytorch/pytorch

> [`pytorch/pytorch`](https://github.com/pytorch/pytorch) · 上游贡献 · Python 优先的深度学习框架,CPU/GPU 张量计算与自动微分引擎

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

## 定位
> PyTorch 是 Meta 开源的主流深度学习框架,与 TensorFlow/JAX 并立为三大框架。在 AI 训练和推理领域占据最大社区份额。团队关注其作为昇腾生态上游的核心地位——昇腾通过 `torch_npu` 插件适配 PyTorch,大部分 AI 工作负载通过 PyTorch 框架提交到昇腾硬件。理解 PyTorch 的架构演进(TorchDynamo/Inductor/FSDP2)直接影响团队在昇腾适配上的技术路线。

## 项目介绍
> **GPU 优先、Python 原生的张量计算与自动微分引擎,覆盖从研究原型到生产部署的全链路。** 核心组件:Tensor(多维数组)、Autograd(自动微分)、NN Module(神经网络层)、DataLoader(高效数据加载)。编译器栈:TorchDynamo(图捕获)→TorchInductor(代码生成)→Triton/CUDA kernel。分布式:FSDP(全分片数据并行)、DDP(分布式数据并行)、torch.distributed。

## 技术栈
Python(主体), C++(core/ATen), CUDA, Triton, CMake

## 关联
- [`pytorch/vision`](../vision/) — 计算机视觉模型库
- [`pytorch/audio`](../audio/) — 音频处理
- [`pytorch/executorch`](../executorch/) — 移动端推理
- [`pytorch/ao`](../ao/) — 量化与稀疏化
- [`vllm-project/vllm`](../../vllm-project/vllm/) — 基于 PyTorch 的 LLM 推理引擎
- [`sgl-project/sglang`](../../sgl-project/sglang/) — 基于 PyTorch 的高效推理框架
- [`pytorch/torchtitan`](../torchtitan/) — 大模型训练参考实现
