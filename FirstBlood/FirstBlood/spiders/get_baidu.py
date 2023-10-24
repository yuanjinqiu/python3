import scrapy


class GetBaiduSpider(scrapy.Spider):
    name = "get_baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["http://www.baidu.com/"]

    def parse(self, response):
        print(response)
