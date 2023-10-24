import requests

url = 'https://www.baidu.com/s'
heads = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
         }
param = {
    'wd':"股票"
}
con = requests.get(url=url,headers=heads ,params=param)
con.encoding = 'utf-8'
print(con.text)