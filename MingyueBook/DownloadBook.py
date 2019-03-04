# -*- coding: utf-8 -*-
"""
爬取明月中文小说网和云中小说网的小说
http://www.365if.com
爬取【云中书库http://m.yunxs.com/】的书需要：书名的汉语拼音，例如龙族5-->"longzu5"
"""
import re
import requests
from bs4 import BeautifulSoup
import os, sys, configparser
import random
from time import sleep
# get mingyuebook , need book's code ; like "79693" in "http://www.cyuedu.com/list/79/79693.html" ;
class MingYueBook():
    # 获取页面HTML的soup
    # proxies = [{'http': '119.101.113.176:9999'}, {'http': '119.101.112.48:9999'}, {'http': '111.177.168.80:9999'}]
    def get_html(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        sleep(0.3)
        return soup
    def get_config(self, option):
        iniFileUrl = r"C:\GitHub\Study\Spider\Spider.ini"
        conf = configparser.ConfigParser()  # 生成conf对象
        conf.read(iniFileUrl)  # 读取ini配置文件
        # return conf.get("DownloadBook", option)
        return r'C:\Users\mhm\Desktop\MingyueBook'
    # 将爬取内容写入文件
    def download(self, bookname, content, name):
        bookname = re.sub('\?|:|"| |\！|', "", bookname)
        filepath = self.get_config("filepath")
        existed = os.path.exists(filepath)
        if not existed:
            print("新建文件夹：%s" % (filepath))
            os.makedirs(filepath)
        with open(filepath+"\{}.txt".format(bookname), "a", encoding='utf-8') as f:
            f.write(content)
    # 获取书中章节的的链接和名称信息
    def get_capters_info(self, bookcode):
        name1 = bookcode[:-3]
        book_url = "http://www.365if.com/list/{}/{}.html".format(name1, bookcode)
        book_soup = self.get_html(book_url)
        bookname = str(book_soup.find("h1").contents[0]).split()[0]
        try:
            capters0 = book_soup.find("table", attrs={"class": "table_01"}).find_all("a")
        except AttributeError:
            capters0 = book_soup.find("td", attrs={"class": "L"})
        capters_info = [{"url": "http://www.cyuedu.com{}".format(i["href"]), "name": i.text} for i in capters0]
        return capters_info, bookname
    # 获取章节内要获取的信息，并调用函数来写入文件
    def get_capter_info(self, bookname, capter):
        capter_url = capter["url"]
        capter_name = capter["name"]
        capter_soup = self.get_html(capter_url)
        capter_div = capter_soup.find("div", attrs={"class", "block_02"})
        capter_content0 = str(capter_div).split('<div id="content">')[1].split('<div class="style3">')[0]
        capter_content = capter_name + "\n\n" + capter_content0.replace("<br/>", "\n") + "\n\n\n"
        self.download(bookname, capter_content, capter_name)

    # 主函数
    def run(self, bookcode):
        capters_info, bookname = self.get_capters_info(bookcode)
        n = 0
        key = len(capters_info)
        for capter in capters_info:
            self.get_capter_info(bookname, capter)
            sys.stdout.write("\r正在下载：《%s》，已下载章节数%s/%s" % (bookname, n, key))
            n+=1


# get YunZhongbook , need book's code ; like "longzu5" in "http://m.yunxs.com/longzu5/";
class YunZhongBook():

    # 获取页面内容
    def get_html(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")

        return soup
    # 在当前文件所在目录已专辑名新建文件
    def make_dir(self, file_name):
        try:
            file_path = "./{}".format(file_name)
            existed = os.path.exists(file_path)
            if not existed:
                print("新建文件夹：%s" % (file_name))
                os.makedirs(file_path)
            else:
                print("文件夹%s已存在！" % (file_path))
                return None
            return file_path
        except:
            return None

    # 下载
    def download(self, bookname, content, name):
        bookname = re.sub('\?|:|"| |\||', "", bookname)
        filepath = r"C:\Users\mhm\Desktop\YunZhongBook"
        existed = os.path.exists(filepath)
        if not existed:
            print("新建文件夹：%s" % (filepath))
            os.makedirs(filepath)
        with open(filepath+"\{}.txt".format(bookname), "a", encoding='utf-8') as f:
            print(name)
            f.write(content)

    # 获取页面中文字内容
    def get_page_content(self, soup):
        div1 = soup.find("div", attrs={"id": "chaptercontent"})
        cap_content0 = div1.text
        cap_content0 = str(cap_content0)
        cap_content1 = cap_content0.replace("云中书库阅读网址：m.yunxs.com", "")
        if re.findall("(1/2页)", cap_content1) != []:
            title = str(cap_content1.split("/2页)")[0].split("(第")[0]).strip()
            cap_content2 = cap_content1.split("/2页)")[1].strip()
            cap_content5 = cap_content2.replace(title, "")
            cap_content6 = cap_content5.replace("-->>(第1", "")
            cap_content3 = cap_content6.strip()
            a = 1
            return cap_content3
        elif re.findall("(2/2页)", cap_content1) != []:
            cap_content4 = cap_content1.split("/2页)")[1].rstrip()
            return cap_content4
        else:
            return cap_content1

    # 获取一章所有页的文字内容
    def get_all_page(self, bookname, url, name):
        soup = self.get_html(url)
        cap_content1 = self.get_page_content(soup)
        div1 = soup.find_all("a", attrs={"class": "Readpage_up"})[2]
        next_page = div1.text
        if next_page == "下一页":
            page2_url = "http://m.yunxs.com/{}/{}".format(url.split("/")[-2], div1["href"])
            page2_soup = self.get_html(page2_url)
            cap_content2 = self.get_page_content(page2_soup)
        else:
            cap_content2 = ""
        print_content = name + "\n\n" + cap_content1 + cap_content2 + "\n\n\n\n"
        self.download(bookname, print_content, name)

    # 获取书的信息：名称和每页的链接
    def get_book_info(self, url):
        soup = self.get_html(url)
        # 爬取书名
        div1 = soup.find("div", attrs={"class": "book_box"})
        bookname = div1.find("dt", attrs={"class": "name"}).text
        bookname = re.sub('\?|:|"| |\||', "", bookname)
        # 获取页数
        div4 = soup.find("div", attrs={"class": "listpage"})
        page = div4.find_all("option")
        pages_url = []
        for i in page:
            page_url = "http://m.yunxs.com{}".format(i["value"])
            pages_url.append(page_url)

        return bookname, pages_url

    # 获取每个章节的信息：URL和名字
    def get_capter_info(self, url):
        soup = self.get_html(url)
        div2 = soup.find_all("div", attrs={"class": "book_last"})[1]
        a2 = div2.find_all("a")
        cap_info = []
        for i in a2:
            data = {}
            data["url"] = "http://m.yunxs.com{}".format(i["href"])
            c = str(i.text)
            ex = c.split("、")[0] + "、"
            data["name"] = c.replace(ex, "")
            cap_info.append(data)
        return cap_info

    # 主函数
    def run(self, iname):
        url = "http://m.yunxs.com/{}/".format(iname)
        bookname, pages_url = self.get_book_info(url)
        self.make_dir("Downloads")
        for url in pages_url:
            cap_info = self.get_capter_info(url)
            for i in range(len(cap_info)):
                self.get_all_page(bookname, cap_info[i]["url"], cap_info[i]["name"])