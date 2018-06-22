
import requests
url = "http://www.amazon.cn/gp/product/B01M8L5z3Y"
try:
    kv = {'use-agent':'Mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
