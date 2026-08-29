# smg

> [`lightseekorg/smg`](https://github.com/lightseekorg/smg) · 上游贡献 · Rust 实现的全功能引擎无关 LLM 网关，支持 KV-cache 感知路由、Responses API、gRPC pipeline、多引擎 mesh 和 WASM 插件

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> SMG（Shepherd Model Gateway）是 AI Agent Gateway 领域最全面的 Rust 方案——它不仅做 Responses API（和 Agentic API 交叉），还做 KV-cache 感知路由、gRPC pipeline、多引擎 mesh 网络和 WASM 插件。在 Agent 推理基础设施中，SMG 的定位是「所有推理引擎的统一前端」：vLLM/SGLang/TensorRT-LLM/OpenAI/Anthropic 等全部通过 SMG 暴露统一的 OpenAI 兼容 API，且 SMG 利用 KV-cache 状态做智能路由优化 GPU 利用率。团队将其作为 AI Gateway 的 Rust 原生标杆跟踪。

## 项目介绍
> **GPU 集群的统一 AI 网关——接 vLLM/SGLang/TensorRT-LLM 等任何推理引擎，提供 KV-cache 感知路由、Responses API 和全功能 API 兼容层。**

核心场景：
- **多引擎统一接入**：vLLM / TensorRT-LLM / TokenSpeed / SGLang 等自建引擎 + OpenAI / Anthropic / Gemini / Bedrock 等云服务，一个 SMG 统一管理
- **KV-cache 感知路由**：根据各推理引擎 worker 的 KV-cache 状态做请求路由，最大化 cache 命中率，减少重复 prefill
- **Responses API 服务**：内置 OpenAI Responses API 支持，与 Agentic API 和 codex-relay 同为 Codex 兼容方案
- **企业级多租户**：OIDC 认证 + 速率限制 + 请求隔离，确保多团队共享 GPU 集群时的安全性和公平性
- **gRPC 高性能 pipeline**：行业首创 gRPC pipeline 架构，零拷贝 tokenization，亚毫秒路由决策

## 技术要点
- **KV-cache 感知路由**：维护每个 worker 的 cache 状态表，将新请求路由到已有相关前缀缓存的 worker，避免冗余 prefill 计算
- **gRPC + HTTP 双传输**：gRPC pipeline 用于高性能推理数据面，HTTP 用于标准 API 兼容，两者统一路由
- **多引擎 mesh 网络**：多个 SMG 节点组成 mesh 集群，worker 状态共享、自动故障转移
- **WASM 插件系统**：用户用 WASM 编写自定义路由策略、请求变换和过滤逻辑，热加载无需重启
- **40+ Prometheus 指标 + OpenTelemetry**：全链路可观测性覆盖请求路由决策、cache 命中率和延迟分布
- **Rust 原生 + PyPI/Docker/Cargo 分发**：`pip install smg`、`cargo install smg`、`docker pull` 三种部署方式

## 技术栈
Rust (Tokio/Axum), gRPC, WASM, OpenTelemetry, Prometheus, PyTorch Blog 推荐, Apache 2.0

## 关联
- [`vllm-project/agentic-api`](../../../vllm-project/agentic-api/) — 竞品/互补：Agentic API 专注 vLLM + Responses API 状态机，SMG 做全引擎 + 全协议网关
- [`BerriAI/litellm`](../litellm/) — 竞品：Python 生态的模型统一代理，SMG 是 Rust 生态的对应方案
- [`MetaFARS/codex-relay`](../codex-relay/) — 竞品/互补：codex-relay 做 Responses 翻译，SMG 内置原生 Responses
- [vLLM](https://github.com/vllm-project/vllm) / [SGLang](https://github.com/sgl-project/sglang) / [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — 被代理的推理引擎

## 开放问题
- [ ] 2026-07-16 SMG 的 KV-cache 感知路由与 vLLM 原生 prefix caching 的配合方式？是否会冲突还是互补？
- [ ] 2026-07-16 WASM 插件系统的性能 overhead？在生产高吞吐场景下是否有实测数据？
