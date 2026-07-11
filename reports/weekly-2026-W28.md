# 开源团队项目进展周报

> 周期: **2026-07-06 (周一) ~ 2026-07-12 (周日)** · Week 28  
> 覆盖: **opensourceways** 组织 · 团队主导项目  
> 统计: 100 merged PRs · 21 活跃仓库 · 15 位贡献者

---

## 活跃仓库

| 仓库 | PRs | 贡献者 | 变更量 | 主要方向 |
|------|-----|--------|--------|---------|
| [ascend-ci-deployment](https://github.com/opensourceways/ascend-ci-deployment) | 36 | 6 | +15/-598 | buildkitd 集群运维、CI Runner 管理 |
| [backlog](https://github.com/opensourceways/backlog) | 18 | 2 | +43/-6 | 003 部署流程优化、需求分析 |
| [om-dataarts](https://github.com/opensourceways/om-dataarts) | 8 | 2 | +384/-185 | TTFHW 测试看板、oss-insight 分类 |
| [oss-map](https://github.com/opensourceways/oss-map) | 8 | 3 | +1,642/-291 | 技术点检索、多公司导出 |
| [APIMagic](https://github.com/opensourceways/APIMagic) | 5 | 2 | +722/-58 | TTFHW 看板接口、AI 度量看板 |
| [community-robots](https://github.com/opensourceways/community-robots) | 3 | 1 | +163/-331 | 003 迁移文档、清理死代码 |
| [datastat-manage-website](https://github.com/opensourceways/datastat-manage-website) | 3 | 1 | +712/-5 | TTFHW 看板前端、AI 度量看板 |
| [apig-openapi-registry](https://github.com/opensourceways/apig-openapi-registry) | 2 | 1 | +1,125/0 | OpenAPI 同步 |
| [message-manager-website](https://github.com/opensourceways/message-manager-website) | 2 | 1 | +1,254/-385 | Logo 替换、漏洞修复 |
| [oneid-website](https://github.com/opensourceways/oneid-website) | 2 | 1 | +105/-89 | Logo 替换 |
| 其他 (11 repos) | 13 | 9 | — | 零星维护 |

---

## 变更详情

### [ascend-ci-deployment](https://github.com/opensourceways/ascend-ci-deployment) — 36 PRs

> 本周活跃贡献者 6 人 | 新增 15 / 删除 598 | 主要方向: buildkitd 集群拆分与运维

| PR | 日期 | 作者 | 审核 | ± | 描述 |
|----|------|------|------|---|------|
| [#1002](https://github.com/opensourceways/ascend-ci-deployment/pull/1002) | 07-10 | 吴鹤俊 | — | +13/-4 | feat: buildkitd 模板渲染 config 参数并调整 GC 策略 |
| [#1001](https://github.com/opensourceways/ascend-ci-deployment/pull/1001) | 07-10 | 吴鹤俊 | — | +0/-592 | remove hk001 extra buildkitd services (amd64/arm64 multi-replica) |
| [#1000](https://github.com/opensourceways/ascend-ci-deployment/pull/1000) | 07-10 | 文浪 | — | — | add nightly runner for vllm-ascend |
| [#999](https://github.com/opensourceways/ascend-ci-deployment/pull/999) | 07-10 | 许广跃 | — | — | add github proxy |
| [#998](https://github.com/opensourceways/ascend-ci-deployment/pull/998) | 07-10 | 龙文韬 | — | +2/-2 | chore: 更新 vllm-ascend a2b3-0 runner 镜像 tag |
| [#997](https://github.com/opensourceways/ascend-ci-deployment/pull/997) | 07-10 | 吴鹤俊 | — | — | Fix memory |
| [#996](https://github.com/opensourceways/ascend-ci-deployment/pull/996) | 07-10 | 吴鹤俊 | — | — | Hk001 buildkitd split services |
| [#995](https://github.com/opensourceways/ascend-ci-deployment/pull/995) | 07-10 | 吴鹤俊 | — | — | split hk001 buildkitd into three services |
| [#994](https://github.com/opensourceways/ascend-ci-deployment/pull/994) | 07-10 | 文浪 | — | — | bugfix |
| [#992](https://github.com/opensourceways/ascend-ci-deployment/pull/992) | 07-10 | 刘洋 | — | — | create cn12 amd64 and arm64 buildkitd |
| [#990](https://github.com/opensourceways/ascend-ci-deployment/pull/990) | 07-10 | 许广跃 | — | — | update vllm-ascend、nv-action gy006 pvc |
| [#989](https://github.com/opensourceways/ascend-ci-deployment/pull/989) | 07-10 | 刘洋 | — | — | cancle pvc |
| [#988](https://github.com/opensourceways/ascend-ci-deployment/pull/988) | 07-10 | 吴鹤俊 | — | — | fix: pvc报错 |
| [#987](https://github.com/opensourceways/ascend-ci-deployment/pull/987) | 07-10 | 刘洋 | — | — | delete securitycontext |
| [#986](https://github.com/opensourceways/ascend-ci-deployment/pull/986) | 07-10 | 刘洋 | — | — | fix buildkitd deploy error |
| [#983](https://github.com/opensourceways/ascend-ci-deployment/pull/983) | 07-09 | 许广跃 | — | — | vllm-ascend、nv-action接入vNPU runner |
| [#978](https://github.com/opensourceways/ascend-ci-deployment/pull/978) | 07-09 | 吴鹤俊 | — | — | fix(buildkitd): revert to rootless + fuse-overlayfs |
| [#977](https://github.com/opensourceways/ascend-ci-deployment/pull/977) | 07-09 | 吴鹤俊 | — | — | fix(buildkitd): fix probe timeout, rootless lchown |
| [#976](https://github.com/opensourceways/ascend-ci-deployment/pull/976) | 07-09 | 吴鹤俊 | — | — | Fix update strategy |
| _其余 17 个 PR 省略_ |

### [backlog](https://github.com/opensourceways/backlog) — 18 PRs

> 本周活跃贡献者 2 人 | 新增 43 / 删除 6 | 主要方向: 003 部署模式 CI/CD 流水线优化

| PR | 日期 | 作者 | 审核 | ± | 描述 |
|----|------|------|------|---|------|
| [#1330](https://github.com/opensourceways/backlog/pull/1330) | 07-10 | 汤佳 | — | +11/-5 | fix(ci): 003 镜像 tag 加时间戳 + 部署耗时日志 + 产物 JSON |
| [#1329](https://github.com/opensourceways/backlog/pull/1329) | 07-10 | 汤佳 | — | +17/-1 | fix(ci): 003 模式部署成功后写产物 JSON 供 tester 读取 |
| [#1328](https://github.com/opensourceways/backlog/pull/1328) | 07-10 | 汤佳 | — | +15/-0 | fix(ci): DinD pod Ready 后额外等待 dockerd 启动 |
| [#1327](https://github.com/opensourceways/backlog/pull/1327) | 07-10 | 汤佳 | — | — | fix(ci): DinD pod 固定 docker:27-dind 避免 OCI 镜像兼容问题 |
| [#1326](https://github.com/opensourceways/backlog/pull/1326) | 07-10 | 汤佳 | — | — | fix(ci): 003 模式用预览集群 DinD pod 构建镜像 |
| [#1324](https://github.com/opensourceways/backlog/pull/1324) | 07-10 | 汤佳 | — | — | fix(ci): 003 模式用 Kaniko 替代 Docker 构建镜像 |
| [#1321](https://github.com/opensourceways/backlog/pull/1321) | 07-10 | 汤佳 | — | — | fix(ci): Docker 步骤仅 003 模式触发，去掉 socket 挂载 |
| [#1320](https://github.com/opensourceways/backlog/pull/1320) | 07-10 | 汤佳 | — | — | fix(ci): implement job 挂载 Docker socket |
| [#1319](https://github.com/opensourceways/backlog/pull/1319) | 07-10 | 汤佳 | — | — | fix(ci): 003 模式增加 Docker 可用性保障步骤 |
| [#1318](https://github.com/opensourceways/backlog/pull/1318) | 07-09 | fly333sky | — | — | docs: 需求分析 #736 会议系统支持自动发送纪要到邮件列表 |
| [#1317](https://github.com/opensourceways/backlog/pull/1317) | 07-09 | 汤佳 | — | — | feat(deploy): 003 模式改用 docker build + push SWR |
| [#1314](https://github.com/opensourceways/backlog/pull/1314) | 07-10 | 汤佳 | — | — | fix(deploy): kubectl cp /app/ 权限拒绝 → cp 到 /tmp |
| [#1313](https://github.com/opensourceways/backlog/pull/1313) | 07-09 | 汤佳 | — | — | fix(deploy): 003 kubectl cp 误将 deploy/ 当作 namespace |
| [#1310](https://github.com/opensourceways/backlog/pull/1310) | 07-08 | fly333sky | — | — | docs: 需求分析 welcome 机器人根据 Issue 标题前缀自动打标签 |
| [#1308](https://github.com/opensourceways/backlog/pull/1308) | 07-08 | 汤佳 | — | — | feat: deploy.sh 增加 003 常驻集群模式路由 |
| _其余 3 个 PR 省略_ |

### [om-dataarts](https://github.com/opensourceways/om-dataarts) — 8 PRs

> 本周活跃贡献者 2 人 | 新增 384 / 删除 185 | 主要方向: TTFHW 测试看板 + oss-insight 分类

| PR | 日期 | 作者 | 审核 | ± | 描述 |
|----|------|------|------|---|------|
| [#434](https://github.com/opensourceways/om-dataarts/pull/434) | 07-11 | 钟君 | — | +13/-0 | fix(ttfhw): dwm community 入库前统一 strip 去尾空白 |
| [#433](https://github.com/opensourceways/om-dataarts/pull/433) | 07-10 | 钟君 | — | +122/-122 | fix(ttfhw): 提交目标仓从 JSON 读，不硬编码 |
| [#432](https://github.com/opensourceways/om-dataarts/pull/432) | 07-10 | 钟君 | — | +249/-63 | fix(ttfhw): 稳定 dwm_ttfhw_issue 与运行的关联 |
| [#430](https://github.com/opensourceways/om-dataarts/pull/430) | 07-09 | 钟君 | — | — | feat(ttfhw): TTFHW 测试总汇看板数据入库 |
| [#429](https://github.com/opensourceways/om-dataarts/pull/429) | 07-09 | 吴彩萍 | — | — | feat(opengauss): refactor opengauss_download |
| [#427](https://github.com/opensourceways/om-dataarts/pull/427) | 07-09 | 吴彩萍 | — | — | fix(cve): update issue retrieval to use html_url |
| [#424](https://github.com/opensourceways/om-dataarts/pull/424) | 07-08 | 钟君 | — | — | feat(oss-insight): 报告按 insight_type 分类 |
| [#416](https://github.com/opensourceways/om-dataarts/pull/416) | 07-07 | 钟君 | — | — | openGauss 社区健康度看板新增"AI 度量看板" |

### [oss-map](https://github.com/opensourceways/oss-map) — 8 PRs

> 本周活跃贡献者 3 人 | 新增 1,642 / 删除 291 | 主要方向: 技术点检索 + user alias 修复

| PR | 日期 | 作者 | 审核 | ± | 描述 |
|----|------|------|------|---|------|
| [#106](https://github.com/opensourceways/oss-map/pull/106) | 07-10 | 李楚阳 | — | +2/-1 | fix(frontend): API 代理超时提高到 10 分钟 |
| [#105](https://github.com/opensourceways/oss-map/pull/105) | 07-10 | 黄堆灿 | — | +878/-290 | fix: user alias 的 github id 错误命名 → github login |
| [#103](https://github.com/opensourceways/oss-map/pull/103) | 07-09 | fly333sky | — | +762/-0 | 增加全局的技术点检索—work部分 |
| [#102](https://github.com/opensourceways/oss-map/pull/102) | 07-09 | fly333sky | — | — | 项目级技术点检索结果额外添加 commit 列表 |
| [#101](https://github.com/opensourceways/oss-map/pull/101) | 07-07 | 李楚阳 | — | — | feat(orgs): 支持多公司合并导出 commit 贡献 |
| [#100](https://github.com/opensourceways/oss-map/pull/100) | 07-07 | 李楚阳 | — | — | feat(backend): 首页项目列表 GitHub 优先排序 |
| [#99](https://github.com/opensourceways/oss-map/pull/99) | 07-07 | 李楚阳 | — | — | fix(backend): seed only test users to avoid CrashLoop |
| [#61](https://github.com/opensourceways/oss-map/pull/61) | 07-07 | fly333sky | — | — | oss-map 前端修正浏览器页签标题与页面语言 |

### [APIMagic](https://github.com/opensourceways/APIMagic) — 5 PRs

> 本周活跃贡献者 2 人 | 新增 722 / 删除 58 | 主要方向: TTFHW 看板 + AI 度量看板

| PR | 日期 | 作者 | 审核 | ± | 描述 |
|----|------|------|------|---|------|
| [#129](https://github.com/opensourceways/APIMagic/pull/129) | 07-10 | fly333sky | — | +73/-56 | 优化AI统计分组与SIG统计的数据展示逻辑 |
| [#128](https://github.com/opensourceways/APIMagic/pull/128) | 07-10 | 钟君 | — | +590/-0 | docs(api): 补 TTFHW 分组接口文档 group-TTFHW.md |
| [#125](https://github.com/opensourceways/APIMagic/pull/125) | 07-09 | 钟君 | — | — | TTFHW 看板接口(总览/运行明细/运行详情/断点问题) |
| [#123](https://github.com/opensourceways/APIMagic/pull/123) | 07-08 | 钟君 | — | +59/-2 | feat(oss-insight): 报告列表返回 insight_type |
| [#111](https://github.com/opensourceways/APIMagic/pull/111) | 07-07 | 钟君 | — | — | openGauss AI 度量看板—APIMagic部分 |

---

## 贡献者统计

| 贡献者 | PRs | 变更量 | 主要方向 |
|--------|-----|--------|---------|
| 吴鹤俊 (JavaPythonAIForBAT) | 22 | +13/-596 | buildkitd 集群运维、CI 基础设施 |
| 汤佳 (TangJia025) | 16 | +206/-337 | 003 部署 CI/CD、文档 |
| 钟君 (flysky22222) | 13 | +1,745/-192 | TTFHW 看板、oss-insight、AI 度量 |
| fly333sky | 9 | +835/-56 | oss-map 检索、需求分析 |
| 刘洋 (githubliuyang777) | 6 | — | buildkitd 部署、GPU runner |
| 谢承志 (2511689622) | 4 | +1,125/0 | OpenAPI 同步、EasySearch |
| 许广跃 (123-prog) | 4 | — | CI proxy、vNPU runner |
| 李楚阳 (licy666) | 4 | +2/-1 | oss-map 前端/后端 |
| 周琪 (sky-winter) | 3 | +105/-89 | 官网 Logo 替换 |
| 龙文韬 (Longwt123) | 2 | +2/-2 | CI runner 镜像 |
| 文浪 (Goalina) | 2 | — | nightly runner |
| 张峻玮 (zjwmiao) | 2 | +1,254/-385 | Logo 替换、漏洞修复 |
| 吴彩萍 (Kaede10) | 2 | — | om-dataarts 重构 |
| 黄世俊 (HuangSJ-TY) | 2 | — | Logo 替换 |
| 其他 (4 人) | 4 | — | 零星维护 |

---

## 未识别 Handle

| Handle | PRs | 建议 |
|--------|-----|------|
| **fly333sky** | 9 | 高频贡献者，建议补充到 user-info.yaml |
| **MrZ20** | 1 | 低频，可能是外部贡献 |

---

## 本周亮点

1. **003 部署模式 CI 流水线成型** — 汤佳连续 15 个 PR 完成 Kaniko→DinD→kubectl cp 全链路调试，从 PoC 进入可用阶段
2. **TTFHW 看板跨 4 仓库联动** — 钟君在 om-dataarts / APIMagic / datastat-manage-website 同步推进测试看板、oss-insight、AI 度量三大看板
3. **buildkitd 集群拆分** — 吴鹤俊将 hk001 集群 buildkitd 从单实例拆分为 amd64/arm64 分离 + cn12 新集群
4. **oss-map 全局技术点检索上线** — fly333sky + 黄堆灿完成技术点检索 + user alias 修复

---

> 🤖 本报告由 KG Agent 自动生成 · 数据来源: GitHub API (opensourceways org, merged PRs 2026-07-06~07-12)
