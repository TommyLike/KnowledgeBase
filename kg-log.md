# KG 操作日志

> Append-only. 每次 KG 操作自动追加一条记录。
> 格式: `### 操作类型` → `- **目标**: 变更描述。影响范围。`

## 2026-07-10

### 🏗️ 系统初始化
- **kg-log.md**: 创建全局操作日志。
- **kg-index.md**: 创建全局可读索引（617 projects, 12 物理目录, 8 agent-runtime 子域）。
- **/kg-lint**: 创建质量检查命令（两层: 确定性 auto-fix + 启发式 report-only）。
- **knowledge/**: 创建知识归档目录，/kg-deep 完成后可归档。
- **CLAUDE.md**: 新增自动触发规则 — /kg-add /kg-refresh 后自动更新索引和日志；/kg-refresh 后自动检查级联影响。
- **invariants.md**: 新增 kg-log.md、kg-index.md、knowledge/ 相关不变量。

### /kg-lint
- 首次全量 lint。617 projects, 201 空 AUTO 区 (D3), 0 断链, 0 stale, 0 孤立, 0 空 tag. 健康评级: 🟡 需关注.

### /kg-add
- **THUDM--slime**: 新增。智谱/清华 RL post-training 基座框架（Megatron+SGLang+Ray），GLM-4.5/4.6 训练框架。→ [summary](projects/agent-infra/slime/summary.md)
- **alibaba--ROLL**: 新增。阿里 RL for LLM，20+ 算法，支持 Ascend NPU。→ [summary](projects/agent-infra/ROLL/summary.md)
- **inclusionAI--AReaL**: 新增。蚂蚁全异步 RL（NeurIPS 2025），2.77× 加速。→ [summary](projects/agent-infra/AReaL/summary.md)
- **radixark--miles**: 新增。企业级 slime fork，FP8/INT4 QAT/R3。→ [summary](projects/agent-infra/miles/summary.md)
- **vllm-project--vime**: 新增。vLLM 原生 RL post-training。→ [summary](projects/vllm-project/vime/summary.md)

---

> 格式说明:
> - `### /kg-add`: 新增项目
> - `### /kg-refresh`: 刷新项目数据
> - `### /kg-delta`: 跟踪代码变更
> - `### /kg-deep`: 深度分析（→ 归档路径）
> - `### /kg-link`: 建立关联
> - `### /kg-topic`: 主题分析
> - `### /kg-lint`: 质量检查
> - `### 系统`: 系统级操作（索引重建、配置变更等）
