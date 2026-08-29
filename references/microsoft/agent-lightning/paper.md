# Agent Lightning v1.0: Towards Harnessed Agentic RL

> Zhiyuan He¹, Yuqing Yang¹, Yu Kang¹, Yuge Zhang¹, Luna K. Qiu¹, Jiahang Xu¹, Chong Luo¹ (¹Microsoft); Siwei Zhang² (²Fudan University); Zhiwen Zhou³ (³Zhejiang University); Tin Yan Tsui⁴ (⁴University of Edinburgh)
>
> Microsoft Tech Report · August 2026 · arXiv:2608.17528 · Code: github.com/microsoft/agent-lightning
>
> Chinese full translation: [paper-zh.md](paper-zh.md) · Compiled Chinese PDF: [paper-zh.pdf](paper-zh.pdf)

## Abstract

Modern agents do not operate as standalone LLMs. They run inside *agent harnesses* that manage tools, context, and control flow, which makes the harness a critical component. Our original Agent Lightning work introduced a disaggregated architecture that connects arbitrary agents to reinforcement learning (RL) training through an LLM endpoint proxy. Recent frameworks such as verl Uni-Agent, AReaL 2.0, slime v0.3.0, and Polar have followed this proxy-based approach. Such a proxy-based training approach enables RL training with the harness. In this work, we use the term *harnessed agentic RL* to describe this paradigm, in which the deploy-time harness is directly involved in model post-training, thereby narrowing the gap between training and actual use.

We find that harnessed agentic RL differs fundamentally from traditional agentic RL and introduces a new set of challenges. In traditional agentic RL, the training engine owns the environment interaction loop. In harnessed agentic RL, the harness owns this loop, while the training engine observes only a sequence of LLM request-response pairs. How to model and assemble these calls into training samples remains an open question. Through a careful study, we identify several challenges, including retokenization, sample merging, advantage calculation, loss normalization, and training backend scheduling. We find that, if not properly addressed, these challenges can lead to ineffective or unstable training. Existing frameworks generally leave these issues underspecified. In this paper, we provide the first comprehensive elaboration of them.

We further present Agent Lightning v1.0, a lightweight framework for harnessed agentic RL. We treat simplicity as a first principle, implementing the framework in **only approximately 3,500 lines of code.** Its compact design supports arbitrary agent harnesses and provides a practical testbed for studying these challenges. We validate Agent Lightning v1.0 on general instruction-following agent, search agent, and coding agent. For coding agent, we find that existing RL frameworks provide limited support, including a lack of data and complete training scripts, as well as a reliance on large-scale computational resources. To address this gap, we provide a complete data-cleaning pipeline and reproducible training scripts based on open-source dataset and models. **Using only 6K training examples and modest compute, RL improves Qwen3.5-9B on SWE-bench Verified from 41.8% to 56.4%, an absolute 14.6% gain.** We release the complete workflow and scripts to facilitate reproducible harnessed agentic RL.

## 1 Introduction

Modern agents do not operate as standalone LLMs. They run inside agent harnesses that manage tools, execution environments, context, and control flow. The harness therefore determines how an agent observes its environment, acts over long horizons, and recovers from failures. Prominent examples include coding-agent harnesses such as mini-SWE-agent, OpenHands, OpenCode, Claude Code, and Codex, as well as general-purpose harnesses such as OpenClaw and Hermes.

Early RL frameworks (verl, AReaL, slime) generally require users to implement the agent loop directly inside the training framework. Integrating existing agent harnesses is difficult because they have complex implementations and their own dependencies. Our original Agent Lightning work introduced a disaggregated architecture connecting arbitrary agents to RL training through an LLM endpoint, with almost no changes to the agent. More recently, this proxy-based approach has become common in verl Uni-Agent, AReaL 2.0, slime v0.3.0, and Polar.

**Paradigm.** We use the term *harnessed agentic RL* for RL training conducted through the same agent harness used at deployment. The harness, rather than the trainer, owns context construction, tool execution, and the agent–environment interaction loop, while the training system observes and optimizes the resulting model calls across a service boundary. This preserves the harness's deployment-time context policy, tool protocols, and execution semantics without requiring its agent loop to be reimplemented inside the RL framework.

**Formal difference.** Both admit a POMDP formulation, but differ in latent state and observations:

- Traditional agentic RL: latent state is primarily environment state; p_t = (p_{t-1}, a_{t-1}, o_t); the policy observes one continuously extended token history, and a rollout naturally forms one linear token trajectory.
- Harnessed agentic RL: latent state = harness state + environment state; the harness independently constructs the request prompt for each model call; a rollout is exposed at the model boundary as a sequence of request–response pairs (p₁,a₁), (p₂,a₂), …; intervening harness and environment state transitions remain latent.

| | Agentic RL | Harnessed Agentic RL |
|---|---|---|
| State | Environment | Harness + environment |
| Model input | Continuous token history | Per-call prompts |
| Agents | Single ReAct agent | Multi-agent, subagents, and handoffs |

Four implementation challenges arise, where existing frameworks make different choices that can affect algorithmic correctness and training stability:

1. **Retokenization and sample merging.** Harnesses communicate via text messages while RL operates on tokens. Most frameworks merge two consecutive calls when p_{i+1} contains (p_i, a_i) as a complete token-level prefix. After retokenization, token IDs can differ even when text is unchanged, breaking token-level continuity.
2. **Advantage calculation.** One rollout may produce a dynamic number of training samples (from retokenization, subagent spawning, context summarization), challenging reward/advantage assignment.
3. **Loss normalization.** Sample-level normalization gives greater optimization weight to rollouts producing more samples, possibly making training unstable.
4. **Training backend scheduling under dynamic sample counts.** The backend must partition a variable sample set onto fixed GPU workers.

We provide the first systematic characterization and present Agent Lightning v1.0 (~3,500 LoC). We validate on instruction-following, search, and coding agents. For the coding agent, building on open-source SWE-smith and Qwen3.5-9B: **RL alone improves SWE-bench Verified from 41.8% to 56.4% (+14.6%) using only 6K training samples and modest compute.**

## 2 Challenges

### 2.1 Formalization

Traditional agentic RL: p_t = (p_{t-1}, a_{t-1}, o_t); the rollout sequence (p₁,a₁,o₁,a₂,o₂,a₃,…) forms a well-defined Markov process mapping naturally to one linear training sample.

Harnessed agentic RL: the harness owns the interaction loop and message state; the training engine observes C(ρ) = ((p₁,a₁),(p₂,a₂),…,(p_T,a_T)). Assembling the observed call sequence into training samples is a modeling problem. Formally, s_t = (s_t^harness, s_t^env); the harness renders C_t^msg = Context_H(s_t^harness) into p_t^tok = Tok(Template(C_t^msg)); each decision is recorded as z_t = (p_t^tok, a_t^tok) with a_t^tok ~ π_θ(· | p_t^tok). No exact token-prefix relation between consecutive prompts is assumed. **Any sequence construction for training must preserve the prompt under which each recorded action was actually sampled.**

### 2.2 Retokenization and Sample Merging

**Why token-prefix continuity breaks.** Text-level prefix (p_i^text, a_i^text) ⪯ p_{i+1}^text typically holds for multi-turn ReAct agents, but token-prefix continuity requires (p_i^tok, a_i^tok) ⪯ p_{i+1}^tok, which retokenization can break through three mechanisms:

1. **Chat-template non-compositionality.** Template(A ‖ B) ≠ Template(A) ‖ Template(B). Templates may insert delimiters or omit markers; e.g., Qwen's chat template can remove an earlier `<think>` marker.
2. **Decode–retokenize drift.** Tok(Decode(a_i^tok)) ≠ a_i^tok. E.g., `having` sampled as `h`+`aving` may retokenize as `hav`+`ing`.
3. **Inference-time output transformation.** Tool-call and structured-output handlers parse, normalize, repair, and reserialize responses, changing text even at the text level.

**Three mitigation strategies:**

| Strategy | Frameworks | Mechanism | Cost |
|---|---|---|---|
| Buffered token replacement | AReaL 2.0, verl Uni-Agent | Proxy request buffer replaces reconstructed response segments with originally sampled tokens | Changes the prompt actually consumed → **off-policy stitching** |
| Prefix-shared / tree-structured training | — | Common prefixes represented once; branch-aware causal attention masks | Tree packing, custom attention kernels, distributed gradients — heavy backend support |
| Best-effort sequence merging (ours) | Agent Lightning v1.0 | Merge only on exact token-prefix match; otherwise close sequence and start a new one | Drift merely lowers merge ratio; preserves consumed prompts; works with standard dense causal kernels |

### 2.3 Advantage Calculation

A rollout ρ can produce a dynamic number of samples N_ρ (retokenization, subagent branches, context summarization). In practice (coding-agent runs): **only 36% of rollouts on average remain a single training sample; each rollout yields 2.4 samples on average** — not an edge case.

Reward is outcome-based and assigned to every sample within the rollout. Should group statistics be computed at rollout level or sample level? Existing frameworks split: verl Uni-Agent and Polar → rollout level; slime and AReaL → sample level.

Example: Rollout 1 (reward 1) splits into 3 samples; Rollout 2 (reward 0) stays 1 sample. Rollout-level baseline: (1+0)/2 = 1/2. Sample-level baseline: (1+1+1+0)/4 = 3/4.

**Our position: rollout level is more principled.** Retokenization is incidental and should not change advantage assignment; subagent spawning and context summarization are internal harness operations and should not change the group baseline. Better credit assignment across samples within a rollout remains future work.

### 2.4 Loss Normalization

With R rollouts, N_ρ samples per rollout, L_{ρ,j} response tokens per sample, per-token loss ℓ_{ρ,j,t}:

1. **Token-mean loss (DAPO)**: L_token-mean = Σ_ρ Σ_j Σ_t ℓ / Σ_ρ Σ_j L
2. **Seq-mean-token-mean loss (GRPO)**: L_seq-mean = (1/ΣN_ρ) Σ_ρ Σ_j (1/L_{ρ,j}) Σ_t ℓ
3. **Rollout-level token-mean loss (slime)**: L_rollout-mean = (1/R) Σ_ρ (Σ_j Σ_t ℓ / Σ_j L)

Concrete example (Rollout A: two samples, lengths 50/100; Rollout B: three samples, length 30 each; Rollout C: one sample, length 40; A₁ etc. denote per-sample loss sums):

- token-mean = (A₁+A₂+B₁+B₂+B₃+C₁)/(50+100+30+30+30+40)
- seq-mean = (1/6)(A₁/50 + A₂/100 + B₁/30 + B₂/30 + B₃/30 + C₁/40)
- rollout-mean = (1/3)((A₁+A₂)/(50+100) + (B₁+B₂+B₃)/(30+30+30) + C₁/40)

**Our position: sample count should not affect gradient normalization.** seq-mean varies with how many samples a rollout happens to produce and overweights multi-sample rollouts; token-mean is sensitive to long sequences (instability later in training when many long negative samples appear). **We therefore prefer the rollout-level token-mean loss.**

### 2.5 Training Backend Complexity

Sample counts/lengths are known only after harness execution; GPU count and parallelism are fixed. The backend must map a variable workload onto fixed workers while:

- **Preserving statistical provenance**: flattened sequences retain rollout and prompt-group identifiers g_ρ; flattening must not give a rollout extra statistical weight for producing more sequences
- **Preserving update boundaries**: sequences from one rollout must stay in the same optimizer update (splitting them evaluates parts of one rollout under different policy versions → within-rollout policy skew)
- Row-based batches, data-parallel partitions, and micro-batch schedules cannot be planned from prompt/rollout counts alone

## 3 System Design

When trainer and harness are disaggregated, no single process owns the complete rollout lifecycle. A lightweight control plane must coordinate durable rollout state, external execution, partial failures, and resource usage without pulling harness logic back into the trainer.

**Agent Lightning v1.0 control plane** = declarative rollout abstraction + reconciliation loop:
- The trainer declares rollouts through the **API Gateway** — source of truth for lifecycle state and append-only events
- The **Rollout Controller** continuously reconciles this state with agent executions running as Kubernetes Jobs or local processes
- Control-plane operations are idempotent; generation attempts are recorded and resolved explicitly; a rollout ID links model requests, rewards, custom events, and execution logs into one diagnostic record
- The Gateway coordinates inference admission during collocated async RL so phase switches are invisible to the harness

Three components bridge the training cluster and execution cluster:

| Component | Responsibility |
|---|---|
| **API Gateway** | Stores rollouts, models, events; forwards harness LLM calls to trainer-registered model endpoints |
| **Rollout Controller** | Manages agent execution on Kubernetes (or a local process pool); polls rollouts and launches agent tasks |
| **Customized Trainer** (on VERL) | Registers rollouts → waits for completion → retrieves events and assembles training samples |

The trainer only creates rollouts and collects trajectories; any harness connects by switching its LLM endpoint to the proxy; training and execution resources are provisioned independently and can run in different locations. **The whole system is approximately 3,500 lines of code.**

### 3.1 Collocated Async RL

- **Sync RL**: the training step waits for the slowest rollout in the batch, leaving GPUs idle
- **Async RL (AReaL)**: rollout and update split onto two machine pools; rollout GPUs keep working during updates; but more GPUs overall and two queues to manage
- **Collocated async (ours)**: rollout and update **time-share the same GPU pool**. Once enough rollout data is collected, the update step begins; the Gateway stops accepting new requests and waits for current ones to complete, pausing any new requests until the rollout phase resumes — invisible to the harness. **~2× end-to-end speedup over sync RL with fewer GPUs.**

### 3.2 Network Issues

Two kinds of calls travel over the network: Trainer/Controller → Gateway, and harness → inference endpoint through the proxy. Two measures:

1. **Idempotent API Gateway endpoints**: repeating the same call any number of times has the same effect as calling it once
2. **Deduplication of repeated LLM API calls**: retried generations cannot be made idempotent, so sample assembly keeps only the last (most recent) model_request among calls sharing the same prompt, discarding retried/superseded ones

### 3.3 Kubernetes Integration

Existing frameworks commonly turn to commercial sandbox services (verl Uni-Agent → Modal Sandbox / Volcano veFaas; slime → E2B), expensive at RL scale. Agent Lightning v1.0 instead schedules each agent execution as a standard Kubernetes Job — entirely self-hosted, no recurring sandbox cost, full open-source stack.

### 3.4 Monitoring

The trainer records training/validation rollouts plus pod-level Kubernetes logs, enabling AI agents to automatically identify reward hacking, bad behavior, and connectivity issues — several reward-hacking examples were found this way (§4.3).

## 4 Experiments

| Setting | Search Agent | Instruction-Following | Coding Agent |
|---|---|---|---|
| Reference setup | Search-R1 | LLM-in-Sandbox | SWE-smith (self-built) |
| Model / algorithm | Llama-3.2-3B-Instruct / GRPO | Qwen3-4B-Instruct-2507 / RLOO | Qwen3.5-9B / GRPO |
| Data | HotpotQA train split | Instruction Pre-Training (80/20) | ~6K train / 400 test |
| Batch / rollouts per prompt | 512 / 4 | 8 / 8 | — |
| Reward | Exact match | — | Test pass rate |
| Validation gain | 25.1% → **41.7%** (+16.6) | 51.9% → **70.2%** (+18.3) | SWE-bench Verified 41.8% → **56.4%** (+14.6) |

### 4.3 Coding Agent Details

**Dataset preprocessing and filtering** (SWE-smith: 59,136 tasks from 128 repos; Docker images only 295 GB vs R2E-Gym 4 TB / SWE-Gym 6 TB):

1. Remove: 18,033 records with empty problem statements; 1,265 with missing problem branches; tasks with > 200 tests (e.g., python-jsonschema needs 7,000+ tests)
2. Model-based difficulty filter: run Qwen3.5-9B four times per candidate — all-solved tasks removed; mixed-success retained (~5K); plus 1,000 all-failed tasks to avoid an overly easy set

**Preventing reward hacking** (agent bypasses problem-solving to obtain reference code directly): ① git history to locate the gold commit; ② wget/curl to retrieve upstream source from GitHub; ③ pip to download package source; ④ Python networking libraries (e.g., urllib). Two safeguards: **disable Git commands and hide the .git directory**; **Kubernetes network policy blocking general outbound access with an explicit whitelist** — forcing the agent to solve tasks with only the problem statement and local information.

**Ablation (same GRPO objective):**

| Setting | Validation reward @ step 128 | SWE-bench Verified |
|---|---|---|
| Sample-level Advantage (+ token-mean) | 35.0% | — |
| Rollout-level Advantage (+ token-mean) | 33.1% | — |
| **Rollout-level Advantage + Rollout-level Norm** | **38.2%** | **41.8% → 56.4% (step 208)** |

Rollout-level normalization also controls policy entropy growth (slower and more stable than the advantage-only fix). Merge behavior measured: only 36% of rollouts remain a single fully merged row on average; 2.41 training samples per rollout — confirming the §2 dynamic-sample-count hypothesis.

## 5 Related Work

Traditional RL frameworks (verl, AReaL, slime) required the agent loop inside the training framework, making reuse of independently maintained harnesses (mini-SWE-agent, OpenHands, OpenCode, Claude Code, Codex, OpenClaw, Hermes) difficult. Agent Lightning introduced the disaggregated proxy-based architecture, since adopted by verl Uni-Agent, AReaL 2.0, slime v0.3.0, and Polar. These frameworks make different, sometimes conflicting, choices on retokenization, advantage calculation, and loss normalization, and commonly rely on commercial sandboxes. Agent Lightning v1.0 runs entirely on a self-hosted Kubernetes cluster in ~3,500 lines of code — a compact, transparent testbed validated on Search-R1, LLM-in-Sandbox, and SWE-smith settings.

## 6 Conclusion

We characterize harnessed agentic RL — the deploy-time harness, not the training engine, owns the environment interaction loop — and identify the resulting challenges in retokenization, advantage calculation, loss normalization, and training backend scheduling. We present Agent Lightning v1.0 (~3,500 lines, arbitrary harnesses, rollout-level design choices). Validated on search, instruction-following, and coding agents, with a complete data pipeline and reward-hacking safeguards: **RL alone improves Qwen3.5-9B on SWE-bench Verified from 41.8% to 56.4% (+14.6 points) using only ~6K training examples.** Full codebase and scripts released.

## Appendix: Detailed System Design

### A.1 API Gateway

A stateful service storing three object types:

- **Rollout**: one agent execution with a unique rollout ID, an input (derived from a training example), a status following the state machine queuing → running → succeeded/failed, and user-defined metadata. Not one-to-one with training examples (GRPO generates multiple independent rollouts per example).
- **Model**: identifies an LLM inference endpoint by name and address.
- **Event**: attaches arbitrary data to a rollout. By default: model_request (prompt token IDs, response token IDs, log probabilities) for every LLM interaction, and reward (scalar, typically reported once at rollout end). Custom event types supported.

Endpoints (rollout API + proxy API):

| Method | Endpoint | Comment |
|---|---|---|
| POST | /api/rollouts | Create a batch of rollouts |
| GET | /api/rollouts | List rollouts, optionally filtered by state |
| GET | /api/rollouts/{rollout_id} | Get one rollout |
| PATCH | /api/rollouts/{rollout_id} | Update rollout status |
| POST | /api/rollouts/{rollout_id}/attempt/{attempt_id}/events | Append an event to a rollout attempt |
| GET | /api/rollouts/{rollout_id}/events | Read rollout events |
| POST | /api/models | Register model endpoints |
| DELETE | /api/models | Remove all registered model endpoints |
| POST | /proxy/rollout/{rollout_id}/attempt/{attempt_id}/mode/{mode}/openai/v1/chat/completions | Forward an OpenAI-compatible model call |

The proxy path embeds the rollout ID, so every call is attributed automatically. Harnesses only need to point their OpenAI-compatible client at the proxy.

### A.2 Rollout Controller

- **K8s Reconciler**: for each queuing rollout without an existing Job, creates one from a user-provided template; watches Job updates for low-latency terminal-state propagation; periodically lists all managed Jobs to recover missed watch events (standard controller pattern)
- **Local Reconciler**: launches agents in a local process pool; owns process handles directly, so periodic polling suffices
- **State consistency**: the Gateway's rollout status is ground truth; Kubernetes-observed state may lag; the reconciler retries synchronization next cycle — best-effort eventual consistency only

### A.3 Customized Trainer

- **Dedicated Sample Adapter** (embeds the paper's design choices):
  - Sample merging: the Gateway keeps no server-side request buffer (training consistent with deployment); merge two consecutive model requests only on exact token-level prefix match
  - Advantage calculation: rollout-level baselines and advantages
  - Loss normalization: rollout-level token-mean loss, equal weight per rollout
- **Trajectory Monitoring**: exposes every training/validation rollout's input, status, model requests, rewards, token/turn statistics, and custom events, with execution logs kept in Kubernetes — inspectable manually or by AI agents

## References (selected)

- verl / HybridFlow; AReaL, AReaL 2.0; slime (incl. v0.3.0); Polar; verl Uni-Agent
- Agent Lightning (predecessor, first disaggregated architecture)
- GRPO (DeepSeekMath); DAPO; RLOO
- Search-R1; LLM-in-Sandbox; SWE-smith; SWE-bench; R2E-Gym; SWE-Gym
- mini-SWE-agent; OpenHands; OpenCode; Claude Code; Codex; OpenClaw; Hermes
- Qwen3.5-9B; Qwen3-4B-Instruct; Llama-3.2-3B-Instruct
