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
<!-- END ARCHIVE INDEX -->
