# buildkit
> [`moby/buildkit`](https://github.com/moby/buildkit) · 上游贡献
<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-07-13T11:22:48 · Go · ~1400 files · 12008n/71562e  
**入口** `cmd/buildkitd/` (daemon) · `cmd/buildctl/` (CLI) · `frontend/dockerfile/` (Dockerfile→LLB)  
**架构** Client(gRPC)→BuildKitd→Solver(LLB DAG)→Worker(containerd/OCI)→Exporter(image/local)  
**热点** `solve`(×562) · `ResolveOp`(×344) · `CacheMap`(×221) · `snapshot`(×189)  
<!-- END AUTO -->

---
## 定位
> Docker/Moby 的下一代镜像构建引擎。LLB图编译+并发DAG执行+可插拔frontend/worker/cache。docker buildx默认后端。
## 项目介绍
> 容器镜像构建生态项目。
## 技术栈
- Go · Docker/OCI
## 关联
> _待补充_
## 开放问题
> _随 delta 追加_
