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

### /kg-refresh
- **THUDM--slime**: codebase-memory 索引完成 (3,425n/12,442e)。Megatron+SGLang+Ray 三模块架构。
- **alibaba--ROLL**: codebase-memory 索引完成 (4,985n/23,201e)。Pipeline→Scheduler→Executor 三层架构，支持 FSDP2/Megatron/HF/vLLM。
- **inclusionAI--AReaL**: codebase-memory 索引完成 (12,134n/63,474e)。全异步 RL 系统，代码规模最大。
- **radixark--miles**: codebase-memory 索引完成 (7,203n/31,721e)。slime fork + 企业增强。
- **vllm-project--vime**: codebase-memory 索引完成 (3,305n/12,642e)。vLLM 后端替代 SGLang。

### 📚 论文入库
- **deepseek--deepseek-r1**: DeepSeek-R1 (2025)。GRPO + 可验证奖励 → 推理涌现。
- **deepseek--deepseekmath**: DeepSeekMath/GRPO (2024)。首次提出 GRPO 算法。
- **stanford--dpo**: DPO (2023)。消掉 reward model 的偏好优化。
- **misc--rl-llm-survey**: RL for LLM Survey (2024)。80+ 页领域圣经。
- **antgroup--areal**: AReaL (NeurIPS 2025)。全异步 RL 系统。
- **bytedance--dapo**: DAPO (2025)。改进 GRPO vanishing advantage。

### 📝 知识归档
- **RL Post-Training 关键论文分析** → [knowledge/rl-post-training-2026-07-10.md](knowledge/rl-post-training-2026-07-10.md)

### /kg-weekly
- **opensourceways 周报 W28** (07-06~07-12): 100 PRs, 21 repos, 15 人。→ [reports/weekly-2026-W28.md](reports/weekly-2026-W28.md)
  - ascend-ci-deployment(36) · backlog(18) · om-dataarts(8) · oss-map(8) · APIMagic(5)
  - 亮点: 003 部署 CI 成型、TTFHW 看板跨4仓库联动、buildkitd 集群拆分

### /kg-add
- **moby--buildkit**: 新增。Docker/Moby 下一代构建引擎 (12,008n/71,562e)。→ [summary](projects/agent-infra/buildkit/summary.md)
- **GoogleContainerTools--kaniko**: 新增。K8s 无守护进程构建 (1,653n/4,650e)。→ [summary](projects/agent-infra/kaniko/summary.md)
- **dragonflyoss--nydus**: 新增。Rafs 懒加载镜像 (10,408n/45,163e)。→ [summary](projects/agent-infra/nydus/summary.md)
- **wagoodman--dive**: 新增。镜像分层可视化分析 (1,233n/4,143e)。→ [summary](projects/agent-infra/dive/summary.md)
- **containerd--stargz-snapshotter**: 新增。eStargz 延迟拉取 (3,063n/10,657e)。→ [summary](projects/agent-infra/stargz-snapshotter/summary.md)
- **slimtoolkit--slim**: 新增。镜像自动瘦身 (4,666n/13,593e)。→ [summary](projects/agent-infra/slim/summary.md)

### 📚 论文入库
- **hust--cbuild**: CBuild (IEEE TC 2025)。跨节点文件级缓存，15.3×构建加速。
- **huawei--flacio**: FlacIO (FAST 2025)。运行时镜像+RTPC，4.6×冷启动加速。
- **tum--2dfs**: 2DFS (ATC 2025)。2D文件系统解耦ML参数，56×构建加速。

### 📝 知识归档
- **容器镜像构建生态全景分析** → [knowledge/container-image-build-2026-07-13.md](knowledge/container-image-build-2026-07-13.md)

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

### /kg-weekly (月度分析)
- **opensourceways 组织近一月代码合入分析**: 覆盖 26 活跃项目、411 PRs、42 贡献者。→ [报告](reports/monthly-2026-06-17-07-17-ows.md)
  - 关键趋势: backlog(88) + om-dataarts(70) + datastat(69) 三项目贡献 55% PR。数据/API/看板方向占比最高(51%)。review 覆盖率偏低。bus factor 风险高。
