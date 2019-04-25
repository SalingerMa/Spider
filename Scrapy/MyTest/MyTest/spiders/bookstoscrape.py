# -*- coding: utf-8 -*-
import scrapy
from ..items import BooksToScrapeItem
from scrapy.linkextractor import LinkExtractor

class BookstoscrapeSpider(scrapy.Spider):
    name = 'bookstoscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            item = BooksToScrapeItem()
            item['name'] = book.xpath('./h3/a/@title').extract_first()
            item['price'] = book.css('p.price_color::text').extract_first()
            yield item
        # next_page = response.css('ul.pager li.next a::attr(href)').extract_first()
        # if next_page:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
        # le = LinkExtractor(restrict_css="ul.pager li.next a")
        # links = le.extract_links(response)
        # if links:
        #     next_url = links[0].url
        #     yield scrapy.Request(next_url, callback=self.parse)