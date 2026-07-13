# 容器镜像构建生态全景分析

> [Archived] 2026-07-13 | 来源: 生态调研
> 涉及: 6 projects (buildkit/kaniko/nydus/dive/stargz/slim) + 3 papers (CBuild/FlacIO/2DFS)
> 本页为时间点快照，知识可能已过时。

## 核心结论

容器镜像构建已从"docker build"的单一模式演化为一个**多层次的工具生态**，可以分为 5 个子方向：构建引擎、构建加速、懒加载、镜像优化、供应链安全。团队因 ascend-ci（buildkitd 运维）和 AI 推理（大镜像冷启动）直接参与了其中 3 个方向。

## 生态全景图

```
容器镜像构建生态 (2025)

① 镜像构建引擎
  BuildKit(9.8k⭐)→LLB图编译+并发DAG+docker buildx默认后端
  Kaniko(15.7k⭐)→K8s无守护进程构建(已归档但仍是标配)
  Buildah(7.5k⭐)→OCI标准构建, podman build后端

② 构建加速与缓存
  BuildKit remote cache→registry/S3/Azure/GHA多后端缓存
  CBuild(2025)→跨节点文件级缓存, 15.3×加速
  2DFS(2025)→ML参数从FS解耦, 56×构建加速

③ 懒加载/按需拉取 ← 团队直接相关
  Nydus(2.5k⭐)→Rafs FS+块级去重, AI推理镜像懒加载首选
  stargz-snapshotter(2.6k⭐)→eStargz+OCI兼容, containerd主线
  overlaybd(1.0k⭐)→块级延迟拉取
  FlacIO(FAST'25)→运行时镜像+RTPC, 4.6×冷启动加速

④ 镜像优化
  dive(48k⭐)→分层可视化分析, 效率评分
  SlimToolkit(23k⭐)→运行时分析→自动瘦身(Go:448×)
  distroless(19k⭐)→最小化安全基础镜像

⑤ 供应链安全
  cosign(4.5k⭐)→镜像签名与验证(Sigstore)
  Syft(6.5k⭐)→SBOM生成
  Grype(9k⭐)→漏洞扫描
```

## 新增项目代码规模

| 项目 | 代码规模 | 语言 | 架构 |
|------|---------|------|------|
| buildkit | 12,008n/71,562e | Go | Client(gRPC)→Solver(LLB DAG)→Worker→Exporter |
| kaniko | 1,653n/4,650e | Go | Dockerfile→Snapshot(用户空间)→Push |
| nydus | 10,408n/45,163e | Rust+Go | OCI→Rafs转换→FUSE mount→按需read |
| dive | 1,233n/4,143e | Go | CLI→Image Analyzer(Layer Diff)→TUI |
| stargz-snapshotter | 3,063n/10,657e | Go | eStargz Layer→TOC→FUSE→range fetch |
| slim | 4,666n/13,593e | Go | CLI→sensor(运行时trace)→Minify→Profile |

## 关键论文

| 论文 | 会议 | 要点 |
|------|------|------|
| CBuild | IEEE TC 2025 | 跨节点文件级缓存，15.3×构建加速，80%减少下载 |
| FlacIO | FAST 2025, 华为 | 运行时镜像+RTPC，4.6×冷启动加速 |
| 2DFS | ATC 2025 | 2D文件系统解耦ML参数，56×构建加速 |

## 团队相关

- **ascend-ci-deployment**: 大量使用 buildkitd 做 CI 构建（上周占 22/36 PRs）
- **backlog 003**: 使用 Kaniko 替代 Docker daemon 构建
- **AI 推理**: Nydus/FlacIO 的懒加载和冷启动优化直接与 GPU 推理服务相关

## 来源

- [moby/buildkit](https://github.com/moby/buildkit) · [kaniko](https://github.com/GoogleContainerTools/kaniko) · [nydus](https://github.com/dragonflyoss/nydus)
- [dive](https://github.com/wagoodman/dive) · [stargz-snapshotter](https://github.com/containerd/stargz-snapshotter) · [slim](https://github.com/slimtoolkit/slim)
- CBuild (IEEE TC 2025) · FlacIO (FAST 2025) · 2DFS (ATC 2025)
