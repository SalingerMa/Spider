# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import re
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

# 获取专辑信息
def get_album_info(album_id):
    guo_url = "https://www.ximalaya.com/xiangsheng/{}/".format(album_id)
    guo_req = requests.get(guo_url, headers=headers)
    guo_soup = BeautifulSoup(guo_req.content, "html.parser")
    # 获取专辑最大页数
    guo_div = guo_soup.find("div", attrs={"class": "dOi2 pagination"})
    guo_a = guo_div.find_all("span", attrs={"class": "Yetd"})
    max_page = guo_a[-1].text
    # 获取专辑名
    _div = guo_soup.find("div", attrs={"class": "_Zr5 info"})
    _h1 = _div.find("h1", attrs={"class": "_Zr5 title"})
    file_name = _h1.text
    # 返回页数和名字
    return max_page, file_name
# 在当前文件所在目录已专辑名新建文件
def make_album_dir(file_name):
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
# 主函数
def Xima(album_id):
    max_page, file_name = get_album_info(album_id)
    file_path = make_album_dir(file_name)
    for j in range(int(max_page)):
        start_url = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&sort=-1&pageSize=30".format(album_id, j+1)
        req = requests.get(start_url, headers=headers)
        _data = json.loads(req.content)
        m4a_data = []
        for i in _data["data"]["tracksAudioPlay"]:
            xima_data = {}
            xima_data["name"] = i["trackName"]
            xima_data["url"] = i["src"]
            m4a_data.append(xima_data)
        for i in m4a_data:
            one_data = requests.get(i["url"], headers=headers)
            _name = re.sub('\?|:|"|', "", i["name"])
            try:
                with open("{}/{}.m4a".format(file_path, _name), "ab") as f:
                    print(_name)
                    f.write(one_data.content)
            except:
                print("error-----------------------------------error")

if __name__ == '__main__':
    album_id = "11219907"
    print("start download ...")
    Xima(album_id)