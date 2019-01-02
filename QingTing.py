# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import re
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

def get_page(channel):
    _url = "http://www.qingting.fm/channels/{}".format(channel)
    _req = requests.get(_url, headers=headers)
    _soup = BeautifulSoup(_req.content, "html.parser")
    _ul = _soup.find("ul", attrs={"class": "pagination"})
    _a = _ul.find_all("a", attrs={"class": "_2k3q"})
    max_page = _a[-1].text

    return max_page

def get_file_name(channel):
    _url = "http://www.qingting.fm/channels/{}".format(channel)
    _req = requests.get(_url, headers=headers)
    _soup = BeautifulSoup(_req.content, "html.parser")
    _div = _soup.find("div", attrs={"class": "_33eu _2lyJ"})
    _h1 = _div.find("h1", attrs={"class": "_3h7q"})
    file_name = _h1.text
    return file_name

def Qingting(channel):
    _page = get_page(channel)
    for q in range(int(_page)):
        start_url = "http://i.qingting.fm/wapi/channels/{}/programs/page/{}/pagesize/10".format(channel, q+1)
        req = requests.get(start_url, headers=headers)
        r = json.loads(req.content)
        mp3_data = []
        for i in r["data"]:
            one_data = {}
            one_data["name"] = i["name"]
            one_data["url"] = "http://upod.qingting.fm/{}".format(i["file_path"])
            mp3_data.append(one_data)

        for j in mp3_data:
            _data = requests.get(j["url"], headers=headers)
            _name = re.sub('\?|:|"|', "", j["name"])
            file_name = get_file_name(channel)
            file_path = r"C:\Users\mhm\Desktop\book\{}".format(file_name)
            existed = os.path.exists(file_path)
            if not existed:
                os.makedirs(file_path)
            try:
                with open("{}\{}.m4a".format(file_path, _name), "ab") as f:
                    print(_name)
                    f.write(_data.content)
            except:
                print("error------------------------------error")

if __name__ == '__main__':
    # 下载蜻蜓FM的一个专辑
    channel = input("enter channel:")
    print("start download ...")
    Qingting(channel)
