import requests
from lxml import etree
import re


url = "https://www.pearvideo.com/popular"

heads = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}

con = requests.get(url=url,headers=heads).text
tree = etree.HTML(con)
li_list = tree.xpath("/html/body/div[2]/div/ul/li")
for li in li_list:
    con = li.xpath('.//a/@href')
    new_url = "https://www.pearvideo.com/" + con[0]
    with open('url.txt', 'a+') as f:
        f.write(new_url + '\n')

    # c = etree.HTML(r)
    # url1 = c.xpath('//*[@id="JprismPlayer"]')
    # print(url1)
    # for u1 in url1:
    #     u = u1.xpath('./video/@src')
    #     print(u)

