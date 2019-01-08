# -*- coding: utf-8 -*-
import scrapy
from ZOLImage.items import ZolimageItem
from ZOLImage.settings import USER_AGENT
import re

class ZolimageSpider(scrapy.Spider):
    name = 'zolimage'
    header = {'User-Agent': USER_AGENT}

    def start_requests(self):
        url = "http://desk.zol.com.cn/"
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + tag + '/'
        yield scrapy.Request(url, self.parse, headers=self.header)

    def parse(self, response):
        img_list = response.css('li.photo-list-padding a::attr(href)').extract()
        for url in img_list:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.get_img_info, headers=self.header)
        next_page = response.css('#pageNext::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, headers=self.header)

    def get_img_info(self, response):
        name = str(response.css('title::text').extract_first()).split("-")[0]
        max_screen = response.xpath('//dd[@id="tagfbl"]/a[1]/text()').extract_first()
        img_list = response.css('#showImg img::attr(src)').extract() + response.css('#showImg img::attr(srcs)').extract()
        new_img_list = [str(img).replace(re.findall('t_s(.*?)c5', img)[0], max_screen) for img in img_list]
        item = ZolimageItem()
        item['name'] = name
        item['imgurl'] = new_img_list
        return item
