---
title: 云中间件配置
---

## ARMS

[应用实时监控服务 ARMS](https://help.aliyun.com/document_detail/125726.html)（Application Real-Time Monitoring Service）是一款阿里云应用性能管理（APM）类监控产品，为部署在容器服务 Kubernetes 版中的 Java 应用提供全方位监控、快速定位问题、重现调用参数、发现系统瓶颈等。

Derrick 会为所有的 Pod 自动生成 ARMS 所需的 Annotations 如下：

```yaml
armsPilotAutoEnable: "off"
armsPilotCreateAppName: "your-app-name"
```

如需使用，请将 `armsPilotAutoEnable` 设置为 `on`，以及填入 `armsPilotCreateAppName` 你的应用名称。

## AHAS


[应用高可用服务 AHAS](https://help.aliyun.com/document_detail/193575.html)（Application High Availability Service）是一款阿里云应用高可用服务相关产品，为部署在容器服务 Kubernetes 版中的 Java 应用进行全方位系统防护，针对性的对系统进行流量管控、服务降级等操作。

Derrick 会为所有的 Pod 自动生成 AHAS 所需的 Annotations 如下：

```yaml
ahasPilotAutoEnable: "off"
ahasAppName: "your-app-name"
ahasNamespace: "default"
```

如需使用，请将 `ahasPilotAutoEnable` 设置为 `on`，以及填入 `ahasAppName` 你的应用名称。

## MSE

[微服务引擎 MSE](https://help.aliyun.com/document_detail/184033.html) （Microservice Engine）是一个面向业界主流开源微服务框架Spring Cloud和Dubbo一站式微服务平台，提供治理中心、托管的注册中心和托管的配置中心。

Derrick 会为所有的 Pod 自动生成 AHAS 所需的 Annotations 如下：

```yaml
msePilotAutoEnable: "off"
msePilotCreateAppName: "your-app-name"
```

如需使用，请将 `msePilotAutoEnable` 设置为 `on`，以及填入 `msePilotCreateAppName` 你的应用名称。
