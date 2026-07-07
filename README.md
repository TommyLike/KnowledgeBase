# Knowledge Graph — 开源项目知识图谱

对团队关注的开源项目进行**代码索引**、**论文关联**、**变更追踪**和**周报生成**。

## 覆盖范围

| 类型 | 标签 | 数量 | 组织 |
|------|------|------|------|
| 团队主导 | `团队主导` | 423 | opensourceways, cosdt |
| 上游贡献 | `上游贡献` | 165+ | vllm-project, sgl-project, triton-lang, NVIDIA, anthropic-experimental 等 |
| Agent Runtime 领域 | `上游贡献` | 72 | sandbox/memory/gateway/observability/tool/protocol/planner/security |
| 参考文献 | — | 5 | 中英双语论文 PDF |
| codebase 索引 | — | 412 | graph.db.zst 持久化 (含 opensourceways/cosdt 等团队仓库) |
| 产品文档 | — | 1 | 昇腾950 NPU 白皮书(docling→MD+图片) |

## 目录结构

```
├── CLAUDE.md              # Agent 行为约束和查询策略
├── README.md              # 本文件
├── projects.md            # 项目纳管清单（按分类）
├── .mcp.json              # codebase-memory MCP 配置
│
├── projects/              # 代码项目 (489)
│   └── <org>/<name>/
│       ├── meta.md        # GitHub 源数据 (url/created/updated/branch)
│       ├── summary.md     # 项目摘要 (定位/架构/技术栈/关联)
│       ├── state.json     # 追踪状态 (commit/delta/codebase)
│       ├── CLAUDE.md      # 项目级上下文 (AUTO 区)
│       ├── digests/       # PR/MR 变更摘要
│       └── .codebase-memory/  # 代码索引 (graph.db.zst)
│
├── references/            # 论文引用 (3)
│   └── <org>/<key>/
│       ├── paper.pdf      # 英文原版
│       ├── paper_cn.pdf   # 中文翻译版
│       └── summary.md     # 中英双语摘要
│
├── config/
│   ├── settings.yaml      # 全局配置 (data_scope / watch_scope)
│   ├── invariants.md      # 设计不变量
│   └── index/             # JSON 索引 (manifest/by-tag/by-org/by-category)
│
├── templates/
│   ├── summary.md         # 项目摘要模板
│   └── research-report.md # 技术调研报告模板
│
├── reports/
│   ├── weekly-YYYY-Www.md  # 周报
│   └── agent-landscape/    # Agent Runtime 技术全景(调研报告+PDF)
│
└── products/               # 产品文档资料
    └── ascend/950/         # 昇腾950 NPU 白皮书(docling 转换输出)
```

## 命令

### 项目维护

| 命令 | 用途 | 示例 |
|------|------|------|
| `/kg-add <url>` | 添加新项目到知识图谱 | `/kg-add https://github.com/opensourceways/cora` |
| `/kg-refresh <key>` | codebase-memory 索引 + 更新 summary | `/kg-refresh opensourceways--cora` |
| `/kg-refresh --all --tag <tag>` | 按标签批量刷新 | `/kg-refresh --all --tag 上游贡献 --mode fast` |
| `/kg-reindex` | 重建全部索引文件 | `/kg-reindex` |
| `/kg-link <a> --related <b>` | 建立项目/论文关联 | `/kg-link vllm --related pagedattention` |

### 变更追踪

| 命令 | 用途 | 示例 |
|------|------|------|
| `/kg-delta <key>` | 同步 PR delta，生成 digest | `/kg-delta opensourceways--cora` |
| `/kg-delta --all-due` | 批量同步所有到期项目 | `/kg-delta --all-due` |
| `/kg-weekly` | 生成周报 (团队主导项目) | `/kg-weekly` |

### 上游洞察

| 命令 | 用途 | 示例 |
|------|------|------|
| `/kg-watch <key>` | 上游项目技术动态摘要 | `/kg-watch sgl-project--sglang --since 2026-06-22` |

> `/kg-watch` 与 `/kg-delta` 不同：不生成 PR 流水账，而是拉 Release Notes、热门 Issues/Discussions、PR 方向聚类，输出"技术动态摘要 + 竞争分析"。仅适用于 `上游贡献` 标签项目。

### 分析与探索

| 命令 | 用途 | 示例 |
|------|------|------|
| `/kg-deep <key>` | 深度探索单项目架构/代码 | `/kg-deep opensourceways--cora` |
| `/kg-topic <tag>` | 按标签聚合分析，自动拉竞品对比 | `/kg-topic llm-inference` |
| `/kg-topic <tag>` | 按分类聚合 | `/kg-topic bot` |

## 跨资源查询

支持在代码、论文、PR 变更之间联动查询：

```
用户提问 "PagedAttention 相关"
  ├─ by-tag['vllm'] → 6 projects + 1 paper
  ├─ manifest.references[].related_projects → 代码仓库
  └─ project.summary.关联节 → 上下游/论文/竞品
```

详见 `CLAUDE.md` 中"跨资源查询策略"节。

## 名称解析

PR 作者通过 `user-info.yaml` 映射为真实姓名：
- 源: https://github.com/opensourceways/opensourceway/blob/master/community/user-info.yaml
- 每次 `/kg-delta` 从远端拉取最新
- 未识别 handle 保留原始 GitHub ID

## 依赖环境

### MCP Server

| MCP Server | 用途 | 配置位置 | 关键依赖 |
|------------|------|---------|---------|
| **codebase-memory-mcp** | 代码架构分析、索引生成(graph.db.zst)、调用链追踪 | `~/.claude/.mcp.json` | 二进制: `~/.local/bin/codebase-memory-mcp`，本地运行，无需 token |
| **docling** | PDF→Markdown 转换（含图片提取、表格识别） | `~/.claude/settings.json` | `uvx --from docling-mcp[local]`，本地模式无需 token；远程模式需 `DOCLING_SERVICE_API_KEY` |
| **kubernetes** | K8s 集群管理（可选） | `~/.claude/settings.json` | kubeconfig |
| **ssh-mcp-server** | 远程服务器 SSH 操作（可选） | `~/.claude/settings.json` | SSH key |
| **gmail** | 邮件搜索/读取（可选） | MCP 配置 | Google OAuth |
| **openeuler-portal** | openEuler 社区论坛/会议/Issue 查询 | MCP 配置 | `FORUM_TOKEN`, `OPENEULER_TOKEN`, `GITCODE_TOKEN` |
| **playwright** | 浏览器自动化/网页截图/PDF 渲染 | MCP 配置 | Chromium (npx playwright install) |
| **pencil** | 设计稿 (.pen 文件) 编辑 | MCP 配置 | 无需额外 token |

### Skill（Agent 能力扩展）

| Skill | 用途 | 触发场景 |
|-------|------|---------|
| **codebase-memory** | 代码知识图谱查询（search_graph / trace_path / get_architecture） | 代码结构分析、调用链追踪、死代码检测 |
| **read-arxiv-paper** | 读取 arXiv 论文 | 论文深度阅读 |
| **arxiv-paper-translator** | 英→中论文翻译（LaTeX 编译） | 论文翻译、技术报告生成 |
| **github-project-analyzer** | GitHub 项目综合评估（技术/社区/风险） | 新项目评估、技术选型 |
| **feedgrab** | 多平台内容抓取（X/微信/YouTube/知乎等） | URL 内容提取 |
| **docling** | PDF/文档转换（PDF→Markdown+图片+表格） | 白皮书/论文转结构化 Markdown |
| **doc-coauthoring** | 结构化文档协作写作 | 提案/技术规格/决策文档 |
| **notebooklm** | Google NotebookLM 查询 | 文档源检索问答 |
| **translate** | 多语言翻译 | 中/英/日/韩/法/德/西 |
| **tavily-research** | 深度网络调研（多源综合+引用） | 市场分析、竞品对比、文献综述 |
| **markdown-formatter** | Markdown 格式化 | 文档规范化 |
| **pptx / docx / xlsx / pdf** | Office 文档处理 | 幻灯片/Word/Excel/PDF 生成 |

### 命令行工具

| 工具 | 用途 | 安装 |
|------|------|------|
| **gh** (GitHub CLI) | PR/MR 查询、私有仓库访问、Issue 操作 | `brew install gh`；需 `gh auth login` 登录 |
| **pandoc** | Markdown→HTML 转换（PDF 生成前步骤） | `brew install pandoc` |
| **playwright** | HTML→PDF 渲染（Chromium 无头浏览器） | `npx playwright install chromium` |
| **uv / uvx** | Python 包管理（docling 运行环境） | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **git** | 代码 clone、delta 分析 | 系统自带 |

### API Token

| Token | 环境变量 | 用途 | 获取方式 |
|-------|---------|------|---------|
| **GitHub Token** | `GH_TOKEN` / `GITHUB_TOKEN` | 私有仓库访问、API 限速提升 | `gh auth token` 或 [GitHub Settings](https://github.com/settings/tokens) |
| **Docling API Key** | `DOCLING_SERVICE_API_KEY` | 远程文档转换（IBM Cloud Docling SaaS） | docling 服务提供方 |
| **openEuler Forum Token** | `FORUM_TOKEN` | openEuler 论坛发帖/评论 | [forum.openeuler.org](https://forum.openeuler.org) 个人设置 |
| **openEuler Portal Token** | `OPENEULER_TOKEN` | openEuler 软件包平台/SIG 管理 | [software-pkg.openeuler.org](https://software-pkg.openeuler.org) 个人设置 |
| **GitCode Token** | `GITCODE_TOKEN` | AtomGit/GitCode PR/Issue 查询 | AtomGit 个人设置 |
| **Anthropic API Key** | `ANTHROPIC_AUTH_TOKEN` | Claude API（已通过 DeepSeek 代理） | 已配置 |
| **HuggingFace Token** | `HF_TOKEN` | 模型下载限速提升（docling 本地模型） | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |

### 系统字体（PDF 渲染）

| 字体 | 用途 | 安装 |
|------|------|------|
| **Source Han Serif SC VF**（思源宋体） | 中文 PDF 正文 | `brew install font-source-han-serif` |
| **Source Serif 4** | 英文 PDF 正文+Ligature | `brew install font-source-serif-4` |

## 硬件加速（可选）

docling 在 macOS Apple Silicon 上支持 MPS GPU 加速：

```bash
export DOCLING_DEVICE=mps
```

性能提升: TableFormer 14× / VLM(mlx-vlm) 17.4× vs CPU。需 PyTorch 2.0+（已内置）。可选安装 `mlx-vlm` 获得 VLM 最优性能。

## 技术栈

- **代码索引**: codebase-memory MCP (graph.db.zst)
- **PR 同步**: GitHub CLI (`gh`) + git log
- **文档转换**: docling (PDF→Markdown) + pandoc (MD→HTML) + Playwright (HTML→PDF)
- **论文翻译**: arXiv LaTeX + Docker XeLaTeX
