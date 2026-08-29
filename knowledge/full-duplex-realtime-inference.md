# vLLM-Omni 全双工实时推理深度分析

> 基于 vLLM-Omni v0.26.0 代码仓库分析 | 2026-08-08
>
> 涉及项目：[vllm-project--vllm-omni](../projects/50-framework/inference/vllm-project/vllm-omni/)

---

## 一句话理解

vLLM-Omni 的全双工实时推理是一套让模型**像人一样对话**的运行时系统：用户一边说话，模型一边听、一边思考、一边生成语音回复——这些步骤是**并行的**，不是停下后它才处理。通过 v0.26.0 进入 **experimental** 阶段，当前唯一支持的模型是 **MiniCPM-o 4.5**。

---

## 核心架构：三层解耦

```
┌─────────────────────────────────────────────┐
│          WebSocket / OpenAI Realtime         │  ← 传输层
│    ws://host:8099/v1/realtime?duplex=1      │
├─────────────────────────────────────────────┤
│   openai/  — 会话控制器 + 协议投影           │  ← 协议层
│   ├─ DuplexSessionRunnerMixin               │
│   ├─ NativeRealtimeSessionProtocol          │
│   ├─ commit_policy (listen/speak decision)  │
│   └─ websocket.py (ordered mailbox)         │
├─────────────────────────────────────────────┤
│   core/  — 模型无关的双工抽象                │  ← 运行时核心
│   ├─ DuplexRuntime   (event loop)           │
│   ├─ DuplexSession   (state machine)        │
│   ├─ DuplexAdapter   (model policy seam)    │
│   └─ protocol.py     (event types)          │
├─────────────────────────────────────────────┤
│   minicpmo45/  — MiniCPM 模型策略            │  ← 模型适配
│   ├─ Stage0 连续 KV 连续性                  │
│   ├─ Stage1 TTS + Token2Wav 连续性          │
│   └─ 模型自有的 listen/speak 决策           │
├─────────────────────────────────────────────┤
│   engine/  — 调度器数据面适配                │  ← 引擎层
│   ├─ AsyncOmni orchestrator                │
│   └─ request 预注册 + 可恢复请求流           │
└─────────────────────────────────────────────┘
```

包边界（来自 `vllm_omni/experimental/fullduplex/README.md`）：

```text
core/        model-agnostic duplex contracts (adapter, session, turn runtime)
engine/      AsyncOmni/orchestrator scheduler data-plane adapter
openai/      WebSocket transport, Realtime projection, and audio codecs
minicpmo45/  MiniCPM input framing, policy, compatibility, and Stage0 state
joyvl/       JoyVL model-specific integration
personaplex/ PersonaPlex lockstep engine, model-owned runtime, and serving
```

---

## 关键设计要点

### 1. Epoch-based Barge-In（打断机制）

这是全双工最核心的机制。会话状态机在 `core/session.py` 的 `DuplexSession` 中：

```
DuplexSession:
  epoch: int           ← 每次打断 +1
  response_index: int  ← 每次生成 +1
  state: IDLE → LISTENING → RESPONDING → ...

begin_response() → (response_index, epoch)
barge_in()       → epoch += 1
is_stale(epoch)  → epoch != self.epoch   ← 旧生成被忽略
```

核心事件协议（`core/protocol.py`）：

| 事件 | 方向 | 含义 |
|------|------|------|
| `INPUT_APPEND` | client → server | 追加音频 chunk |
| `INPUT_COMMIT` | client → server | 当前一段话语结束 |
| `RESPONSE_CREATE` | client → server | 请求模型生成回复 |
| `RESPONSE_CANCEL` | client → server | 取消当前生成（打断） |
| `RESPONSE_CREATED` | server → client | 回复开始生成 |
| `RESPONSE_DELTA` | server → client | 音频/文本增量 |
| `RESPONSE_DONE` | server → client | 回复完成（模型决定说话） |
| `PLAYBACK_ACK` | client → server | 回放确认 |

**工作流**（`core/runtime.py` 的 `DuplexRuntime.run()`）：

1. 用户开始说话 → `INPUT_APPEND` audio chunks → state = LISTENING
2. 模型决定回应 → `RESPONSE_CREATE` → 启动异步生成 task（`_respond()`）
3. 用户**打断**（继续说话/另起 `INPUT_APPEND`）→ `barge_in()` → epoch += 1 → 旧 task 被 `cancel()`，输出被 `is_stale()` fence
4. 新 `INPUT_COMMIT` → 新一轮 `respond()` 以新 epoch 启动

这意味着模型生成的语音可以被**中途打断并丢弃**（cancel），不会积压过期输出。

### 2. Async Chunk：TTFP 降低 92%

来自 `docs/design/feature/async_chunk.md`，是降低实时对话延迟的核心技术：

```
Qwen3-Omni: Thinker → Talker → Code2Wav

async_chunk OFF:
  Thinker decode all → Talker all → Code2Wav all → 首音频到达
  TTFP ≈ 6.5s  ← 用户等了 6 秒才听到第一声

async_chunk ON:
  Thinker token → Talker per-token chunk → Code2Wav chunk → 首音频到达
  各 stage 异步重叠执行，chunk 到达即处理
  TTFP ≈ 0.52s  ← 降低 92%
```

Chunk 规格：
- **Thinker → Talker**：per decode step (chunk_size=1)
- **Talker → Code2Wav**：累积到 `codec_chunk_frames`（默认 25）后发送；初始阶段用动态 IC 进一步降低 TTFP
- **Code2Wav**：流式解码

性能数据（H800, cuGraph enabled, Qwen3-Omni, text 100 token input, 50 prompts）：

| 指标 | async_chunk OFF | async_chunk ON | 改善 |
|------|:---:|:---:|:---:|
| E2E Latency (conc=1) | 6581ms | 6179ms | -6% |
| E2E Latency (conc=10) | 13522ms | 11152ms | -17% |
| TTFP 首音频 (conc=1) | 6459ms | **523ms** | **-92%** |
| RTF 实时率 (conc=1) | 0.24 | 0.22 | -8% |
| RTF 实时率 (conc=10) | 0.49 | 0.41 | -16% |

**关键优化点**：
- **IO-Compute 重叠**：chunk get/put 通过后台线程异步，不阻塞调度器
- **Non-blocking Scheduler**：等待 chunk 的请求不阻塞整个调度器
- **Code2Wav Batch Inference**：支持 code2wav 阶段的批处理（batch_size=64 在高并发下可额外提升 30% 吞吐）

### 3. 模型自有的 Listen/Speak 决策

vLLM-Omni **不做**浏览器端 VAD（voice activity detection）。MiniCPM-o 4.5 在模型内部做 turn-taking 决策：

- `response.listen` — 模型决定"我在听，用户继续说话"
- `response.done` — 模型决定"我该说话了"，开始生成回复

这意味着**模型自己控制对话节奏**，不是靠固定的静音检测阈值。代码中的 `decide_commit_action()` 在 `openai/commit_policy.py` 中实现。

### 4. Stage 连续性保证

对于 MiniCPM-o 4.5 的三阶段（Stage0 理解 KV → Stage1 TTS → Token2Wav），全双工要求**跨 turn 的 KV 连续性**：

- **Stage0 KV 不因打断而重置**：打断只是弃掉旧 response 的生成部分，但理解阶段产生的 KV cache 保留，新 response 可以从已有的语义理解继续
- **Transcript/Audio cursor**：转录和音频输出有 response 和 turn 两个层级的光标管理
- **Playback acknowledgement**：客户端回放确认后，服务端才知道哪些音频已经被播放，哪些可以丢弃

来自 `DESIGN.md` 记录的已验证契约：

> - MiniCPM Stage0 conversation KV continuity
> - Stage1 TTS and Token2Wav continuity
> - model-owned listen/speak decisions on the normal auto-response path
> - continuous browser PCM upload during assistant playback, without browser VAD
> - segment EOS and turn EOS as different boundaries
> - transcript/audio cursors scoped to a response and turn
> - stale epoch/turn/response fencing

---

## 客户端视角

demo 代码位于 `examples/online_serving/minicpmo/realtime_duplex_demo.py`，展示了完整的使用流程：

```python
# 1. WebSocket 连接（OpenAI Realtime 兼容协议）
url = "ws://localhost:8099/v1/realtime?duplex=1"
client = RealtimeDuplexClient(url)

# 2. 配置会话（模型、参考音频、温度）
await client.configure(model="openbmb/MiniCPM-o-4_5",
                        ref_audio=ref_audio_data_url,
                        temperature=0.7)

# 3. 边录边传（200ms 一个 PCM chunk）
await client.stream_pcm16(input_pcm16, chunk_ms=200, realtime=True)

# 4. Commit → 等待模型决策
await client.commit()

# 5. 流式接收事件
#    response.audio_transcript.delta  → 转写文本流
#    response.audio.delta             → 音频 chunk (base64 PCM16)
#    response.listen                  → 模型决定继续听
#    response.done                    → 模型决定说话
```

**关键延迟指标**（demo 中实际测量）：
- **TTFT**（首文本延迟）：commit 发送到第一个文本 token
- **TTFP**（首音频延迟）：commit 发送到第一个音频 chunk
- **RTF**（实时率）：生成耗时 / 音频时长，<1 表示比实时快

---

## 实验状态与限制

| 方面 | 状态 |
|------|------|
| **生产就绪** | ❌ experimental，不视为生产级 |
| **模型支持** | 仅 MiniCPM-o 4.5（还有 JoyVL 和 PersonaPlex 两个 demo 集成） |
| **并发会话** | 已验证 2 路并发（H20），check-in 配置限制为 2 路 |
| **VAD** | 不依赖浏览器 VAD，模型自行决策 turn-taking |
| **视频/音画同步** | ❌ 不支持 |
| **长会话 KV 管理** | ❌ 无上限控制（bounded KV 未实现） |
| **确定性 VAD 打断** | ❌ 不提供（浏览器端有意不跑 VAD） |
| **Multi-session fairness** | ❌ 无生产级准入/公平/容量/故障恢复 |

来自 `DESIGN.md` 的明确声明：

> The checkpoint does not claim:
> - scheduler-native KV append
> - deterministic VAD-triggered interruption
> - production multi-session admission, fairness, capacity, or failure recovery
> - bounded long-session KV
> - video input or audio/video synchronization

---

## 可复用的分层思想

vLLM-Omni 的全双工架构有三个可以应用到其他项目的设计原则：

1. **模型无关的 DuplexAdapter 接口**：只需实现 `on_input()` + `respond()` + `should_respond()` 三个方法就能接入新模型，`core/` 包处理所有生命周期、epoch fence、playback cursor。接入新模型只需创建 `vllm_omni/experimental/fullduplex/<model>/` 并实现 `DuplexAdapter`。

2. **OpenAI Realtime 协议兼容**：WebSocket + `/v1/realtime` 接口与 OpenAI 的 realtime API 协议一致，可以直接接现有的前端/客户端生态。

3. **Async Chunk 是独立特性**：不依赖 fullduplex，任何多 stage pipeline 都可以用它来降低首字节/首音频延迟。在多并发场景下改善更显著（E2E -17%, RTF -16% at conc=10）。

---

## 相关文件索引

| 文件 | 内容 |
|------|------|
| `vllm_omni/experimental/fullduplex/core/runtime.py` | DuplexRuntime 主事件循环 |
| `vllm_omni/experimental/fullduplex/core/session.py` | DuplexSession 状态机 + epoch fence |
| `vllm_omni/experimental/fullduplex/core/protocol.py` | 事件类型定义 |
| `vllm_omni/experimental/fullduplex/openai/session_runner.py` | WebSocket 会话控制器 |
| `vllm_omni/experimental/fullduplex/openai/commit_policy.py` | listen/speak 决策逻辑 |
| `vllm_omni/experimental/fullduplex/DESIGN.md` | 运行时架构 checkpoint 记录 |
| `vllm_omni/experimental/fullduplex/README.md` | 包边界 + 接入指南 |
| `docs/design/feature/async_chunk.md` | Async Chunk 设计与性能数据 |
| `examples/online_serving/minicpmo/realtime_duplex_demo.py` | 客户端 demo |
| `examples/online_serving/minicpmo/realtime_web/` | 浏览器 demo (WebSocket) |
