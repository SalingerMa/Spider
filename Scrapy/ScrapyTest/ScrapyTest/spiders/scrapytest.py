# -*- coding: utf-8 -*-
import scrapy


class ScrapytestSpider(scrapy.Spider):
    name = 'scrapytest'
    allowed_domains = ['scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        print(response.url)
        next_page = response.css('li.next a::attr(href)').extract_first()
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)

            yield scrapy.Request(next_page, callback=self.parse)
