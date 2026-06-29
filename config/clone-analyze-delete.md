# clone-analyze-delete 工作流

## 目标
对每个项目执行"clone → codebase-memory 索引 → 生成 summary → 记录 commit → 删除 repo"，
保留分析数据（codebase.db + summary.md），释放磁盘空间。

## 为什么记录 commit
- state.json 中的 `repo.last_commit` 是后续 `/kg-delta` 的基准点
- delta 时：重新 clone → `git log <last_commit>..HEAD` → 找到新 merged PR
- 如果 commit 为空，delta 从 repo 创建时间开始扫描

## 工作流步骤

### Step 1: Clone
```bash
git clone --depth 1 <url> projects/<key>/repo/
```

### Step 2: Index
```
mcp__codebase-memory-mcp__index_repository(repo_path, project, mode="moderate")
```

### Step 3: Analyze & Summarize
```
mcp__codebase-memory-mcp__get_architecture(project, aspects=["all"])
→ 写入 projects/<key>/summary.md（中文）
```

### Step 4: Record
```json
// state.json
{
  "repo": {
    "cloned": true,
    "clone_url": "<url>",
    "last_commit": "<sha>",
    "last_indexed": "<iso8601>"
  },
  "last_refresh": "<iso8601>",
  "codebase_stats": { "nodes": N, "edges": M }
}
```

### Step 5: Delete repo
```bash
rm -rf projects/<key>/repo/
# state.json: repo.cloned = false
```
> codebase.db 由 MCP server 集中存储，删除 repo 不影响已索引数据。

## Delta 基准
执行 `/kg-delta <key>` 时：
1. 检查 state.json → repo.last_commit
2. 重新 clone repo（非 --depth 1，需完整历史）
3. `git log <last_commit>..HEAD --merges` 找 merged PR
4. 对比 diff 生成 digest
5. 更新 last_commit 为最新 HEAD
6. 删除 repo

## 批量策略
- 每批 10-20 个仓库
- 优先索引：bot（核心）、infra（基础）、backend（服务）
- 代码量大的仓库（>50MB）酌情跳过
