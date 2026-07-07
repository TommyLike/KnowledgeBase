# sandbox-sdk

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

Cloudflare Sandbox SDK 是 Cloudflare 开源的边缘沙箱运行环境方案，团队以**上游贡献**方式参与。该 SDK 允许开发者在 Cloudflare 全球边缘网络上创建和运行隔离的代码沙箱环境，将代码执行从传统中心化服务器推向靠近用户的边缘节点。

## 项目介绍

Cloudflare Sandbox SDK 提供了一套在边缘网络上运行沙箱化代码环境的工具和 API。核心场景：让 AI Agent 在不安全代码执行场景（如运行用户生成的 Python 脚本、动态插件系统、可编程数据处理管线）中，将代码隔离到 Cloudflare Workers 的边缘沙箱中执行，结合 Cloudflare 的全球节点实现低延迟、高安全性的代码执行体验。

## 核心场景

- **AI Agent 代码执行隔离**：Agent 需要运行用户提交的动态代码（如数据分析脚本、模型调用逻辑），通过 Sandbox SDK 将代码在边缘沙箱中安全执行，防止逃逸和资源滥用。
- **多租户 SaaS 插件系统**：SaaS 平台允许用户上传自定义代码插件，每个插件在独立沙箱中运行，互不干扰，满足多租户隔离需求。
- **边缘数据处理管线**：在靠近数据源的位置执行数据过滤、转换、聚合逻辑，减少中心服务器带宽消耗和延迟。
- **教育与在线评测**：在线编程教育平台或技术面试系统，用户在浏览器中编写代码，后端通过 Sandbox SDK 在隔离环境中编译运行并返回结果。

## 技术要点

- **基于 Cloudflare Workers 运行时**：利用 Workers 的 V8 隔离（isolates）机制实现进程级安全隔离，每个沙箱实例运行在独立的 isolate 中，启动延迟极低（毫秒级）。
- **边缘全球化部署**：沙箱实例自动分布到 Cloudflare 全球 330+ 边缘节点，用户代码在距离用户最近的 PoP 执行，端到端延迟通常低于 50ms。
- **资源配额与限流**：支持 CPU 时间、内存上限、执行超时、网络出口等细粒度资源限制，防止单个沙箱耗尽节点资源。
- **文件系统抽象**：提供虚拟文件系统接口，沙箱内代码可以读写隔离的文件存储空间，不与宿主环境和其他沙箱共享。
- **网络策略控制**：可配置沙箱出站网络规则（允许/禁止访问的外部域名和 IP 范围），适用于需要联网但需防数据外泄的场景。
- **RESTful API + WebSocket**：支持 HTTP 请求式执行和 WebSocket 双向实时通信，满足短任务和长连接交互两种模式。

## 技术栈

- **运行环境**：Cloudflare Workers (V8 Isolates)
- **开发语言**：TypeScript / JavaScript
- **沙箱语言**：支持 WebAssembly 子集（可通过编译链支持多种语言）
- **协议**：REST + WebSocket
- **部署**：Cloudflare 全球边缘网络

## 关联

- **上游**：Cloudflare Workers 平台（运行时基础）
- **同类项目**：Fly.io Machines、AWS Lambda (隔离粒度为容器/VM)、Modal (Python 沙箱)、E2B (AI Agent 代码执行沙箱)
- **竞争对比**：与 E2B 相比，Sandbox SDK 更侧重于边缘部署和 Cloudflare 生态集成；与 Modal 相比，Sandbox SDK 的抽象层级更低，面向 SDK 集成而非 PaaS 平台

## 开放问题

- Sandbox SDK 的安全隔离边界是否经过第三方审计？V8 isolate 级别的隔离是否足以防御恶意代码攻击？
- 支持的沙箱内语言是否已扩展到 Python（通过 WebAssembly 编译链或其他方式）？与 E2B 和 Modal 的 Python 原生支持相比差距多大？
- 沙箱间通信（inter-sandbox communication）的支持程度如何？是否存在消息队列或共享内存模式？
- 存储持久化机制如何？沙箱销毁后文件系统数据是否可保留？是否有与 Cloudflare R2/KV 的集成接口？
- 开源社区活跃度如何？是否有非 Cloudflare 外部团队在生产环境中使用？
- Cloudflare 是否会将其作为独立产品线持续投入，还是仅作为内部工具？商业化路径是否清晰？
