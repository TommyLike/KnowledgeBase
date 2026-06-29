# /kg-reindex

扫描 projects/ 和 references/ 的 meta，重建所有 config/index/*.json。

## 读取范围（严格遵守）

本命令维护索引。允许读：
- projects/*/meta.md（所有项目）
- references/*/meta.md（所有引用）
- projects.md

禁止读：
- 项目的 summary.md、digests/、repo/、codebase.db

允许写：
- config/index/manifest.json
- config/index/by-tag.json
- config/index/by-org.json
- config/index/by-category.json
- config/index/by-status.json

## 行为

1. 扫描所有 projects/*/meta.md，提取 frontmatter
2. 扫描所有 references/*/meta.md
3. 对照 projects.md 做一致性检查
4. 重建所有索引文件
5. 报告差异（如 projects.md 有但目录不存在的项目）

## 使用示例

```
/kg-reindex
```
