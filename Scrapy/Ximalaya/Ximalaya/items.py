# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XimalayaItem(scrapy.Item):
    # define the fields for your item here like:
    albumName = scrapy.Field()
    albumId = scrapy.Field()
    trackId = scrapy.Field()
    trackName = scrapy.Field()
    trackUrl = scrapy.Field()
