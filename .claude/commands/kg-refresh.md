# /kg-refresh <key> [--all] [--mode fast|moderate|full]

对项目执行 code-memory 索引并更新 summary.md。

## 读取范围（严格遵守）

本命令聚焦单项目的代码分析。允许读：
- config/settings.yaml
- 目标项目的 projects/<org>/<name>/CLAUDE.md
- 目标项目的 projects/<org>/<name>/meta.md
- 目标项目的 projects/<org>/<name>/state.json
- 目标项目的 projects/<org>/<name>/repo/（所有源码）
- config/index/manifest.json

禁止读：
- 其他项目的任何文件
- references/ 任何文件
- reports/ 任何文件
- digests/ 下的 digest 文件

允许写：
- projects/<org>/<name>/summary.md（重写）
- projects/<org>/<name>/CLAUDE.md（更新 AUTO 区）
- projects/<org>/<name>/state.json（更新 last_refresh, repo 字段）
- config/index/manifest.json（更新 last_refresh）

## 行为

1. 如果 repo 未 clone，先 `git clone --depth 1`
2. 调用 codebase-memory-mcp index_repository
3. 用 get_architecture 获取架构概览
4. 生成/更新 summary.md（中文）
5. 更新 CLAUDE.md AUTO 区（关键模块、入口点）
6. 更新 state.json 的 last_refresh 和 repo 字段
7. 更新 manifest.json

## 使用示例

```
/kg-refresh opensourceways--cora
/kg-refresh --all --mode fast
```
