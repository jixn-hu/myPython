# 项目名称：爬取斗图网图片

- **项目URL**：http://www.doutula.com/
- **项目简介**：爬取斗图网100页的图片并存储到mysql数据库
- **项目所需库**：
> - pymysql
> - re
> - requests
> - os


- **项目内容**：


> -  使用requests库、修改user-agent来获取网页的内容
> -  使用正则表达式来解析网页，获取每张图片的链接以及名称
> -  下载图片到本地
> -  使用pymysql将图片在本地的地址和图片的名称存储到mysql数据库

- **项目成果**：

数据库结果图：

![图片](http://paxd6g86d.bkt.clouddn.com/Q%25%286E~SMC%7B%5BTYU%292@1%5BO04O.png)


本地图片：

![图片](http://paxd6g86d.bkt.clouddn.com/%29A5Z@0S@NHUF2YO64E4Q%60DM.jpg)