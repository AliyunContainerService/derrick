# 必要条件
对于Node.js应用而言，首先需要在根目录下具备package.json文件且当前项目的npm包管理依赖都已经保存到了pacakge.json中。

# 版本支持
Derrick会根据package.json中的配置或者系统的Nodejs版本来探测具体的Node.js版本，并根据探测的版本查找对应的Node.js官方镜像，默认情况下会生成debian base的基础镜像。       

可以通过如下的方式在package.json中设置Node.js的版本

```
{
      "name": "application",
      "engines": {
        "node": "6.5.0"
      }
}

```
# 支持的框架   
Node.js    
io.js
NPM     
Grunt  
Gulp
Bower   

注：系统会自动探测 Gruntfile.js、gulp.js、bower.json 并会自动安装全局依赖。

# 启动命令与扩展
Derrick中启动命令的优先级如下 Procfile中的命令 > package.json中的scripts.start > package.json中的main > 系统自动探测的默认命令。

```
{
    "name": "nodejs-demo",
    "version": "0.0.1",
    "private": true,
    "main": "./bin/www",
    "scripts": {
        "start": "node ./bin/www",
        "test": "mocha",
        "preinstall":"npm install -g mocha",
        "postbuild":"grunt build"
    },
    "dependencies": {
        "body-parser": "~1.15.1",
        "cookie-parser": "~1.4.3",
        "debug": "~2.2.0",
        "express": "~4.13.4",
        "jade": "~1.11.0",
        "morgan": "~1.7.0",
        "serve-favicon": "~2.3.0"
    },
    "devDependencies": {
        "mocha": "^3.2.0"
    }
}
```

start中的命令会转换为 Dockerfile 的 CMD
test中的命令会转变为 Dockerfile.test的 CMD
pre开头的命令会在应用的包管理器安装依赖前执行
post开头的命令会在应用的包管理器安装依赖后执行

# Procfile支持
对于传统的PaaS标准中的Profile，目前Derrick也进行了支持，并且在Procfile中的命令会作为最高等级，覆盖从其他位置探测出的命令。
例如，一个Node.js的应用的启动命令可以写成：

```
    web: npm start
```
注：请注意Profile的语法，冒号后在有一个空格。
