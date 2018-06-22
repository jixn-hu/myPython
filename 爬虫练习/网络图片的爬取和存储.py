import requests
import os
url = "http://p2.cri.cn/M00/96/09/CqgNOlsMeBGAEEnvAAAAAAAAAAA356.660x330.jpg"
root = "D://360安全浏览器下载//"     #给定文件路径
path = root + url.split('/')[-1]     #给文件命名
try:
    if not os.path.exists(root): 
        os.mkdir(root)               #创建文件
    if not os.path.exists(path):
        r = requests.get(url)        #爬取网址
        with open (path, 'wb') as f:
            f.write(r.content)       #以二进形式存储文件
            f.close()
            print("文件保存成功")
    else:
        
        print("文件已经存在")
except:
    print("爬取失败")
