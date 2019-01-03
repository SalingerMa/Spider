# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from tutorial.items import TutorialItem


class TestxmlfeedSpider(CSVFeedSpider):
    name = 'testxmlfeed'
    allowed_domains = ['cyuedu.com']
    start_urls = [r'file:///C:\Users\mhm\Desktop\study\test1.csv']
    delimiter = ','
    quotechar = "'"
    headers = ['id', 'name', 'desc']

    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row!: %r', row)
        item = TutorialItem
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item

