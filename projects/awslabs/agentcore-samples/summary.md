# agentcore-samples

> 快照: 无 | 入口: 无 | 架构: 无 | 热点: 无

<!-- BEGIN AUTO -->
<!-- END AUTO -->

## 定位

Amazon Bedrock Agentcore 的官方示例和参考实现仓库，由 AWS 实验室（awslabs）维护。展示如何利用 Bedrock Agentcore 平台将 AI Agent 从原型加速推向生产环境。团队以**上游贡献**方式参与，关注 Agent 运行时沙箱的行业实践和 AWS 生态的演进方向。

## 项目介绍

Amazon Bedrock Agentcore 是 AWS 推出的 AI Agent 生产化平台，提供安全的沙箱运行时环境，让开发者能够在隔离的、可治理的环境中构建、测试和部署 AI Agent。agentcore-samples 汇集了平台的最佳实践示例，覆盖多场景的 Agent 构建模式。

## 核心场景

- **代码执行沙箱**：在隔离的运行时环境中安全执行 AI 生成的代码，防止恶意代码影响宿主系统
- **多工具 Agent 编排**：Agent 调用外部 API、数据库、文件系统等多种工具的复杂工作流示例
- **可观测性与治理**：Agent 执行过程的日志、监控、审计和合规性追踪
- **企业级部署**：将 Agent 集成到现有 AWS 基础设施（IAM、VPC、CloudWatch 等）的生产级参考架构

## 技术要点

- **安全隔离**：基于 Firecracker microVM 的轻量级沙箱，提供接近容器的启动速度和虚拟机的安全边界
- **生命周期管理**：Agent 实例的创建、挂载、快照、恢复和销毁的完整生命周期控制
- **工具集成框架**：标准化的 Agent 工具注册和调用机制，支持 HTTP API、SDK、CLI 等多种工具形态
- **上下文注入**：运行时向沙箱注入文件系统挂载、环境变量、密钥等上下文信息的机制
- **会话持久化**：支持 Agent 执行状态和文件系统的快照保存与跨会话恢复
- **流式响应**：Agent 执行过程中实时流式返回中间结果和最终输出的传输层协议

## 技术栈

Python / TypeScript | AWS CDK / CloudFormation | Docker / Firecracker | Amazon Bedrock | AWS Lambda / ECS | IAM / VPC / CloudWatch

## 关联

- 上游: `aws/bedrock-agentcore`（核心平台服务，非开源）
- 相关项目: `aws-samples/bedrock-agent-samples`（Bedrock Agent 通用示例）
- 生态: Anthropic Claude、LangChain、CrewAI 等 Agent 框架与 Bedrock Agentcore 的集成示例

## 开放问题

- Agentcore 的沙箱隔离级别与 gVisor/Firecracker 自建方案的对比如何？
- 平台当前的沙箱冷启动延迟在什么量级，是否有预热优化？
- 多 Agent 协作场景下沙箱间通信的安全性如何保障？
