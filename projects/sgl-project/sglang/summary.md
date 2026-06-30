# sglang

> [`sgl-project/sglang`](https://github.com/sgl-project/sglang) · 上游贡献

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `a2b5ce2e` · Python · 6695文件/? · 102,166n/606,179e  
<!-- END AUTO -->

---

## 定位
> LLM 结构化生成和高效推理框架，通过 RadixAttention（KV cache 自动复用）和压缩 FSM（约束解码加速）实现最高 6.4× 吞吐量提升。NeurIPS 2024 论文支撑。

## 项目介绍
> 高效 LLM 推理与结构化生成框架。核心场景：(1) AI Agent 多轮工具调用推理 (2) JSON/正则约束的结构化输出生成 (3) 多模态模型（文本/图像/视频）高效推理 (4) 通过 RadixAttention 自动复用跨请求的 KV cache。

## 技术栈
- Python · Git · Docker · CI/CD

## 关联
- [`vllm-project/vllm`](../../projects/vllm-project/vllm/) — 竞品（推理框架，PagedAttention vs RadixAttention）
- [`sgl-project/sgl-kernel-npu`](../../projects/sgl-project/sgl-kernel-npu/) — Ascend NPU 算子库

## 开放问题
> _随 delta 追加_

