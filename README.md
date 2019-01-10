# Derrick
[![PIP release](https://img.shields.io/badge/pypi-v0.0.24-green.svg)](https://github.com/alibaba/derrick)
[![Platform](https://img.shields.io/badge/platform-Windows&Linux&Mac-green.svg)](https://github.com/alibaba/derrick)
[![Orchestration](https://img.shields.io/badge/orchestration-swarm&kubernetes-green.svg)](https://github.com/alibaba/derrick)
[![Language](https://img.shields.io/badge/language-NodeJs&PHP&Java&Python&Golang-red.svg)](https://github.com/alibaba/derrick)
[![GitHub release](https://img.shields.io/badge/release-0.0.24-green.svg)](https://github.com/alibaba/derrick/releases)
[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![Build Status](https://travis-ci.org/alibaba/derrick.svg?branch=master)](https://travis-ci.org/alibaba/derrick)
[![Codecov](https://codecov.io/gh/alibaba/derrick/branch/master/graph/badge.svg)](https://codecov.io/gh/alibaba/derrick)

Derrick is a tool to help you dockerizing application in seconds. Derrick focus on the developer's workflow in local development environment. Derrick will inspect your workspace and generate Dockerfile, docker-compose.yml, Jenkinsfile, etc. You can simply use Derrick to set up your DevOps process in container way smoothly.

<img src="http://container-service.oss-cn-beijing.aliyuncs.com/derrick.png" width=100%/>    

Using Derrick is very simple:    
1. `derrick init` to dockerize your application based on Derrick.    
2. `derrick up` to build your application to a Docker image and run in local.        
3. Use your favorite text editor to modify the Dockerfile or some others and run your application in local.        
4. Integrate into your workflow and have fun.       


## Language Support
NodeJs,Python,Java,Golang,PHP.      

## Framework and Build tool Support
Here is the list of frameworks passed the tests.If you want more frameworks or can not dockerize application,please submit a issue.
* Java (maven)
  * springcloud
  * springboot
* PHP (composer)
  * Laravel
  * Lumen
  * ThinkPHP
  * Symfony
* PYTHON (pip or setup)
  * flask
  * Django
* Golang (tools by vendor)
  * Gin
  * Beego
* NodeJs (npm)
  * Express
  * Sails

## Documentation
* <a href="https://github.com/alibaba/derrick/wiki">Documentation Home</a>
* <a href="https://github.com/alibaba/derrick/wiki">Frequently Asked Questions</a>  

## Installation
Requirements:     
Docker(17.06~),Python2.7.9~python3.6,docker-compose or minikube in local.

Linux/mac/windows    

```
sudo pip install -i https://pypi.python.org/simple  python-derrick
```
if you find some error like: fatal error: Python.h: No such file or directory,Please install python-dev or python-devel with package manager.Windows please use powershell or winshell.


## Demo
<a href="https://www.youtube.com/watch?v=IHq_gTvOCSs" target="_blank"><img src="http://derrick.oss-cn-beijing.aliyuncs.com/static/WX20171024-172428%402x.png" width=800px/></a>


### *License*
This software is released under the Apache 2.0 license.
