# Repo 本地管理策略

## 设计原则

- **本地保留代码，远端只存引用**：`projects/*/repo/` 已加入 `.gitignore`，不会被 git 追踪
- **clone 状态追踪**：每个项目的 `state.json` 中 `repo` 字段记录 clone 信息和最后已知 commit
- **按需 clone**：不批量 clone，由 `/kg-refresh` 或 `/kg-deep` 按需触发

## state.json 中的 repo 字段

```json
{
  "key": "opensourceways--cora",
  "repo": {
    "cloned": false,
    "clone_url": null,
    "last_commit": null,
    "last_indexed": null
  }
}
```

## 工作流

### 首次 clone & 索引
```
/kg-refresh <key>    # agent 自动 clone → code-memory index → 更新 state.json
```

### 后续同步
```
/kg-delta <key>      # agent 拉取最新代码 → 检查 PR delta → 生成 digest
```

### 深度探索
```
cd projects/<key>/repo && claude    # 手动 cd 进入项目目录
> /kg-deep <key>
```

## 清理策略
- 超过 30 天未访问的 repo clone 可被清理（保留 `projects/<key>/` 目录和所有 meta 文件）
- 清理后 state.json 的 `repo.cloned` 置为 false
