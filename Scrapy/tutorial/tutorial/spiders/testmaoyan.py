# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class TestmaoyanSpider(scrapy.Spider):
    name = 'testmaoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ["https://maoyan.com/board/4"]

    def parse(self, response):
        for movie in response.css("dd"):
            item = TutorialItem()
            item["index"] = movie.css("i.board-index::text").extract_first()
            item["name"] = movie.css("p.name a::text").extract_first()

            yield item
            # yield {
            #     "index": movie.css("i.board-index::text").extract_first(),
            #     "image": movie.css("img::attr(data-src)").extract_first(),
            #     "name": movie.css("p.name a::text").extract_first(),
            #     "star": str(movie.css("p.star::text").extract_first()).strip(),
            #     "time": str(movie.css("p.releasetime::text").extract_first())[5:],
            #     "score": str(movie.css("i.integer::text").extract_first())
            #              + str(movie.css("i.fraction::text").extract_first()),
            # }
