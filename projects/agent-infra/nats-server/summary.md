# nats-server

> [`nats-io/nats-server`](https://github.com/nats-io/nats-server) · 上游贡献 · CNCF 毕业项目，Go 实现的云原生高性能消息中间件，内置 JetStream 持久化流处理

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> NATS Server 是 CNCF 首个毕业级消息中间件，在 Agent 基础设施生态中扮演轻量级通信骨干角色。团队将其作为云原生微服务间的默认消息总线进行上游跟踪，关注其 JetStream 持久化能力在 Agent 工作流状态传递、多 Agent 协同通信中的应用潜力。NATS 的零外部依赖、单二进制部署特性使其在边缘 Agent 场景中具有显著优势。

## 项目介绍
> **NATS Server 是一个用 Go 编写的云原生高性能消息系统，以极简运维和极小资源消耗支撑从边缘设备到超大规模云集群的分布式通信。**

核心场景：
- **微服务间异步通信**：作为服务网格的消息总线，通过 Subject-Based Pub/Sub 实现服务间松耦合异步通信，支持请求-回复（Request-Reply）模式实现 RPC 语义，可替代 gRPC 直连的服务发现和负载均衡
- **持久化消息队列与事件流**：通过内置 JetStream 层提供「至少一次」和「恰好一次」投递保证，支持消息重放、流式处理、工作队列（WorkQueue）等场景，可作为 Kafka/Redis Streams 的轻量替代
- **边缘/IoT 与云端统一通信**：通过 Leaf Node 和 Gateway 架构，在边缘端运行轻量 NATS 实例，经 Leaf Node 安全接入中心集群，实现云端-边缘的跨网络统一消息路由
- **分布式 Key-Value 与 Object Store**：基于 JetStream 构建内建的 KV Store 和 Object Store，为分布式配置共享、Leader 选举、服务发现提供开箱即用的基础能力，无需额外部署 etcd/Consul
- **多租户隔离平台**：通过 Account 和 JWT 的层级化安全模型，在同一集群中实现不同团队/应用的完全隔离，支持导入/导出约束实现受控的跨账户服务暴露

## 技术要点
- **分层架构（Core + JetStream）**：Core NATS 负责轻量级 Pub/Sub（at-most-once），无持久化、无共识协议，消息到达时无订阅者直接丢弃；JetStream 是内建分布式持久化层，提供 Stream、Consumer、ACK 跟踪语义，两套功能集成在同一二进制中，按需启用
- **Subject-Based 层级寻址**：消息不发送到队列名，而是发送到层级化主题（如 `orders.us.east`），订阅者使用通配符 `*`（单级匹配）和 `>`（多级匹配）进行灵活过滤，这种设计天然支持消息多播和动态路由
- **基于 Raft 的 JetStream 集群**：三类 Raft 组各自独立运行——Meta Group 负责 JetStream API 和资源管理元数据，Stream Group 负责消息数据复制（per-stream），Consumer Group 跟踪消费者位置和确认状态，raft 与数据面流量复用同一通信层，无外部依赖
- **Gateway / Leaf Node / SuperCluster 三层拓扑**：Gateway 连接独立集群实现跨区域消息路由（最终一致）；Leaf Node 将集群扩展到边缘端，支持双向 TLS 认证；SuperCluster 结合两者实现大规模多区域全域部署
- **JWT + Account 去中心化安全模型**：Account 定义命名空间和用户操作限制，JWT 由外部签发服务（nsc）生成，nats-server 仅做零信任验证，支持导入/导出约束精确控制跨账户间的服务可见性和数据流向
- **双重投递语义保证**：JetStream Consumer 持久化跟踪每条消息的 ACK 状态，支持双窗口去重实现 exactly-once 语义，Consumer 同时提供 push（服务器主动推送，适合低延迟场景）和 pull（客户端按需拉取，适合批处理/流量控制）两种消费模式
- **零外部依赖的单二进制部署**：JetStream 持久化存储、Raft 分布式共识和 TLS 安全通信全部自包含在单个 nats-server 二进制中，不需要 ZooKeeper、etcd 或外部数据库，启动即可组建集群
- **极高吞吐与极简协议**：单节点可处理数百万 msg/s，协议为纯文本控制命令（CONNECT/PUB/SUB/UNSUB/MSG）辅以二进制长度前缀的数据体，TCP 多路复用和零拷贝优化，最小化内核上下文切换开销

## 技术栈
Go, Go Modules, GoReleaser, Docker, Helm, 自定义文本协议, 自研文件存储引擎, Raft, TLS, JWT

## 关联
- [`agent-infra/temporal`](../temporal/summary.md) — Temporal 内部使用消息队列进行 Worker 调度，NATS 可作为其轻量级传输层的替代方案
- [`agent-infra/restate`](../restate/summary.md) — Restate 是事件驱动的持久执行引擎，NATS JetStream 可作为其持久化事件日志的底层传输
- [`agent-infra/redpanda`](../redpanda/summary.md) — Redpanda 是 Kafka 兼容的流处理平台，与 NATS JetStream 在持久化事件流场景中互为竞品
- [`agent-infra/inngest`](../inngest/summary.md) — Inngest 是事件驱动的持久函数框架，依赖消息队列实现可靠的事件投递，NATS 可成为其消息传输后端

## 开放问题
- [ ] 2026-07-02 JetStream 的 exactly-once 语义在跨 Leaf Node 场景下是否依然保证？边缘断连恢复后的消息去重策略是什么？
