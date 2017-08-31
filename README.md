Derrick: a dockerize tool for Aliyun Container Service
======================================================
Derrick is an open source project that help you to migrate a application to cloud native containerized application. 

Docker Container is cool enough but it is not very easy to set up a complex program with it alone.    
Sometimes you need K8S or Swarm to orchestrate your service and SLB(Server Load Balancer) to balance network flow and so on.    


<img src="http://container-service.oss-cn-beijing.aliyuncs.com/derrick.png" width=600px/>     

Derrick will help you to reduce the effort of struggling with docker.

## Hello Derrick  

```
    pip install derrick 
    
    git clone git@gitlab.alibaba-inc.com:zhongwei.lzw/nodejs-demo.git 
    
    derrick init 
    
    derrick build 
    
```

## Documentation 
Derrick's docs is hosted by mkdocs.you can install mkdocs to view all docs.
```
    pip install mkdocs 
    mkdocs serve 
```
