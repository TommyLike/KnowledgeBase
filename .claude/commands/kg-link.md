# /kg-link <key> --related <other-key> [--type <type>]

手动建立项目/引用之间的**类型化**关联关系。

## 关系类型（--type，对齐 Backstage well-known relations）

| type | 含义 | 方向 |
|------|------|------|
| `upstream` | 本项目的上游/被依赖方 | key → other 为 upstream |
| `downstream` | 本项目的下游/使用方 | key → other 为 downstream |
| `alternative` | 同类竞品 / 可替代方案 | 对称 |
| `complements` | 互补 / 常搭配使用 | 对称 |
| `benchmarks` | 评测 / 对比基准关系 | 对称 |
| `paper` | 项目 ↔ 论文（设计/理论底座） | project ↔ reference |

未给 `--type` 时按名称/描述推断并回显确认；无法判定时记为通用 `related`。

## 行为
1. 更新目标项目 summary.md 的「关联」节（标注关系类型）
2. 更新 manifest.json 中的 related_projects 字段（存 `{key, type}` 或带类型后缀）
3. 对称类型（alternative/complements/benchmarks）**双向写入**；有向类型（upstream/downstream）在对端写反向
4. 资源类型自动识别: project↔project / project↔reference / reference↔reference
5. **🔄 自动维护（不可跳过）**：
   - 追加 `kg-log.md`（记录本次关联建立 + 类型）

## 使用示例
```
/kg-link triton-lang--triton-ascend --related triton-lang--triton --type upstream
/kg-link vllm-project--vllm --related sgl-project--sglang --type alternative
/kg-link deepseek-ai--deepseek-harness --related cordiverse--spatiotemporal-composability --type paper
```
