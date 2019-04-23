# -*- coding: utf-8 -*-
import scrapy
from ..items import BookItem

class CyueduSpider(scrapy.Spider):
    name = 'cyuedu'
    allowed_domains = ['cyuedu.com']
    start_urls = ['http://www.cyuedu.com/xiaoshuosort7/0/1.html']
    base_url = 'http://www.cyuedu.com'

    def parse(self, response):
        books = response.css('.line')
        item = BookItem()
        for book in books:
            item['url'] = self.base_url + book.css('a::attr(href)').extract_first()
            item['name'] = book.css('a::text')[1].extract()
            item['author'] = book.css('span::text').extract_first()
            yield item

        pageNum, countNum = response.css(".page::text").re('\(第(\d*)\/(\d*)页\)')
        if int(pageNum) != int(countNum):
            next_url = self.base_url + response.xpath("//a[contains(text(), '下页')]/@href").extract_first()
            yield scrapy.Request(next_url, callback=self.parse)

