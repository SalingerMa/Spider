# -*- coding: utf-8 -*-
import scrapy
from enum import Enum

class Enumitem(Enum):
    xuanhaun = 1
    wuxia = 2
    quanben = 0
print(Enumitem['quanben'].name)
class MingyueSpider(scrapy.Spider):
    name = 'mingyue'
    allowed_domains = ['cyuedu.com']
    start_urls = ['http://cyuedu.com/']
    def start_requests(self):
        base_url = 'http://cyuedu.com/'
        tag = getattr(self, 'tag', None)
        if  tag is not None:
            if Enumitem.tag.name == 'quanben':
                url = 'http://www.cyuedu.com/quanben/1'

    def parse(self, response):
        pass
