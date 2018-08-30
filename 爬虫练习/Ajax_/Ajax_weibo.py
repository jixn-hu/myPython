# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:16:55 2018

@author: Administrator

获取了最基本的json数据，没有进行解析
"""

import requests
#from pyquery import PyQuery as pq


def get_html(page):
    url = 'https://m.weibo.cn/api/container/getIndex?'
    params = {
            'type': 'uid',
            'value': '2830678474',
            'containerid':'1076032830678474',
            'page': page
            }
    headers = {
            'Cookie': '_T_WM=8993f48a9a9839b25c7a3a3415179849; MLOGIN=0; WEIBOCN_FROM=1110106030; M_WEIBOCN_PARAMS=oid%3D4253432191641911%26luicode%3D10000011%26lfid%3D1076032830678474%26fid%3D1076032830678474%26uicode%3D10000011',
            'Host': 'm.weibo.cn',
            'Referer': 'https://m.weibo.cn/u/2830678474',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
    html = requests.get(url,headers=headers,params=params).json()
   
    return html

# =============================================================================
# def pares_page(json):
#     if json:
#         items = json.get('data').get('cards')
#         for item in items:
#             wb={}
#             item = item.get('mblog')
#             print(item)
#             wb['id']=item.get('bid')
#             wb['text'] = pq(item.get('text')).text()
#             
# =============================================================================

def main(n):
    get_html(n)

    
if __name__ == '__main__':
    main(1)
