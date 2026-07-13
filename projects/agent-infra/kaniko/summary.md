# kaniko
> [`GoogleContainerTools/kaniko`](https://github.com/GoogleContainerTools/kaniko) · 上游贡献
<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-07-13T11:22:48 · Go · ~200 files · 1653n/4650e  
**入口** `cmd/executor/cmd/` (主入口) · `pkg/executor/` (Dockerfile 执行) · `pkg/snapshot/` (用户空间快照)  
**架构** Dockerfile→Snapshot(用户空间逐层执行)→Push(registry)。无Docker daemon依赖。  
**热点** `Run`(×98) · `TakeSnapshot`(×78) · `PushImage`(×56) · `CopyDir`(×42)  
<!-- END AUTO -->

---
## 定位
> Google 的无守护进程容器镜像构建工具。在K8s中用户空间执行Dockerfile，不依赖Docker daemon。已归档但仍是K8s构建标配。
## 项目介绍
> 容器镜像构建生态项目。
## 技术栈
- Go · Docker/OCI
## 关联
> _待补充_
## 开放问题
> _随 delta 追加_
