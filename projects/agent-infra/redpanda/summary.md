# redpanda

> [`redpanda-data/redpanda`](https://github.com/redpanda-data/redpanda) · 上游贡献 · C++ 重写的 Kafka 协议兼容流式数据平台，单二进制部署、10x 更低延迟

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> Redpanda 是 Apache Kafka 的 C++ 高性能替代品，在 agent-infra 分类中扮演**消息队列与事件流基础设施**的关键角色。团队使用 Kafka 生态（om-kafka 运维管理、kafka-lib 消息库）做数据管道，Redpanda 作为上游关注对象，其架构设计（线程独占、Raft 共识、WASM 内联处理）对理解高性能流式系统演进方向有直接参考价值。当团队评估 Kafka 替代方案或边缘部署场景时，Redpanda 是首要候选。

## 项目介绍
> **Redpanda 是一个与 Apache Kafka 协议完全兼容的流式数据平台，使用 C++ 和 Seastar 异步框架彻底重写，消除了 JVM 和 ZooKeeper 依赖，实现单二进制部署和可预测的低延迟。**

核心场景：
- **实时消息队列与事件流**：作为 Kafka 的即插即用替代品，支撑微服务间异步通信、事件溯源和 CDC（变更数据捕获）。
- **日志与指标采集管道**：接收海量应用日志和系统指标，向下游分析引擎（ClickHouse、Elasticsearch）实时推送。
- **流式 ETL 与数据集成**：通过 Redpanda Connect（基于 Benthos）连接数百种数据源和目标，实现声明式数据搬运和转换。
- **边缘 / 混合云部署**：单二进制零依赖特性使其适合资源受限的边缘节点或 IoT 网关，大幅减少运维复杂度。
- **无状态流处理**：内置 WebAssembly（WASM）内联转换，在 broker 内部直接对消息做过滤、脱敏或格式转换，无需外部处理框架。

## 技术要点
- **C++ + Seastar 异步框架**：采用 thread-per-core 共享无关（shared-nothing）反应器模型，每 CPU 核心独占一个事件循环和一组分区，消除锁竞争和 JVM GC 停顿，实现可预测的 p99 < 10ms 延迟。
- **原生 Raft 共识**：每个分区是独立的 Raft 组，leader 选举和日志复制均通过 Raft 实现。元数据管理内嵌于 broker 节点中，无需 ZooKeeper 或 KRaft 独立控制器，自动完成 leader 和分区重平衡。
- **Kafka 线协议兼容**：原生实现 Kafka wire protocol，现有 Kafka 客户端无需修改代码即可接入。内置 Schema Registry，兼容 Confluent Schema Registry 协议。
- **分层存储（Tiered Storage）**：支持将冷数据段自动卸载到 S3 / GCS / Azure Blob，降低本地磁盘成本，实现近乎无限的保留期。
- **Redpanda Connect**：收购并集成了 Benthos（Go 语言），提供声明式 YAML 配置驱动的数据管道，支持 200+ 连接器，覆盖主流数据库、消息队列和云服务。
- **内联 WASM 变换**：将 WebAssembly 函数嵌入 broker，在消息路径上直接做低延迟的数据转换，无需部署独立的流处理引擎（如 Kafka Streams 或 Flink）。
- **BSL 许可证模型**：社区版采用 Business Source License 1.1，源码可用但限制作为竞争性托管服务提供；每个版本发布 4 年后自动转为 Apache 2.0。企业版包含分层存储、高级安全和官方支持。

## 技术栈
C++, Seastar, Raft, Bazel, Go (rpk CLI), Go (Redpanda Connect / Benthos), WebAssembly (WASM), Python, Rust, Java, Linux (amd64/arm64)

## 关联
- [`opensourceways/om-kafka`](../opensourceways/om-kafka/summary.md) — 团队 Kafka 运维管理项目，Redpanda 作为 Kafka 替代方案可纳入其运维范围
- [`opensourceways/kafka-lib`](../opensourceways/kafka-lib/summary.md) — 团队 Kafka 消息库，Redpanda 兼容 Kafka 协议，理论上可无缝切换
- [`agent-infra/temporal`](../temporal/summary.md) — 同为 agent-infra 下的工作流引擎，事件驱动架构中 Kafka/Redpanda 常作为 Temporal 的上游消息源
- [`agent-infra/nats-server`](../nats-server/summary.md) — 同为消息与流式基础设施，NATS 侧重轻量级主题推送，Redpanda 侧重持久化日志存储，两者互补
- Apache Kafka — Redpanda 的直接替代对象和协议兼容目标
- Apache Pulsar — Kafka 竞品，架构差异较大（多租户 BookKeeper 存储层）
- WarpStream (Confluent) — 零运维 Kafka 兼容方案，基于 BYOC S3 架构，与 Redpanda 在简化运维方向上形成竞争
- Benthos (已收购) — Redpanda Connect 的上游，声明式数据管道引擎
- Seastar — C++ 异步引擎，Redpanda 的运行时基础框架

## 开放问题
- [ ] 2026-07-02 Redpanda 的 WASM 内联变换在复杂数据处理场景下（join、窗口聚合）的性能上限如何？是否仍需要外部流处理引擎配合？
- [ ] 2026-07-02 BSL 许可证是否会成为团队内部使用的障碍？当前团队使用场景（om-kafka 管理、kafka-lib 消息库）是否属于许可证豁免范围？
- [ ] 2026-07-02 Redpanda Connect 与 Kafka Connect 生态的兼容性如何？现有 Kafka Connect 插件能否直接迁移到 Redpanda Connect？

