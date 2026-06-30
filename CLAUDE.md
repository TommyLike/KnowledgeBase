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
- config/index/by-tag.json — tag → {projects: [...], references: [...]}（跨资源桥梁）
- config/index/by-org.json — org → [project_keys]
- config/index/by-category.json — category → [project_keys]
- config/index/manifest.json — 全量项目/引用元数据（含 related_projects 关联）
- config/index/by-status.json — reference status 索引

## 跨资源查询策略

Agent 回答问题时，必须考虑三类资源之间的关联：

```
用户提问 → 关键词/主题
  ├─→ by-tag.json[tag] → projects: [...] + references: [...]    ← 同一 tag 下的代码+论文
  ├─→ manifest.json.references[key].related_projects            ← 论文 → 关联项目
  └─→ projects/<org>/<name>/summary.md 的「关联」节             ← 项目 → 关联论文/项目
```

### 典型查询路径

| 用户问 | Agent 路径 |
|--------|-----------|
| "PagedAttention 相关项目" | by-tag → `vllm` tag → 4 projects + 1 paper |
| "SGLang 的论文是什么" | manifest → references → sglang → related_projects |
| "triton-ascend 的上游是谁" | 读 project summary → 关联节 → triton-lang/triton |
| "AI 推理方向有哪些论文" | by-category `ai` → 筛选 type=paper 的 references |
| "所有 Ascend 相关的代码+论文" | by-tag `ascend` → 12 projects + 论文（如果有 tag） |

### 关联维护
- `/kg-link <key> --related <other-key>`: 手动建立 project↔project 或 project↔reference 关联
- 索引自动更新: by-tag.json 和 manifest.json 同步

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

### PR 编号提取

**同一个 GitHub 仓库的 merge commit 消息有两种格式：**
- `Merge pull request #123 from ...` → PR #123
- `!123 feat: ...` → 同样是 GitHub PR #123，`!` 只是格式差异

**处理规则**：
1. 从 merge commit 消息提取数字（`#\d+` 或 `!\d+`），去掉前缀
2. 用 `gh pr view <数字>` 查询（`gh` 不要带前缀）
3. 内部 merge（`Merge remote-tracking branch` / `Merge branch 'main'`）→ **排除**

### PR 编号格式（输出）
- `#number` → 链接到 `https://github.com/<org>/<name>/pull/<number>`
- 内部 merge commit: 排除，不出现在报告中

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

## 技术调研报告规范

模板: `templates/research-report.md`。生成技术调研报告时遵守。

### 面向读者
- 默认读者是不熟悉该领域的技术人员，需要从背景讲起
- 每个新概念必须先解释再使用
- 优先用类比和示意图，少用代码

### 报告结构
1. **背景**: 解释"为什么需要解决这个问题"，用具体数据
2. **核心方案**: 用通俗类比建立直觉，再展开技术细节
3. **子系统/进阶特性**: 深入 1-2 个最重要的子话题
4. **完整流程**: 把分散的概念串成一条线，附流程图
5. **工程实现**: 只讲关键模块和核心参数，不堆砌
6. **实验结果**: 对比表格
7. **相关项目**: 上下游依赖

### 禁止事项
- 禁止 V1/V2 版本对比（只关注最新实现）
- 禁止堆砌代码复杂度、行数等无上下文意义的数字
- 禁止直接贴代码签名而不解释参数含义
- 禁止在不讲背景的情况下直接引入代码模块名

### 数据来源优先级
1. codebase-memory (get_architecture, search_graph) → 代码实现
2. by-tag.json → 跨资源关联
3. references/ → 论文摘要和翻译
4. projects/ → 项目定位和架构

## 参考文献位置（agent 按需读取）
- references/<org>/<key>/meta.md
- references/<org>/<key>/summary.md（中英双语）
- references/<org>/<key>/paper.pdf
- config/index/by-status.json（ref status 索引）

## summary.md 生成规范

模板: `templates/summary.md`。Agent 生成/更新 summary 时严格遵守。

### 生成时机
- `/kg-refresh`: 有 codebase 数据 → AUTO 区写入口/架构/热点，手动区填定位/介绍/技术栈
- `/kg-add`: 仅写 header 行和手动区（定位、介绍、技术栈），AUTO 区留空
- 手动区（定位/介绍/技术要点/技术栈/关联/开放问题）由 Agent 填写后不自动覆盖

### AUTO 区（Agent 维护）
- 由 /kg-refresh 自动更新，只包含快照+入口+架构+热点四个事实行
- `<!-- BEGIN AUTO -->` / `<!-- END AUTO -->` 标记
- 无 codebase 数据时留空
- 每次 /kg-refresh 或 /kg-delta 后更新快照行

### 手动区（Agent 首次填写，人类可改）
- 定位: 2-4 句，为什么在 KG 里、和团队什么关系
  - 团队主导: 写负责范围
  - 上游贡献: 写贡献点和上游关系
- 项目介绍: 一句话 + 核心场景
- 技术要点: 有价值才填，否则删掉
- 技术栈: 语言/框架/数据库
- 关联: 有关联才填（上游依赖/下游用户/竞品）
- 开放问题: 随 delta 追加

### 名称解析
- 贡献者映射来源: https://github.com/opensourceways/opensourceway/blob/master/community/user-info.yaml
- 每次 /kg-delta 从远端拉取，不本地缓存
