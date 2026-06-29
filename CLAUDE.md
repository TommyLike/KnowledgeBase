# KG Root Context

本目录是开源项目知识图谱。Agent 在此工作时遵守以下约定。

## 运行约束（人类维护）
- 贡献者映射来源：https://github.com/opensourceways/opensourceway/blob/master/community/user-info.yaml（每次 /kg-delta 从远端拉取，不本地缓存）
- digest 语言：中文
- 邮件配置见 config/settings.yaml
- 数据范围：仅 merged PR + 合入代码 diff，禁止 open PR / issue / discussion 入 digest
- 贡献者实名从远端 user-info.yaml 实时拉取，不本地缓存。未识别 handle 保留原始 GitHub ID
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

## 会话隔离
- 运维命令（/kg-delta、/kg-refresh、/kg-weekly）：`claude -p` 一次性会话
- 分析命令（/kg-deep、/kg-topic）：交互会话，每次开新的，不延续
- 多项目深入：多个 `/kg-deep` 会话，不在同一会话里切换项目

## 不变量见 config/invariants.md

<!-- BEGIN AUTO -->
<!-- END AUTO -->
