# -*- coding: utf-8 -*-
import json
import pymongo
from mitmproxy import ctx

client = pymongo.MongoClient()
db = client['oupeng']
collection = db['books']


def response(flow: http.HTTPFlow):
    global collection
    url = 'http://zixun.oupeng.com/v1/fetch_novel'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('data')
        for book in books:
            data = dict(book)
            ctx.log.info(str(data))
            collection.insert(data)