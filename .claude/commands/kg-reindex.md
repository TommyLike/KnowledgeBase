# /kg-reindex

递归扫描 projects/ 和 references/ 的 meta，重建所有 config/index/*.json。

## 读取范围（严格遵守）

本命令维护索引。允许读：
- projects/**/meta.md（所有项目，**递归** — 物理层级为 `<layer>/[<domain>/][<org星座>/]<name>`）
- references/**/meta.md（所有引用，递归）
- projects.md

禁止读：
- 项目的 summary.md、digests/、repo/、codebase.db

允许写：
- config/index/manifest.json
- config/index/by-tag.json
- config/index/by-org.json
- config/index/by-category.json
- config/index/by-layer.json
- config/index/by-status.json

## 行为

1. 递归扫描所有 projects/**/meta.md，提取 frontmatter（key/tags/status/layer/domain）
2. 从物理路径推导 `path`（唯一真源）与 `category`（= 一级目录名，如 `50-framework`）
3. 递归扫描所有 references/**/meta.md
4. 对照 projects.md 做一致性检查
5. 重建所有索引：
   - manifest.json（path/category/layer/domain/tags/status/related_projects）
   - by-category.json（category → keys，category = 物理一级目录名）
   - by-layer.json（layer → keys，语义软件层；meta 未标 layer 时回退用 category 去数字前缀）
   - by-org.json（org → keys，org 取自 key 前缀，与物理解耦）
   - by-tag.json（tag → {projects, references}）
   - by-status.json（reference status）
6. 报告差异（如 projects.md 有但目录不存在的项目、path 与磁盘不符）

## 使用示例

```
/kg-reindex
```
