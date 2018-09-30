yxf_mysite_py_django : 网站服务项目
=========================================================

------------

## 项目开发

项目主题：一整套网站  

开发环境：Linux（CentOS 7），python，django，postgresql，uwsgi，nginx  

编程语言：python  

git根目录：yxf_mysite_py_django  

网站项目根目录：yxf_mysite_py_django/mysite（后面以./mysite表示）  

与网站内容无关的环境配置脚本：yxf_mysite_py_django/scripts  

### 项目依赖  

python==2.7.x  

django==1.11.x  

pip>=18.x  

uwsgi==2.x  

ngnix==2.x  

postgresql==10.x  

./mysite/requirments.txt  

### 项目架构

数据库服务器（提供数据持久化服务）：postgresql  

应用容器（MVC模式的容器，服务主体）：django（manage.py+mysite/*）  

通用网关服务器（中间件，只提供通信转交服务）：uwsgi（mysite_conf/uwsgi.ini）  

网络服务器（HTTP及反向代理，只提供通信转交服务）：ngnix（/etc/nginx.conf+mysite_conf/nginx.conf）  

#### Django内部架构

项目管理：./mysite/manage.py  

网关配置：./mysite/mysite/uwsgi.py  

网站配置：./mysite/mysite/settings.py  

地址映射：./mysite/mysite/urls.py  

公共静态资源：./mysite/static  

缓存数据库：redis  

MVC子应用（提供具体服务功能的子模块）：./mysite/app_*  

MVC子应用的前端模板：./mysite/templetes/app_*  

MVC子应用的视图（响应请求，提取、组合模板，后端渲染）：./mysite/app_*/views.py   

MVC子应用的控制器（各式各样的控制逻辑）：./mysite/app_*/apps.py   

MVC子应用的模型（数据对象模型，定义的对象与数据库表一一对应）：./mysite/app_*/models.py   

------------

## 部署

服务器主机：Vultr-VPS（ip，ssh（22），sftp（22），root管理员），提供HTTP网站服务，正向代理服务  

服务端口：80-nginx，9090-uwsgi(local)，50003-ss，5432-postgresql  

