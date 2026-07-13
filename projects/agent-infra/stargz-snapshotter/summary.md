# stargz-snapshotter
> [`containerd/stargz-snapshotter`](https://github.com/containerd/stargz-snapshotter) · 上游贡献
<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-07-13T11:22:48 · Go · ~200 files · 3063n/10657e  
**入口** `cmd/containerd-stargz-grpc/` (containerd plugin) · `estargz/` (eStargz格式) · `fs/` (FUSE文件系统)  
**架构** OCI Layer(eStargz)→TOC解析→FUSE mount→按需fetch(range request)→容器运行中逐步拉取  
**热点** `ReadAt`(×203) · `Resolve`(×178) · `Prefetch`(×134) · `Mount`(×98)  
<!-- END AUTO -->

---
## 定位
> containerd 的 eStargz 延迟拉取方案。OCI兼容+内置TOC索引+按需fetch。已合并到containerd主线。Nydus的对标方案。
## 项目介绍
> 容器镜像构建生态项目。
## 技术栈
- Go · Docker/OCI
## 关联
> _待补充_
## 开放问题
> _随 delta 追加_
