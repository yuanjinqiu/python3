import requests
from lxml import etree

for num in range(23001,23054):
    url = 'https://kaijiang.500.com/shtml/dlt/{}.shtml'.format(num)
    heads = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
    }
    con = requests.get(url=url,headers=heads).text
    tree = etree.HTML(con)
    li_list = tree.xpath('//div[@class="ball_box01"]/ul/li')
    # print(li_list)
    l=[]
    for li in li_list:
        l.append(li.xpath('./text()')[0])
    print(l)
    # for i in l:
    #     with open('2023.txt', 'a+')as f:
    #         f.write(i + ' ')
    # with open('2023.txt', 'a+')as f:
    #     f.write('\n')