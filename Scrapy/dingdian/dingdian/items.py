# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 书名
    author = scrapy.Field()  # 作者
    serialstatus = scrapy.Field()  # 本书状态：更新或完结
    serialtime = scrapy.Field()  # 更新时间
    category = scrapy.Field()  # 分类
    bookid = scrapy.Field()  # 本书编号ID

class ChapterItem(scrapy.Item):
    chaptername = scrapy.Field()
    chaptercontent = scrapy.Field()
    book_id = scrapy.Field()
    num_id = scrapy.Field()
    chapterurl = scrapy.Field()

