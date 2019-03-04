# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import re

def download_video(data_id):
    url = "http://www.meipai.com/media/{}".format(data_id)
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")
    try:
        # get_video_url
        _div = soup.find("img", attrs={"class": "pa pai"})
        video_vid = re.findall("meitudata.com/(.*).jpg", str(_div))
        video_url = "http://mvvideo10.meitudata.com/{}.mp4".format(video_vid[0])
        # get video name
        name_div = soup.find("h1", attrs={"class": "detail-cover-title break js-convert-emoji"})
        video_name = str(name_div.text).split()[0]
        video_name1 = re.sub("\?|。|！|！|》|《", "", video_name)
        # download video
        req = requests.get(video_url, headers=headers)
        with open("./video/{}.mp4".format(video_name1), "ab") as f:
            print("下载成功：%s" % video_name1)
            f.write(req.content)
    except:
        print("error--------------------error")
        error_list.append(n)

def get_data_id():
    data_ids = []
    for j in range(5):
        url = "http://www.meipai.com/topics/hot_timeline?page={}&count=24&tid=5872239354896137479&maxid=1040739667".format(j+1)
        req = requests.get(url, headers=headers)
        r = json.loads(req.content)["medias"]
        for i in r:
            data_ids.append(i["id"])

    return data_ids

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    n = 0
    error_list = []
    data_ids = get_data_id()
    for i in data_ids:
        n += 1
        download_video(i)
    if error_list != None:
        print("error:", error_list)
    else:
        print("all download")