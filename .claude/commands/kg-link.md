# /kg-link <key> --related <other-key>

手动建立项目/引用之间的关联关系。

## 行为
1. 更新目标项目 summary.md 的「关联」节
2. 更新 manifest.json 中的 related_projects 字段
3. 关联类型自动推断: project↔project, project↔reference, reference↔reference

## 使用示例
```
/kg-link cosdt--triton-ascend --related triton-lang--triton
/kg-link vllm-project--vllm --related vllm-project--pagedattention
```
