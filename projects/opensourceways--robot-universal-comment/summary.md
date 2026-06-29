# robot-universal-comment — 项目摘要
> [https://github.com/opensourceways/robot-universal-comment](https://github.com/opensourceways/robot-universal-comment)

> opensourceways | 多平台 PR 评论统一处理微服务，适配器模式支持三平台
> ? | ? 文件 | commit: 24eb0a99
> Codebase: 91 nodes / 238 edges

## 入口
main.go

## 架构
main → robot.CommentHandler → iClient (GitHub/Gitee/GitCode 适配器) + Redis 分布式锁

## 热点模块
lock.InitLocks(9), robot.CommentHandler(6), robot.HandleCommentRequest(3)

