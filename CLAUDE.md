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

## 周报格式规范 (/kg-weekly)

### 范围
- 仅包含标签为 `团队主导` 的项目（不含 `上游贡献`）
- 统计周期: 上周一 ~ 周日

### 报告结构
1. **标题**: "开源团队项目进展周报" + 周期
2. **项目范围**: 说明覆盖的标签和组织
3. **活跃仓库列表**: 按 PR/MR 数降序，全部列出
4. **变更详情**: 每个仓库的完整 PR/MR 列表
   - 仓库标题: 可点击的 GitHub 链接
   - 3+ PR 的仓库: 增加改动摘要（变更行数、贡献者数、主要方向）
   - 表格列: PR/MR | 日期 | 作者(真实姓名) | 审核 | ± | 描述
5. **贡献者统计**: 真实姓名 + 变更数
6. **未识别 Handle**: 保留原始 ID 列表

### PR 编号格式
- GitHub PR: `#number` → 链接到 `https://github.com/<org>/<name>/pull/<number>`
- GitCode MR: `!number` → 链接到 GitHub (fallback)
- 内部 merge commit (Merge remote-tracking): 排除，不出现在报告中

### 名称解析
- 从 `https://github.com/opensourceways/opensourceway/blob/master/community/user-info.yaml` 拉取
- 找到 → 真实姓名 | 机器人 → "机器人" | 未找到 → 保留原始 GitHub ID

### 输出
- `reports/weekly-YYYY-Www.md` + `reports/weekly-YYYY-Www.pdf`
- 仅保留最新一份报告
- PDF 中所有仓库名和 PR 编号为可点击链接

### 排除项
- `上游贡献` 标签的项目
- `Merge remote-tracking branch` 内部合并
- forks
