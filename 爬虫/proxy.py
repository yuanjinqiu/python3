import requests
import os

if os.path.exists('ip.html'):
    os.remove("ip.html")

url = 'https://www.baidu.com/s'
heads = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
         }
param = {
    'wd':"ip"
}
con = requests.get(url=url,headers=heads,params=param,proxies={"https":'119.91.76.114:7890'})
con.encoding = 'utf-8'

with open('ip.html','a+')as f:
    f.write(con.text)
