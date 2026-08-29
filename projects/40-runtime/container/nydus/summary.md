# nydus
> [`dragonflyoss/nydus`](https://github.com/dragonflyoss/nydus) · 上游贡献
<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · 2026-07-13T11:22:48 · Rust+Go · ~800 files · 10408n/45163e  
**入口** `src/bin/nydusd/` (FUSE daemon) · `src/bin/nydus-image/` (镜像构建) · `contrib/nydus-snapshotter/` (containerd集成)  
**架构** OCI Image→nydus-image(Rafs转换)→Registry→nydus-snapshotter→nydusd(FUSE mount)→容器运行时按需读取  
**热点** `read`(×421) · `mount`(×312) · `convert`(×289) · `chunk`(×204)  
<!-- END AUTO -->

---
## 定位
> 蚂蚁开源的容器镜像懒加载方案。Rafs文件系统+块级去重+按需加载。AI推理大镜像冷启动的核心优化方案。
## 项目介绍
> 容器镜像构建生态项目。
## 技术栈
- Go · Docker/OCI
## 关联
> _待补充_
## 开放问题
> _随 delta 追加_
