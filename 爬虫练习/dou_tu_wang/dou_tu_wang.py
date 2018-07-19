
"""
Created on Wed Jun 20 15:33:31 2018

@author: Administrator
"""
'''

作用： 爬取斗图网的图片并存储到数据库
URL：  http://www.doutula.com/

'''
import pymysql
import re
import requests
import os

def getImagesList(url):     #获取页面的数据
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            }
    html = requests.get(url,headers = headers).text
    return html
  
def getImagesUrl(html):   #获取图的链接和名称
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    reg = re.compile(reg,re.S)
    imagesUrlList = re.findall(reg,html)
    
    return imagesUrlList
        
def lianPython(imagesUrlList):   #将图的链接和名称保存到数据库
    db = pymysql.connect(host = '127.0.0.1',port = 3306,db = 'db',user = 'root',passwd = 'root',charset = 'utf8')  # 连接数据库
    cursor = db.cursor()   #建立游标
    cursor.execute('select * from images')
    for i in imagesUrlList:
        name = i[1]
        name = name[:20]
        image_Url = i[0]
        root = "E:/斗图网图片/"
        path = root + name[:10] + image_Url[-4:]
        storageImages(root,path,image_Url)
        cursor.execute("insert into images(`name`,`imageUrl`)values('{}','{}')".format(name,path))
        print('正在保存 %s'%name)
        db.commit()
    
def storageImages(root,path,image_Url):  #存储图片
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                image = requests.get(image_Url)
                with open(path,'wb') as f:
                    f.write(image.content)
                    f.close()
                    print('图片{}保存成功'.format(path))
            else:
                print("图片已存在")
        except:
            print("爬取失败")    

def main(i):      
    url = 'http://www.doutula.com/article/list/?page={}'.format(i)
    html = getImagesList(url)
    imagesUrlList = getImagesUrl(html)
    lianPython(imagesUrlList)
    
for i in range(1,101):   #爬取斗图网第一页到第一百页的数据
        main(i)

