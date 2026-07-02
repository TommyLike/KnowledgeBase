# cora

> [`opensourceways/cora`](https://github.com/opensourceways/cora) · 团队主导 · 开源社区统一命令行工具

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `?` · Go · 1,762n  
**入口** `cmd/cora/main.go` · `cmd/smoke/main.go`  
**架构** CLI → config → spec(OpenAPI) → builder → executor → view → smoke → auth  
**热点** log.Error(×35) · executor.New(×31) · view.NewRegistry(×17)  
<!-- END AUTO -->

---

## 定位
> 开源社区服务的统一命令行工具（Community Collaboration CLI）。通过单一二进制文件，用统一的 `cora <服务> <资源> <操作>` 语法访问 GitHub/GitCode/论坛/Jenkins/Etherpad 等社区服务。命令由各后端服务发布的 OpenAPI Spec 动态驱动生成，接入新服务只需一行配置，零代码扩展。团队自主设计开发。

## 项目介绍
> **社区服务 API 的统一 CLI 入口**，告别在浏览器、curl、Postman 之间来回切换。

核心场景：
- **跨平台数据查询**：`cora gitcode issues list --owner my-org --state open` 一行命令查 GitCode Issue
- **脚本和 Agent 友好**：`--format json` 输出可直接 pipe 给 `jq`，stdout/stderr 分离，语义化退出码
- **Smoke 测试**：`cora smoke` 子命令支持声明式的 API 健康检查，适合 CI/CD 集成
- **多平台认证统一**：支持 PAT、OAuth、Basic Auth 等多种认证方式，按服务自动注入

## 技术要点
- **OpenAPI 驱动命令生成**：运行时根据各服务的 OpenAPI 3.0 Spec 动态生成 CLI 命令树，接入新服务零 Go 代码
- **Spec 本地缓存**：Spec 缓存到本地（24h 有效），冷启动无需网络，延迟 < 200ms
- **声明式输出定制**：每个操作可按配置文件定制输出字段和展示方式（table/JSON/YAML）
- **六平台支持**：GitCode(15 API) · GitHub(19) · Discourse Forum(30) · Jenkins(3) · Etherpad(1) · EUR(3)

## 技术栈
Go · Cobra（CLI 框架）· OpenAPI 3.0（Spec 驱动）· YAML（配置/视图定义）· Makefile + Docker

## 关联
- [`opensourceways/infra-common`](../../projects/opensourceways/infra-common/) — 依赖的各服务 API 定义
- 对标：GitHub CLI (`gh`) / GitCode CLI — 但 cora 跨平台统一语法

## 开放问题
- [ ] 2026-06-30 是否考虑增加 MCP Server 模式，让 AI Agent 直接通过 cora 访问社区数据？
