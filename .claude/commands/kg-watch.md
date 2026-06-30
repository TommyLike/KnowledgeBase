# /kg-watch <key> [--since <date>] [--output report]

对上游贡献项目生成"技术动态摘要"，不同于 PR 流水账的 /kg-delta。

## 与 /kg-delta 的区别

| | /kg-delta | /kg-watch |
|------|-----------|-----------|
| 目标项目 | 团队主导 | 上游贡献 |
| 数据源 | merged PR + diff | Release Notes + Issues + Discussions + PR 方向聚类 |
| 产出 | PR 列表 + 贡献者统计 | 技术动态摘要 + 竞争分析 |
| settings | data_scope | watch_scope |

## 读取范围

允许读：
- config/settings.yaml（watch_scope 段）
- config/index/manifest.json
- 目标项目的 summary.md（关联节，找竞品关系）
- GitHub API: releases, issues, discussions, PRs

## 行为

1. 读 watch_scope 配置，确定抓取范围
2. 拉目标项目的Release Notes、热门 Issues/Discussions、PR 合入方向
3. 从 summary.md 的"关联"节读取竞品关系
4. 生成技术动态摘要：
   - **版本变化**: Release Notes 中最近的 breaking changes / 新特性
   - **社区热点**: >5 👍 的 Issues/Discussions 标题（社区在争议什么）
   - **PR 方向聚类**: 本周合入 PR 的主要方向（性能/安全/新功能/Bug修复）
   - **竞争分析**: 与竞品（如 sglang vs vllm）的功能差距变化

## 竞品关系维护

在 project summary.md 的"关联"节标注竞品：
```markdown
## 关联
- [`sgl-project/sglang`](../../projects/sgl-project/sglang/) — 竞品（推理框架）
- [`vllm-project/vllm-ascend`](../../projects/vllm-project/vllm-ascend/) — 上游
```

`/kg-topic llm-inference` 时自动将竞品拉在一起对比。

## 产出格式

```markdown
# <org>/<name> 技术动态摘要

> 周期: <since> ~ <now> | 数据源: Releases/Issues/Discussions/PRs

## 版本变化
- <release tag>: <key changes>

## 社区热点
- [#<num>](url) (👍 N) <title>

## PR 方向聚类
- 性能优化: N 个 | 安全修复: M 个 | 新功能: K 个

## 竞争分析
- vs <竞品>: <差距变化>
```

## 使用示例

```
/kg-watch vllm-project--vllm
/kg-watch sgl-project--sglang --since 2026-06-22
/kg-watch vllm-project--vllm --output reports/vllm-watch-2026-W26.md
```
