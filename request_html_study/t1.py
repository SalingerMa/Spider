# -*- coding: utf-8 -*-
"""
requests-html学习：
获取书籍信息
"""
from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://www.qidian.com/free')
html = r.html

books = html.find('.book-img-text li')

for book in books:
    url = book.find('.book-mid-info > h4 > a')[0].attrs['href']
    name = book.find('.book-mid-info > h4 > a')[0].text
    author = book.find('.book-mid-info .author .name')[0].text

    bookinfo = {
        'name': name,
        'author': author,
        'url': url,
    }
    print(bookinfo)