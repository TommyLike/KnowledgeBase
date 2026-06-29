# /kg-add <repo-url> [--category <cat>] [--tags <t1,t2>]

向知识图谱添加新项目。

## 读取范围（严格遵守）

本命令添加单个项目。允许读：
- config/settings.yaml
- config/index/manifest.json
- config/index/by-category.json
- config/index/by-org.json
- projects.md

禁止读：
- 其他项目的任何文件
- references/ 任何文件
- reports/ 任何文件

允许写：
- projects/<org>/<name>/ 目录及所有初始文件（meta.md, state.json, CLAUDE.md, summary.md）
- projects/<org>/<name>/digests/ 目录
- projects.md（对应 category 段追加）
- config/index/manifest.json
- config/index/by-category.json
- config/index/by-org.json

## 行为

1. 解析 repo URL，提取 org 和 repo name
2. 生成 key：`<org>--<repo-name>`
3. 如果 key 已存在，报错退出
4. 通过 GitHub API 获取 repo 元信息
5. 自动分类（基于名称规则匹配）
6. 创建项目目录和所有初始文件
7. 更新所有索引文件
8. 可选：追加到 projects.md

## 使用示例

```
/kg-add https://github.com/opensourceways/new-project --category tool --tags "go,cli"
```
