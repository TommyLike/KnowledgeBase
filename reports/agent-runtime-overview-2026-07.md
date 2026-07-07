# Agent Runtime 技术概览

> 调研周期:2026-07-07 | 覆盖 72 开源项目 / 8 子领域 | 数据源:KG summary + codebase-memory 49 zst

---

## 一、背景:为什么 Agent Runtime 是一个独立的基础设施层

2024-2026 年,AI Agent 从"ChatGPT 的玩具"变成生产级应用。但 Agent 不是 LLM API 调用者的简单封装——它是一个**自主生成代码、调用工具、跨多轮持久化状态的不可信进程**。这催生了一个全新的基础设施需求:Agent Runtime。

不同于 LLM 推理引擎(vLLM/SGLang/Triton)解决"怎么高效跑模型",Agent Runtime 解决的是"模型跑起来之后,怎么安全、可靠、可观测地让 Agent 与世界交互"。从 Agent 收到用户指令到返回最终结果的全链路,每一层都需要专门的运行时能力:

```
用户指令
   │
   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Planner    │    │   Protocol   │    │   Gateway    │
│ 任务分解与   │◄──►│ Agent间通信  │◄──►│ API/模型     │
│ 推理执行     │    │ MCP + A2A    │    │ 统一路由治理 │
└──────┬───────┘    └──────────────┘    └──────┬───────┘
       │                                       │
       ▼                                       ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Sandbox    │    │   Memory     │    │  Security    │
│ 代码执行隔离 │◄──►│ 状态与上下文 │◄──►│ 内容安全     │
│ VM/容器/进程 │    │ 持久化管理   │    │ 输入输出拦截 │
└──────┬───────┘    └──────────────┘    └──────────────┘
       │                                       │
       ▼                                       ▼
┌──────────────┐    ┌──────────────┐
│    Tool      │    │ Observability│
│ 浏览器/API   │    │ 追踪/评估/   │
│ 外部世界交互 │    │ 成本监控     │
└──────────────┘    └──────────────┘
```

---

## 二、关键问题全景:8 个子领域各自要解决什么

| # | 子领域 | 核心矛盾 | 项目数 |
|---|--------|---------|--------|
| 1 | **Sandbox** | Agent 生成不可信代码,「隔离强度」vs「启动速度」vs「运维成本」三元权衡 | 27 |
| 2 | **Memory** | 多轮/跨 session 的上下文持久化,「存储结构」vs「检索精度」的取舍 | 14 |
| 3 | **Gateway** | 多模型/多 Provider/多 Agent 之间的统一路由、协议转换、认证、成本归因 | 10 |
| 4 | **Observability** | Agent 非确定性行为的追踪、评估、回归测试——没有 exception,只有不可靠的答案 | 10 |
| 5 | **Tool** | Agent 如何与外部世界交互(浏览器/API/文件系统)?「发现-调用-解析」闭环 | 7 |
| 6 | **Protocol** | Agent↔Tool(MCP)与 Agent↔Agent(A2A)的通信标准化 | 2 |
| 7 | **Planner** | Agent 多步任务分解与执行,框架层还是运行时层? | 1 |
| 8 | **Security** | Agent 输入/输出的越狱/注入/有害内容/敏感信息泄露如何实时拦截 | 1 |

---

## 三、技术方向分类

### 3.1 Sandbox(执行隔离与安全)——27 项目

#### 方向 1:MicroVM 硬件级隔离(安全优先)

以 Firecracker/Kata/gVisor 实现 VM 级安全边界,适合多租户、不可信代码。代表:
- **E2B**(1219★):Agent 沙箱事实标杆,Firecracker microVM,<200ms 冷启动,API-first
- **NVIDIA/OpenShell**(7434★):多后端(microVM/Podman/Docker/K8s),核心差异是凭据代理出口网关+GPU VFIO 直通
- **OpenSandbox**(11856★):协议驱动,5 语言 SDK+MCP 原生集成,Credential Vault

#### 方向 2:容器级隔离(主流平衡点)

利用 Docker/K8s/Podman 成熟生态,启动快于 VM 但隔离弱于 VM。代表:
- **kubernetes-sigs/agent-sandbox**(3077★):K8s 原生 Sandbox CRD 规范
- **coder**(13722★):Terraform 模板化开发环境,Terraform 模板化工作空间
- **CubeSandbox**(7986★):腾讯云容器安全增强,Rust 实现
- **cohere-terrarium**(312★):双运行时(Docker+Pyodide 浏览器端),最轻量

#### 方向 3:进程级轻量隔离(速度优先)

利用 OS 原生安全基元(macOS Seatbelt/Linux bubblewrap/WASM),零基础设施依赖。代表:
- **sandbox-runtime**(4592★):Claude Code 安全底座,npm 安装即用,无容器
- **DTVM**(158★):WASM 确定性执行,状态快照回滚
- **sandbox-sdk**(1059★):Cloudflare V8 isolates,毫秒启动,330+边缘节点

#### 方向 4:安全策略、标准化与平台托管

在现有沙箱之上提供安全策略插件、标准化 API 或全托管平台。代表:
- **agent-aegis**(173★):Agent 全生命周期安全防护插件
- **AWS Bedrock AgentCore 套件**(3 项目):全托管 Firecracker 沙箱平台
- **google/ax**(1838★):Google 分布式 Agent 运行时,DAG 任务调度
- **NemoClaw**(21629★):OpenShell 之上细粒度权限白名单,凭证不落盘

**关键趋势**:凭据管理与沙箱解耦(多项目不约而同让 Agent 看不到 API key)、多后端可插拔成为共识、OpenTelemetry 集成几乎成为标配。

---

### 3.2 Memory(状态与记忆管理)——14 项目

#### 方向 1:记忆层框架(API-First)

独立于 Agent 框架的记忆中间层,提供标准 `add()/search()/update()` API。代表:
- **mem0**(60253★):领域标杆,三层记忆+向量+图(Neo4j),记忆关系图是核心差异
- **memU**(13991★):最结构化方案,六类定型抽取+Tool Memory+Salience 强化记忆
- **ReMe**(3159★):AgentScope 生态记忆工具包
- **TencentDB-Agent-Memory**(6831★):全本地部署,隐私优先,零云端依赖

#### 方向 2:有状态 Agent(OS 级记忆管理)

将记忆嵌入 Agent 进程内部,Agent 自主管理"页面调度"。代表:
- **letta**(23678★):学术先驱(MemGPT),虚拟上下文管理,Self-Editing Memory
- **powermem**(738★):OceanBase 出品,数据库基因(LSM-Tree+事务),数据可靠性优先

#### 方向 3:混合索引与统一搜索

一引擎内融合向量+全文+图三种搜索范式。代表:
- **OpenViking**(26377★):字节/火山的 Context DB,专为 Agent 设计
- **beads**(25125★):Go 原生三合一(HNSW+倒排+邻接表)嵌入式引擎

#### 方向 4-7:RAG 平台 / 事件溯源 / 原文优先 / 后端基础设施

- **ragflow**(84446★):中文 RAG 标杆,DeepDoc 深度文档解析
- **mempalace**(57043★):**不做摘要不抽取不改写**,纯原文+层次结构,LongMemEval 96.6% R@5 第一
- **supabase**(105832★):PostgreSQL 底座一站式 Agent 后端
- **hindsight**(18062★):事件溯源引擎,不可变日志
- **seekdb**(2784★):分布式数据库内建 AI 搜索

**核心争论**:「原文优先(mempalace)」vs「LLM 抽取(mem0/memU)」——原文路线在 LongMemEval 上碾压摘要路线,但数万轮对话的存储成本和检索精度仍是未知数。

---

### 3.3 Gateway(API 与模型访问治理)——10 项目

#### 方向 1:LLM 统一路由

一行代码换模型,Gateway 负责路由/负载均衡/故障转移。代表:
- **LiteLLM**(52800★):事实标准,100+Provider,OpenAI 格式作为通用界面
- **New API**(41323★):国内最活跃,唯一实现 OpenAI-Claude-Gemini 双向格式互转
- **Higress**(8799★):阿里开源,Envoy Wasm 层 FNV-1a 一致性哈希 AI 路由
- **Envoy AI Gateway**(1813★):Envoy Filter 层透明拦截,与 Service Mesh 集成

#### 方向 2:协议转换

OpenAI 兼容(路线 A,主流)vs 双向互转(路线 B,多 Agent 协作场景)。CC Switch(114028★)走桌面端配置级切换。

#### 方向 3:认证与流控

双层认证(Agent 侧+Provider 侧),流控从 QPS→RPM/TPM→Token 三级跃迁。Higress 的 Token 粒度方案最精细;MCP Gateway Registry(772★)的 6 IdP 联邦认证最灵活。

#### 方向 4:MCP 网关注册

MCP Gateway Registry / Higress MCP Bridge / CC Switch 三种互补路线:注册中心 vs 网关内嵌 vs 桌面管理,尚未统一。

**特殊项目**:rtk(69019★,CLI proxy 减 Token 消耗 60-90%)和 agentgateway(3720★,Agentic Proxy for MCP)属于 GateWay 的创新边缘。

---

### 3.4 Observability(可观测性与评估)——10 项目

#### 方向 1:全景追踪平台

像分布式追踪看微服务一样看 Agent。全部拥抱 OTel。代表:
- **Langfuse**(30580★):最流行,Trace+Eval+Prompt Management 三位一体
- **Phoenix**(10423★):Arize 出品,OpenInference 语义约定+自动插桩
- **Opik**(20379★):Comet 出品,从 ML 实验到 LLM 追踪全栈连续性(93K 节点,最大代码库)
- **OpenLIT**(2579★):GPU+LLM 全栈,填补 GPU 利用率/VRAM 监控缺口

#### 方向 2:专项评估框架

将 LLM 质量评估包装为可编程 CI/CD 测试。代表:
- **DeepEval**(16684★):pytest 式通用评估,15+ 指标
- **RAGAS**(14695★):RAG 专项评估手术刀,v2 扩展到 Agent 评估
- **LM Evaluation Harness**(13204★):模型基准,200+ 标准化任务

#### 方向 3:安全评估

- **Promptfoo**(22986★):Red teaming,OpenAI 和 Anthropic 都在用
- **TruLens**(3423★):Snowflake 出品,OTel 原生+RAG 三合一+Agent 七维评估

**关键洞察**:三类平台正在趋同——Langfuse+RAGAS、Phoenix+DeepEval、Promptfoo+TruLens 都在构建"追踪→评估→改进"闭环。

---

### 3.5 Tool(工具集成与执行)——7 项目

#### 方向 1:浏览器自动化

让 Agent 操作网页。代表:
- **browser-use**(103174★):重量级完整功能,视觉+DOM 双模式
- **agent-browser**(37975★):Rust 轻量 CLI,Serverless 友好
- **browser-harness**(15778★):自愈型 harness,LLM 驱动修复
- **page-agent**(24675★):JS in-page GUI agent,纯前端路线

#### 方向 2:网页内容提取

让 Agent 读懂网页。代表:
- **firecrawl**(146442★):⭐最高,深度爬取+结构化提取+反反爬
- **reader**(11480★):jina.ai,URL→Markdown 零配置,Late Chunking

#### 方向 3:工具集成平台

- **composio**(29118★):1000+工具集成,Managed Auth 托管认证是核心创新

**趋势**:DOM+VLM 混合定位成为共识,反检测能力是硬壁垒。

---

### 3.6 Protocol(Agent 间通信协议)——2 项目

**核心分工**:
- **MCP**(8545★):Agent 的"手"——调用工具/数据/API,Anthropic 提出,已成事实标准(月 SDK 下载 9700 万+)
- **A2A**(24661★):Agent 的"社交名片"——互相发现/委托任务/交换结果,Google 提出,150+组织支持

两个协议**分层互补,非竞争**:MCP 解决 Agent"用什么"(垂直),A2A 解决"找谁"(水平)。2025.12 双双进入 Linux Foundation Agentic AI Foundation 统一治理。更广版图中还有 AGNTCY/ANP/ACP/AGTP/AP2 五协议在博弈。

---

### 3.7 Planner(规划与推理执行)——1 项目

**gpt-researcher**(28121★):自主深度研究 Agent。实现了 ReAct/Plan-and-Execute/Tree-of-Thought/Goth-of-Thought 等多种范式变体。2811 节点/7487 边,Python 实现。与 Sandbox(无隔离)、Memory(仅会话级)、Gateway(进程内紧耦合)在交叉点存在明确差距。

领域级技术方向包括六大范式:ReAct → Plan-and-Execute → Tree/Graph-of-Thought → Multi-Agent → Code/DSL 驱动(LangGraph)→ 端到端隐式规划。

---

### 3.8 Security(内容安全)——1 项目

**llm-guard**(3151★):输入/输出安全拦截。1455 节点/4296 边,21 种输入扫描器+25 种输出扫描器,支持 Vault 凭据脱敏/RiskScore/vLLM 兼容 API。三层防御模型:预处理(Guardrails)→后处理(LLM-Guard)→工具调用(Agent Aegis),覆盖 OWASP LLM Top 10(2025)中与内容安全相关的条目。

2025-2026 关键威胁:间接注入成为首要威胁,RL 攻击跨模型迁移(GPT-4o 被 RL-Hammer 达 98% 攻击成功率)。

---

## 四、项目全景图(72 项目速查)

| 项目 | Sub | Stars | 核心一句话 |
|------|-----|-------|-----------|
| firecrawl | tool | 146442 | Web 抓取+结构化提取 |
| cc-switch | gateway | 114028 | 桌面端多工具 API 一键切换 |
| supabase | memory | 105832 | PostgreSQL 底座一站式后端 |
| browser-use | tool | 103174 | 浏览器自动化标杆 |
| ragflow | memory | 84446 | 中文 RAG 标杆,DeepDoc |
| rtk | gateway | 69019 | CLI proxy,Token 减 60-90% |
| mem0 | memory | 60253 | 记忆层框架标杆 |
| mempalace | memory | 57043 | 纯原文,LongMemEval 第一 |
| LiteLLM | gateway | 52800 | LLM 统一路由事实标准 |
| New API | gateway | 41323 | 唯一双向格式互转 |
| agent-browser | tool | 37975 | Rust 轻量浏览器 CLI |
| Langfuse | observability | 30580 | 最流行 Trace+Eval 平台 |
| composio | tool | 29118 | 1000+工具+Managed Auth |
| gpt-researcher | planner | 28121 | 自主深度研究 Agent |
| OpenViking | memory | 26377 | 字节火山 Context DB |
| beads | memory | 25125 | Go 三合一嵌入式引擎 |
| A2A | protocol | 24661 | Agent 间协作协议 |
| page-agent | tool | 24675 | JS GUI agent,纯前端 |
| letta | memory | 23678 | MemGPT 虚拟上下文管理 |
| promptfoo | observability | 22986 | Red teaming 安全评估 |
| NemoClaw | sandbox | 21629 | OpenShell 安全封装 |
| Opik | observability | 20379 | ML 实验→LLM 追踪全栈 |
| hindsight | memory | 18062 | 事件溯源不可变日志 |
| DeepEval | observability | 16684 | pytest 式通用评估 |
| browser-harness | tool | 15778 | 自愈型浏览器 harness |
| RAGAS | observability | 14695 | RAG 评估手术刀 |
| memU | memory | 13991 | 六类定型+Tool Memory |
| coder | sandbox | 13722 | Terraform 模板化开发环境 |
| LM Eval Harness | observability | 13204 | 200+模型基准任务 |
| OpenSandbox | sandbox | 11856 | 协议驱动+5SDK+MCP |
| reader | tool | 11480 | URL→Markdown 零配置 |
| Phoenix | observability | 10423 | OpenInference+自动插桩 |
| Higress | gateway | 8799 | Envoy Wasm AI 路由 |
| MCP | protocol | 8545 | Agent↔Tool 协议,月下载 97M |
| CubeSandbox | sandbox | 7986 | 腾讯云容器安全,Rust |
| OpenShell | sandbox | 7434 | 凭据网关+GPU VFIO 直通 |
| OpenLLMetry | observability | 7275 | OTel LLM Span 标准 |
| TencentDB-Agent-Memory | memory | 6831 | 全本地部署,零云端 |
| kgateway | gateway | 5597 | 云原生 API+AI Gateway |
| sandbox | sandbox | 5353 | All-in-One Docker 沙箱 |
| AgentTeams | sandbox | 5005 | 多 Agent 协作 OS |
| sandbox-runtime | sandbox | 4592 | Claude Code 进程级沙箱 |
| agentgateway | gateway | 3720 | Agentic Proxy for MCP |
| TruLens | observability | 3423 | OTel 原生+Agent 七维评估 |
| agentcore-samples | sandbox | 3166 | AWS Bedrock AgentCore 示例 |
| ReMe | memory | 3159 | AgentScope 记忆工具包 |
| llm-guard | security | 3151 | 输入/输出安全拦截 |
| k8s-sigs agent-sandbox | sandbox | 3077 | K8s Sandbox CRD 规范 |
| seekdb | memory | 2784 | 分布式 DB 内建 AI 搜索 |
| OpenLIT | observability | 2579 | GPU+LLM 全栈监控 |
| google/ax | sandbox | 1838 | Google 分布式 Agent 运行时 |
| Envoy AI Gateway | gateway | 1813 | Envoy Filter 透明 LLM 拦截 |
| e2b-dev/infra | sandbox | 1219 | Firecracker 沙箱事实标杆 |
| sandbox-sdk | sandbox | 1059 | Cloudflare V8 isolates 边缘 |
| agent-aegis | sandbox | 954 | Agent 全生命周期安全插件 |
| WindowsAgentArena | sandbox | 878 | Windows Agent 评测平台 |
| agentscope-runtime | sandbox | 831 | Python Agent 运行时 |
| MCP Gateway Registry | gateway | 772 | MCP Server OAuth 联邦 |
| powermem | memory | 738 | OceanBase 数据库基因记忆 |
| cwc-long-running-agents | sandbox | 472 | Anthropic 长运行 Agent |
| NoKV | memory | 442 | AI 原生分布式文件系统 |
| bedrock-agentcore-starter-toolkit | sandbox | 498 | AWS AgentCore 旧版 CLI |
| cohere-terrarium | sandbox | 312 | 最轻量 Python 沙箱 |
| openkruise/agents | sandbox | 230 | K8s Operator 沙箱 |
| shell | sandbox | 213 | 沙箱化 Shell 执行 |
| agentcore-cli | sandbox | 204 | AWS AgentCore CLI |
| OpenShell-Community | sandbox | 171 | OpenShell 社区发行版 |
| agentscope-runtime-java | sandbox | 168 | Java AgentScope 运行时 |
| DTVM | sandbox | 158 | WASM 确定性执行 |
| agentkit-sdk-python | sandbox | 157 | 火山引擎 Agent SDK |
| agentcube | sandbox | 154 | Volcano GPU 批量调度 |

---

## 五、交叉分析:跨子领域的模式与张力

### 5.1 凭据管理:从「沙箱的附庸」到「横跨 Sandbox+Gateway+Security 的第一需求」

凭据(API key/OAuth token)不应该被 Agent 拿到——这个共识在三个子领域分别兑现:
- **Sandbox 层**:OpenShell(出网关注入)、NemoClaw(加密注入不落盘)、OpenSandbox(Credential Vault)
- **Gateway 层**:LiteLLM(Virtual Key)、MCP Gateway Registry(OAuth 联邦认证)
- **Security 层**:llm-guard(vault 脱敏)、agent-aegis(tool call 审计)

但三层之间还没有统一凭据管理标准——Key 该在网关注入还是沙箱边界注入?短期 token 的 refresh 谁负责?凭据泄露告警如何跨层关联?**凭据管理可能是 Agent Runtime 生态最需要统一标准的跨层能力。**

### 5.2 隔离强度:从「一层」到「纵深」

单个沙箱不再是安全的全部答案。深度防御金字塔正在形成:
```
L1: 代码执行隔离 (Sandbox 四方向)
L2: 网络出口控制 + 凭据注入 (Gateway + Supervisor Network)
L3: 行为审计 + 策略审批 (OCSF + OPA + agent-aegis)
L4: 内容安全输入/输出拦截 (llm-guard)
```
OpenShell 是这个纵深模型最接近完整实现的单一项目(同时覆盖 L1+L2 并有 L3 审计能力)。

### 5.3 OTel:可观测性的统一数据总线

Phoenix(OpenInference)、OpenLLMetry(LLM Span 类型)、TruLens(OTel 后端)都在推动 OTel 成为 LLM 可观测性的统一标准。但 Sandbox/Gateway/Memory 层对 OTel 的采纳程度参差不齐——大部分沙箱项目仍使用自定义日志格式,没有统一的可观测性输出。

### 5.4 Protocol × Gateway × Sandbox 的理想三角

MCP 和 A2A 填补了通信标准的空白,但协议的落地需要 Gateway(路由/认证/审计)和 Sandbox(安全执行 MCP Server)的配合。目前三者是独立演进的,理想图景是:
```
Planner(决策) → Gateway(路由+认证) → Sandbox(安全执行) + Memory(持久化)
                                       ↑
                                  Protocol(MCP/A2A)
```

---

## 六、趋势与展望

1. **凭据与沙箱解耦不可逆**:Agent 不应持有 API key 正在成为设计准则,出口网关注入/短期 token 代理/占位符重写三条路线会融合。
2. **MCP 生态爆发**:月 SDK 下载 9700 万+,从协议变成平台,MCP Server 会像 npm 包一样爆炸增长,催生 MCP Registry/Gateway/治理层的需求。
3. **隔离纵深化**:单靠沙箱不够,网络出口+凭据注入+行为审计+内容安全构成四层纵深,OpenShell 是最接近完整实现的方案。
4. **原文 vs 摘要之争**:mempalace 96.6% R@5 为原文路线背书,但对话轮数扩大后的存储成本和检索精度是未知数;LLM 上下文窗口持续扩大(128K→1M)可能改变整个博弈。
5. **OTel 统一化**:Tracing 维度 OTel 统一已成定局,评估维度的标准化(Agent 专项基准)是下一个战场。
6. **GPU 沙箱仍处早期**:AgentCube/OpenShell VFIO 都在尝试,但 GPU 虚拟化粒度远不如 CPU/内存,多租户 GPU 安全隔离是开放问题。
7. **间接注入成为首要安全威胁**:OWASP LLM Top 10(2025)+RL 攻击跨模型迁移(RL-Hammer 98%对 GPT-4o)让内容安全从次要需求升级为核心刚需。

---

## 七、快速选型指南

| 场景 | Sandbox | Memory | Gateway | Observability |
|------|---------|--------|---------|---------------|
| 本地编码 Agent | sandbox-runtime | mem0 | LiteLLM | Langfuse |
| 多租户 SaaS | E2B/OpenSandbox | mem0/memU | LiteLLM+Hipress | Phoenix+Opik |
| K8s 集群 | k8s-sigs/openkruise | OpenViking/seekdb | Higress | Langfuse |
| GPU Agent | OpenShell | OpenViking | LiteLLM | OpenLIT |
| 企业合规 | E2B+agent-aegis | TencentDB-Agent-Memory | MCP Gateway Registry | promptfoo+TruLens |
| 全本地隐私 | sandbox-runtime | mempalace/TencentDB-Agent-Memory | LiteLLM(本地) | Langfuse(self-host) |
| 轻量 Python | cohere-terrarium | powermem | LiteLLM | DeepEval |
| 边缘计算 | sandbox-sdk | mem0(轻量) | - | - |

---

## 八、参考资料

- 72 项目 summary.md(KG `projects/agent-runtime/*/`)
- 49 codebase-memory zst 代码图
- GitHub 实时数据(stars/活跃度/语言,刷新于 2026-07-07)
- agent-runtime 8 份子领域调研:artifacts/02-{sandbox,memory,gateway,observability,tool,protocol,planner,security}.md
- OWASP LLM Top 10 (2025)
- LongMemEval / LoCoMo 记忆性能基准
