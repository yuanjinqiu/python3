import requests
import os
from lxml import etree


heads = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
         }

if os.path.exists('/Users/v_yuanjinqiu/Desktop/ip_list'):
    os.remove("/Users/v_yuanjinqiu/Desktop/ip_list")
for i in range(1,10):
    url = 'https://proxy.ip3366.net/free/?action=china&page={}'.format(i)
    content = requests.get(url=url,headers=heads).text
    # print(content)
    tree = etree.HTML(content)
    tr_list = tree.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr')

    for tr in tr_list:
        ip = tr.xpath('./td[1]/text()')
        port = tr.xpath('./td[2]/text()')
        print(ip[0]+':'+port[0])

#//*[@id="content"]/section/div[2]/table/tbody/tr[1]
#//*[@id="content"]/section/div[2]/table/tbody/tr[1]/td[1]/text()