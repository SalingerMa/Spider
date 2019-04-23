# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MongoPipeline(object):
    def __init__(self, mongo_host, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_host=crawler.settings.get('MONGO_HOST'),
                   mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item




class MytestPipeline(object):
    def process_item(self, item, spider):
        return item
