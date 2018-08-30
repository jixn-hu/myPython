# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
import scrapy
import sys
sys.path.append(r'E:\Python\PythonSpider\images360\images360')
from items import ImageItem
import json

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    def start_requests(self):
        #拼接url
        data = {'ch': 'photography', 'listtype': 'new'}
        base_url = 'https://images.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data) #用于转码
            url = base_url + params
            yield Request(url, self.parse)


    def parse(self, response):
        #解析数据并存储成字典形式
        result= json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item