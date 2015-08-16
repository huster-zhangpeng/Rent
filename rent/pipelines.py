# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.mail import MailSender

class RentPipeline(object):
    collection_name = 'house'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get("MONGO_URI"),
            mongo_db = crawler.settings.get("MONGO_DATABASE", "items")
        )

    def open_spider(self, spider):
        self.mailer = MailSender(smtphost="smtp.exmail.qq.com",
                                 mailfrom="xxx@xx.com",
                                 smtpuser="xxx@xx.com",
                                 smtppass="xxxxx")
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        row = {}
        row['id'] = item['id'][0]
        row['title'] = item['title'][0].strip()
        row['link'] = item['link'][0]
        doc = self.db[self.collection_name].find({"id": row['id']})
        if doc.count() == 0:
            self.mailer.send(to=["zhangpeng@exatech.cn", "huangzhiwu@exatech.cn"],
                             subject=u"［新房源］".encode('utf-8') + row['title'].encode('utf-8'),
                             body=u"［链接地址］".encode('utf-8') + row['link'])
            self.db[self.collection_name].insert(row)
        else:
            print "has exist", row['id']
        return item
