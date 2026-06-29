# cora — 项目摘要
> [https://github.com/opensourceways/cora](https://github.com/opensourceways/cora)

> opensourceways | 开源社区服务统一 CLI 工具，基于 OpenAPI spec 的命令自动生成和 smoke 测试框架
> ? | ? 文件 | commit: 0a4d0367
> Codebase: 1,762 nodes / 4,049 edges

## 入口
cmd/cora/main.go, cmd/smoke/main.go

## 架构
CLI 分层: cmd → config → spec → builder → executor → view → smoke → auth

## 热点模块
log.Error(35), executor.New(31), view.NewRegistry(17), config.Load(16)

## 支持平台
GitHub(15), GitCode(19), Discourse(30), Jenkins(3), Etherpad(1), EUR(3)
