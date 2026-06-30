# /kg-refresh <key> [--all] [--tag <tag>] [--mode fast|moderate|full]

对项目执行 code-memory 索引并更新 summary.md。

## 关键规则：保护人工内容

**summary.md 有两部分，处理方式不同：**

```
<!-- BEGIN AUTO -->                    ← /kg-refresh 可改写
**快照** · commit · lang · files · nodes
**入口** · **架构** · **热点**
<!-- END AUTO -->                      ← /kg-refresh 可改写

---                                    ← 以下全部保护，禁止覆盖

## 定位          ← 手动区，Agent 首次填，后续不自动覆盖
## 项目介绍      ← 手动区
## 技术要点      ← 手动区
## 技术栈        ← 手动区
## 关联          ← 手动区
## 开放问题      ← 手动区，随 delta 追加，不删历史
```

**处理方式**：
- 首次 /kg-refresh（summary.md 无 AUTO 块）：生成完整模板（AUTO + 手动区）
- 再次 /kg-refresh（summary.md 已有 AUTO 块）：**只替换 `<!-- BEGIN AUTO -->` 到 `<!-- END AUTO -->` 之间的内容**，其余部分一字不动

## 读取范围（严格遵守）

本命令聚焦单项目的代码分析。允许读：

**配置与元数据**
- config/settings.yaml
- config/index/manifest.json
- 目标项目的 projects/<org>/<name>/CLAUDE.md
- 目标项目的 projects/<org>/<name>/meta.md
- 目标项目的 projects/<org>/<name>/state.json

**代码仓库（clone 后）**
- 目标项目的 projects/<org>/<name>/repo/README.md（必读，最高优先级）
- 目标项目的 projects/<org>/<name>/repo/docs/（如存在，读 index/README/overview 等入口文件）
- 目标项目的 projects/<org>/<name>/repo/CHANGELOG.md 或 RELEASES.md（如存在）
- 目标项目的 projects/<org>/<name>/repo/（完整源码，供 codebase-memory 索引）

**补充上下文（首次生成手动区时）**
- GitHub API：repo description、topics、近 20 条 merged PR 标题+描述（用于提炼当前方向）
- GitHub API：最近 3 个 Release 的 tag + release notes（如有）

禁止读：
- 其他项目的任何文件
- references/ 任何文件
- reports/ 任何文件
- digests/ 下的 digest 文件

允许写：
- projects/<org>/<name>/summary.md（首次完整写，再次只替换 AUTO 块）
- projects/<org>/<name>/CLAUDE.md（更新 AUTO 区）
- projects/<org>/<name>/state.json（更新 last_refresh, repo 字段）
- config/index/manifest.json（更新 last_refresh）

## --all 优先级保护

`--all` 不会对全量 489 个项目平等刷新。必须配合以下参数之一：

| 参数 | 含义 | 适用场景 |
|------|------|---------|
| `--tag 团队主导` | 只刷新团队项目 | 日常维护 |
| `--tag 上游贡献` | 只刷新上游项目 | 上游洞察 |
| `--tag <custom>` | 按标签过滤 | 定向分析 |

无 `--tag` 时，`--all` 默认等同于 `--all --tag 团队主导`。

## 行为

### 每次都执行（AUTO 块刷新）

1. 如果 repo 未 clone，先 `git clone --depth 1`
2. 调用 codebase-memory-mcp `index_repository`
3. 调用 `get_architecture` 获取模块依赖树
4. 调用 `search_graph` 定向查询：核心数据结构、主调度路径、高扇入节点
5. 更新 `<!-- BEGIN AUTO -->` 块（快照 + 入口 + 架构 + 热点）
6. 更新 CLAUDE.md AUTO 区和 state.json
7. 清理 repo（clone-analyze-delete 流程）

### 仅首次执行（手动区初始填写）

首次判断条件：summary.md 不存在，或存在但无 `<!-- BEGIN AUTO -->` 标记。

按以下顺序收集素材，再统一生成手动区：

**步骤 A：读文档**
- 读 `repo/README.md`，提取：项目定位、核心算法/设计、关键 benchmark、使用场景
- 读 `repo/docs/` 入口文件（如有），提取：架构说明、关键概念
- 读 `repo/CHANGELOG.md` 或最近 3 个 GitHub Release（如有），提取：版本演进脉络

**步骤 B：读近期动态**
- 拉取近 20 条 merged PR 标题 + 描述，归纳当前工作重心（新功能/优化/修复的比例和方向）

**步骤 C：读 codebase-memory 结果**
- 结合步骤 A/B 与代码结构，验证并补全架构理解

**步骤 D：写手动区**，要求如下：

`## 定位`（2-4 句）
- 说清楚：这个项目是什么、解决什么问题、和团队的关系（主导/贡献/观察）
- 团队主导：写负责范围和业务价值
- 上游贡献：写贡献点、和上游的关系、团队为什么关注

`## 项目介绍`
- 一句话核心定位
- 3-5 个具体使用场景（不写泛化描述，写实际 use case）

`## 技术要点`（有实质内容才写，否则省略整节）
- 每条写一个有价值的技术点，格式：`- **<概念名>**：<一句话解释原理或设计权衡>`
- 示例：`- **PagedAttention**：将 KV cache 按固定 block 分页管理，消除显存碎片，利用率从 20-40% 提升至 96%+`
- 不写泛化的"使用了 X 技术"，要写"为什么用、解决了什么问题、有什么权衡"

`## 技术栈`
- 语言 + 核心框架/库（具体到库名，不写 "Git · Docker · CI/CD"）
- 示例：`Python · PyTorch · Ray（分布式调度）· xFormers · Triton（kernel）· CUDA/ROCm`

`## 关联`（有关联才写）
- 上游依赖、下游用户、竞品，每条一句话说清关系

`## 开放问题`
- 首次留空占位，格式：`- [ ] <YYYY-MM-DD> <问题>`

## 使用示例

```
/kg-refresh cosdt/triton-ascend
/kg-refresh vllm-project/vllm
/kg-refresh --all --tag 上游贡献 --mode fast
/kg-refresh --all --tag 团队主导
```
