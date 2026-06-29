# software-package-server — 项目摘要
> [https://github.com/opensourceways/software-package-server](https://github.com/opensourceways/software-package-server)

> opensourceways | openEuler 软件包管理平台，全生命周期: 引入→审核→CI→发布
> ? | ? 文件 | commit: e3626424
> Codebase: 2,434 nodes / 8,502 edges

## 入口
main.go, download/download.go, message-server/main.go, watch/main.go

## 架构
DDD 四层: controller → app → domain(20+ 值对象) → infrastructure(Kafka/DB/CI)

## 热点模块
allerror.Error(167), allerror.New(97), NewPackageName(31)

