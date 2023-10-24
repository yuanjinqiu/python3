import requests
from lxml  import etree

url = 'https://q.10jqka.com.cn'
heads = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
content = requests.get(url=url,headers=heads).text

tree = etree.HTML(content)

tr_list = tree.xpath('//*[@id="maincont"]/table/tbody/tr')
# print(tr_list)
for tr in tr_list:
    t = tr.xpath('./td[3]/a/text()')
    f = tr.xpath('./td[5]/text()')
    h = tr.xpath('./td[8]/text()')
    print(t[0]+"\t"+f[0]+"\t"+h[0])

