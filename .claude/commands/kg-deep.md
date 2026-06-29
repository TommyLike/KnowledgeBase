# /kg-deep <project-or-ref-key> [--with <other-key>...] [--question "..."]

深度探索单项目或引用。切换工作目录以自动加载项目级 CLAUDE.md。

## 读取范围（严格遵守）

本命令聚焦单项目/引用的深度分析。允许读：
- 根 CLAUDE.md
- config/settings.yaml
- 目标项目的 projects/<org>/<name>/CLAUDE.md
- 目标项目的 projects/<org>/<name>/summary.md
- 目标项目的 projects/<org>/<name>/meta.md
- 目标项目的 projects/<org>/<name>/digests/ 最近 3 篇
- 目标项目的 projects/<org>/<name>/repo/（如果已 clone）
- --with 指定的其他项目的 summary.md（仅摘要）
- config/index/manifest.json（查找 --with 目标）

禁止读：
- 非目标项目的任何 digest 或 repo 文件（--with 除外且仅限 summary）
- references/ 任何文件（除非目标本身就是引用）
- reports/ 任何文件

允许写：
- 无（本命令只读，除非你显式要求更新 summary 或追加 note）

## 行为

1. 如果目标是项目：切换 cwd 到 `projects/<org>/<name>/repo/`（如果没有 clone，停留在 vault 根）
2. 如果目标是引用：保持在 vault 根
3. 加载项目上下文并进入交互模式
4. --question 直接回答后退出，否则等待用户提问
5. 退出时不写任何文件

## 使用示例

```bash
cd ${KG_ROOT}/projects/opensourceways--cora/repo
claude    # 自动加载根 + 项目 CLAUDE.md
> /kg-deep opensourceways--cora --question "这个项目的主要架构是什么"
```
