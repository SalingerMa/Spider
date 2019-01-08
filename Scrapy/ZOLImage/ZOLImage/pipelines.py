# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from ZOLImage.items import ZolimageItem
from ZOLImage.spiders.zolimage import ZolimageSpider
from ZOLImage.settings import IMAGES_STORE
import requests
import os
from ZOLImage.settings import USER_AGENT

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
# 使用Scrapy自带方法获取图片
class ZolimagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        n = 0
        for url in item['imgurl']:
            n += 1
            yield Request(url, meta={'name':item['name'],'img': str(n) + '.jpg'})

    def file_path(self, request, response=None, info=None):
        name = request.meta['name']
        imgname = request.meta['img']
        filename = u'full/%s/%s' % (name, imgname)
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item


# 使用requests方法获取图片
# class ZolimagePipeline(object):
#
#     def process_item(self, item, spider):
#         if isinstance(item, ZolimageItem):
#             name = item['name']
#             dir_name = os.path.join(IMAGES_STORE, name)
#             existed = os.path.exists(dir_name)
#             if not existed:
#                 os.makedirs(dir_name)
#             else:
#                 print("文件%s已存在！" % name)
#             n = 1
#             for url in item['imgurl']:
#                 img = requests.get(url, headers=ZolimageSpider.header)
#                 with open('%s\%s\%s.jpg' % (IMAGES_STORE, name, n), 'wb') as f:
#                     f.write(img.content)
#                 n += 1
