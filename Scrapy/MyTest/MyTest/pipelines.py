# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem
from scrapy.item import Item

class MongoPipeline(object):
    def __init__(self, mongo_host, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongscrapyo_host=crawler.settings.get('MONGO_HOST'),
                   mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        collection = self.db[name]
        ifRepeat = self.db[name].find_one(dict(url=item['url']))
        if not ifRepeat:
            collection.insert_one(dict(item))
        else:
            raise DropItem('该书已存在：%s' % item['name'])

        return item

    def close_spider(self, spider):
        self.client.close()

class PriceConverterPipeline(object):
    rate = 8.53

    def process_item(self, item, spider):
        price = float(item['price'][1:]) * self.rate
        item['price'] = '￥%.2f' % price

        return item


class DuplicatesPipeline(object):
    def __init__(self):
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['name']
        if name in self.book_set:
            raise DropItem("Duplicate book found:%s" % name)
        self.book_set.add(name)
        return item

class MongoDBPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URI = crawler.settings.get('DB_URI', 'mongodb://localhost:27017/')
        cls.DB_NAME = crawler.settings.get('DB_NAME', 'scrapy_book2')
        return cls()


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URI)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item

class MytestPipeline(object):
    def process_item(self, item, spider):
        return item
