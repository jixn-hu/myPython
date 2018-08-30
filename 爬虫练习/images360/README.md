# 爬取360摄影图片及信息 #

- **项目URL**：https://images.so.com/
- **项目简介**：爬取360摄影图片及信息存储到数据库mongodb中
- **项目所需库/框架**：
> - scrapy框架
> - pymongo库
> - sys库
> - urllib库
> - json库


- **项目实操：**

1. **使用cmd创建项目和爬虫:**

		scrapy startproject images360
		scrapy genspider images images.so.com

2. **修改images.py:**

	- 创建start_requests函数，拼接url，设置为初始url
	- 修改parse函数，用于解析数据，提取信息并存储到mongodb中

3. **修改settings.py:**

	- 定义一个变量，用来设置最大爬取页
	
			MAX_PAGE = 50
	- 修改ROBOTSTXT_OBEY函数，将其设置为False，关闭robots协议
	- 添加一个变量,用来定义路径：
	
			IMAGES_STORE = './images'
	- 启用变量ITEM_PIPELINE,并修改：
	
			ITEM_PIPELINES = {
				'images360.pipelines.ImagePipeline': 300,
    			'images360.pipelines.MongoPipeline': 301,
			}

4. **修改items.py:**

	- 我们这里定义一个Item，叫做ImageItem，并且定义4个字段：id，url，title，thumb，分别表示ID，链接，标题和缩略图
	
5. **修改pipelines.py:**

	- 创建一个MongoPipeline类，用来将信息保存的mongodb中
	- 创建一个ImagePipeline类，

- **项目结果图：**
- 
图片结果图：

![图](http://paxd6g86d.bkt.clouddn.com/images360/images360%E5%9B%BE%E7%89%87%E7%BB%93%E6%9E%9C%E5%9B%BE-.png)

mongodb结果图：

![图](http://paxd6g86d.bkt.clouddn.com/images360/images360%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BB%93%E6%9E%9C%E5%9B%BE.png)




