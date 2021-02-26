# Derrick

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![GitHub release](https://img.shields.io/badge/release-0.1.2-green.svg)](https://github.com/alibaba/derrick/releases)
[![Build Status](https://travis-ci.org/alibaba/derrick.svg?branch=master)](https://travis-ci.org/alibaba/derrick)
[![Codecov](https://codecov.io/gh/alibaba/derrick/branch/master/graph/badge.svg)](https://codecov.io/gh/alibaba/derrick)

Derrick is a tool to help you containerize application in seconds.
Derrick focuses on developer workflow in local development environment.
Derrick will inspect your workspace and generate Dockerfile and other manifests to achieve containerization.
You can use Derrick to set up your DevOps processes in container-native way.

<img src="http://container-service.oss-cn-beijing.aliyuncs.com/derrick.png" width=100%/>    

Using Derrick is very simple:    
1. `derrick gen` to automatically inspect the workspace and generate the Dockerfile for your application, or
2. `derrick list` to show all available riggings and pick one via `derrick gen -r <rigging>` to generate the Dockerfile.
3. Use your favorite text editor to modify the Dockerfile or other manifests before building and shipping the containers.
4. Integrate into your workflow and have fun.


## Language Support

Here is the list of frameworks passed the tests. If you want to support more languages and frameworks, please submit an issue.

* Java
* PHP
* PYTHON
* Golang
* NodeJs
  
## Quick Start

### Installation

Build `derrick` binary: 

```shell
make build
cp _bin/derrick /usr/local/bin/
```

Verify it in command line:

```shell
$ derrick -h
🐳 A tool to help you containerize applications in seconds

Usage:
  derrick [command]

Available Commands:
  gen         Inspect the application and generate Dockerfile
  help        Help about any command
  list        List all available riggings to inspect the applications
  version     Prints out build version information

Flags:
  -h, --help   help for derrick

Use "derrick [command] --help" for more information about a command.
```

### Show available riggings

```shell
$ derrick list

Available riggings:
	golang
	java
	nodejs
	php
	python
```

### Build golang application

- Clone a sample project

Clone this sample project into your Golang path.

```shell
$ git clone git@github.com:zzxwill/golang-web-application.git
$ cd golang-web-application
```

- Compile the application

```shell
$ derrick gen
Successfully detected your platform is 'golang'
Successfully generated: Dockerfile
Successfully generated: derrick.conf
```

- (Optional) You can also manually specify to use golang rigging:

```shell
$ derrick gen -r golang
```

### Build NodeJS application

```shell
$ git clone git@github.com:zzxwill/nodejs-web-application.git
$ cd nodejs-web-application
$ derrick gen
```

### Build Java application

Clone a Java application, and build it.

```shell
$ git clone git@github.com:zzxwill/java-maven-web-application.git
$ cd java-maven-web-application
$ derrick gen
```

## *License*

This software is released under the Apache 2.0 license.
