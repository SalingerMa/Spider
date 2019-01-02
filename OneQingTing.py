# -*- coding: utf-8 -*-
import requests
import re
import json

def get_web_json(url):
    req = requests.get(url, headers=headers)
    r = json.loads(req.content)
    return r

def get_json_data(web_json):
    json_data = []
    for i in web_json:
        one_data = {}
        one_data["name"] = i["name"]
        one_data["url"] = "http://upod.qingting.fm/{}".format(i["file_path"])
        json_data.append(one_data)
    return json_data

def download_data(name, url):
    _data = requests.get(url, headers=headers)
    _name = re.sub('\?|\:', "", name)
    try:
        with open("./{}.m4a".format(_name), "ab") as f:
            print(_name)
            f.write(_data.content)
    except:
        print("error-----------------------------------------error")

def OneQingTing(channel, page, row):
    start_url = "http://i.qingting.fm/wapi/channels/{}/programs/page/{}/pagesize/10".format(channel, page)
    req_json = get_web_json(start_url)
    mp3_data = get_json_data(req_json["data"])
    j = mp3_data[int(row)-1]
    download_data(j["name"], j["url"])

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    print("--下载蜻蜓FM单曲音频--")
    channel = input("enter channel:")
    page = input("enter page:")
    row = input("enter row:")
    print("start download ...")
    OneQingTing(channel, page, row)




