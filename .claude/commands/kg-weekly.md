# /kg-weekly [--date <yyyy-mm-dd>]

生成周报，聚合本周所有项目的 delta。

## 读取范围（严格遵守）

本命令生成周报。允许读：
- config/index/manifest.json（过滤本周有 delta 的项目）
- 本周有更新的项目的 projects/<key>/digests/<本周日期>.md
- config/settings.yaml

禁止读：
- 非本周的 digest 文件
- references/ 任何文件
- 项目的 repo/ 或 codebase.db

允许写：
- reports/weekly-<monday-date>.md
- outbox/pending/<date>-weekly.eml.md

## 行为

1. 读 manifest.json，过滤 last_delta 在本周的项目
2. 只读这些项目的本周 digest
3. 聚合生成周报摘要
4. 突出关键变化和趋势

## 使用示例

```
/kg-weekly
/kg-weekly --date 2026-06-22
```
