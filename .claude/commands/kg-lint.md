# /kg-lint [--fix] [--full]

KG 全局质量检查。两层层级：确定性 auto-fix + 启发式 report-only。

## 读取范围

允许读：
- 本文件
- CLAUDE.md
- config/invariants.md
- config/index/manifest.json
- config/index/by-tag.json
- config/index/by-org.json
- config/index/by-category.json
- kg-index.md
- kg-log.md
- 所有 projects/*/summary.md（关联节）
- 所有 projects/*/state.json

禁止写（除 auto-fix 项）：
- 项目 summary.md（仅关联节断链修复）
- kg-index.md（重建索引）
- kg-log.md（追加 lint 记录）

## 行为

分两阶段执行。报告写入 stderr 同时输出到对话。

### 第一阶段：确定性检查（有 --fix 时自动修复）

| # | 检查项 | Auto-Fix 行为 |
|---|--------|--------------|
| D1 | **索引一致性** — manifest.json 中 path 是否指向存在的目录 | 标记 `status: "missing"` |
| D2 | **断链** — summary.md「关联」节中的 `[...]` 引用 target 是否存在 | 标记 `[MISSING: <key>]` |
| D3 | **空 AUTO 区** — 有 codebase_key 但 AUTO 区为空的项目 | 报告，不修复 |
| D4 | **kg-index.md 过时** — 与 manifest.json 的项目数不一致 | 重建 kg-index.md |
| D5 | **重复 key** — manifest.json 中 key 重复 | 报告，不自动修复 |
| D6 | **路径不一致** — manifest.path 与 filesystem 物理路径不一致 | 更新 manifest.path |
| D7 | **state.json 缺失** — 项目目录存在但无 state.json | 报告，不自动修复 |

### 第二阶段：启发式检查（仅报告）

| # | 检查项 | 判定标准 |
|---|--------|---------|
| H1 | **Stale 快照** — last_refresh > 30 天且 status=active | 建议 /kg-refresh |
| H2 | **孤立项目** — 无 tag、无 category、summary.md 无关联 | 可能是漏标 |
| H3 | **缺失交叉引用** — 同 tag 的两个项目，A 的关联节没提 B | 可能遗漏关联 |
| H4 | **无摘要项目** — summary.md 手动区为空（定位/介绍均缺失） | 可能是 /kg-add 后未补充 |
| H5 | **关联不对称** — A 关联 B，但 B 未关联 A | 建议补全 |
| H6 | **Dormant 但活跃** — status=dormant 但 last_delta < 7 天 | 建议更新 status |
| H7 | **空 tag 项目** — tags 数组为空（非 org 聚落项目） | 建议补充 tag |

## 输出格式

```
🔍 KG Lint — 2026-07-10

## 确定性检查 (7 项)
| # | 状态 | 检查项 | 发现 | 处理 |
|----|------|--------|------|------|
| D1 | ✅ | 索引一致性 | 0 异常 | - |
| D2 | ⚠️ | 断链 | 3 处 | 已修复 |
| D3 | ⚠️ | 空 AUTO 区 | 12 项目 | 列表如下 |
| D4 | ✅ | 索引过时 | kg-index.md 已是最新 | - |
| D5 | ✅ | 重复 key | 0 | - |
| D6 | ✅ | 路径不一致 | 0 | - |
| D7 | ⚠️ | state.json 缺失 | 2 项目 | 列表如下 |

## 启发式检查 (7 项)
| # | 状态 | 检查项 | 发现 |
|----|------|--------|------|
| H1 | ⚠️ | Stale 快照 | 25 项目 > 30 天未刷新 |
| H2 | ⚠️ | 孤立项目 | 8 项目无 tag/关联 |
| H3 | ℹ️ | 缺失交叉引用 | 15 对同 tag 项目可能遗漏关联 |
| H4 | ⚠️ | 无摘要 | 120 项目（opensourceways 为主） |
| H5 | ℹ️ | 关联不对称 | 8 对单向关联 |
| H6 | ℹ️ | Dormant 但活跃 | 3 项目 |
| H7 | ℹ️ | 空 tag | 45 项目 |

## 建议操作
1. `P0`: 修复断链 (D2) — 已自动完成
2. `P1`: 刷新 stale 快照 (H1) — `kg-refresh` 批量执行
3. `P2`: 补充无摘要项目 (H4) — 优先 agent-framework 和 agent-runtime
4. `P3`: 审查孤立项目 (H2) — 确认是否需要归档或补充关联
```

## 完成后
- 追加 `kg-log.md`: `### /kg-lint | N 问题发现, M 自动修复`
- 如果 kg-index.md 被重建，追加日志
