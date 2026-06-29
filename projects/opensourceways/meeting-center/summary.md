# meeting-center — 项目摘要
> [https://github.com/opensourceways/meeting-center](https://github.com/opensourceways/meeting-center)

> opensourceways | 社区会议管理中心，支持单次/周期会议、WELINK/ZOOM 集成、活动管理
> ? | ? 文件 | commit: fdd91fcd
> Codebase: 1,501 nodes / 5,971 edges

## 入口
manage.py (Django)

## 架构
Django DDD: apps/meeting + apps/activity → application/domain/infrastructure/controller

## 热点模块
MeetingView.get(74), MeetingView.post(54), ActivityApplication.get(34)

