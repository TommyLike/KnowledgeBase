# 50-framework · 框架层


> **MOC 导览页** · 本层 85 个项目 · [↑ 返回栈总览](../README.md)

AI 栈的**主战场**：训练框架（pytorch 生态）、推理引擎（vllm / sglang 星座）、RL 后训练（slime / AReaL 等）。上层 Agent 的"智力"从这里生产，下层编译器/运行时为它服务。本库最大的一层。

## 推理引擎（62）

- [`sgl-project--SpecForge`](inference/sgl-project/SpecForge/) — 上游贡献
- [`sgl-project--ci-data`](inference/sgl-project/ci-data/) — 上游贡献
- [`sgl-project--cuLA`](inference/sgl-project/cuLA/) — 上游贡献
- [`sgl-project--genai-bench`](inference/sgl-project/genai-bench/) — 上游贡献
- [`sgl-project--mini-sglang`](inference/sgl-project/mini-sglang/) — 上游贡献
- [`sgl-project--ome-crd`](inference/sgl-project/ome-crd/) — 上游贡献
- [`sgl-project--rbg`](inference/sgl-project/rbg/) — 上游贡献
- [`sgl-project--rbg-api`](inference/sgl-project/rbg-api/) — 上游贡献
- [`sgl-project--sgl-cookbook`](inference/sgl-project/sgl-cookbook/) — 上游贡献
- [`sgl-project--sgl-docs`](inference/sgl-project/sgl-docs/) — 上游贡献
- [`sgl-project--sgl-eval`](inference/sgl-project/sgl-eval/) — 上游贡献
- [`sgl-project--sgl-kernel-npu`](inference/sgl-project/sgl-kernel-npu/) — ascend、npu、sglang
- [`sgl-project--sgl-kernel-xpu`](inference/sgl-project/sgl-kernel-xpu/) — 上游贡献
- [`sgl-project--sgl-learning-materials`](inference/sgl-project/sgl-learning-materials/) — 上游贡献
- [`sgl-project--sgl-project.github.io`](inference/sgl-project/sgl-project.github.io/) — 上游贡献
- [`sgl-project--sgl-test-files`](inference/sgl-project/sgl-test-files/) — 上游贡献
- [`sgl-project--sgl-whl`](inference/sgl-project/sgl-whl/) — 上游贡献
- [`sgl-project--sglang`](inference/sgl-project/sglang/) — radix-attention、sglang、structured-generation
- [`sgl-project--sglang-ci-stats`](inference/sgl-project/sglang-ci-stats/) — 上游贡献
- [`sgl-project--sglang-jax`](inference/sgl-project/sglang-jax/) — 上游贡献
- [`sgl-project--sglang-omni`](inference/sgl-project/sglang-omni/) — 上游贡献
- [`sgl-project--whl`](inference/sgl-project/whl/) — 上游贡献
- [`vllm-project--agentic-api`](inference/vllm-project/agentic-api/) — 上游贡献
- [`vllm-project--aibrix`](inference/vllm-project/aibrix/) — 上游贡献
- [`vllm-project--bart-plugin`](inference/vllm-project/bart-plugin/) — 上游贡献
- [`vllm-project--ci-infra`](inference/vllm-project/ci-infra/) — 上游贡献
- [`vllm-project--compressed-tensors`](inference/vllm-project/compressed-tensors/) — 上游贡献
- [`vllm-project--dllm-plugin`](inference/vllm-project/dllm-plugin/) — 上游贡献
- [`vllm-project--guidellm`](inference/vllm-project/guidellm/) — 上游贡献
- [`vllm-project--llm-compressor`](inference/vllm-project/llm-compressor/) — 上游贡献
- [`vllm-project--llm-multimodal`](inference/vllm-project/llm-multimodal/) — 上游贡献
- [`vllm-project--media-kit`](inference/vllm-project/media-kit/) — 上游贡献
- [`vllm-project--perf-dashboard`](inference/vllm-project/perf-dashboard/) — 上游贡献
- [`vllm-project--perf-eval`](inference/vllm-project/perf-eval/) — 上游贡献
- [`vllm-project--production-stack`](inference/vllm-project/production-stack/) — 上游贡献
- [`vllm-project--recipes`](inference/vllm-project/recipes/) — 上游贡献
- [`vllm-project--rfcs`](inference/vllm-project/rfcs/) — 上游贡献
- [`vllm-project--router`](inference/vllm-project/router/) — 上游贡献
- [`vllm-project--semantic-router`](inference/vllm-project/semantic-router/) — 上游贡献
- [`vllm-project--speculators`](inference/vllm-project/speculators/) — 上游贡献
- [`vllm-project--tpu-inference`](inference/vllm-project/tpu-inference/) — 上游贡献
- [`vllm-project--vLLM-in-PyTorch-Conference-2025`](inference/vllm-project/vLLM-in-PyTorch-Conference-2025/) — 上游贡献
- [`vllm-project--vime`](inference/vllm-project/vime/) — 上游贡献
- [`vllm-project--vllm`](inference/vllm-project/vllm/) — continuous-batching、pagedattention、vllm
- [`vllm-project--vllm-ascend`](inference/vllm-project/vllm-ascend/) — ascend、npu、vllm
- [`vllm-project--vllm-bench`](inference/vllm-project/vllm-bench/) — 上游贡献
- [`vllm-project--vllm-bnb-plugin`](inference/vllm-project/vllm-bnb-plugin/) — 上游贡献
- [`vllm-project--vllm-daily`](inference/vllm-project/vllm-daily/) — 上游贡献
- [`vllm-project--vllm-dashboard`](inference/vllm-project/vllm-dashboard/) — 上游贡献
- [`vllm-project--vllm-docs`](inference/vllm-project/vllm-docs/) — 上游贡献
- [`vllm-project--vllm-gaudi`](inference/vllm-project/vllm-gaudi/) — 上游贡献
- [`vllm-project--vllm-gguf-plugin`](inference/vllm-project/vllm-gguf-plugin/) — 上游贡献
- [`vllm-project--vllm-metal`](inference/vllm-project/vllm-metal/) — 上游贡献
- [`vllm-project--vllm-nccl`](inference/vllm-project/vllm-nccl/) — 上游贡献
- [`vllm-project--vllm-neuron`](inference/vllm-project/vllm-neuron/) — 上游贡献
- [`vllm-project--vllm-omni`](inference/vllm-project/vllm-omni/) — 全模态推理引擎（文本/图像/音频/视频/动作），Stage Pipeline + OmniConnector 分离式部署
- [`vllm-project--vllm-openvino`](inference/vllm-project/vllm-openvino/) — 上游贡献
- [`vllm-project--vllm-project.github.io`](inference/vllm-project/vllm-project.github.io/) — 上游贡献
- [`vllm-project--vllm-project.github.io-static`](inference/vllm-project/vllm-project.github.io-static/) — 上游贡献
- [`vllm-project--vllm-report`](inference/vllm-project/vllm-report/) — Daily commit monitor and AI analysis for vllm/vllm-ascend
- [`vllm-project--vllm-skills`](inference/vllm-project/vllm-skills/) — 上游贡献
- [`vllm-project--vllm-xpu-kernels`](inference/vllm-project/vllm-xpu-kernels/) — 上游贡献

## RL 后训练（4）

- [`THUDM--slime`](rl-posttrain/slime/) — rl、rlhf、post-training
- [`alibaba--ROLL`](rl-posttrain/ROLL/) — rl、rlhf、post-training
- [`inclusionAI--AReaL`](rl-posttrain/AReaL/) — rl、rlhf、post-training
- [`radixark--miles`](rl-posttrain/miles/) — rl、rlhf、post-training

## 训练框架（19）

- [`ByteDance-Seed--VeOmni`](training/ByteDance-Seed/VeOmni/) — 字节 Seed 任意模态训练框架 OmniScale(AAAI'26),Trainer-free+FSDP2/SP/EP,支持昇腾 NPU
- [`pytorch--FBGEMM`](training/pytorch/FBGEMM/) — pytorch、训练、推理
- [`pytorch--TensorRT`](training/pytorch/TensorRT/) — pytorch、训练、推理
- [`pytorch--ao`](training/pytorch/ao/) — pytorch、训练、推理
- [`pytorch--audio`](training/pytorch/audio/) — pytorch、训练、推理
- [`pytorch--executorch`](training/pytorch/executorch/) — pytorch、训练、推理
- [`pytorch--extension-cpp`](training/pytorch/extension-cpp/) — pytorch、训练、推理
- [`pytorch--gloo`](training/pytorch/gloo/) — pytorch、训练、推理
- [`pytorch--helion`](training/pytorch/helion/) — pytorch、训练、推理
- [`pytorch--ignite`](training/pytorch/ignite/) — pytorch、训练、推理
- [`pytorch--kineto`](training/pytorch/kineto/) — pytorch、训练、推理
- [`pytorch--ort`](training/pytorch/ort/) — pytorch、训练、推理
- [`pytorch--pytorch`](training/pytorch/pytorch/) — pytorch、训练、推理
- [`pytorch--rl`](training/pytorch/rl/) — pytorch、训练、推理
- [`pytorch--tensordict`](training/pytorch/tensordict/) — pytorch、训练、推理
- [`pytorch--tensorpipe`](training/pytorch/tensorpipe/) — pytorch、训练、推理
- [`pytorch--torchtitan`](training/pytorch/torchtitan/) — pytorch、训练、推理
- [`pytorch--vision`](training/pytorch/vision/) — pytorch、训练、推理
- [`pytorch--xla`](training/pytorch/xla/) — pytorch、训练、推理

## 关联论文

- [`antgroup--areal`](../../references/antgroup/areal/summary.md) — `rl, system, asynchronous, llm, areal`
- [`bytedance--dapo`](../../references/bytedance/dapo/summary.md) — `rl, dapo, reasoning, llm`
- [`deepseek--deepseek-r1`](../../references/deepseek/deepseek-r1/summary.md) — `rl, grpo, reasoning, llm`
- [`deepseek--deepseekmath`](../../references/deepseek/deepseekmath/summary.md) — `rl, grpo, math, llm`
- [`microsoft--agent-lightning`](../../references/microsoft/agent-lightning/summary.md) — `rl, agentic-rl, agent-harness, llm`
- [`misc--rl-llm-survey`](../../references/misc/rl-llm-survey/summary.md) — `rl, survey, rlhf, llm`
- [`sgl-project--sglang`](../../references/sgl-project/sglang/summary.md) — `read`
- [`stanford--dpo`](../../references/stanford/dpo/summary.md) — `rl, rlhf, alignment, llm`
- [`vllm-project--pagedattention`](../../references/vllm-project/pagedattention/summary.md) — `read`
