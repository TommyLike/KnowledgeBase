# /kg-delta <key> [--since <date>] [--all-due]

同步项目最近的 merged PR delta，生成 digest。

## 贡献者名称解析（重要）

**每次运行 /kg-delta 时，必须先从远程拉取最新的用户名映射：**

```bash
# 1. 拉取最新映射
curl -s "https://raw.githubusercontent.com/opensourceways/opensourceway/master/community/user-info.yaml" \
  | python3 -c "
import sys, re, json
entries = {}
current_id = None
for line in sys.stdin:
    line = line.strip()
    if line.startswith('- github_id:'):
        current_id = line.split(':',1)[1].strip()
    elif line.startswith('name:') and current_id:
        entries[current_id] = line.split(':',1)[1].strip()
with open('config/contributors.json','w') as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
print(f'Loaded {len(entries)} mappings')
"

# 2. 查询真实名称
python3 -c "
import json
with open('config/contributors.json') as f:
    m = json.load(f)
print(m.get('$HANDLE', '\$HANDLE'))
"
```

**映射规则**：
- `github_id` → `name`（如 `zhongjun2` → `钟君`，`TommyLike` → `胡胜`）
- 未找到 → 保留原始 handle，记录到 `unknowns` 列表
- 机器人账号 `opensourceways-bot` / `app/github-actions` → `机器人`
- `open-common` → `机器人`

## 读取范围（严格遵守）

本命令处理单个或多个项目的 delta 同步。允许读：
- config/settings.yaml
- config/contributors.json（本地缓存，每次运行前从远程刷新）
- config/index/manifest.json（用于 --all-due 时确定哪些到期）
- 目标项目的 projects/<key>/CLAUDE.md
- 目标项目的 projects/<key>/meta.md
- 目标项目的 projects/<key>/state.json
- 目标项目的 projects/<key>/summary.md（仅用于上下文，不修改）

禁止读：
- 其他项目的任何文件
- references/ 任何文件（delta 与引用无关）
- reports/ 任何文件

允许写：
- projects/<key>/digests/YYYY-MM-DD.md（新建）
- projects/<key>/state.json（备份后更新）
- outbox/pending/<date>-delta-daily.eml.md
- config/index/manifest.json（更新 last_delta 字段）
- config/contributors.json（刷新缓存）
- config/unknowns.md（追加未识别 handle）

## 行为

1. **刷新贡献者映射**：从 `user-info.yaml` URL 拉取最新
2. 拉取 repo 最新代码
3. 获取上次 delta 以来的 merged PR 列表
4. 对每个 PR：获取标题、diff、文件变更
5. **名称转换**：PR 作者查 `contributors.json`，转真实姓名；未找到保留原 handle
6. 按 digest 模板生成中文摘要
7. 更新 state.json（last_delta, digest_count++）
8. 可选：生成邮件到 outbox

## Digest 格式要求

每个 digest 必须包含：
- 全部 PR 列表（编号、日期、**真实姓名**、审核者、文件变更、描述）
- 贡献者统计（**真实姓名** + PR 数 + 变更量）
- 审核者统计

## 使用示例

```
/kg-delta opensourceways--cora
/kg-delta opensourceways--cora --since 2026-06-21
/kg-delta --all-due
```
