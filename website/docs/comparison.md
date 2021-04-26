---
title: 对比其他项目
---

## Buildpack

[Buildpack](https://buildpacks.io/) 是一个客户端工具，用于从源代码自动化构建出应用镜像。

Derrick 在很大程度上借鉴了 Buildpack 的思想，包括 auto-detection 等简单易用的体验。但是，Buildpack 作用的场景过于局限，很多用户需要的场景没法满足。比如说：

1. 用户不想要自动构建镜像，而是想要先自动生成 Dockerfile 文件，然后在里面手动做一些更改。
1. 用户想要自动生成 K8S 部署配置。
1. 用户想要自动生成一些云资源配置的模板，比如跟中间件 AHAS/MSE/ARMS 的集成，然后进一步填入信息。
1. 用户想要一步到位把镜像上传到镜像服务中。
1. 用户已经有一些服务跑在 VM 里面，想要进一步把这些应用给容器化后运行到 K8S 上。

这些都是 Buildpack 无法解决的问题。而 Derrick 的出现正是为了解决这些用户问题，为了能够更好地帮助用户容器化应用。

另一方面，Derrick 计划直接利用 Buildpack 做自动生成镜像的工作，充分利用 Buildpack 社区已有的能力。从这点看，Derrick 更像是 Buildpack 的一个超集。

Derrick 跟 Buildpack 的对比总结如下：

- Derrick 能够生成 Dockerfile 等配置文件，让用户进一步修改。
- Derrick 能够生成 K8S 部署配置、云资源配置等。
- Derrick 能够将已经在运行的服务容器化。
- Buildpack 能够自动生成镜像。而且这方面在社区有大量已有的能力。Derrick 有计划直接利用起来，而不是重复建设。
