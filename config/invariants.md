# 关键设计不变量

本文档记录 KG 系统的硬约束，违反这些约束会导致数据不一致或上下文污染。

## 数据边界
- **仅 merged PR + 合入代码 diff**：禁止 open PR / issue / discussion 入 digest
- **贡献者实名**：走 contributors.yaml，未知 handle 入 unknowns，不臆造
- **时间 UTC 存储，展示用 Asia/Shanghai**

## 文件修改规则
- digests/YYYY-MM-DD.md 已存在不覆盖（追加 -2/-3 后缀）
- 改 state.json 前先备份 .bak
- projects.md 只改对应二级标题段
- CLAUDE.md 的 BEGIN/END AUTO 区外严禁改动
- /kg-note 必须 review 才写入人类笔记区
- **kg-log.md 只追加不修改** — 历史条目不可删除或改写
- **kg-index.md 每次操作后自动重建** — 不手动编辑
- **knowledge/ 归档页面不参与级联更新** — 保留时间点快照

## Agent 行为约束
- 默认只读：根 CLAUDE.md + settings.yaml + kg-index.md + 命令明确指定的文件
- 索引文件按需读取，不自动 cat
- 命令停留在能完成任务的最低上下文层
- **每次 KG 变更操作后必须自动同步 kg-index.md 和 kg-log.md** — 不可跳过
- **/kg-refresh 后必须检查级联影响** — 扫描 related_projects 引用

## 物理路径寻址
- **`manifest.path` 是项目物理路径的唯一真源** — 命令/agent 禁止拼 `projects/<org>/<name>` 之类路径，一律从 manifest 解析（软件分层可变，key 恒定）
- **项目 key 恒为 `<真实github-org>--<name>`** — 物理搬迁不改 key，by-org 逻辑视图不受影响
- projects/ 为自底向上软件分层（10-compiler … 80-workflow），一级目录名 = manifest.category

## 分层上下文（<dir> = manifest.path 解析出的项目物理目录）
- L0 规则：根 CLAUDE.md（自动加载）
- L0 全局索引：kg-index.md（自动加载，全局定位）
- L0 操作日志：kg-log.md（按需读最近 7 天条目）
- L1 索引：config/index/*.json（按需）
- L2 项目摘要：<dir>/CLAUDE.md AUTO 区（进入项目时）
- L3 项目完整摘要：<dir>/summary.md（跨项目分析）
- L4 单次 delta：<dir>/digests/<date>.md（时间窗查询）
- L5 全详：<dir>/repo/ + codebase.db（仅深度探索）
- L5 归档：knowledge/*.md（时间点快照，只读）

## 会话隔离
- 运维命令（/kg-delta、/kg-refresh）：`claude -p` 一次性会话
- 分析命令（/kg-deep、/kg-topic）：交互会话，每次开新的
- 不延续旧会话做新任务
