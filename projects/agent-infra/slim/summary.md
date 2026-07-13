# slim
> [`slimtoolkit/slim`](https://github.com/slimtoolkit/slim) · 上游贡献
<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-07-13T11:22:48 · Go · ~350 files · 4666n/13593e  
**入口** `cmd/slim/` (CLI) · `cmd/slim-sensor/` (运行时探针) · `pkg/app/master/` (构建编排)  
**架构** CLI→Container Inspect→slim-sensor(运行时分析+syscall追踪)→Minify(瘦身)→Seccomp/AppArmor生成  
**热点** `OnEvent`(×187) · `Minify`(×156) · `Monitor`(×123) · `GenerateProfile`(×89)  
<!-- END AUTO -->

---
## 定位
> CNCF沙箱项目。运行时分析自动瘦身容器镜像(23k stars)。Go:700MB→1.56MB(448×)。自动生成Seccomp/AppArmor策略。
## 项目介绍
> 容器镜像构建生态项目。
## 技术栈
- Go · Docker/OCI
## 关联
> _待补充_
## 开放问题
> _随 delta 追加_
