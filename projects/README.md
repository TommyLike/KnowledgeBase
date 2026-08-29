# 项目知识地图（MOC）

> 自底向上软件栈。每层一张导览页；查找/联想优先走本页 + `config/index/by-tag.json`（多标签）+ `by-layer.json`（语义层）+ 各 summary.md 的类型化「关联」节。

```
┌─ 80-workflow  工作流 / 消息      （编排可靠性）
│  70-data      数据 / 向量库      （长期记忆）
│  60-agent     智能体层          ← Agent 主战场
│  50-framework 框架层            ← 训练/推理/RL 主战场
│  40-runtime   运行时 / 容器 / 沙箱
│  30-cluster   集群 / 云原生
└─ 10-compiler  编译器与代码生成   （最接近芯片）
```

| 层 | 领域 | 项目 | 导览 |
|----|------|-----:|------|
| **10-compiler** 编译器与代码生成 | 编译器 | 11 | [→](10-compiler/README.md) |
| **30-cluster** 集群 / 云原生 | 集群 | 2 | [→](30-cluster/README.md) |
| **40-runtime** 运行时 / 容器 / 沙箱 | 容器 / microVM、Agent 沙箱 | 34 | [→](40-runtime/README.md) |
| **50-framework** 框架层 | 推理引擎、RL 后训练、训练框架 | 85 | [→](50-framework/README.md) |
| **60-agent** 智能体层 | 编码 Agent、框架 / 编排、网关 / 路由、记忆、可观测 / 评测、规划、协议、安全、工具 | 70 | [→](60-agent/README.md) |
| **70-data** 数据 / 向量库 | 向量库 | 7 | [→](70-data/README.md) |
| **80-workflow** 工作流 / 消息 | 工作流 | 7 | [→](80-workflow/README.md) |

> 共 216 个业务项目。团队自有组织（opensourceways/cosdt）不在此库。

## 检索心法
- **按软件层找**：本页表格 → 层 README
- **按主题找**：`config/index/by-tag.json`（tag → 项目+论文）
- **按语义层找**（不依赖物理目录，卫星可跨层标注）：`config/index/by-layer.json`
- **按关系联想**：项目/论文 summary.md 的「关联」节（upstream/alternative/complements…）或 manifest `relations`
- **物理路径**：一律以 `config/index/manifest.json` 的 `path` 为准（key 不变，层次可变）
