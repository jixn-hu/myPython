import requests
from bs4 import BeautifulSoup

def getHtml(url):               #获取网页内容
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def fillText(html):                     #将网页内容整理成列表
    soup = BeautifulSoup(html , "html.parser")
    allTr = soup.find_all('tr')
    allt = []
    for tr in allTr:
        if len(allTr)==0:
            continue6
        textt = []
        allTd = tr.find_all('td') 
        for td in allTd:
            textt.append(td.string)#获取列表行元素
        allt.append(textt)             #将每行存入列表，形成列 
    return allt
 

   
def printText(allt):            #按照一定格式输出
    print("{1:^4}{2:{0}^9}{3:{0}^6}{4:{0}^7}".format(chr(12288),"排名","学校名称","省市","总分"))
    for i in range(1,11):
        alltz = allt[i]
        print("{1:^4}{2:{0}^10}{3:{0}^6}{4:^10.1f}".format(chr(12288),alltz[0],alltz[1],alltz[2],eval(alltz[3])))

def main():
    allt = []
    url = 'http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2017.html'
    html = getHtml(url)
    allt = fillText(html)
    printText(allt)

main()
    
