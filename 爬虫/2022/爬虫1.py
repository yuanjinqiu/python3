import requests
from lxml import etree

url = 'https://pic.netbian.com/e/search/result/?searchid=1176'
heads = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
content = requests.get(url=url,headers=heads).text

# print(content.text)
tree = etree.HTML(content)
li_list = tree.xpath("/html/body/div[2]/div/div[2]/ul/li")
print(li_list)
# uri = 'https://pic.netbian.com'
# for li in li_list:
#     con = li.xpath('.//a/img/@src')
#     new_url = uri + con[0]
#     con = requests.get(url=new_url, headers=heads).content
#     img_name = new_url.split('/')[-1]
#     path = '/Users/v_yuanjinqiu/python3/爬虫/img/' + img_name
#     print(path)
#     with open(path, 'wb') as f:
#         f.write(con)
