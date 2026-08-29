# karmada

> [`karmada-io/karmada`](https://github.com/karmada-io/karmada) · 上游贡献 · CNCF 孵化项目 · 开放多集群 Kubernetes 编排系统

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
**快照** · commit `ffbade9` · Go · 11,622文件/181MB · 12,211n/56,653e  
**入口** `cmd/controller-manager`, `cmd/scheduler`, `cmd/karmadactl`, `cmd/aggregated-apiserver`, `cmd/karmada-search`, `cmd/descheduler`  
**架构** 集中式控制面：API Server → Controller Manager（集群/策略/绑定/执行） → Scheduler（多集群调度决策） → Agent（成员集群执行）。Operator 简化部署，karmadactl 提供 CLI 管理  
**热点** `pkg/util`(×1646) · `pkg/controllers`(×1463) · `pkg/search`(×428) · `pkg/scheduler`(×137)
<!-- END AUTO -->

---

## 定位
> 上游关注的 Kubernetes 多集群管理系统，CNCF 孵化项目。Karmada 以集中式控制面 + 声明式策略方式管理跨集群工作负载分发，提供完整的调度、故障转移、自动伸缩能力。相比 Liqo 的 P2P 虚拟节点路线，Karmada 更接近企业级多集群管理平台。

## 项目介绍
> 开放式多集群 Kubernetes 编排系统，不改应用代码即可实现跨集群调度和容灾。
> 核心场景：(1) 跨集群高可用——跨 Region/AZ/集群/Provider 多维度 HA 部署，(2) 集群资源池化——多集群统一管理和工作负载重平衡，(3) 跨云迁移——自动分配和迁移工作负载避免厂商锁定，(4) 多集群自动伸缩——跨集群 HPA 和 CronHPA。

## 技术要点
- 分离式架构：Resource Template（标准 K8s 资源）+ PropagationPolicy（调度策略）+ OverridePolicy（差异化配置）
- 多维度调度：集群亲和性、多集群拆分、ReplicaScheduling（按权重/比例分发副本）
- 完整控制器矩阵：binding/execution/status/gracefuleviction/applicationfailover/workloadrebalancer 等 15+ 控制器
- 资源解释器框架：可扩展的 ResourceInterpreter，默认支持 Deployment/Service/Ingress 等原生 K8s 类型
- FederatedHPA + CronFederatedHPA：跨集群自动伸缩
- MultiClusterService：跨集群服务发现和负载均衡
- Operator 模式部署：内置 Operator 简化控制面安装和升级
- 与 K8s API 完全兼容：零修改迁移，kubectl 直接可用

## 技术栈
- Go
- Kubernetes API Server / Controller Runtime
- etcd
- CRD + Controller 模式（15+ 控制器）
- karmadactl CLI（类似 kubectl）

## 关联
- [`liqotech/liqo`](../liqo/) — 同领域竞品，P2P 虚拟节点调度方案
- [CNCF Sandbox (2023)](https://www.cncf.io/projects/karmada/) — CNCF 孵化项目
- Kubernetes SIG Multicluster — 上游 K8s 多集群标准化

## 开放问题
> _随 delta 追加_
