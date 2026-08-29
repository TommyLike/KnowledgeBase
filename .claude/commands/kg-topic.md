# /kg-topic <tag-or-topic> [--depth summary|full]

> **`<项目目录>`** = 由 `config/index/manifest.json` 的 `path` 字段解析出的物理路径（软件分层可变，key 不变）。禁止拼 `projects/<org>/<name>`。


按 tag 或主题聚合分析多个项目。

## 读取范围（严格遵守）

本命令做跨项目主题分析。允许读：
- config/index/by-tag.json（确定目标项目范围）
- config/index/manifest.json
- 匹配项目的 <项目目录>/summary.md
- 匹配项目的 <项目目录>/meta.md
- config/settings.yaml

禁止读：
- 非匹配项目的任何文件
- 任何项目的 digests/ 或 repo/ 文件（除非 --depth full）
- references/ 任何文件（除非 tag 匹配了引用）

允许写：
- reports/topic-<slug>-<date>.md（可选输出报告）

## 行为

1. 读 by-tag.json 找匹配的 tag
2. 如果 tag 不存在，尝试全文搜索项目名和描述
3. 读取所有匹配项目的 summary.md
4. 按主题聚合分析
5. 输出主题报告
6. **🔄 完成后询问归档**（不可跳过）：
   - 分析结束后，Agent **必须**询问："是否归档本次分析结果？"
   - 用户确认 → 写入 `knowledge/<topic-slug>-<YYYY-MM-DD>.md`
   - 追加 `kg-log.md`（记录归档）

## 使用示例

```
/kg-topic bot
/kg-topic compiler --depth full
```
