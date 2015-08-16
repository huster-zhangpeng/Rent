# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.loader import ItemLoader
from rent.items import RentItem
from scrapy.http import Request

class GanjiSpider(scrapy.Spider):
    name = "ganji"
    allowed_domains = ["http://bj.ganji.com"]
    start_urls = (
        'http://bj.ganji.com/fang1/haidian/a1h3m1p6/',
    )

    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, sdch',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Cache-Control' : 'no-cache',
        "Referer" : 'http://bj.ganji.com/fang1/haidian/a1h3m1p6/',
        "User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36',
        "Pragma" : 'no-cache'
    }

    def parse(self, response):
        for url in response.xpath("//ul[@class = 'list-style1']/li/div[1]/a/@href").extract():
            yield Request(response.urljoin(url),
                          headers = self.headers,
                          callback = self.parsePage,
                          dont_filter = True)

    def parsePage(self, response):
        rentHouse = ItemLoader(item = RentItem(), response = response)
        rentHouse.add_value('id', self.name + '-' +
                            response.url.split('/')[-1].split('.')[0])
        rentHouse.add_value('link', response.url)
        rentHouse.add_xpath('title', "//h1[@class = 'title-name']/text()")
        return rentHouse.load_item()
