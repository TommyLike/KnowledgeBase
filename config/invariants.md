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

## Agent 行为约束
- 默认只读：根 CLAUDE.md + settings.yaml + 命令明确指定的文件
- 索引文件按需读取，不自动 cat
- 命令停留在能完成任务的最低上下文层

## 分层上下文
- L0 规则：根 CLAUDE.md（自动加载）
- L1 索引：config/index/*.json（按需）
- L2 项目摘要：projects/<key>/CLAUDE.md AUTO 区（进入项目时）
- L3 项目完整摘要：projects/<key>/summary.md（跨项目分析）
- L4 单次 delta：projects/<key>/digests/<date>.md（时间窗查询）
- L5 全详：repo/ + codebase.db（仅深度探索）

## 会话隔离
- 运维命令（/kg-delta、/kg-refresh、/kg-weekly）：`claude -p` 一次性会话
- 分析命令（/kg-deep、/kg-topic）：交互会话，每次开新的
- 不延续旧会话做新任务
