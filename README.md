# Derrick
[![PIP release](https://img.shields.io/badge/pypi-v0.0.1-yellow.svg)](https://github.com/alibaba/derrick)
[![Platform](https://img.shields.io/badge/platform-Windows&Linux&Mac-green.svg)](https://github.com/alibaba/derrick)
[![Language](https://img.shields.io/badge/language-NodeJs Java Python-red.svg)](https://github.com/alibaba/derrick)
[![GitHub release](https://img.shields.io/badge/release-0.0.1-green.svg)](https://github.com/alibaba/derrick/releases)
[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)


Derrick is an automation tool to help you dockerize App in seconds. Derrick focus on the developer's workflow in local developement.Derrick will generate Dockerfile，docker-compose.yml，.dockerignore，Jenkinsfile and so on.You can simply use Derrick to accelerate application migration smoothly.  

<img src="http://container-service.oss-cn-beijing.aliyuncs.com/derrick.png" width=100%/>    

Using Derrick is very simple:    
1. `derrick init` to dockerize your application based on Derrick [Rigging].    
2. `derrick build` to build your application to a docker image.          
3. Use your favorite text editor to modify the Dockerfile or some others and run your application in local.        
4. Integrate your workflow left and have fun.       


## Documentation
* Documentation Home 
* Frequently Asked Questions   

## Installation 
 
```
	pip install alibaba-derrrick 
```

### *License*
Derrick is released under the Apache 2.0 license.

```
Copyright 1999-2017 Alibaba Group Holding Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at following link.

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```