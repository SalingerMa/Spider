# -*- coding: utf-8 -*-
from .sql import SQL
from dingdian.items import DingdianItem

class DingdianPinelines(object):

    def process_item(self, item, spider):
        if isinstance(item, DingdianItem):
            xs_name = item['name']
            bookid = item["bookid"]
            ret = SQL.select_book(bookid)
            if ret == 1:
                print("《%s》已存在！" % xs_name)
                pass
            else:

                xs_author = item['author']
                status = item["serialstatus"]
                updatetime = item["serialtime"]
                category = item["category"]
                SQL.insert_bookinfo(xs_name,xs_author,bookid,category,status,updatetime)
                print("开始存储小说《%s》的信息。。。" % xs_name)