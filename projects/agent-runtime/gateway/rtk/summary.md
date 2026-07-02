# rtk

> [`rtk-ai/rtk`](https://github.com/rtk-ai/rtk) · 上游贡献 · AI 编码 Agent 的 CLI 输出压缩代理，将 AI 工具调用的 shell 命令输出压缩 60–90%，大幅降低 LLM 上下文消耗与 API 成本

<!-- BEGIN AUTO — 由 /kg-refresh 维护，勿手动改 -->
<!-- END AUTO -->

---

## 定位
> rtk (Rust Token Killer) 是当前 Agent 编码工具链中最关键的基础设施组件之一，解决 AI Agent 频繁执行 shell 命令时输出 Token 消耗过大的痛点。它作为透明代理层插入 Agent 与 shell 之间，在不改变用户工作流的前提下实现巨大成本节约。随着 Claude Code、Cursor、Copilot 等 AI 编码工具在国内团队中逐步落地，rtk 是降低日常使用成本的有效手段，也是团队利用上游开源项目服务内部的典型案例。

## 项目介绍
> **RTK 是一个高性能 CLI 代理，位于 AI 编码 Agent 和系统 shell 之间，智能拦截并压缩命令输出，使 LLM 只看到最精简的上下文，从而将 shell 命令的 Token 消耗降低 60–90%。**

核心场景：
- **Git 操作输出截断**：`git status`、`git diff`、`git log` 等高频命令输出常达数千 Token，rtk 提取统计数据后仅输出摘要，压缩率达 85–99%。
- **测试运行器输出精简**：pytest、cargo test、vitest、playwright、go test 等测试命令只显示失败用例，隐藏通过项，压缩率 90–99%。
- **代码文件读取压缩**：rtk 的文件读取模块支持按语言感知剥离注释（Minimal 模式）和函数体（Aggressive 模式），节省 20–90% Token，支持 Rust、Python、JS/TS、Go、C/C++、Java 六种语言。
- **Linter 输出聚合**：ESLint、ruff、tsc、golangci-lint 等输出按规则 / 文件分组聚合，只显示问题计数和最关键的错误，压缩 80–90%。
- **云平台 CLI 输出优化**：aws、docker、kubectl、psql 等 Cloud 命令输出截断至摘要，压缩 60–80%，防止冗长的 JSON/表格输出塞满 Agent 上下文窗口。

## 技术要点
- **透明代理模式**：rtk 以 CLI 二进制形式运行，不依赖 shell alias 或 LD_PRELOAD 等侵入式机制。Agent 调用命令时，rtk 的 hook 自动将命令重写为 `rtk <原始命令>`，拦截输出后再将压缩结果返回给 Agent。用户可随时通过 `-v` 或 `--verbose` 标志查看原始输出，也可全局关闭 rtk 而不影响任何工作流。
- **六阶段命令生命周期**：每条命令经过 PARSE（Clap 解析器提取命令、参数、标志）→ ROUTE（main.rs 按 Commands 枚举分发至对应模块）→ EXECUTE（`std::process::Command` 执行真实命令）→ FILTER（按命令类型应用压缩策略）→ PRINT（输出带 ANSI 颜色的压缩结果）→ TRACK（写入 SQLite 数据库记录 Token 节省）六个阶段。
- **十二种压缩策略**：统计提取（git status 类，90–99% 压缩）、失败聚焦（测试类，94–99%）、按模式分组（Linter 类，80–90%）、去重计数（日志类，70–85%）、结构提取（JSON 输出只保留 key 和类型，80–95%）、代码过滤（按语言级别剥离注释和函数体，20–90%）、树形压缩（ls/tree 目录结构压缩，50–70%）、进度过滤（去 ANSI 进度条留最终结果，85–95%）、JSON/Text 双模（ruff/pip）、状态机解析（pytest 生命周期跟踪，90%+）、NDJSON 流式处理（go test，90%+）。
- **无异步运行时、单线程阻塞 I/O**：rtk 明确拒绝引入 tokio 等异步运行时，所有 I/O 使用标准的阻塞 `std::process::Command::output()`。启动时间 <10ms，命令代理额外开销 5–15ms。技术决策理由为：异步运行时会增加 5–10ms 启动延迟，而 rtk 的核心场景不需要并发，单线程阻塞 I/O 足够高效且易于调试。
- **失败安全与退出码透传**：任何过滤模块崩溃或异常时，rtk 自动回退到原始输出，保证底层命令不会被阻塞。退出码严格透传，CI/CD 管线中行为与不安装 rtk 时完全一致。任何 rtk 未知的命令直接透传，零干扰。
- **Hook 引擎双模式**：Auto-Rewrite 模式（默认）100% 采用率，在 bash 工具调用前静默重写命令为 rtk 代理形式；Suggest 模式非侵入式，通过 systemMessage 提示 Agent 使用 rtk，采纳率约 70–85%，适合学习阶段或审计场景。Hook 引擎 v2 用 Rust 重写了此前基于 shell script 的实现，支持流式输出、多 handler 协调和健壮的 stderr / 退出码处理。
- **本地 SQLite Token 追踪**：所有压缩后的命令输出均记录在 `~/.local/share/rtk/history.db` 中，保留 90 天。`rtk gain` 命令提供全量 Token 节省分析面板，`rtk session` 查看单次会话效果，`rtk discover` 分析 Claude Code 命令历史发现遗漏的节省机会。
- **Tee 恢复机制**：当命令失败时，rtk 保存完整的未过滤输出，Agent 可通过 tee 机制获取原始错误信息，避免因输出被过滤而遗失关键错误上下文，同时仍然享受日常成功场景的压缩收益。
- **42 个命令模块覆盖 8 大生态**：Git（status/diff/log/gh）、Rust（cargo test/build/clippy）、JS/TS（lint/tsc/next/vitest/playwright/pnpm）、Python（ruff/pytest/mypy/pip）、Go（test/build/vet/golangci-lint）、Ruby（rake/rspec/rubocop）、.NET（dotnet build/test/binlog）、Cloud（aws/docker/kubectl/curl/psql）和 System（ls/tree/read/grep/find/json），覆盖 AI Agent 编码中几乎所有高频 CLI 工具。
- **声明式 TOML 过滤器**：对于规则性强的行级输出场景，rtk 支持声明式 TOML 格式定义过滤规则，在编译期内嵌，无需为每个新命令编写 Rust 模块，降低了社区贡献的实现门槛。

## 技术栈
Rust (93.1%), Shell (4.6%), TypeScript (1.5%), SQLite (rusqlite), Clap, serde, regex, Rust 标准库 I/O

## 关联
- 上游无硬依赖：rtk 是独立的 Rust 静态链接二进制，不依赖任何第三方运行时或守护进程
- 生态集成：支持 Claude Code、Cursor、Windsurf、Cline/Roo Code、Gemini CLI、OpenCode、Pi Coding Agent、Copilot、Codex、Qoder 等 14 种 AI 编码工具的 hook 集成

## 开放问题
- [ ] 2026-07-02 rtk 的 Hook 引擎 v2 已从 shell script 迁移到 Rust，但在企业级 CI/CD 场景中是否已充分验证与各类沙箱 / 容器运行时（如 Docker exec、K8s pod exec）的兼容性？
- [ ] 2026-07-02 rtk 的 TOML 声明式过滤器为社区贡献提供了低门槛入口，国内团队是否已将常见的中文 / 国产开发工具（如 Alibaba Cloud CLI、华为云 CLI、内部 CI 工具）的过滤规则贡献回流上游？
- [ ] 2026-07-02 rtk 的 Token 节省数据（约 80% 平均节省率）在基于 Claude Opus / Sonnet 等高价模型的编码场景中，实际 API 成本节约是否有定量分析和 ROI 报告？这对团队预算规划有直接参考价值。
