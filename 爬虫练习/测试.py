# -*- coding: utf-8 -*-
"""

Created on Tue Jun 26 20:38:13 2018
@author: Administrator

"""

import os
import requests

url = 'https://www.icourse163.org/learn/NEU-1002127001?tid=1002758017#/learn/content'
response = requests.get(url)
root = 'E://中国大学mooc//'
path = root + 'mooc.mp4'
if not os.path.exists(root):
    os.mkdir(root)    

if not os.path.exists(path):
    
    with open(path,'wb')as f:
        f.write(response.content)
        f.close()
else:
    print('已存在')
    
