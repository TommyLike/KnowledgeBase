# /kg-add <repo-url> [--layer <layer>] [--domain <domain>] [--tags <t1,t2>]

向知识图谱添加新项目。

## 读取范围（严格遵守）

本命令添加单个项目。允许读：
- config/settings.yaml
- config/index/manifest.json
- config/index/by-category.json
- config/index/by-layer.json
- config/index/by-org.json
- projects.md

禁止读：
- 其他项目的任何文件
- references/ 任何文件
- reports/ 任何文件

允许写：
- <目标物理目录>/ 及所有初始文件（meta.md, state.json, CLAUDE.md, summary.md）
- <目标物理目录>/digests/ 目录
- projects.md（对应 category 段追加）
- config/index/manifest.json
- config/index/by-category.json
- config/index/by-layer.json
- config/index/by-org.json

## 目录布局（见根 CLAUDE.md「目录布局约定」）

自底向上软件分层，一级目录名 = manifest.category：

| layer | 一级目录 | domain（领域子目录） |
|-------|---------|--------------------|
| compiler | `10-compiler` | org 星座名（triton-lang / tile-ai） |
| cluster | `30-cluster` | 扁平 |
| runtime | `40-runtime` | `container` / `sandbox` |
| framework | `50-framework` | `training[/org星座]` / `inference[/org星座]` / `rl-posttrain` / `multimodal` |
| agent | `60-agent` | `framework` / `memory` / `gateway` / `observability` / `tool` / `protocol` / `planner` / `security` / `coding` |
| data | `70-data` | 扁平 |
| workflow | `80-workflow` | 扁平 |

## 行为

1. 解析 repo URL，提取 org 和 repo name
2. 生成 key：`<org>--<repo-name>`
3. 如果 key 已存在，报错退出
4. 通过 GitHub API 获取 repo 元信息
5. **定位置**：
   - `--layer` + `--domain` 给定则直接用；未给定则按名称/描述规则推断，并**在写入前回显推断结果供确认**
   - 若该 repo 属于已有 org 星座（如 vllm-project 的新卫星），落进该星座目录：`50-framework/inference/vllm-project/<name>`
   - 计算目标物理路径 `<一级目录>/[<domain>/][<org星座>/]<name>`
6. 创建项目目录和所有初始文件；**meta.md frontmatter 写入 `layer` 与 `domain` 字段**
7. 更新索引（manifest.json 含 path/category/layer/domain、by-category.json、by-layer.json、by-org.json、by-tag.json）
8. 可选：追加到 projects.md 对应 category 段
9. **🔄 自动维护（不可跳过）**：
   - 重建 `kg-index.md`（新项目入索引）
   - 追加 `kg-log.md`（记录本次操作）

## 使用示例

```
/kg-add https://github.com/vllm-project/new-plugin --layer framework --domain inference --tags "vllm,plugin"
/kg-add https://github.com/some-org/vecdb --layer data --tags "vector-db,rust"
```
