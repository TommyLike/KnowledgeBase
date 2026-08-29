# liqo

> [`liqotech/liqo`](https://github.com/liqotech/liqo) · 上游贡献 · 动态 Kubernetes 多集群拓扑平台

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `5119476` · Go · 1543文件/18MB · 8,460n/27,413e  
**入口** `cmd/liqo-controller-manager`, `cmd/virtual-kubelet`, `cmd/liqoctl`, `cmd/gateway`  
**架构** 多组件 K8s Operator 模式：controller-manager（对等协商/网络/卸载） + virtual-kubelet（远程集群虚拟化为本地节点） + gateway（跨集群隧道） + fabric（网络连通） + ipam（IP 管理）  
**热点** `pkg/utils`(×623) · `pkg/liqo-controller-manager`(×572) · `pkg/virtualKubelet`(×88)
<!-- END AUTO -->

---

## 定位
> 上游关注的 Kubernetes 多集群调度方案。Liqo 以 Virtual Kubelet + 对等协商方式实现集群间动态资源共享，适合快速搭建多云/混合云拓扑。与 Karmada 同属多云调度领域但技术路线不同。

## 项目介绍
> 通过 Virtual Kubelet 将远程集群抽象为本地虚拟节点，Pod 无需改造即可被调度到远程集群运行。
> 核心场景：(1) 集群间动态资源共享——以 P2P 方式协商资源消费关系，(2) 透明跨集群网络——Pod-to-Pod 和 Service 连通无需管理 CNI，(3) 有状态应用跨集群运行——支持数据引力模型和跨集群存储。

## 技术要点
- Virtual Kubelet 虚拟节点：远程集群映射为本地 K8s Node，标准 K8s 调度器即可使用
- 自动 Peering：无需手动配置 VPN/CA，集群间自动协商信任关系
- 网络 Fabric + Gateway：Geneve/WireGuard 隧道实现跨集群透明通信，独立于底层 CNI
- 存储 Fabric：数据引力模型支持有状态应用远程执行
- Namespace 级卸载策略：按 namespace 配置 offloading 策略和目标集群
- 多 Provider 支持：GKE/AKS/EKS/OpenShift

## 技术栈
- Go
- Kubernetes Operator (controller-runtime)
- Virtual Kubelet
- Geneve / WireGuard 隧道
- gRPC (IPAM)

## 关联
- [`karmada-io/karmada`](../karmada/) — 同领域竞品，集中式控制面调度方案
- Kubernetes SIG Multicluster — 上游 K8s 多集群标准化工作

## 开放问题
> _随 delta 追加_
