# lm-evaluation-harness

> [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) · 上游贡献 · LLM 统一基准评测框架，Hugging Face Open LLM Leaderboard 核心引擎

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> LM Evaluation Harness 是 LLM 评测领域的事实标准框架，被 Hugging Face Open LLM Leaderboard 作为核心评测引擎。团队将其纳入知识图谱用于追踪上游评测标准演进，确保自研模型和 agent 系统的评测方法与国际基准对齐。作为 EleutherAI 生态的核心项目，它定义了模型能力评估的统一接口，直接影响我们在模型选型、agent 能力评估和 benchmark 设计上的技术决策。

## 项目介绍
> **为生成式语言模型提供统一、可复现的跨基准测试评估框架，覆盖 200+ 标准化评测任务，支持从本地模型到商业 API 的多种后端。**

核心场景：
- **学术基准测试**：在 MMLU、HellaSwag、ARC、GSM8K、TruthfulQA 等 60+ 学术基准上评估模型能力，支持生成式 (generate_until) 和对数似然 (loglikelihood) 两种评测模式
- **多后端模型对比**：同一套评测任务，无缝切换 HuggingFace Transformers、vLLM、SGLang、Megatron-LM、NeMo、GGUF (llama.cpp)、OpenVINO、ONNX Runtime 等本地后端，以及 OpenAI API、Anthropic API 等商业 API
- **大规模分布式评测**：通过 accelerate、torchrun、PyTorch DTensor (TP)、Ray 等支持数据并行、张量并行、专家并行和模型分片，适合千亿参数级模型的评测
- **社区排行榜引擎**：作为 Hugging Face Open LLM Leaderboard 的核心评测引擎，被 NVIDIA、Cohere、BigScience、BigCode、Nous Research、Mosaic ML 等组织使用
- **可扩展自定义任务**：通过 YAML 配置 + Jinja2 模板快速定义新基准任务，支持 few-shot 示例定制、答案抽取正则、后处理逻辑等

## 技术要点
- **三核心请求类型 API Contract**：模型必须实现 `generate_until`（自由生成直到停止词）、`loglikelihood`（单条对数似然）、`loglikelihood_rolling`（滑动窗口对数似然），外加 `multiple_choice` 输出类型，构成框架的抽象边界，实现模型后端与评测任务的解耦
- **YAML 任务定义 + Jinja2 提示工程**：每个评测任务通过 YAML 文件定义（包含 metric、dataset_path、prompt 模板、fewshot 配置、doc_to_text/doc_to_target 转换函数等），使用 Jinja2 模板引擎构造 prompt，支持灵活的 few-shot 示例选择和排序
- **多级并行策略**：支持数据并行、张量并行 (DTensor TP)、流水线并行 (accelerate device_map)、vLLM TP + Ray 多副本数据并行，覆盖从小规模单卡到大集群的各种场景
- **PEFT/量化/控制向量支持**：原生支持 LoRA adapter 评测、GPTQ/AutoGPTQ 量化模型、bitsandbytes 4-bit 量化、delta-weight 模型，以及 steering vector 注入评测，覆盖模型训练后修改的各类评测需求
- **日志与可观测性**：内置 Weights & Biases 集成、Zeno 可视化错误分析、支持上传结果到 HuggingFace Hub 并记录 sample-level 生成结果，便于结果复现和错误模式分析
- **Task Versioning 机制**：每个任务有 version 字段，任务定义变更时更新版本号，确保不同时期评测结果可复现和可追溯，避免因 benchmark 定义变化导致的评测结论漂移
- **Answer Extraction 与后处理 Pipeline**：支持正则提取答案、标准化去空格等后处理链、多数投票等聚合策略，确保从模型原始输出到最终评分的处理过程标准化
- **Proxy 模型接口**：可通过 `--model_args` 传入自定义 API endpoint，将任意兼容 OpenAI API 格式的服务包装为评测后端，极大降低自定义模型接入门槛

## 技术栈
Python, PyTorch, HuggingFace Transformers/Datasets, Accelerate, vLLM, SGLang, llama.cpp, ONNX Runtime, OpenVINO, Mamba SSM, Ray, torchrun, PyTorch DTensor, GPTQModel, AutoGPTQ, bitsandbytes, Jinja2, Weights & Biases, Zeno, MIT License

## 关联
- [`agent-runtime/inference/vllm`](../../inference/vllm/summary.md) — vLLM 是本框架支持的高吞吐推理后端之一，用于大规模模型评测加速
- [`agent-runtime/inference/sglang`](../../inference/sglang/summary.md) — SGLang 是本框架支持的推理后端之一，提供结构化生成和高效推理能力
- 上游依赖: HuggingFace Transformers/Datasets, PyTorch, vLLM, SGLang
- 下游使用者: Hugging Face Open LLM Leaderboard（核心评测引擎）, GPT-NeoX, Megatron-DeepSpeed
- 竞品/同类: HELM (Stanford CRFM), OpenCompass (上海 AI Lab), BigBench (Google), lmms-eval (多模态 fork)
- EleutherAI 体系关联: GPT-NeoX, Pythia, The Pile 等 EleutherAI 核心项目共用此评测框架

## 开放问题
- [ ] 2026-07-02 框架对多模态评测（如 lmms-eval fork）的支持程度如何？是否需要单独引入 lmms-eval？
- [ ] 2026-07-02 对于 agent 场景的评测（工具调用、多轮对话、规划能力），现有 benchmark 覆盖是否充分？是否需要自定义 agent-specific 任务？
- [ ] 2026-07-02 vLLM/SGLang 后端在大规模评测时的稳定性表现如何？是否有已知的性能瓶颈或兼容性问题？
