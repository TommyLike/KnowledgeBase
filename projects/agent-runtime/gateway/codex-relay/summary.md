# codex-relay

> [`MetaFARS/codex-relay`](https://github.com/MetaFARS/codex-relay) · 上游贡献 · Rust 实现的轻量 Responses API → Chat Completions 协议翻译桥，让 Codex CLI 对接任意 OpenAI 兼容推理服务

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> Codex-relay 是 Agentic API 生态中「协议翻译」路线的代表——不自己实现 Responses API 的完整状态机，而是在 Codex CLI（发 Responses API 请求）和任意 Chat Completions 推理服务之间做实时协议翻译。与 Agentic API（vLLM 原生实现 Responses API 服务端状态机）和 SMG（全功能网关内置 Responses API）形成技术路线对比。团队关注 AI Agent Gateway 领域的协议翻译 vs 原生实现两条技术路线的演进。

## 项目介绍
> **Codex 的万能翻译器——启动一个本地 Rust 代理，Codex 的 Responses API 请求自动转为标准 Chat Completions，让任何 OpenAI 兼容 API 都能跑 Codex。**

核心场景：
- **用 DeepSeek/Kimi/Qwen 跑 Codex**：Codex 默认只支持 OpenAI，codex-relay 在本地把 Responses API 协议翻译为 Chat Completions，一行 pip install 即可对接任何提供商
- **零配置模型元数据生成**：`--print-config` 自动生成 Codex 所需的 `model_properties` 配置段，避免「Model metadata not found」警告
- **多 Provider 切换**：通过环境变量切换上游 Provider，无需修改 Codex 配置

## 技术要点
- **Responses → Chat 协议翻译**：核心转换逻辑将 OpenAI 的有状态 Responses API（input items、tool calls、tool outputs、previous_response_id）转为无状态的 Chat Completions API 的 messages 格式
- **Python/Rust 双重分发**：PyPI wheel 发布 + crates.io 发布，覆盖 Python 和 Rust 用户
- **模型能力元数据自动发现**：从上游 API 自动获取可用模型列表并生成 Codex `model_properties` 配置
- **轻量单进程代理**：`codex-relay` 一个二进制，启动即用，无外部依赖

## 技术栈
Rust, OpenAI API protocol, PyPI/Cargo, MIT

## 关联
- [`vllm-project/agentic-api`](../../../vllm-project/agentic-api/) — 竞品/互补：Agentic API 原生实现 Responses API（服务端状态机），codex-relay 做协议翻译（无状态代理）
- [`lightseekorg/smg`](../smg/) — 竞品：SMG 是全功能 Rust Gateway 内置 Responses API
- [OpenAI Codex](https://github.com/openai/codex) — 被代理的客户端
- [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses) — 源协议

## 开放问题
- [ ] 2026-07-16 Responses→Chat 的协议翻译是否会丢失有状态会话的语义信息（如 tool call 结果的精确映射）？未来是否计划实现原生 Responses API 状态机？
