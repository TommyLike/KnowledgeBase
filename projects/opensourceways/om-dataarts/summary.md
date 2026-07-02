# om-dataarts

> [`opensourceways/om-dataarts`](https://github.com/opensourceways/om-dataarts) · 团队主导 · 开源社区数据采集与分析系统

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `?` · Python · 9,998n/41,929e  
**入口** `om/tasks/` → 各 task 独立执行采集/计算  
**架构** API 层(HTTP) → Collector(采集转换) → DB(PostgreSQL) → DWS(数仓分析)  
**热点** PostgresClient.bulk_upsert · BaseCollector.fetch_from_api · 60+ 采集任务  
<!-- END AUTO -->

---

## 定位
> 开源社区运营数据中台的核心采集与计算引擎。从 Gitee/GitHub/GitCode 等平台拉取原始数据（仓库/Issue/PR/Commit/讨论），经清洗转换后入 PostgreSQL，再通过 DWS 层计算社区健康度、贡献者排行、技术雷达等指标。团队自主设计开发，数据驱动社区运营的基石。

## 项目介绍
> **开源社区数据中台**，采集→清洗→计算→展示全链路自动化。

核心场景：
- **多平台数据采集**：GitHub/Gitee/GitCode 的 PR/Issue/Commit/Star/Fork 全覆盖，含速率限制和 Token 轮换
- **贡献者画像**：D0~D2 开发者分层、co-author 识别、组织归属推断
- **TTFHW 四阶段**：开发者全流程体验（Discover→Learn→Build→Contribute）的时间采集
- **开源技术雷达**：社区技术趋势分析和洞察报告自动生成
- **流水线代码化**：`.job` 文件驱动的声明式数据管道，单命令执行全流程

## 技术要点
- **分层架构强制**：API(HTTP) → Collector(业务) → DB(存储) → DWS(分析)，跨层调用在 CI 中检测并拒绝
- **Job Runner 引擎**：Python 驱动的 DAG 流水线，支持 dry-run/单节点执行/全量执行/增量采集
- **多 Token 轮换**：`request_api.py` 内置 Token 池和指数退避重试，应对平台 API 频率限制
- **PostgreSQL 批量写入**：`bulk_upsert_data()` 基于 ON CONFLICT 的幂等 upsert，支持大吞吐
- **数据字典驱动**：`docs/DATA-DICTIONARY.md` 覆盖 ~70 张表的字段来源/计算口径/反查索引

## 技术栈
Python · PostgreSQL（主存储）· psycopg2 · GitHub/Gitee/GitCode API · Jenkins（调度）· Docker

## 关联
- [`opensourceways/datastat-manage-website`](../../projects/opensourceways/datastat-manage-website/) — 数据展示前端
- [`opensourceways/backlog`](../../projects/opensourceways/backlog/) — 需求管理和 AI 编排

## 开放问题
- [ ] 2026-06-30 TTFHW 四阶段时间口径是否需要统一标准化文档？
