租房抓取
===
抓取赶集、搜房、安居客上面最新的房东直租房源，并给特定的人发邮件的服务

依赖
---
该项目使用scrapy，所以在使用之前先安装之，`sudo pip install scrapy`

设置
---
- 关于mongo数据库的设置，要去rent/settings.py里面去自己设置
- 关于自己邮箱的设置，要去rent/pipelines.py下面去自己运行

运行
---
在项目根目录，运行`scrapy crawl ganji|anjuke|soufang`
可以配置成crontab的定时任务，以达到更好的效果

