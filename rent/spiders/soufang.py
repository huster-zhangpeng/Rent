# -*- coding: utf-8 -*-
import scrapy


class SoufangSpider(scrapy.Spider):
    name = "soufang"
    allowed_domains = ["zu.fang.com"]
    start_urls = (
        'http://www.http://zu.fang.com/house-a00/a21-c25000-d28000-g23-h316-n31/',
    )

    def parse(self, response):
        pass
