# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 08:16:17 2018

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
    html = requests.get(url,headers=headers).text
    
    return html

def get_data(html):
    
    topz,titlez = [],[]
    soup = BeautifulSoup(html,'lxml')
    divs_top = soup.find_all('div',class_='pic')
    divs_hd = soup.find_all('div',class_ = 'hd')
    for tops in divs_top:
        top = tops.em.text.strip()
        topz.append(top)   #添加数据
        
    for titles in divs_hd:
        title = titles.a.span.text.strip()
        titlez.append(title)
    return topz,titlez
    
def prints(topz,titlez):
    for i in range(0,25):
        print(topz[i],titlez[i])
        
def main():

    for n in range(0,250,25):
        url = 'https://movie.douban.com/top250?start={}'.format(n)
        topz,titlez = get_data(get_html(url))
        prints(topz,titlez)
        
main()