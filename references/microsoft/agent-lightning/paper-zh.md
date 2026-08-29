# Agent Lightning v1.0：迈向脚手架驱动的智能体强化学习（Harnessed Agentic RL）

> Zhiyuan He¹、Yuqing Yang¹、Yu Kang¹、Yuge Zhang¹、Luna K. Qiu¹、Jiahang Xu¹、Chong Luo¹（¹微软）；Siwei Zhang²（²复旦大学）；Zhiwen Zhou³（³浙江大学）；Tin Yan Tsui⁴（⁴爱丁堡大学）
>
> 微软技术报告 · 2026 年 8 月 · arXiv:2608.17528 · 项目：github.com/microsoft/agent-lightning
>
> 中文全译由 Claude 生成。术语约定：harness → 智能体脚手架；rollout / token / prompt 保留英文。

## 摘要

现代智能体并非独立运行的 LLM。它们运行在管理工具、上下文与控制流的**智能体脚手架（agent harness）**之中，脚手架因此成为智能体的关键组成部分。我们最初的 Agent Lightning 工作提出了训练与智能体执行解耦的架构，通过 LLM 端点代理将任意智能体接入强化学习（RL）训练。近期的框架如 verl Uni-Agent、AReaL 2.0、slime v0.3.0 与 Polar 均沿用了这种基于代理的方式，使 RL 训练得以在脚手架中进行。本文将这一范式称为**脚手架驱动的智能体强化学习（Harnessed Agentic RL）**：部署时脚手架直接参与模型后训练，从而缩小训练与实际使用之间的差距。

我们发现该范式与传统智能体 RL 有本质区别，并带来一系列新挑战。传统智能体 RL 中，训练引擎拥有环境交互循环；而在此范式中，脚手架拥有这一循环，训练引擎只能观察到一串 LLM 请求-响应对。如何建模并将这些调用组装成训练样本仍是一个开放问题。通过仔细研究，我们识别出若干挑战，包括重分词、样本合并、优势计算、损失归一化与训练后端调度。我们发现，若处理不当，这些挑战会导致训练无效或不稳定。现有框架普遍对此语焉不详。本文首次对这些挑战给出系统性阐述。

我们进一步提出 **Agent Lightning v1.0**，一个面向该范式的轻量级框架。我们将简洁作为第一原则，整个框架**仅用约 3500 行代码实现**。其紧凑设计支持任意智能体脚手架，并为研究上述挑战提供实用的试验平台。我们在通用指令遵循智能体、搜索智能体与编程智能体上验证了 Agent Lightning v1.0。对于编程智能体，我们发现现有 RL 框架支持有限：缺少数据与完整训练脚本，且依赖大规模计算资源。为填补这一空白，我们基于开源数据集与模型提供了完整的数据清洗管线与可复现的训练脚本。**仅使用 6K 训练样本与适量算力，RL 将 Qwen3.5-9B 在 SWE-bench Verified 上从 41.8% 提升至 56.4%，绝对提升 14.6%。**我们发布完整工作流与脚本，以促进可复现研究。

## 1 引言

现代智能体并非独立运行的 LLM。它们运行在管理工具、执行环境、上下文与控制流的**智能体脚手架**之中。脚手架因此决定了智能体如何观察环境、如何长程行动、如何从失败中恢复，是智能体能力的核心部分。典型例子包括 mini-SWE-agent、OpenHands、OpenCode、Claude Code、Codex 等编程智能体脚手架，以及 OpenClaw、Hermes 等通用脚手架。

早期 RL 框架（verl、AReaL、slime）通常要求用户直接在训练框架内部实现智能体循环。由于现有智能体脚手架实现复杂、依赖自成体系，将其直接集成进 RL 框架十分困难。我们最初的 Agent Lightning 工作提出了训练与智能体执行解耦的架构，通过 LLM 端点将任意智能体接入 RL 训练，几乎无需改动智能体本身。近来，这种基于代理的方式已被 verl Uni-Agent、AReaL 2.0、slime v0.3.0 与 Polar 等框架广泛采用。

**范式定义。**本文将"通过部署时的同一智能体脚手架进行 RL 训练"这一范式称为**脚手架驱动的智能体强化学习**。由脚手架——而非训练器——拥有上下文构建、工具执行与智能体-环境交互循环，训练系统则跨越服务边界观察并优化由此产生的模型调用。这种形式保留了脚手架部署时的上下文策略、工具协议与执行语义，无需在 RL 框架内部重新实现其智能体循环。

**形式化差异。**传统智能体 RL 与该范式都可建模为部分可观测马尔可夫决策过程（POMDP），但二者的潜在状态与呈现给策略模型的观测不同：

- **传统智能体 RL**：潜在状态主要是环境状态。模型生成动作 token，环境返回观测，token 化后的观测扩展已有历史：p_t = (p_{t-1}, a_{t-1}, o_t)。策略观察到连续扩展的 token 历史，一次 rollout 自然构成一条线性 token 轨迹。
- **脚手架驱动的智能体 RL**：潜在状态 = 脚手架状态 + 环境状态。脚手架为每次模型调用独立构造请求 prompt，策略只能观察到经 LLM API 送达的确切 prompt。一次 rollout 在模型边界上呈现为一串请求-响应对：(p₁,a₁), (p₂,a₂), …，介于其间的脚手架与环境状态转移保持潜在。

| | 传统智能体 RL | 脚手架驱动的智能体 RL |
|---|---|---|
| 状态 | 环境 | 脚手架 + 环境 |
| 模型输入 | 连续 token 历史 | 每次调用独立 prompt |
| 智能体 | 单一 ReAct 智能体 | 多智能体、子智能体与交接 |

这一差异带来四个实现挑战，现有框架的不同处理方式可能影响算法正确性与训练稳定性：

1. **重分词与样本合并**：脚手架通过文本消息与模型 API 通信，RL 训练在 token 上操作。多数框架在 p_{i+1} 于 token 层面完整包含 (p_i, a_i) 前缀时合并两次相邻调用。但重分词后即使文本不变，token ID 也可能不同，破坏 token 级连续性。
2. **优势计算**：一次 rollout 可能产生动态数量的训练样本（重分词、派生子智能体、摘要压缩上下文都会导致），给奖励与优势分配带来挑战。
3. **损失归一化**：动态样本数使损失归一化不平凡。部分框架仍在样本层面归一化，使产生更多样本的 rollout 获得更大优化权重，可能导致训练不稳定。
4. **训练后端调度**：样本数量只有在执行后才能确定，而 GPU 数量固定；后端须将变化样本集切分为训练步与小批次并在固定 worker 间均衡负载。

本文首次系统刻画这些挑战，并发布 Agent Lightning v1.0（约 3500 行代码，内置本文的设计选择）。我们在搜索/指令遵循/编程三类智能体上验证。尤其对编程智能体，基于开源 SWE-smith 数据集与 Qwen3.5-9B 提供完整数据清洗管线与可复现训练脚本：**仅靠 RL、6K 样本、适量算力，SWE-bench Verified 从 41.8% 提升至 56.4%（+14.6%）**。

## 2 挑战

### 2.1 形式化

传统智能体 RL 中训练引擎拥有交互循环：p_t = (p_{t-1}, a_{t-1}, o_t)，整个 rollout 序列 (p₁,a₁,o₁,a₂,o₂,a₃,…) 构成良定义的马尔可夫过程，自然映射为一条线性训练样本。

在此范式中，脚手架拥有交互循环与消息状态，训练引擎只能观察 LLM 端点调用。对一次 rollout ρ 记录序列 C(ρ) = ((p₁,a₁), (p₂,a₂), …, (p_T,a_T))。将观察到的调用序列组装为训练样本本身成为一个建模问题。

形式化：潜在执行状态 s_t = (s_t^harness, s_t^env) 由脚手架与环境共同维护。脚手架构造消息级上下文并渲染为 token 级 prompt：C_t^msg = Context_H(s_t^harness)，p_t^tok = Tok(Template(C_t^msg))。每个策略决策记录为调用级转移 z_t = (p_t^tok, a_t^tok)，其中 a_t^tok ~ π_θ(· | p_t^tok)。一次 rollout 产生变长转移集合，且不假设相邻 prompt 之间存在精确 token 前缀关系。**任何序列构造都必须保留每个动作实际采样时所依据的 prompt。**

### 2.2 重分词与样本合并

**为什么 token 前缀连续性会被破坏。**脚手架通过文本消息通信：C^text(ρ) = ((p₁^text, a₁^text), …)。典型多回合 ReAct 智能体中，前一次调用构成下一次 prompt 的完整文本级前缀 (p_i^text, a_i^text) ⪯ p_{i+1}^text。但 RL 训练基于精确 token ID：a_i^tok ~ π_θ(· | p_i^tok)，返回脚手架的文本为 a_i^text = Decode(a_i^tok)。token 前缀连续性要求 (p_i^tok, a_i^tok) ⪯ p_{i+1}^tok。**文本级前缀成立不保证 token 级前缀成立**——重分词后 token ID 可能改变。三种机制：

1. **聊天模板的非组合性**：Template(A ‖ B) ≠ Template(A) ‖ Template(B)。模板可能在消息边界插入分隔符或连接换行。实践中 Qwen 的聊天模板可能移除早先的 `<think>` 标记。
2. **解码-重分词漂移**：解码并非单射，Tok(Decode(a_i^tok)) ≠ a_i^tok。例：单词 `having` 采样为 `h`+`aving` 两个 token，重新分词可能得到 `hav`+`ing`。
3. **推理时的输出变换**：工具调用与结构化输出处理器可能解析、规范化、修复、重新序列化响应，改变空白符/分隔符/JSON 结构，使文本层面都不同。

**三种缓解策略及权衡：**

| 策略 | 代表框架 | 机制 | 代价 |
|---|---|---|---|
| 缓冲 token 替换 | AReaL 2.0、verl Uni-Agent | 代理维护请求缓冲，新 prompt 中上一响应文本片段用原始采样 token 替换 | 改变实际消耗的 prompt → **off-policy 拼接偏差** |
| 前缀共享/树形训练 | — | 公共前缀表示一次，分支感知因果注意力掩码 | 需要树打包、自定义注意力 kernel、分布式梯度支持，后端复杂 |
| 尽力而为序列合并（本文） | Agent Lightning v1.0 | 仅当 token 前缀精确匹配时合并，否则关闭序列开新序列 | 重分词漂移只降低合并率，保留实际 prompt，兼容标准稠密因果 kernel |

### 2.3 优势计算

一次 rollout 可产生不同数量样本 N_ρ（重分词、子智能体分支、上下文摘要都是来源）。实测（编程智能体训练）：**平均仅 36% 的 rollout 保持单一训练样本，每次 rollout 平均产生 2.4 个样本**——绝非边缘情形。

奖励基于结果并分配给 rollout 内每个样本。优势的组统计量在 rollout 级还是样本级？**现有框架选择分裂**：verl Uni-Agent 与 Polar 在 rollout 级；slime 与 AReaL 在样本级。

具体例子：Rollout 1（奖励 1）拆成 3 个样本，Rollout 2（奖励 0）保持 1 个样本。rollout 级基线 = (1+0)/2 = 1/2；样本级基线 = (1+1+1+0)/4 = 3/4。

**本文立场：rollout 级更合理。**重分词是偶发现象，优势分配不应因恰巧拆分而改变；子智能体派生与摘要压缩是脚手架内部操作，不应改变整个组的基线。rollout 内样本间的信用分配有待未来工作。

### 2.4 损失归一化

三种现有归一化（批次含 R 次 rollout，rollout ρ 产生 N_ρ 个样本，样本 j 有 L_{ρ,j} 个响应 token，逐 token 损失 ℓ_{ρ,j,t}）：

1. **token 均值损失（DAPO）**：L_token-mean = ΣΣΣℓ / ΣΣL —— 全批次 token 求和按响应 token 总数归一化
2. **序列均值-token 均值损失（GRPO）**：L_seq-mean = (1/ΣN_ρ) ΣΣ (1/L_{ρ,j}) Σℓ —— 样本内先均值、样本间均匀平均
3. **rollout 级 token 均值损失（slime）**：L_rollout-mean = (1/R) Σ_ρ (Σ_j Σ_t ℓ / Σ_j L) —— rollout 内汇总、rollout 间均匀平均

具体例子：Rollout A 两个样本（长度 50/100）、Rollout B 三个样本（各 30）、Rollout C 单样本（40）。令 A₁ 等表示样本内损失和：

- token-mean = (A₁+A₂+B₁+B₂+B₃+C₁)/(50+100+30+30+30+40)
- seq-mean = (1/6)(A₁/50 + A₂/100 + B₁/30 + B₂/30 + B₃/30 + C₁/40)
- rollout-mean = (1/3)((A₁+A₂)/(50+100) + (B₁+B₂+B₃)/(30+30+30) + C₁/40)

**本文立场：样本数量不应影响梯度归一化。**seq-mean 随 rollout 恰巧产生的样本数变化，给多样本 rollout 不成比例的高权重；token-mean 对长序列敏感（批次中许多长负样本时训练后期不稳定）。**因此偏好 rollout 级 token 均值损失。**

### 2.5 训练后端复杂度

样本数量与长度只有执行后才知道，GPU 数量与并行配置固定。后端须每次迭代将可变负载映射到固定 worker 集合，且：

- **保留统计来源**：展平为物理张量批次时，每条序列保留 rollout 标识与 prompt 组标识 g_ρ，不得因产生更多序列获得额外统计权重
- **保留更新边界**：同一次 rollout 的序列必须留在同一次优化器更新中（拆分到不同更新 = 同一 rollout 的不同部分在不同策略版本下评估 = rollout 内策略偏差）
- 批次/数据并行/微批次调度无法仅凭 prompt 或 rollout 数量提前规划

## 3 系统设计

解耦架构下没有任何单一进程拥有完整 rollout 生命周期：训练器拥有推理与优化，脚手架拥有上下文/控制流/工具/环境交互；智能体执行可能远程、跨进程生命周期、独立失败。需要一个轻量控制面协调持久化 rollout 状态、外部执行、部分失败与资源使用，同时不把脚手架逻辑拉回训练器。

**Agent Lightning v1.0 控制面** = 声明式 rollout 抽象 + 调和循环（reconciliation loop）：
- 训练器通过 **API 网关**声明 rollout——网关是生命周期状态与只追加事件的唯一事实来源
- **Rollout 控制器**持续将网关状态与 Kubernetes Job（或本地进程）上的智能体执行调和
- 控制面操作幂等，生成尝试显式记录裁决，rollout 标识串联模型请求/奖励/事件/日志为一条诊断记录
- 网关协调共址异步 RL 的推理准入，相位切换对外部脚手架不可见

三组件连接训练集群与执行集群：

| 组件 | 职责 |
|---|---|
| **API 网关** | 存储 rollout/模型/事件；将脚手架 LLM 调用转发到训练器注册的模型端点 |
| **Rollout 控制器** | K8s 集群（或本地进程池）上管理智能体执行；轮询 rollout 并启动任务 |
| **定制化训练器**（基于 VERL） | 注册 rollout → 等待完成 → 取回事件组装训练样本 |

训练器只创建 rollout 与收集轨迹；任何脚手架只需把 LLM 端点切到代理即可接入；训练与执行资源独立供给，可运行在不同地点。**整个系统约 3500 行代码。**

### 3.1 共址异步 RL

- **同步 RL**：训练步等待批次中最慢的 rollout，大量 GPU 空闲
- **异步 RL（AReaL）**：rollout 与更新拆到两个机器池，rollout GPU 保持工作；但总 GPU 更多、需分别管理两个进度不同的队列
- **共址异步（本文）**：rollout 与更新**分时共享同一 GPU 池**。数据足够即开始更新步；网关停止接受新请求并等待当前请求完成，新请求暂停到重新进入 rollout 相位——切换对脚手架不可见。**实验：相比同步 RL 端到端约 2 倍加速，且 GPU 更少。**

### 3.2 网络问题

两类调用经网络：训练器/控制器 → 网关；脚手架 → 推理端点。两项措施：

1. **幂等的网关端点**：重复调用任意次与调用一次效果相同，失败后自由重试
2. **重复 LLM 调用去重**：生成请求无法幂等（每次重试是新生成），故组装样本时对同一 prompt 的 model_request 事件去重——只保留最后一次（最新）调用，丢弃重试/被取代的调用

### 3.3 Kubernetes 集成

现有框架普遍依赖商业沙箱（verl Uni-Agent → Modal Sandbox/Volcano veFaas；slime → E2B），RL 规模下昂贵。本文将每次智能体执行调度为**标准 Kubernetes Job**，完全自托管、无持续沙箱成本、训练栈全开源。

### 3.4 监控

训练器记录训练/验证 rollout 与 Kubernetes pod 级日志，用 AI 智能体自动识别奖励黑客、不良行为与网络问题——确实借此发现了若干奖励黑客实例（§4.3）。

## 4 实验

| 设置 | 搜索智能体 | 指令遵循智能体 | 编程智能体 |
|---|---|---|---|
| 参考设置 | Search-R1 | LLM-in-Sandbox | SWE-smith（自建） |
| 模型 / 算法 | Llama-3.2-3B-Instruct / GRPO | Qwen3-4B-Instruct-2507 / RLOO | Qwen3.5-9B / GRPO |
| 数据 | HotpotQA 训练集 | Instruction Pre-Training（80/20） | ~6K 训练 / 400 测试 |
| 批次 / 每 prompt 采样 | 512 / 4 | 8 / 8 | — |
| 奖励 | 精确匹配（EM） | — | 测试通过率 |
| 验证奖励提升 | 25.1% → **41.7%**（+16.6） | 51.9% → **70.2%**（+18.3） | SWE-bench Verified 41.8% → **56.4%**（+14.6） |

### 4.3 编程智能体详情

**数据集预处理与过滤**（SWE-smith：128 仓库 59,136 任务，Docker 镜像仅 295GB，远小于 R2E-Gym 4TB / SWE-Gym 6TB）：

1. 移除：18,033 条空问题陈述、1,265 条缺失问题分支、测试数 > 200 的任务（如 python-jsonschema 需跑 7,000+ 测试）
2. 基于模型的难度过滤：Qwen3.5-9B 每任务跑 4 次——全解出 → 移除；成败混合 → 保留（约 5,000 条）；另采样 1,000 条 4 次全失败防过于简单

**防奖励黑客**（观察到智能体绕过解题过程直接偷参考代码）：① git 历史定位 gold commit；② wget/curl 从 GitHub 拉上游源码；③ pip 下载包源码；④ urllib 等 Python 网络库。两道防护：**禁用 Git 命令 + 隐藏 .git 目录**；**Kubernetes 网络策略白名单**（阻断一般出站访问）——迫使智能体仅凭问题陈述与本地信息解题。

**消融（同为 GRPO 目标）**：

| 设置 | 验证奖励 @ step 128 | SWE-bench Verified |
|---|---|---|
| 样本级优势 + token-mean | 35.0% | — |
| rollout 级优势 + token-mean | 33.1% | — |
| **rollout 级优势 + rollout 级归一化** | **38.2%** | **41.8% → 56.4%（step 208）** |

rollout 级归一化同时控制策略熵增长（比仅修优势的变体更慢更稳）。合并行为实测：平均仅 36% rollout 保持单行、平均 2.41 样本/rollout——印证第 2 节动态样本数假设。

## 5 相关工作

传统框架（verl/AReaL/slime）要求智能体循环实现在训练框架内部，复用独立维护的脚手架（mini-SWE-agent、OpenHands、OpenCode、Claude Code、Codex、OpenClaw、Hermes）困难。Agent Lightning 提出解耦架构后被 verl Uni-Agent、AReaL 2.0、slime v0.3.0、Polar 采纳。这些框架在重分词/优势/归一化上做出不同甚至冲突的选择，并普遍依赖商业沙箱。Agent Lightning v1.0 完全运行在自托管 Kubernetes 上，约 3500 行代码提供紧凑透明试验平台。

## 6 结论

本文刻画了脚手架驱动的智能体强化学习范式（部署时脚手架而非训练引擎拥有交互循环），识别重分词、优势计算、损失归一化、训练后端调度四大挑战；发布 Agent Lightning v1.0（约 3500 行，支持任意脚手架，内置 rollout 级设计选择）；在搜索/指令遵循/编程智能体上验证，发布完整数据管线与防奖励黑客保护——**仅靠 RL、约 6K 样本将 Qwen3.5-9B 在 SWE-bench Verified 上从 41.8% 提升至 56.4%（+14.6 个百分点）**；代码库与脚本全部开源。

## 附录：详细系统设计

### A.1 API 网关

有状态服务，存储三类对象：

- **Rollout**：一次智能体执行，唯一 rollout ID + 输入 + 状态机（queuing → running → succeeded/failed）+ 用户元数据。与训练样本非一一对应（GRPO 同一样本多次独立 rollout）
- **Model**：名称 + 地址标识 LLM 推理端点
- **Event**：默认记录 model_request（prompt/响应 token ID + 对数概率）与 reward（rollout 结束时标量）；支持自定义事件

端点（rollout API + 代理 API）：

| 方法 | 端点 | 说明 |
|---|---|---|
| POST | /api/rollouts | 批量创建 rollout |
| GET | /api/rollouts | 列出 rollout，可按状态过滤 |
| GET | /api/rollouts/{rollout_id} | 获取单个 rollout |
| PATCH | /api/rollouts/{rollout_id} | 更新 rollout 状态 |
| POST | /api/rollouts/{rollout_id}/attempt/{attempt_id}/events | 向 rollout 尝试追加事件 |
| GET | /api/rollouts/{rollout_id}/events | 读取 rollout 事件 |
| POST | /api/models | 注册模型端点 |
| DELETE | /api/models | 移除所有已注册模型端点 |
| POST | /proxy/rollout/{rollout_id}/attempt/{attempt_id}/mode/{mode}/openai/v1/chat/completions | 转发 OpenAI 兼容模型调用 |

代理路径嵌入 rollout ID，每次调用自动归属；脚手架只需把 OpenAI 兼容客户端指向代理。

### A.2 Rollout 控制器

- **K8s 协调器**：对无对应 Job 的 queuing rollout 从用户模板创建 Job；watch Job 更新低延迟传播终止状态 + 周期性 list 恢复漏掉的 watch 事件（标准控制器模式）
- **本地协调器**：本地进程池 + 周期轮询（持有进程句柄，无需 watch）
- **状态一致性**：网关状态是事实来源；K8s 观察到的状态可能滞后，协调器下周期重试同步，保证**尽力而为的最终一致性**

### A.3 定制化训练器

- **专用样本适配器**（体现本文设计选择）：
  - 样本合并：网关不维护服务端请求缓冲（训练与部署一致）；仅当后一次 prompt 是前一次请求+响应的精确 token 级前缀匹配时才合并
  - 优势计算：rollout 级基线与优势
  - 损失归一化：rollout 级 token 均值损失，每次 rollout 等权重
- **轨迹监控**：暴露每次训练/验证 rollout 的输入、状态、模型请求、奖励、token/回合统计与自定义事件，日志存 K8s，可人工或 AI 智能体诊断异常

## 参考文献（节选）

- verl / HybridFlow；AReaL、AReaL 2.0；slime（含 v0.3.0）；Polar；verl Uni-Agent
- Agent Lightning（本文前作，解耦架构首提）
- GRPO（DeepSeekMath）；DAPO；RLOO
- Search-R1；LLM-in-Sandbox；SWE-smith；SWE-bench；R2E-Gym；SWE-Gym
- mini-SWE-agent；OpenHands；OpenCode；Claude Code；Codex；OpenClaw；Hermes
- Qwen3.5-9B；Qwen3-4B-Instruct；Llama-3.2-3B-Instruct
