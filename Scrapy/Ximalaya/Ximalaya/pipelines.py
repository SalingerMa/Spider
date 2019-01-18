# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Ximalaya.items import XimalayaItem
import requests
from Ximalaya.spiders.ximalaya import XimalayaSpider
from Ximalaya.settings import DOWN_PATH
import re, os
class XimalayaPipeline(object):

    def process_item(self, item, spider):
        name = item['trackName']
        album = item['albumName']
        url = item['trackUrl']
        _name = re.sub('\?|:|"|', "", name)
        self.mkdir(album)
        req = requests.get(url, headers=XimalayaSpider.headers)
        with open(DOWN_PATH+'\{}\{}.m4a'.format(album, _name), 'ab') as f:
            f.write(req.content)

    def mkdir(self, name):
        try:
            file_path = DOWN_PATH + '/{}'.format(name)
            existed = os.path.exists(file_path)
            if not existed:
                os.makedirs(file_path)
            else:
                return None
            return file_path
        except:
            return None



