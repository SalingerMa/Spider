# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'

    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        for movie in movies:
            item = MovieItem()
            item["name"] = movie.xpath('h5/a/@title').extract()[0]
            yield item

MeijuSpider()