# -*- coding: utf-8 -*-
import scrapy
import json
from Ximalaya.items import XimalayaItem
import re

class XimalayaSpider(scrapy.Spider):
    name = 'ximalaya'
    allowed_domains = ['ximalaya.com']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    pageNum = 1

    def get_url(self, albumId, pageNum=None):
        baseurl = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}"
        if pageNum == None:
            url = baseurl.format(str(albumId), str(1))
        else:
            url = baseurl.format(str(albumId), str(pageNum))
        return url

    def start_requests(self):
        albumId = getattr(self, 'albumId', None)
        if albumId is not None:
            url = self.get_url(albumId)
            yield scrapy.Request(url, self.parse, headers=self.headers, meta={'albumId': albumId})

    def parse(self, response):
        albumData = json.loads(response.text)
        item = XimalayaItem()
        for track in albumData['data']['tracksAudioPlay']:
            item['trackId'] = track['trackId']
            item['trackName'] = track['trackName']
            item['albumId'] = track['albumId']
            item['albumName'] = track['albumName']
            item['trackUrl'] = track['src']
            yield item

        if albumData['data']['hasMore'] == True:
            self.pageNum += 1
            albumId = response.meta['albumId']
            next_url = self.get_url(albumId, self.pageNum)
            yield scrapy.Request(next_url, self.parse, headers=self.headers, meta={'albumId': albumId})
