# agentcore-cli

> [`aws/agentcore-cli`](https://github.com/aws/agentcore-cli) · 上游贡献 · AWS Bedrock AgentCore 的新一代命令行工具，为 Agent 开发者提供本地开发到云端部署的全流程 CLI 体验

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> AgentCore CLI 是 AWS Bedrock AgentCore 的官方命令行工具，作为 AgentCore 平台的主要交互入口。在 Agent 运行时生态中，AgentCore CLI 是 AWS 托管 Agent 运行时的开发者体验层。

## 项目介绍
> **AWS AgentCore 的命令行入口——本地开发、云端部署、Agent 生命周期管理的一条命令体验。**

核心场景：
- **Agent 本地开发与测试**：`agentcore dev` 本地运行和调试 Agent
- **一键云端部署**：`agentcore deploy` 将 Agent 部署到 AWS Bedrock AgentCore
- **Agent 生命周期管理**：创建/更新/删除/监控云上 Agent 实例

## 技术要点
- **TypeScript 实现**：Node.js 生态 CLI 工具
- **与 AgentCore SDK 集成**：CLI 内部调用 Bedrock AgentCore API
- **TypeScript 开发者友好**：针对 JS/TS 生态 Agent 开发者优化

## 技术栈
TypeScript, Node.js, AWS Bedrock SDK, Apache 2.0

## 关联
- [`aws/bedrock-agentcore-starter-toolkit`](../bedrock-agentcore-starter-toolkit/) — 旧版 CLI 工具包
- [`awslabs/agentcore-samples`](../../awslabs/agentcore-samples/) — AgentCore 示例集
- [AWS Bedrock](https://aws.amazon.com/bedrock/) — 托管 AI 平台

## 开放问题
- [ ] 2026-07-05 AgentCore CLI 是否支持非 AWS 环境的 Agent 部署？还是完全锁定 AWS 生态？
