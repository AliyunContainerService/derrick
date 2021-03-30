# Derrick

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![GitHub release](https://img.shields.io/badge/release-0.1.2-green.svg)](https://github.com/alibaba/derrick/releases)
[![Build Status](https://travis-ci.org/alibaba/derrick.svg?branch=master)](https://travis-ci.org/alibaba/derrick)
[![Codecov](https://codecov.io/gh/alibaba/derrick/branch/master/graph/badge.svg)](https://codecov.io/gh/alibaba/derrick)
[![Go Reference](https://pkg.go.dev/badge/github.com/alibaba/derrick.svg)](https://pkg.go.dev/github.com/alibaba/derrick)

Homepage: https://alibaba.github.io/derrick/

## Overview

Derrick is a tool to help you containerize application in seconds.
Derrick focuses on developer workflow in local development environment.
Derrick will inspect your workspace first, then generate definitions and templates to boost your journey to run apps as containerized services. This includes generating Dockerfile for your app, k8s definitions to deploy it, Helm Chart or Kustomize folders for multi-environment setup, Terraform templates to bootstrap your infrastructure resources, CI/CD pipelines to build/test/deploy the whole thing continously.
You can use Derrick to set up your DevOps processes in cloud-native way.

<img src="http://container-service.oss-cn-beijing.aliyuncs.com/derrick.png" width=100%/>

Using Derrick is very simple:

1. `derrick gen` to automatically inspect the workspace and generate the Dockerfile for your application, or
2. `derrick list` to show all available riggings and pick one via `derrick gen -r <rigging>` to generate the Dockerfile.
3. Use your favorite text editor to modify the Dockerfile or other manifests before building and shipping the containers.
4. Integrate into your workflow and have fun.

## Documentation

- [Installation](https://alibaba.github.io/derrick/docs/installation)
- [Getting started](https://alibaba.github.io/derrick/docs/quickstart)

## Language Support

Here is the list of frameworks passed the tests. If you want to support more languages and frameworks, please submit an issue.

- Java
- PHP
- PYTHON
- Golang
- NodeJs

## _License_

This software is released under the Apache 2.0 license.
