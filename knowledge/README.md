# Knowledge Archive

> 时间点快照。每次 /kg-deep 或 /kg-topic 完成后，可将核心结论归档至此。
> 归档页面不参与级联更新——保留当时的分析状态。

## 归档模板

```markdown
# <主题>

> [Archived] YYYY-MM-DD | 来源: /kg-deep (or /kg-topic)
> 涉及项目: <project-keys>
> 本页为时间点快照，知识可能已过时。

## 核心结论
...

## 分析过程
...

## 来源
- [project-a](../../projects/<org>/<name>/summary.md)
- [project-b](../../projects/<org>/<name>/summary.md)
```

## 命名约定
- `<topic-slug>-<YYYY-MM-DD>.md`
- slug 使用 kebab-case，≤60 字符

## 生命周期
- 创建: /kg-deep 或 /kg-topic 完成后，Agent 询问是否归档
- 只读: 归档后不再自动修改（保留时间点快照）
- 清理: 由人类决定何时删除过时归档

## 已归档

<!-- BEGIN ARCHIVE INDEX -->
- [RL Post-Training 关键论文分析](rl-post-training-2026-07-10.md) — 2026-07-10 · 6 papers + 5 projects · slime 生态 + GRPO/DPO/DAPO
- [容器镜像构建生态全景分析](container-image-build-2026-07-13.md) — 2026-07-13 · 6 projects + 3 papers · BuildKit/Nydus/dive/lazy-pulling
- [vLLM-Omni 全双工实时推理深度分析](full-duplex-realtime-inference.md) — 2026-08-08 · 1 project · DuplexRuntime/Barge-In/AsyncChunk/MiniCPM-o
- [Authenticated Workflows 论文分析](authenticated-workflows-2026-08-14.md) — 2026-08-14 · 1 paper + 中文全译 PDF · 认证工作流/四控制面/MAPL
- [让软件可以"安全地反悔"：可逆插件系统科普](cordis-reversible-plugin-system-2026-08-16.md) — 2026-08-16 · 1 reference + 1 project · Cordis/可逆效应/守卫/惯性状态机/DeepSeek Harness
- [凌晨两点的告警：Cordis 叙事版（PDF）](cordis-narrative-2026-08-16.md) — 2026-08-16 · 叙事长文 + [PDF](cordis-narrative-2026-08-16.pdf) 5页 · 事故现场线 + 6 幅技术蓝墨 TikZ 插图
- [量化算法：历史演进与主要技术方向](quantization-algorithms-2026-08-20.md) — 2026-08-20 · 9 projects · LLM.int8/GPTQ/AWQ → FP8/FP4/HiFloat · 硬件-算法协同 · vLLM/SGLang 落地 + 昇腾 HiF8
<!-- END ARCHIVE INDEX -->
