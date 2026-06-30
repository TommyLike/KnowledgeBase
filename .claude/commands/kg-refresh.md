# /kg-refresh <key> [--all] [--tag <tag>] [--mode fast|moderate|full]

对项目执行 code-memory 索引并更新 summary.md。

## 关键规则：保护人工内容

**summary.md 有两部分，处理方式不同：**

```
<!-- BEGIN AUTO -->                    ← /kg-refresh 可改写
**快照** · commit · lang · files · nodes
**入口** · **架构** · **热点**
<!-- END AUTO -->                      ← /kg-refresh 可改写

---                                    ← 以下全部保护，禁止覆盖

## 定位          ← 手动区，Agent 首次填，后续不自动覆盖
## 项目介绍      ← 手动区
## 技术栈        ← 手动区
## 关联          ← 手动区
## 开放问题      ← 手动区，随 delta 追加，不删历史
```

**处理方式**：
- 首次 /kg-refresh（summary.md 无 AUTO 块）：生成完整模板（AUTO + 手动区）
- 再次 /kg-refresh（summary.md 已有 AUTO 块）：**只替换 `<!-- BEGIN AUTO -->` 到 `<!-- END AUTO -->` 之间的内容**，其余部分一字不动

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
- projects/<org>/<name>/summary.md（首次完整写，再次只替换 AUTO 块）
- projects/<org>/<name>/CLAUDE.md（更新 AUTO 区）
- projects/<org>/<name>/state.json（更新 last_refresh, repo 字段）
- config/index/manifest.json（更新 last_refresh）

## --all 优先级保护

`--all` 不会对全量 489 个项目平等刷新。必须配合以下参数之一：

| 参数 | 含义 | 适用场景 |
|------|------|---------|
| `--tag 团队主导` | 只刷新 423 个团队项目 | 日常维护 |
| `--tag 上游贡献` | 只刷新 66 个上游项目 | 上游洞察 |
| `--tag <custom>` | 按标签过滤 | 定向分析 |

无 `--tag` 时，`--all` 默认等同于 `--all --tag 团队主导`。

## 行为

1. 如果 repo 未 clone，先 `git clone --depth 1`
2. 调用 codebase-memory-mcp index_repository
3. 用 get_architecture 获取架构概览
4. 检查 summary.md 是否有 AUTO 块：
   - 无 → 生成完整 summary（首次）
   - 有 → 只替换 AUTO 区间内容（再次）
5. 更新 CLAUDE.md AUTO 区和 state.json
6. 清理 repo（clone-analyze-delete 流程）

## 使用示例

```
/kg-refresh opensourceways--cora
/kg-refresh --all --tag 上游贡献 --mode fast
/kg-refresh --all --tag 团队主导
```
