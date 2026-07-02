# message-manager

> [`opensourceways/message-manager`](https://github.com/opensourceways/message-manager) · 团队主导 · 开源社区统一消息管理中心

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `?` · Go · 908n/2,688e  
**入口** `main.go` → Gin HTTP Server  
**架构** DDD 四层: controller → app → domain → infrastructure (PostgreSQL/Cassandra)  
**热点** allerror.Error(×92) · postgresql.DB(×31) · user.GetSystemUserName(×29)  
<!-- END AUTO -->

---

## 定位
> openEuler 社区的统一消息中心，为社区用户提供消息订阅、聚合、推送和收件箱管理。集成论坛/会议/CVE/Issue 等多种消息源，用户可定制订阅规则，系统按规则推送通知。团队自主设计开发。

## 项目介绍
> **社区消息的统一入口**，从"信息碎片化"到"一站式收件箱"。

核心场景：
- **多源消息聚合**：论坛回帖、会议通知、CVE 警报、Issue 更新 → 统一收件箱
- **按需订阅**：用户可选择关注的 SIG/仓库/话题（35 个 API 端点支持 CRUD）
- **多渠道推送**：邮件 + IM + 站内通知，按用户偏好分发
- **内部消息管理**：`/inner/count` 统计未读、`/inner/todo` 聚合待办、`/inner/cve/todo` CVE 待办

## 技术要点
- **DDD 严格分层**：controller → app(用例编排) → domain(领域模型) → infrastructure(DB 实现)，跨层依赖单向
- **双数据库**：PostgreSQL（主存储，用户/订阅/消息）+ Cassandra（高吞吐日志）
- **统一错误体系**：`allerror.Error` 为全系统 92 个调用点提供类型安全的错误包装
- **35 个 API 端点**：覆盖订阅 CRUD、消息聚合、推送管理、内部管理，Gin 框架路由

## 技术栈
Go · Gin（Web 框架）· GORM · PostgreSQL · Cassandra · Redis

## 关联
- [`opensourceways/message-collect`](../../projects/opensourceways/message-collect/) — 消息采集上游
- [`opensourceways/message-push`](../../projects/opensourceways/message-push/) — 消息推送下游
- [`opensourceways/forum-reply-robot`](../../projects/opensourceways/forum-reply-robot/) — 论坛消息源

## 开放问题
- [ ] 2026-06-30 消息去重和聚合策略是否可以公开为配置项？
