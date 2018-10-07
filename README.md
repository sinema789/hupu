### 虎扑用户信息爬虫
>爬取近30万虎扑用户基本信息存储至mongodb,并进行数据可视化

* scrapy实现,中间件携带cookie保证获取数据完全,scrapy-redis完成分布式爬取
* 存储使用mongodb,将用户唯一的uid设置为索引保证查询速度
* 项目部署采用docker部署scrapyd,避免重复搭建爬虫环境
* flask-echarts:使用flask对接pyecharts完成简单的数据可视化