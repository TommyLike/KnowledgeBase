# app-cla-server — 项目摘要

> [https://github.com/opensourceways/app-cla-server](https://github.com/opensourceways/app-cla-server)
> opensourceways | auth | Go + Beego | 3,069 nodes / 11,487 edges | commit: da1be169

## 用途
开源社区 CLA（贡献者许可协议）签署服务后端。为 GitHub/Gitee 等多平台提供统一的 CLA 签署、验证、管理能力。

## 技术栈
- **框架**: Beego v2 (Go Web)
- **数据库**: MongoDB + Redis
- **认证**: GitHub OAuth + Gitee OAuth
- **PDF 生成**: gofpdf（生成签署 PDF 存证）
- **监控**: Prometheus
- **架构**: DDD 四层

## 架构

```
main.go
├── signing/ (核心签署域)
│   ├── adapter/        ← 错误模型转换 (toModelError, fan-in: 47)
│   ├── app/            ← 签署应用服务
│   ├── domain/         ← 领域模型: email, random bytes, error
│   │   ├── dp/         ← 值对象 (EmailAddr, LinkID, PDF 字段)
│   │   ├── error/      ← 统一领域错误 (fan-in: 61)
│   │   └── randombytes/← 加密随机数 (fan-in: 49)
│   └── infrastructure/ ← MongoDB DAO + 外部 API 调用
├── controllers/        ← HTTP 层 (Beego)
│   └── response/       ← 统一响应格式 (sendSuccessResp: 46)
├── models/             ← 数据模型
├── routers/            ← URL 路由
├── utils/              ← 工具函数
└── watch/              ← 配置监听/热更新
```

## 核心流程
1. 用户通过 GitHub/Gitee OAuth 登录
2. 平台校验 CLA 签署状态
3. 未签署 → 展示 CLA 文本 → 用户签署
4. 生成 PDF 存证 → MongoDB 持久化
5. 后续 PR 自动校验 CLA 签署状态

## 领域模型
- **EmailAddr** (fan-in: 48): 邮箱值对象，校验格式
- **randombytes**: 加密签名随机数
- **signing app service**: 签署状态管理、PDF 管理

## Tags
`auth` `cla` `go` `beego` `mongodb` `redis` `oauth` `pdf` `prometheus` `ddd`
