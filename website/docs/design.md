---
title: 项目设计
---

在介绍 Derrick 内部设计之前不得不先介绍两个概念:

- **Rigging**：Rigging 是对特定语言框架的一个封装包，类似于 Buildpack。它包含检测逻辑等钩子函数、配置模板等，实现了 Derrick 所规定的生命周期接口，然后 Derrick 可以使用它所能装载到的 Riggings 来检测和生成部署配置。
- **AutoParam**：AutoParam 是用来自动检测语言环境并将这些作为参数值传入到模板中用于渲染。

Derrick 的整体设计如下：

- 用户在应用项目中运行 `derrick gen` 之后，Derrick 将装载 Riggings 并逐一调用检测钩子函数。
- 如果一个 Rigging 检测结果返回成功，那么 Derrick 将使用这个 Rigging 来进一步生成配置文件。
- Derrick 进一步为这个 Rigging 调用 AutoParam 钩子函数，生成所有需要的参数值。
- Derrick 将所有的参数值收集起来，传入模板渲染函数中，得到最终生成的配置文件。
