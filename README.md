# Knowledge Graph — 开源项目知识图谱

对团队关注的开源项目进行**代码索引**、**论文关联**、**变更追踪**和**周报生成**。

## 覆盖范围

| 类型 | 标签 | 数量 | 组织 |
|------|------|------|------|
| 团队主导 | `团队主导` | 423 | opensourceways, cosdt |
| 上游贡献 | `上游贡献` | 66 | vllm-project, sgl-project, triton-lang |
| 参考文献 | — | 3 | 中英双语论文 PDF |

## 目录结构

```
├── CLAUDE.md              # Agent 行为约束和查询策略
├── README.md              # 本文件
├── projects.md            # 项目纳管清单（按分类）
├── .mcp.json              # codebase-memory MCP 配置
│
├── projects/              # 代码项目
│   └── <org>/<name>/
│       ├── meta.md        # GitHub 源数据 (url/created/updated/branch)
│       ├── summary.md     # 项目摘要 (定位/架构/技术栈)
│       ├── state.json     # 追踪状态 (commit/delta/codebase)
│       ├── CLAUDE.md      # 项目级上下文 (AUTO 区)
│       ├── digests/       # PR/MR 变更摘要
│       └── .codebase-memory/  # 代码索引持久化文件 (graph.db.zst)
│
├── references/            # 论文引用
│   └── <org>/<key>/
│       ├── paper.pdf      # 英文原版
│       ├── paper_cn.pdf   # 中文翻译版
│       ├── summary.md     # 中英双语摘要
│       └── meta.md        # 论文元数据
│
├── config/
│   ├── settings.yaml      # 全局配置
│   ├── invariants.md      # 设计不变量
│   └── index/             # JSON 索引 (manifest/by-tag/by-org/by-category)
│
├── templates/
│   ├── summary.md         # 项目摘要模板
│   └── research-report.md # 技术调研报告模板
│
└── reports/               # 周报/日报/调研报告
```

## 命令

| 命令 | 用途 |
|------|------|
| `/kg-add <url>` | 添加新项目 |
| `/kg-refresh <key>` | codebase-memory 代码索引 + 更新 summary |
| `/kg-delta <key>` | 同步 PR delta，生成 digest |
| `/kg-weekly` | 生成周报 (团队主导项目) |
| `/kg-deep <key>` | 深度探索单项目 |
| `/kg-topic <tag>` | 按标签聚合分析 |
| `/kg-link <a> --related <b>` | 手动建立关联 |
| `/kg-reindex` | 重建全部索引 |

## 跨资源查询

支持在代码、论文、PR 变更之间联动查询：

```
用户提问 "PagedAttention 相关"
  ├─ by-tag['vllm'] → 6 projects + 1 paper
  ├─ manifest.references[].related_projects → 代码仓库
  └─ project.summary.关联节 → 上下游/论文
```

详见 `CLAUDE.md` 中"跨资源查询策略"节。

## 名称解析

PR 作者通过 `user-info.yaml` 映射为真实姓名：
- 源: https://github.com/opensourceways/opensourceway/blob/master/community/user-info.yaml
- 每次 `/kg-delta` 从远端拉取最新
- 未识别 handle 保留原始 GitHub ID

## 技术栈

- **代码索引**: codebase-memory MCP (graph.db.zst)
- **PR 同步**: GitHub API + git log
- **报告生成**: Pandoc + WeasyPrint (PDF)
- **论文翻译**: arXiv LaTeX + Docker XeLaTeX
