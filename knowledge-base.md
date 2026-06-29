# 增量设计 v1 — 基于最终设计文档

> 本文件是对《开源项目知识图谱 — 最终设计文档》的增量修订。
> 涵盖两个变更：
> 1. 暂缓 Obsidian 兼容相关设计（后续可补回）
> 2. 上下文规模化与聚焦深度问题（核心架构调整）

---

## A. 暂缓 Obsidian 兼容

### A.1 从最终设计中移除的内容

| 位置 | 原内容 | 处理 |
|------|--------|------|
| §1 设计原则 | 第 7 条"Obsidian 兼容" | 删除 |
| §3 CLAUDE.md / §5/§6 summary | `[[<key>]]` wikilink 写法 | 改为相对路径引用 `projects/<key>/` |
| §4.1 settings.yaml | `obsidian_compat` 段 | 删除 |
| §12 整节 | Obsidian 兼容 | 删除 |
| §13 阶段 3 | "视体验决定是否引入 Obsidian" | 删除 |

### A.2 保留的"无关 Obsidian"良性约定

这些不是为 Obsidian 设计的，是跨平台 / 跨工具的基本卫生：

- 文件名避免 `:` `?` `*` `<` `>` `|` `"` 等不友好字符
- `<!-- BEGIN AUTO -->` / `<!-- END AUTO -->` 区段标记（agent 定位用，与 Obsidian 无关）
- frontmatter 作为 tag 唯一来源（避免漂移）

---

## B. 上下文规模化与聚焦深度

### B.1 问题陈述

随着项目和引用规模增长（30+ 项目、50+ 引用是合理预期），原设计有三个风险：

| 风险 | 现状 | 后果 |
|------|------|------|
| **根 CLAUDE.md 膨胀** | 设计里有"纳管清单"AUTO 段，会列所有项目 + 引用 | 每次进入 vault 都自动加载几百行清单，做单项目任务时全是噪声 |
| **跨项目命令拉太多** | `/kg-topic`、`/kg-weekly` 会读多个 summary | 上下文窗口被填满，深入分析没空间 |
| **深度探索缺入口** | 现有命令偏"日常运维"，没有"今天我就想吃透 X 项目" | 你要手动 cd + 读 + 提问，agent 也不知道边界 |

合起来表现为你担心的"上下文快速扩展、单次讨论不聚焦、知识点不深入"。

### B.2 设计原则（新增）

1. **CLAUDE.md 是规则而非数据**：自动加载的只有"agent 行为约束"，不放任何会随规模增长的清单。
2. **索引文件是数据**：所有"快速查找"用 JSON 索引文件承载，agent 按需读取，不自动加载。
3. **命令声明读取范围**：每个 kg 命令在指令模板里明确"我会读什么、不读什么"，避免 agent 自由探索。
4. **分层上下文**：CLAUDE.md（最简）→ summary.md（中等）→ digests/repo/code-memory（按需深入）。一次任务停在哪一层是显式决定。
5. **会话隔离优先**：日常运维全部走 `claude -p` 一次性会话；交互模式只为深度探索保留。

### B.3 具体设计

#### B.3.1 根 CLAUDE.md 瘦身（修订 §3.1）

**移除**：原设计中的 `<!-- BEGIN AUTO --> 纳管清单 <!-- END AUTO -->` 整段。

**保留**：纯规则，目标 < 50 行。修订后内容：

```markdown
# KG Root Context

本目录是开源项目知识图谱。Agent 在此工作时遵守以下约定。

## 运行约束（人类维护）
- digest 语言：中文
- 邮件配置见 config/settings.yaml
- 数据范围：仅 merged PR + 合入代码 diff，禁止 open PR / issue / discussion 入 digest
- 贡献者实名走 contributors.yaml，未知 handle 入 unknowns，不臆造
- 时间 UTC 存储，展示用 Asia/Shanghai

## Agent 操作规范
- digests/YYYY-MM-DD.md 已存在不覆盖（追加 -2/-3 后缀）
- 改 state.json 前先备份 .bak
- projects.md 只改对应二级标题段
- CLAUDE.md 的 BEGIN/END AUTO 区外严禁改动
- /kg-note 必须 review 才写入人类笔记区

## 索引位置（agent 按需读取，不要自动 cat）
- config/index/by-tag.json
- config/index/by-org.json
- config/index/by-category.json
- config/index/manifest.json

## 命令上下文边界
任何 kg 命令运行时，agent 默认只读：
1. 本文件
2. config/settings.yaml
3. 命令明确指定的项目/引用文件
其他文件不在默认上下文，需要时显式打开。

## 不变量见 config/invariants.md
```

把原"关键设计不变量"长清单挪到 `config/invariants.md`，根 CLAUDE.md 只引用，不展开。

#### B.3.2 引入索引文件（新增）

新目录 `config/index/`，agent 在每次 add/refresh 后维护：

```
config/index/
├── manifest.json          # 所有项目和引用的 key + path + 最近更新
├── by-tag.json            # tag → [keys]
├── by-org.json            # org → [project_keys]
├── by-category.json       # category → [project_keys]
└── by-status.json         # ref 的 status → [ref_keys]
```

**`manifest.json` 示例**：

```json
{
  "projects": {
    "ascend--triton-ascend": {
      "path": "projects/ascend--triton-ascend",
      "category": "team",
      "tags": ["compiler", "npu"],
      "last_delta": "2026-06-28",
      "last_refresh": "2026-06-21"
    }
  },
  "references": {
    "2023-cidr-git-is-for-data": {
      "path": "references/2023-cidr-git-is-for-data",
      "type": "paper",
      "tags": ["model-storage", "cdc"],
      "status": "read",
      "related_projects": ["huggingface--xet-core"]
    }
  }
}
```

**`by-tag.json` 示例**：

```json
{
  "compiler": {
    "projects": ["openai--triton", "ascend--triton-ascend"],
    "references": ["2024-mlir-talk"]
  }
}
```

**为什么用 JSON 而非 markdown**：
- 索引是机器读为主，JSON 解析快
- 不在 git diff 里制造大量噪声（每次刷新都重写）
- 不会被 markdown 工具误识别

**典型用法**：

- `/kg-topic compiler`：先读 `by-tag.json["compiler"]` → 得到 keys → 只读这些 keys 的 summary.md。**不再遍历整个 projects/ 目录**。
- `/kg-weekly`：先读 `manifest.json` 过滤 `last_delta` 在本周的项目 → 只读这些项目的本周 digest。
- 新加项目时：agent 必须更新 `manifest.json` 和相关 `by-*.json`。

#### B.3.3 项目 CLAUDE.md 加载策略（修订 §3.2）

**关键观察**：Claude Code 自动加载 CLAUDE.md 时会沿 cwd 向上找。所以：

- 在 `${KG_ROOT}` 跑命令 → 只加载根 CLAUDE.md
- 在 `${KG_ROOT}/projects/<key>/repo/` 跑命令 → 加载根 CLAUDE.md + 项目 CLAUDE.md

**约定**：

| 场景 | 工作目录 | 自动加载 |
|------|---------|---------|
| 日常运维（delta / refresh / weekly） | `${KG_ROOT}` | 仅根 CLAUDE.md |
| 单项目深度探索 | `${KG_ROOT}/projects/<key>/repo/` | 根 + 项目 CLAUDE.md |
| 直接在已有的本地 clone 工作 | `~/work/triton-ascend` 等 | 不加载 kg 任何 CLAUDE.md，干净环境 |

> 项目 CLAUDE.md 位置保持在 `projects/<key>/CLAUDE.md`，恰好能被 `projects/<key>/repo/` 子目录的 cwd 向上搜到。

#### B.3.4 命令读取范围（每条命令在指令模板里声明）

每个 `.claude/commands/kg-*.md` 的指令模板顶部必须包含 **"读取范围声明"** 段，例如：

`/kg-delta` 指令模板片段：

```markdown
# 读取范围（严格遵守）

本命令处理单个或多个项目的 delta 同步。允许读：
- config/settings.yaml
- config/contributors.yaml
- config/index/manifest.json（用于 --all-due 时确定哪些到期）
- 目标项目的 projects/<key>/CLAUDE.md
- 目标项目的 projects/<key>/meta.md
- 目标项目的 projects/<key>/state.json
- 目标项目的 projects/<key>/summary.md（仅用于上下文，不修改）

禁止读：
- 其他项目的任何文件
- references/ 任何文件（delta 与引用无关）
- reports/ 任何文件
- 本项目的 codebase.db（delta 不依赖 code-memory，由 /kg-refresh 负责）

允许写：
- projects/<key>/digests/YYYY-MM-DD.md（新建）
- projects/<key>/state.json（备份后更新）
- outbox/pending/<date>-delta-daily.eml.md
- config/index/manifest.json（更新 last_delta 字段）
- config/contributors.yaml（追加 unknowns）
```

这种声明既约束 agent，也方便你 review 时一眼看清"这个命令会动什么"。

#### B.3.5 分层上下文（新增约定）

| 层级 | 文件 | 大小 | 何时读 |
|------|------|------|--------|
| L0 规则 | 根 CLAUDE.md | < 50 行 | 自动 |
| L1 索引 | config/index/*.json | KB 级 | 按需 |
| L2 项目摘要 | projects/<key>/CLAUDE.md（AUTO 区） | < 100 行 | 进入项目时 |
| L3 项目完整摘要 | projects/<key>/summary.md | 几百行 | 跨项目分析、深度探索 |
| L4 单次 delta | projects/<key>/digests/<date>.md | 几百行 | 时间窗内查询 |
| L5 全详 | repo/ + codebase.db | 大 | 仅深度探索 |

**默认行为**：命令停留在能完成任务的最低层。L3+ 必须显式触发。

#### B.3.6 新增指令 `/kg-deep`（深度探索入口）

```markdown
/kg-deep <project-or-ref-key> [--with <other-key>...] [--question "..."]
```

**用途**：你想吃透某个项目（或某篇论文），不希望被其他项目干扰。

**行为**：
1. 切换 cwd 到 `projects/<key>/repo/`（如果是项目）或保持在 vault 根（如果是引用）
2. 加载：根 CLAUDE.md + 该项目/引用的 CLAUDE.md + summary.md + 最近 3 篇 digest（如果是项目）
3. 显式排除：其他所有项目和引用
4. `--with <other-key>` 允许显式拉入另一个项目/引用做对比（仍受限）
5. 进入交互模式，等你提问。退出时不写任何文件（除非你显式让 agent 更新 summary 或追加 note）

**这条命令是聚焦深度的主入口**。日常你应该 70% 用 `claude -p` 跑运维命令，30% 用 `/kg-deep` 做主题攻坚。

#### B.3.7 会话隔离原则（新增）

| 场景 | 推荐方式 |
|------|---------|
| `/kg-delta`、`/kg-refresh`、`/kg-weekly` 等运维命令 | `claude -p "/kg-..."` 一次性会话 |
| `/kg-deep`、`/kg-topic` 等分析命令 | 交互会话，每次开新的，不延续 |
| 跨命令组合（如 delta 后立刻 weekly） | cron 里串起来，仍是一次性 `claude -p` |
| 多个项目深入 | 多个 `/kg-deep` 会话，**不要**在同一会话里切换项目 |

文档化这条规则进根 CLAUDE.md，提醒你和 agent。

### B.4 上下文预算估算

修订后，单次命令的上下文占用（粗估）：

| 命令 | 自动加载 | 显式读 | 总估算 |
|------|---------|--------|--------|
| `/kg-delta <single>` | 根 CLAUDE (~2k) + settings (~1k) | meta + state + summary (~3k) + PR API 返回 (~5k) | **~11k tokens** |
| `/kg-delta --all-due`（10 个项目）| 同上 | manifest 过滤后只处理 due 项目，每个 ~8k | **~50k tokens** |
| `/kg-weekly`（30 个项目）| 同上 | manifest + 30 × digest 头部摘要 (~600 tokens each) + 跨项目分析 | **~30k tokens** |
| `/kg-topic compiler` | 同上 | by-tag.json + 5 个匹配项目的 summary (~3k each) | **~25k tokens** |
| `/kg-deep <key>` | 根 + 项目 CLAUDE | summary + 最近 3 digest + 你的对话 | **~20k tokens** 起步，按对话深入 |

对比：如果没有索引、没有读取范围声明，`/kg-weekly` 可能轻易吃 150k+ tokens，且大部分是噪声。

### B.5 修订后的命令清单（增量）

新增 `/kg-deep`，其他不变。但每个命令的指令模板要补上 **"读取范围声明"** 段。

| 指令 | 增量 |
|------|------|
| `/kg-deep <key> [--with ...]` | **新增**，深度探索单项目/引用 |
| 其他所有 `/kg-*` | 指令模板补 "读取范围声明" 段 |

### B.6 索引维护责任

| 触发 | 更新 |
|------|------|
| `/kg-add` 成功 | manifest.json + by-tag/org/category.json |
| `/kg-add-ref` 成功 | manifest.json + by-tag.json + by-status.json |
| `/kg-refresh` 成功 | manifest.json 的 last_refresh |
| `/kg-delta` 成功 | manifest.json 的 last_delta |
| `/kg-link` 成功 | manifest.json 的 related_projects |
| 你手动改 projects.md 加 tag | **需要你主动跑 `/kg-reindex`**（新增辅助命令） |

新增辅助命令 `/kg-reindex`：扫描 projects/ 和 references/ 的 meta，重建所有 index/*.json。运行时也对照 projects.md 和实际目录做一致性检查。

### B.7 对最终设计文档的精确修订点

下次合并到主文档时按这个清单改：

| 主文档位置 | 修订 |
|-----------|------|
| §1 设计原则 | 删第 7 条 Obsidian；新增"上下文按需加载、分层、命令声明读取范围"3 条 |
| §2 目录结构 | 新增 `config/index/`，新增 `config/invariants.md`；删除"Obsidian 友好"措辞 |
| §3.1 根 CLAUDE.md | 整段替换为 B.3.1 的瘦身版 |
| §3.2 项目 CLAUDE.md | 加 B.3.3 的加载策略说明 |
| §3.3 | 补"分层上下文 L0~L5"约定 |
| §4.1 settings.yaml | 删 `obsidian_compat` 段 |
| §5.3、§6.2 | wikilink `[[key]]` 改为相对路径 `projects/<key>/` |
| §9 指令清单 | 新增 `/kg-deep`、`/kg-reindex` |
| §9 指令清单 | 每条加注"指令模板含读取范围声明" |
| §12 整节 | 删除 |
| §13 阶段 0 | 加"建 config/index/ 骨架"任务 |
| §15 不变量 | 内容挪到 `config/invariants.md`，本节缩为引用 |

---

## C. 这次修订没动的部分

确认仍然有效，不必再讨论：

- 项目 / 引用的目录结构与文件格式
- 数据范围（仅 merged PR + diff）
- 邮件 outbox 模式
- 定时任务方式（cron + `claude -p`）
- code-memory-mcp 集成方式
- 分阶段实施节奏
- 14 个实施时需确认事项

---

## D. 仍待你拍板（仅 1 个）

**`/kg-deep` 的工作目录切换**：是命令自动 `cd projects/<key>/repo/`，还是要你手动 cd 后运行？

- **自动 cd**：体验顺滑，但有"agent 跳到我没预期的目录"风险
- **手动 cd**：你完全控制，但要多敲一行

我推荐手动 cd，下面是约定写法：

```bash
cd ${KG_ROOT}/projects/ascend--triton-ascend/repo
claude    # 交互模式，自动加载根 + 项目 CLAUDE.md
> /kg-deep ascend--triton-ascend --question "近一个月 NPU 后端的 op 覆盖率提升了哪些"
```

确认这点后增量定稿，可以合并回主文档。
