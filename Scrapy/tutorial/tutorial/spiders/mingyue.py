# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MingyueSpider(CrawlSpider):
    name = 'mingyue'
    allowed_domains = ['cyuedu.com']
    start_urls = ['http://www.cyuedu.com/xiaoshuosort1/0/1.html']
    rules = (
        Rule(LinkExtractor(allow=".html", ), callback="parse_item"),
    )

    def parse_item(self, response):
        self.logger.info("this is %s",response.url)
