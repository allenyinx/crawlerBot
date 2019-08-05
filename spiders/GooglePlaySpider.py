import scrapy
from items import ProductItem
from items import GPReviewItem


class GooglePlaySpider(scrapy.Spider):
    name = 'gp'
    allowed_domains = ['play.google.com']

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', [])  # 获取参数
        if urls:
            self.start_urls = urls.split(',')
        print('start urls = ', self.start_urls)

    def parse(self, response):
        print('Begin parse ', response.url)

        item = ProductItem()

        content = response.xpath('//div[@class="LXrl4c"]')

        try:
            item['gp_icon'] = response.urljoin(content.xpath('//img[@class="T75of ZqMJr"]/@src')[0].extract())
        except Exception as error:
            print('gp_icon except = ', error)
            item['gp_icon'] = ''

        try:
            item['gp_name'] = content.xpath('//div[@class="UD7Dzf"]/span/text()')[0].extract()
        except Exception as error:
            print('gp_name except = ', error)
            item['gp_name'] = ''

        yield item
