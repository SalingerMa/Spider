# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from dingdian.items import DingdianItem

class BookSpider(scrapy.Spider):

    name = 'book'
    allowed_domains = ['x23us.com']
    end_url = ".html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"}

    def start_requests(self):
        url = 'https://www.x23us.com/class/3_1.html'
        yield Request(url, callback=self.parse)

    def parse(self, response):
        max_num = response.css("div.pagelink a.last::text").extract_first()
        base_url = response.url[:-7]
        for i in range(int(max_num)):
            newurl = base_url + "_" + str(i+1) + self.end_url
            yield Request(newurl, callback=self.get_bookurl, headers=self.headers)

    def get_bookurl(self, response):
        book_list = response.xpath("//tr[@bgcolor='#FFFFFF']")
        for book in book_list:
            bookname = book.xpath(".//a[2]/text()").extract_first()
            bookurl = book.xpath(".//a[1]/@href").extract_first()
            bookid = str(bookurl).split("/")[-1]

            yield Request(bookurl, callback=self.get_bookinfo, meta={
                'bookname': bookname,
                'bookid': bookid,
            })

    def get_bookinfo(self, response):
        bookinfo = response.xpath("//table[@bgcolor='#E4E4E4']")
        category = bookinfo.xpath(".//tr[1]/td[1]/a/text()").extract_first()
        author = bookinfo.xpath(".//tr[1]/td[2]/text()").extract_first()
        serialstatus = bookinfo.xpath(".//tr[1]/td[3]/text()").extract_first()
        serialtime = bookinfo.xpath(".//tr[2]/td[3]/text()").extract_first()

        item = DingdianItem()
        item['name'] = response.meta["bookname"]
        item['author'] = str(author).strip()
        item["serialstatus"] = str(serialstatus).strip()
        item["serialtime"] = str(serialtime).strip()
        item["category"] = category
        item["bookid"] = response.meta["bookid"]

        # yield item
        if len(item["bookid"]) == 3:
            bookurl = "https://www.x23us.com/html/0/%s/" % str(item["bookid"])
        else:
            bookurl = "https://www.x23us.com/html/%s/%s/" %(str(item["bookid"])[:2], str(item["bookid"]))
        yield Request(bookurl, callback=self.get_chapterurl, headers=self.headers)

    def get_chapterurl(self,response):




