import requests
from lxml  import etree
import os


heads = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
         }

if os.path.exists('/Users/v_yuanjinqiu/Desktop/gp.txt'):
    os.remove("/Users/v_yuanjinqiu/Desktop/gp.txt")
for i in range(1,11):
    url = 'https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{}/ajax/1/'.format(i)
    content = requests.get(url=url,headers=heads).text
    # print(content)
    tree = etree.HTML(content)
    tr_list = tree.xpath('/html/body/table/tbody/tr')

    while tr_list == []:
            content = requests.get(url=url, headers=heads).text
            # print(content)
            tree = etree.HTML(content)
            tr_list = tree.xpath('/html/body/table/tbody/tr')
    for tr in tr_list:
        t = tr.xpath('./td[3]/a/text()')
        f = tr.xpath('./td[5]/text()')
        h = tr.xpath('./td[8]/text()')
        s = tr.xpath('./td[13]/text()')
        con = t[0]+"\t"+f[0]+"\t"+h[0]+'\t'+s[0]+"\n"
        print(con)
        with open('/Users/v_yuanjinqiu/Desktop/gp.txt','a+') as f:
            f.write(con)
print("爬取结束")

