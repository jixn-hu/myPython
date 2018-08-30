# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:27:34 2018

@author: Administrator

已经爬取成功，但是存储信息时出错：
储存到txt文件必须为str类型，不能为list类型，
用str强制转换以后还是报错，显示存在非法字符，无法写入


"""


import requests
from bs4 import BeautifulSoup as bs

def get_html(url):  #请求获取网站
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
    html = requests.get(url,headers=headers).text
    return html

def get_data(html):  #取房屋信息
    data = []
    soup = bs(html,'lxml')
    houses_data = soup.find_all('li',class_='list-item')
    for house_data in houses_data:
        house_details = house_data.find('div',class_='house-details')
        title = house_details.find('div',class_='house-title').a.string
        data.append(title)
        detail = house_details.find_all('div',class_='details-item')
        for span in detail:
            data.append(span.text)
        advantage = house_data.find_all('div',class_='tags-bottom')
        for span in advantage:
            data.append(span.text)
    return data
            
# =============================================================================
# def storage(data):
#     root = 'E:\\临时文件存储区\\'
#     path = root+'house_data.csv'
#     try:
#         with open (path,'a+') as f:
#              f.write(data)
#              f.close()
#              print('爬取成功')
#     except:
#         print('爬取失败')
# =============================================================================
    
def main(n):
    url = 'https://beijing.anjuke.com/sale/p{}/#filtersort'.format(n)
    print('现在爬取第%s页'%n)
    get_data(get_html(url))
    #storage(data)
    
    
for n in range(1,10):
    main(n)