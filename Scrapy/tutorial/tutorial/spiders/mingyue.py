# -*- coding: utf-8 -*-
import scrapy


class MingyueSpider(scrapy.Spider):
    name = 'mingyue'
    allowed_domains = ['cyuedu.com']
    start_urls = ['http://cyuedu.com/']

    def parse(self, response):
        pass
