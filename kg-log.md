# KG 操作日志

> Append-only. 每次 KG 操作自动追加一条记录。
> 格式: `### 操作类型` → `- **目标**: 变更描述。影响范围。`

## 2026-08-29

### 🗂️ 知识库重组（阶段 1/4：删除团队组织）
- **删除 opensourceways + cosdt 团队开发组织**：团队自有开发仓库，不属于业务知识范畴，整体移除。
  - 物理删除：`projects/opensourceways/`（397 项目）+ `projects/cosdt/`（23 项目）= 420 个。
  - 团队报告删除：`reports/` 中 daily-2026-06-29 / monthly-*-ows / ows-monthly-2026-07 / weekly-W26/W27/W28（保留业务报告 pagedattention / sglang-watch / sandbox 系列 / agent-landscape）。
  - 索引清理：manifest（projects 636→216）、by-org（删 2 组织）、by-category（删 420 key，剩 8 类）、by-tag（删 1425 key，清空并删 36 个 tag）；by-status 无影响（仅索引 references）。
  - 悬空修复：`huawei--hifloat8`/`hifloat4` 的 related_projects `cosdt--vllm-ascend`→`vllm-project--vllm-ascend`、`cosdt--triton-ascend`→`triton-lang--triton-ascend`；hifloat8 summary.md 正文删除失效的 cosdt fork 死链。
  - 索引备份：`.kg-backup/phase1/`。全程 git 可回滚。

### 🗂️ 知识库重组（阶段 2/4：216 业务项目按软件层 + 领域重组）
- **消除 org/category 混用，改为自底向上软件分层**。参考 infrasys-ai/aiinfra 分层 + Backstage Domain/System/Component 模型。
  - 新一级目录（数字前缀编码栈序）：`10-compiler`(11) / `30-cluster`(2) / `40-runtime`(34: container 6 + sandbox 28) / `50-framework`(85: inference 62 + training 19 + rl-posttrain 4) / `60-agent`(70: framework/memory/gateway/observability/tool/protocol/planner/security/coding) / `70-data`(7) / `80-workflow`(7)。
  - 生态星座整簇保留在主项目层：vllm-project/sgl-project → 50-framework/inference/；pytorch/ByteDance-Seed → 50-framework/training/；triton-lang/tile-ai → 10-compiler/。`agent-infra`（最混乱目录）按语义拆 3 处（RL→50 / container→40 / workflow→80）后消失。
  - `git mv` 搬迁 216 项目（保留 history），旧 12 个一级目录清空删除。项目 key 全程不变（`<org>--<name>`），逻辑 org 视图不受影响。
  - 索引：manifest 重写 path + category(=新物理一级目录)；by-category 按 7 新层重建；跨文件相对链接批量改写 50 处（16 文件，按路径长度降序避免 slim/slime 子串误伤）；kg-index.md + projects.md 全量重建（分层分组，References 区保留）。
  - 一致性校验全过：by-category 覆盖 216、category 一致、路径 100% 磁盘存在、related_projects 悬空 0、by-tag 无孤儿。索引备份 `.kg-backup/`（phase1 + phase2-moves.json）。
  - ⏭️ 待续：阶段 3（command 刷新：改硬编码路径为 manifest 解析 + 修示例 + 重写 CLAUDE.md 目录约定）、阶段 4（A layer/domain 字段+by-layer.json / B 每层 MOC / C 关系边类型化 / D lint 新鲜度）。

### 🗂️ 知识库重组（阶段 3/4：command + 文档刷新）
- **根因**：11 个命令本就硬编码 `projects/<org>/<name>` 两级路径（与多级物理结构脱耦），重组后必断。统一改为**从 `manifest.path` 解析物理路径**（占位 `<项目目录>`，附一行定义 + "禁止拼路径"）。
  - `kg-add`：`--category` → `--layer`+`--domain` 语义 + 目录布局表 + 星座落位规则 + 写 layer/domain 到 meta；索引同步加 by-layer.json。
  - `kg-reindex`：`projects/*/meta.md` → `projects/**/meta.md` 递归；category 从物理一级目录推导；新增 by-layer.json 重建。
  - `kg-link`：新增 `--type`（upstream/downstream/alternative/complements/benchmarks/paper，对齐 Backstage 关系模型），对称/有向双向写入；修 cosdt 示例。
  - `kg-lint`：summary/state 扫描改递归；H1 新鲜度治理强化（active>30d / 任意>90d，按陈旧度 Top-N）；删 osw 陈述；孤立判定用 layer/domain；P2 类名换新层。
  - `kg-delta/deep/refresh/topic/watch/weekly/doc` + README + repo-management：路径占位改 manifest 解析（36 处），示例键业务化（opensourceways--cora→vllm-project--vllm-ascend，cosdt--triton-ascend→triton-lang--triton-ascend）；保留 user-info.yaml 外部 URL 与 bot 账号（映射源有效）。
  - 文档：重写 `CLAUDE.md`「目录布局约定」为七层分层表 + "path 唯一真源走 manifest / key 不变 / facet 多维检索"约定；「索引位置」加 by-layer.json + 各层 MOC；`invariants.md` 加「物理路径寻址」不变量、L2-L5 改 `<dir>=manifest.path 解析`。
  - ⚠️ **语义后果**：删团队组织后 `团队主导` 项目 = 0，`/kg-weekly`（范围仅团队主导）无覆盖对象，待用户决定重定义范围或退役。业务项目全为 `上游贡献`（131）+ 未标。
  - ⏭️ 待续：阶段 4（A/B/C/D 补充措施）。

### 🗂️ 知识库重组（阶段 4/4：知识地图补充措施 A/B/C/D）
- 让重组从"整理文件夹"升级为真正的"知识地图"（浅树 + facet + graph + MOC，对照 Backstage / PKM-MOC / faceted classification）。
  - **A｜layer/domain 可查询字段 + by-layer.json**：manifest 每项目加 `layer`（compiler/cluster/runtime/framework/agent/data/workflow）+ `domain`；写入 204 个 meta.md（12 个无 url 行跳过，manifest 兜底）；新建 `config/index/by-layer.json`（layers + 18 个 domain 细分）。星座卫星可后续手工改 layer 表达真实所属层，物理不迁移。
  - **B｜MOC 导览页**：`projects/README.md`（自底向上栈图 + 七层表 + 检索心法）+ 7 张 `projects/<层>/README.md`（这层解决什么 + 按领域列项目带链接与一句话 + 关联论文）。共 8 张，248 条内部链接 0 断链。kg-index.md 顶部加 MOC 指针。
  - **C｜关系边类型化**：manifest 加 `relations:[{target,type}]`（对齐 Backstage well-known relations）。回填 30 条：硬件后端 port→upstream（triton-ascend/vllm-ascend/tilelang-* 等 10）、vllm↔sglang alternative、miles→slime upstream(fork)、agent-lightning→RL 框架群 alternative、论文↔项目 paper/downstream。去重 hifloat 重复关联。同域项目=隐式竞品（靠 by-layer domain，不炸开 pairwise）。
  - **D｜新鲜度治理**：kg-lint H1 强化（active>30d / 任意>90d，按陈旧度 Top-N）。实检：43 项目有 last_refresh，18 个 active 已陈旧（vllm-ascend/triton/sglang 61d 等），173 个从未刷新——真实健康信号浮现。
  - **最终一致性全绿**：layer/domain 全覆盖、by-layer 覆盖 216、relations/related_projects 悬空 0 无重复、路径全存在、索引无 osw/cosdt、MOC 8/8。
- **✅ 四阶段重组完成**。
- **收尾（用户确认）**：`/kg-weekly` 退役删除（团队主导项目=0，无覆盖对象）——删命令文件 + CLAUDE.md「周报格式规范」整节 + 运维命令列表 + invariants + README 表/目录树引用（knowledge-base.md 设计随笔的示例性提及保留）。删临时备份 `.kg-backup/`。全部改动提交。

## 2026-08-25

### 📚 论文入库
- **microsoft--agent-lightning**: Agent Lightning v1.0: Towards Harnessed Agentic RL (arXiv:2608.17528, 2026 微软技术报告)。用户提供 arXiv 链接 → 拉取 TeX 源 + PDF → 中文全译（9 个 .tex 文件，Docker XeLaTeX 编译 18 页中文 PDF，0 错误）→ paper.md/paper-zh.md 双语文档 + 中英双语 summary。核心: Harnessed Agentic RL 范式（脚手架拥有交互循环），四大挑战（重分词/优势计算/损失归一化/后端调度）首次系统阐述，rollout 级设计选择，~3500 行框架，共址异步 RL，6K 样本 SWE-bench Verified 41.8%→56.4%。tags: rl/agentic-rl/agent-harness/llm。→ [summary](references/microsoft/agent-lightning/summary.md)
  - 索引同步: manifest.json（related_projects: THUDM--slime/inclusionAI--AReaL/radixark--miles/vllm-project--vime/alibaba--ROLL/deepseek-ai--deepseek-harness）、by-status（analyzed）、by-tag（rl/llm 追加 + 新建 agentic-rl/agent-harness tag）、by-org（microsoft org 追加）、kg-index.md References 区。
  - 译文工件: [paper-zh.md](references/microsoft/agent-lightning/paper-zh.md) + [paper-zh.pdf](references/microsoft/agent-lightning/paper-zh.pdf)，TeX 源在 arXiv_2608.17528/paper_cn/（保留未删）。

## 2026-08-20

### /kg-topic
- **主题: 量化算法（历史 + 主要技术方向）**: 涉及 9 projects（vllm/llm-compressor/compressed-tensors/vllm-bnb-plugin/vllm-gguf-plugin/sglang/sgl-kernel-npu/vllm-ascend/miles）。外部调研 + KG 索引关联。核心结论: 演进主轴为比特宽度下探（INT8→W4A16→FP8→FP4→1.58bit），2025-2026 主线为硬件-算法协同设计（NVFP4/MXFP4，旋转法在新格式失效），推理框架收敛于 GPTQ/AWQ/FP8 + Marlin/DeepGEMM kernel。→ [归档](knowledge/quantization-algorithms-2026-08-20.md)
  - **补充（用户提问）**: 华为 HiFloat 系列。调研后补充 HiF8（点位域变长编码，38 阶码逼近 FP16，950PR 原生 919 TFLOPS）与 HiF4（三级层次缩放）。**HiFloat16 公开渠道未检索到**，待用户提供来源后补充。

### 📚 论文入库
- **huawei--hifloat8**: Ascend HiFloat8 Format for Deep Learning (arXiv:2409.16626, 2024)。用户提供本地 PDF → 拷贝 + pdftotext 提取全文转 markdown（13 页，5 章节）+ 中英双语 summary。核心: 点位域锥形精度，38 阶码，训推一体。tags: quantization/ascend/npu。→ [summary](references/huawei/hifloat8/summary.md)
- **huawei--hifloat4**: HiFloat4 Format for Language Model Inference (arXiv:2602.11287, 2026)。用户提供本地 PDF → 提取转 markdown（8 页，两栏排版已修复）+ 中英双语 summary。核心: 三级层次缩放（E6M2+两级 E1 微指数），组 64，4.5 bit/值，direct-cast 全面超越 NVFP4。tags: quantization/ascend/npu。→ [summary](references/huawei/hifloat4/summary.md)
  - 索引同步: manifest.json（related_projects: sgl-kernel-npu/vllm-ascend×2/triton-ascend×2）、by-status（analyzed）、by-tag（新增 quantization tag）、by-org（新增 huawei org）、kg-index.md References 区。

## 2026-08-16

### /kg-doc
- **cordiverse--spatiotemporal-composability**: 中文全译本生成。88 页论文 → 30 页中文 PDF（散文全译 + 数学符号保留 + 定理/引理编号沿用原文）。流程: pdftotext 提取 → 8 章节拆分 → 内联翻译为 LaTeX 片段 → Docker XeLaTeX 编译（Fandol 字体，3 遍，0 错误）。→ [paper-zh.pdf](references/cordiverse/spatiotemporal-composability/paper-zh.pdf) + [paper-zh.tex](references/cordiverse/spatiotemporal-composability/paper-zh.tex)

### /kg-deep
- **主题: Cordis 可逆插件系统科普 + 代码实现分析**: 涉及 1 reference + 1 project（deepseek-ai--deepseek-harness）。clone cordiverse/cordis（1848 行核心）逐点映射论文定理→代码（.reverse()=LIFO、provide dispose=守卫、epoch=承诺视图、inertia=惯性）。科普文档: 问题三维度→六个解法（含代码）→整体设计→五个引申。配套归档 dsh 官方 7 篇中文教程。→ [归档](knowledge/cordis-reversible-plugin-system-2026-08-16.md)
- **叙事版生成**: 事故现场故事线（用户选定）+ 戴老板笔法（先读 5 篇语料）→ 5 节叙事长文 + 6 幅技术蓝墨 TikZ 插图（封面告警图/三病图/叠盘子/插线板树/守卫四步/六态状态机）→ Docker XeLaTeX 编译 5 页 PDF。→ [叙事版](knowledge/cordis-narrative-2026-08-16.md) | [PDF](knowledge/cordis-narrative-2026-08-16.pdf)

## 2026-08-14

### /kg-link
- **deepseek-ai--deepseek-harness ↔ cordiverse--spatiotemporal-composability**: 建立关联。关联类型: 项目↔论文（上游设计论文）。Cordis 时空可组合性论文（PKU×DeepSeek, 88页）为 dsh 插件架构的理论底座，已归档 PDF + 中英双语摘要。
- **配套文章归档**: 《可逆的插件系统》（Shigma, Koishi 官方设计文档, 2023, 中文原文）已存入 references/cordiverse/spatiotemporal-composability/disposable-plugin-system-koishi-2023.md。非学术论文（官网设计文章），原文即中文无需翻译。另生成 PDF 版（6页，pandoc→Docker XeLaTeX，Fandol 字体，修复 2 处 array 公式）。

## 2026-08-14

### /kg-deep
- **主题: Authenticated Workflows 论文（arXiv 2602.10465）**: 涉及 1 paper。read-arxiv-paper + arxiv-paper-translator 双 skill 流程：通读全文 + 15 个 .tex 文件中文全译 + Docker XeLaTeX 编译 15 页 PDF。核心结论: 四控制面（prompt/tool/data/context）完备最小、MAPL 策略语言 O(log M+N) 缩放、9 框架零协议修改集成。→ [归档](knowledge/authenticated-workflows-2026-08-14.md) | [中文 PDF](arXiv_2602.10465/paper_cn/authenticated-workflows-sp26-v28.pdf)

## 2026-08-13

### /kg-add
- **deepseek-ai--deepseek-harness**: 新增。DeepSeek AI 官方 agent harness（dsh），"Everything is a Plugin"，基于 Cordis 插件架构，TypeScript monorepo（50+ 插件包）。2026-08-13 发布当天即 42k+ stars。→ [summary](projects/60-agent/framework/deepseek-harness/summary.md)

### /kg-refresh
- **deepseek-ai--deepseek-harness**: 刷新。commit null → `47f9438`。主要变更: clone 代码 + codebase-memory fast 索引（42465 nodes / 92315 edges）。AUTO 区填充快照/入口/架构/热点：ReactLoopAgent 主循环（core/agent-loop）、CommandRuntime（interaction/commands）、54 插件包 Cordis 插件树架构。无级联影响。

## 2026-08-08

### /kg-refresh
- **vllm-project--vllm-omni**: 刷新。更新 summary.md AUTO 区和手动区（定位/介绍/技术要点/技术栈/关联）。repo 已 clone。主要变更: 补充完整项目描述、架构要点（Stage Pipeline + OmniConnector）、6 个技术要点、5 个核心场景。无级联影响。

### /kg-deep
- **主题: vLLM-Omni 全双工实时推理**: 涉及 1 project（vllm-project--vllm-omni）。深度分析 DuplexRuntime/Barge-In/AsyncChunk/OpenAI Realtime 协议/客户端 demo。→ [归档](knowledge/full-duplex-realtime-inference.md)

## 2026-08-04

### /kg-add
- **vllm-project--vllm-report**: 新增。vllm-ascend 日常提交监控与 AI 分析工具，为 vllm-ascend 代码升级和 main2main 适配提供知识库支撑。→ [summary](projects/50-framework/inference/vllm-project/vllm-report/)

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
- **THUDM--slime**: 新增。智谱/清华 RL post-training 基座框架（Megatron+SGLang+Ray），GLM-4.5/4.6 训练框架。→ [summary](projects/50-framework/rl-posttrain/slime/summary.md)
- **alibaba--ROLL**: 新增。阿里 RL for LLM，20+ 算法，支持 Ascend NPU。→ [summary](projects/50-framework/rl-posttrain/ROLL/summary.md)
- **inclusionAI--AReaL**: 新增。蚂蚁全异步 RL（NeurIPS 2025），2.77× 加速。→ [summary](projects/50-framework/rl-posttrain/AReaL/summary.md)
- **radixark--miles**: 新增。企业级 slime fork，FP8/INT4 QAT/R3。→ [summary](projects/50-framework/rl-posttrain/miles/summary.md)
- **vllm-project--vime**: 新增。vLLM 原生 RL post-training。→ [summary](projects/50-framework/inference/vllm-project/vime/summary.md)

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
- **moby--buildkit**: 新增。Docker/Moby 下一代构建引擎 (12,008n/71,562e)。→ [summary](projects/40-runtime/container/buildkit/summary.md)
- **GoogleContainerTools--kaniko**: 新增。K8s 无守护进程构建 (1,653n/4,650e)。→ [summary](projects/40-runtime/container/kaniko/summary.md)
- **dragonflyoss--nydus**: 新增。Rafs 懒加载镜像 (10,408n/45,163e)。→ [summary](projects/40-runtime/container/nydus/summary.md)
- **wagoodman--dive**: 新增。镜像分层可视化分析 (1,233n/4,143e)。→ [summary](projects/80-workflow/dive/summary.md)
- **containerd--stargz-snapshotter**: 新增。eStargz 延迟拉取 (3,063n/10,657e)。→ [summary](projects/40-runtime/container/stargz-snapshotter/summary.md)
- **slimtoolkit--slim**: 新增。镜像自动瘦身 (4,666n/13,593e)。→ [summary](projects/40-runtime/container/slim/summary.md)

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

## 2026-08-26

### /kg-add
- **ByteDance-Seed--VeOmni**: 新增。字节 Seed 任意模态模型训练框架(OmniScale,AAAI 2026),Trainer-free + FSDP2/SP(Ulysses)/EP,支持昇腾 NPU。→ [summary](projects/50-framework/training/ByteDance-Seed/VeOmni/summary.md)
  - 索引同步: manifest.json(projects 635→636)、by-org(ByteDance-Seed 新增 org)、by-tag(ai/training/distributed/multimodal/ascend)、projects.md ai 段(89→90, active 1→2)、kg-index.md(新增 ByteDance-Seed 段)。
  - repo: 已浅克隆至 projects/50-framework/training/ByteDance-Seed/VeOmni/repo(commit 32d537d,2026-08-25,25M);codebase-memory 索引待 /kg-refresh。
