# 40-runtime · 运行时 / 容器 / 沙箱


> **MOC 导览页** · 本层 34 个项目 · [↑ 返回栈总览](../README.md)

模型和 Agent 代码**在哪里、以什么隔离级别执行**。含两条线：容器/microVM 镜像与冷启动（firecracker、nydus 等），以及 Agent 执行沙箱（安全隔离地跑不可信代码/工具调用）。是"框架之下、硬件之上"的执行底座。

## 容器 / microVM（6）

- [`GoogleContainerTools--kaniko`](container/kaniko/) — container、build、kubernetes
- [`containerd--stargz-snapshotter`](container/stargz-snapshotter/) — container、image、lazy-pulling
- [`dragonflyoss--nydus`](container/nydus/) — container、image、lazy-pulling
- [`firecracker-microvm--firecracker`](container/firecracker/) — agent
- [`moby--buildkit`](container/buildkit/) — container、build、oci
- [`slimtoolkit--slim`](container/slim/) — container、image、optimization

## Agent 沙箱（28）

- [`DTVMStack--DTVM`](sandbox/DTVM/) — agent、runtime、vm
- [`NVIDIA--NemoClaw`](sandbox/NemoClaw/) — agent、runtime、security
- [`NVIDIA--OpenShell`](sandbox/OpenShell/) — agent、sandbox、runtime
- [`NVIDIA--OpenShell-Community`](sandbox/OpenShell-Community/) — agent、runtime、community
- [`TencentCloud--CubeSandbox`](sandbox/CubeSandbox/) — agent
- [`agent-infra--sandbox`](sandbox/sandbox/) — agent
- [`agent-substrate--substrate`](sandbox/substrate/) — agent、sandbox、runtime
- [`agentscope-ai--AgentTeams`](sandbox/AgentTeams/) — agent、runtime、multi-agent
- [`agentscope-ai--agentscope-runtime`](sandbox/agentscope-runtime/) — agent、runtime、sandbox
- [`agentscope-ai--agentscope-runtime-java`](sandbox/agentscope-runtime-java/) — agent、runtime、java
- [`antgroup--agent-aegis`](sandbox/agent-aegis/) — agent、sandbox、security
- [`anthropic-experimental--sandbox-runtime`](sandbox/sandbox-runtime/) — agent、sandbox、上游贡献
- [`anthropics--cwc-long-running-agents`](sandbox/cwc-long-running-agents/) — agent、runtime、long-running
- [`aws--agentcore-cli`](sandbox/agentcore-cli/) — agent、runtime、aws
- [`aws--bedrock-agentcore-starter-toolkit`](sandbox/bedrock-agentcore-starter-toolkit/) — agent、runtime、aws
- [`awslabs--agentcore-samples`](sandbox/agentcore-samples/) — agent、runtime、aws
- [`cloudflare--sandbox-sdk`](sandbox/sandbox-sdk/) — agent、sandbox、边缘计算
- [`coder--coder`](sandbox/coder/) — agent
- [`cohere-ai--cohere-terrarium`](sandbox/cohere-terrarium/) — agent、sandbox、上游贡献
- [`e2b-dev--infra`](sandbox/infra/) — agent
- [`google--ax`](sandbox/ax/) — agent、runtime、distributed
- [`kubernetes-sigs--agent-sandbox`](sandbox/agent-sandbox/) — agent
- [`microsoft--WindowsAgentArena`](sandbox/WindowsAgentArena/) — agent、runtime、windows
- [`openkruise--agents`](sandbox/agents/) — agent、sandbox、kubernetes
- [`opensandbox-group--OpenSandbox`](sandbox/OpenSandbox/) — agent
- [`strands-agents--shell`](sandbox/shell/) — agent、sandbox、上游贡献
- [`volcano-sh--agentcube`](sandbox/agentcube/) — agent、sandbox、kubernetes
- [`volcengine--agentkit-sdk-python`](sandbox/agentkit-sdk-python/) — agent、runtime、sdk

## 关联论文

- [`firecracker-microvm--firecracker`](../../references/firecracker-microvm/firecracker/summary.md) — `read`
- [`huawei--flacio`](../../references/huawei/flacio/summary.md) — `container, io, lazy-pulling, cold-start`
- [`hust--cbuild`](../../references/hust/cbuild/summary.md) — `container, build, cache, distributed`
- [`tum--2dfs`](../../references/tum/2dfs/summary.md) — `container, ml, filesystem, build`
