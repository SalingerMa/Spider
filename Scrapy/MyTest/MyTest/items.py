# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()

class BooksToScrapeItem(scrapy.Item):

    name = scrapy.Field()
    price = scrapy.Field()



class ForeignBookItem(BooksToScrapeItem):
    translator = scrapy.Field()
