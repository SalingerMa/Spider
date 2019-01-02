# -*- coding: utf-8 -*-
from Spider.DownloadBook import MingYueBook
import requests
from bs4 import BeautifulSoup
import threadpool
class download():
    # 获取页面HTML的soup
    def get_html(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        return soup

    def get_bookcode(self, url):
        soup = self.get_html(url)
        book_soup = soup.find("div", attrs={"class": "cover"}).find_all("a")
        bookcode = (str(str(i["href"]).split("/")[-1]).split(".")[0] for i in book_soup)
        return bookcode


base_url = "http://www.cyuedu.com/quanben/1"
bookcode = download().get_bookcode(base_url)
pool = threadpool.ThreadPool(5)
req = threadpool.makeRequests(MingYueBook().run, bookcode)
[pool.putRequest(r) for r in req]
pool.wait()