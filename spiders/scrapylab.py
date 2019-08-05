import scrapy
import glob
import os


def clear():
    test = '/html/*'
    r = glob.glob(test)
    for i in r:
        os.remove(i)


class SlabSpider(scrapy.Spider):
    name = "slab"

    def start_requests(self):
        urls = [
            'http://lab.scrapyd.cn/',
        ]
        clear

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=None)

    def parse(self, response):
        for quote in response.css('div.quote'):
            page = response.url.split("/")[-2]
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            filename = 'html/slab-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('保存文件: %s' % filename)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, headers=None)
