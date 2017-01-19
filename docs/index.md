# Derrick简介  

# 支持的语言  
<a href="./nodejs.md">Node.js</a>      
<a href="./python.md">Python</a>    

# 使用方式   
安装derrick的<a href="../dist/derrick-0.0.1-py2.7.egg" target="_blank">egg包</a>  

```
  easy_install derrick-0.0.1-py2.7.egg
```

# 安装buildpack包   

```
  # 安装nodejs的buildpack包
  derrick install git@gitlab.alibaba-inc.com:zhongwei.lzw/buildpack-nodejs.git
  # 安装python的buildpack包
  derrick install git@gitlab.alibaba-inc.com:zhongwei.lzw/buildpack-python.git
```

# 测试

Node.js
```
git clone  git@gitlab.alibaba-inc.com:zhongwei.lzw/nodejs-demo.git
cd nodejs-demo
derrick init nodejs
docker build -t nodejs-test:latest
docker run -d -p 3000:3000 nodejs-test:latest
# 开启浏览器访问127.0.0.1:3000  
```

Python uwsgi
```
git clone git@gitlab.alibaba-inc.com:zhongwei.lzw/python-demo.git
cd python-demo
derrick init python
docker build -t python-test:latest
docker run -d -p 8080:80 python-test:latest
# 开启浏览器访问127.0.0.1:8080
```
