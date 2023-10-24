import requests
from lxml import etree

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
}

# 设置 URL 和参数
url = 'https://www.zhipin.com/job_detail/'
params = {
    'query': 'python',
    'city': '101010100',
    'page': 1,
}

# 循环获取多个页面的信息
for i in range(5):  # 获取前5页的信息
    params['page'] = i + 1  # 设置页码参数
    response = requests.get(url, params=params, headers=headers)
    html = response.text
    selector = etree.HTML(html)

    # 使用 XPath 获取职位名称、薪资、公司名称、公司地址等信息
    job_names = selector.xpath('//div[@class="job-title"]/text()')
    salaries = selector.xpath('//span[@class="red"]/text()')
    company_names = selector.xpath('//div[@class="company-text"]/h3/a/text()')
    company_addresses = selector.xpath('//div[@class="job-desc"]/p/text()[1]')

    # 打印当前页面的信息
    for job_name, salary, company_name, company_address in zip(job_names, salaries, company_names, company_addresses):
        print('职位名称:', job_name)
        print('薪资:', salary)
        print('公司名称:', company_name)
        print('公司地址:', company_address)
        print('------------------------------')
