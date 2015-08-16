# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader
from rent.items import RentItem
from scrapy.http import Request

class SoufangSpider(scrapy.Spider):
    name = "soufang"
    allowed_domains = ["http://zu.fang.com"]
    start_urls = (
        'http://zu.fang.com/house-a00/a21-c25000-d28000-g23-h316-n31/',
    )

    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, sdch',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Cache-Control' : 'no-cache',
        "Referer" : 'http://zu.fang.com/house-a00/a21-c25000-d28000-g23-h316-n31/',
        "User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36',
        "Pragma" : 'no-cache'
    }

    def parse(self, response):
        for url in response.xpath("//div[@class = 'houseList']/dl/dt/a/@href").extract():
            yield Request(response.urljoin(url),
                          headers = self.headers,
                          callback = self.parsePage,
                          dont_filter = True)
        pass

    def parsePage(self, response):
        rentHouse = ItemLoader(item = RentItem(), response = response)
        rentHouse.add_value('id', self.name + '-' +
                            response.url.split('/')[-1].split('.')[0])
        rentHouse.add_value('link', response.url)
        rentHouse.add_xpath('title', "//dl[@class = 'title']/dt/p/text()")
        return rentHouse.load_item()
