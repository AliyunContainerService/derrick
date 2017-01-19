# 必要条件
对于Python应用而言，必须在根目录下包含 requirements.txt(推荐) 或者 setup.py，并且应用的所有包依赖需完整的保存在两个文件中。
提示：可以使用 pip freeze > requirements.txt 命令生成 requirements.txt 文件
# 版本支持
Derrick会根据runtime.txt中的配置或者系统的Python版本来探测具体的Python版本，并根据探测的版本查找对应的Python官方镜像，默认情况下会生成debian base的基础镜像。       

可以通过如下的方式在runtime.txt中设置python的版本

```
python-2.7.12

```
# 支持部署结构   

uwsgi + nginx
gunicorn  
python ****.py 启动    


注: 默认情况下需要根路径下具备 Procfile 或者 uwsgi.ini      

Procfile的例子，在Procfile中定义

```
python web.py

```
gunicorn的例子，在Procfile中定义gunicorn的启动命令，例如

```
gunicorn hello:app
```

uwsgi的例子，在根目录下添加uwsgi.ini，内容如下：    

```
[uwsgi]
socket = /tmp/uwsgi.socket
chown-socket = www-data:www-data
chmod-socket = 664
callable=app
```
其中 [uwsgi] 与 socket的结构为必须，其他的字段可以根据需求进行修改
