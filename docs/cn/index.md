### 简介 
<img src="http://container-service.oss-cn-beijing.aliyuncs.com/derrick.png" width=600px/>   
<b>Derrick</b> 是一个帮助应用Docker化的工具，通过探测、编译、构建，自动生成Dockerfile，快速在本地验证容器化后的业务正常与否。
### 快速开始   
#### 安装Derrick
```
	pip install derrick
	
	注：开源前暂无法使用，请使用源码安装 python setup.py install 
```
#### 使用示例项目  
下面以一个Node.Js项目为例，演示Derrick的使用方法。
##### 下载demo项目
```
	git clone git@gitlab.alibaba-inc.com:zhongwei.lzw/nodejs-demo.git 
```
##### 运行Derrick   
```
	derrick init 
	
	运行结果如下   
	
    8888888b.                       d8b        888
    888  "Y88b                      Y8P        888
    888    888                                 888
    888    888 .d88b. 888d888888d888888 .d8888b888  888
    888    888d8P  Y8b888P"  888P"  888d88P"   888 .88P
    888    88888888888888    888    888888     888888K
    888  .d88PY8b.    888    888    888Y88b.   888 "88b
    8888888P"  "Y8888 888    888    888 "Y8888P888  888

    ===================================================
    Derrick is a scaffold tool to migrate applications
    You can use Derrick to migrate your project simply.
    ===================================================

	This is the first time to run Derrick.

	Successfully create DERRICK_HOME in /Users/zhongweilzw/.derrick
	Derrick detect your platform is NodeJs and compile successfully.
```
初次运行Derrick的时候会创建在当前用户的根路径下创建.derrick目录，里面会保存用户未来定义的插件、Rigging等等。     

此时会发现在项目的目录中已经可以看到探测生成的Dockerfile。      

```
	derrick build 
	
	运行结果： 
	Sending build context to Docker daemon  32.77kB
	Step 1/14 : FROM node:6 AS base
 	---> cb4fff641acf
	Step 2/14 : WORKDIR /app
 	---> Using cache
 	---> 02b898c5e4e2
	Step 3/14 : COPY package.json .
 	---> Using cache
 	---> 908c48134d94
	Step 4/14 : RUN npm set progress=false && npm config set depth 0
 	---> Using cache
 	---> 656bd3e3d0c6
	Step 5/14 : RUN npm install --only=production
 	---> Using cache
 	---> 4499d1526017
	Step 6/14 : RUN cp -R node_modules prod_node_modules
 	---> Using cache
 	---> b2062d2a27bf
	Step 7/14 : RUN npm install
	
	... ... 
	... ... 
	
	npm info ok
	Successfully built 64ee04137bd5
	Successfully tagged nodejs-demo:latest
	Build nodejs-demo:latest successfully.
	You can execute `derrick serve` to run this image.
```
此时一个镜像已经构建完成，在本地进行镜像的验证即可。      

### 成为一个 Derrick Rigging 开发者
#### 什么是Rigging 
<img src="http://container-service.oss-cn-beijing.aliyuncs.com/java.png" style="width:200px"/>
<img src="http://container-service.oss-cn-beijing.aliyuncs.com/nodejs.png" style="width:200px"/>  
Derrick的本意是起重机的意思，在码头上Derrick是用来吊Container（集装箱）的。而绑定Container（集装箱）的Rigging（绳索）。吊起不同的Container需要使用不同的Rigging。Derrick探测、编译不同的语言与框架也就需要不同的Rigging。
#### 如何创建一个内置Rigging 
```
开发环境：Python2.7.*   

	1.下载Derrick的源代码   
	git clone git@gitlab.alibaba-inc.com:cos/derrick.git 
	
	2.在derrick/derrick/rigging目录下创建Rigging目录   
	例如目前已有的nodejs_rigging，希望构建ruby的可以创建ruby_rigging目录   
	
	3.创建Rigging的具体实现类    
	例如已有的nodejs_rigging.py      
	
	#! /usr/bin/env python
	# -*- coding: utf-8 -*-

	from __future__ import absolute_import, division, print_function

	import os

	from derrick.core.rigging import Rigging
	from derrick.detectors.image.node import NodeVersionDetector

	PLATFORM = "NodeJs"


	class NodejsRigging(Rigging):
    	def detect(self, context):
        	"""
        	:param context:
        	:return: handled(bool),platform(string)
        	"""
        	workspace = context.get("WORKSPACE")
        	package_json_file = os.path.join(workspace, "package.json")
        	if os.path.exists(package_json_file) == True:
            	return True, PLATFORM
        	return False, None

    	def compile(self, context):
        	node_version_detector = NodeVersionDetector()
        	image_version = node_version_detector.execute()
        	return {"Dockerfile.j2": {"version": image_version}}
	
	 所有的Rigging必须继承自derrick.core.rigging.Rigging.    
	 必须实现的方法为detect与compile.    
	 
	 detect 方法的作用是探测当前语言、平台是否为当前Rigging可以处理的。   
	 
	 compile 方法的作用是通过探测内容将预设的模板进行渲染。例如本例中是
	 进行Dockerfile的渲染，那么compile的返回结果只需要返回对应的数据
	 的dict即可。例如需要渲染Dockerfile.j2，那么只需要在dict中定义
	 Dockerfile.j2以及对应需要渲染的数据。     
	 
	 如果需要其他的模板但是无需渲染，例如.dockerignore，只需简单的将
	 模板放置在templates目录中。Derrick会自动拷贝内容到当前命令执行
	 目录中。
	 
	 4.创建单元测试代码，进行测试    
	 
	 5.从源码安装Derrick进行黑盒测试
	 python setup.py install  
	 
	 6.运行Derrick
	
```

<p style="color:red">注意：<br/>   
① Python默认情况下是不打包非.py的文件的，因此在调试的时候需要将代码提交到本地，在setup.py中会自动将SCM控制的文件一同打包。<br/><br/>
② 调试代码的时候，如果已经安装过Derrick会自动先寻找系统中安装的Derrick，因此最好在调试Derrick代码的时候，卸载已经安装的Derrick。
</p>
   
