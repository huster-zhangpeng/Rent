# -*- coding: utf-8 -*-
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = "anjuke"
    allowed_domains = ["bj.zu.anjuke.com"]
    start_urls = (
        'http://www.http://bj.zu.anjuke.com/fangyuan/haidian/fx3-je6000-js4000-l2-px3/',
    )

    def parse(self, response):
        pass
