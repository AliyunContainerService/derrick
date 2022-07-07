---
title: 项目介绍
slug: /
---

Derrick 是一个帮助用户快速容器化应用的工具。Derrick 适用于本地开发环境，能够自动检测项目的语言框架，然后自动生成容器化所需的配置文件，包括不限于：

- Dockerfile
- Kubernetes 资源定义
- Helm Chart 模板
- Kustomize 模板
- 更多在实现中 (如 Terraform 模板等)

这些配置文件能够帮助用户构建容器镜像，利用云资源搭起 k8s 等基础设施，部署到 K8s 中，管理不同环境的配置，等等。总而言之，Derrick 能够帮助开发者降低容器化门槛，简化部署操作。
