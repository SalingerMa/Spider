# -*- coding: utf-8 -*-
# 本段代码是爬取喜马拉雅免费的音频，根据专辑号来爬取

import requests
import json
import re
import os
import sys
from time import sleep

class Ximalaya():
    def __init__(self, id):
        self.id = id
        self.dpath = 'C:\work\pictures'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        self.baseurl = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}"
        self.page = 1
        self.key = ''
        self.album = ''
        self.get_m4a()

    def make_album_dir(self, file_name):
        file_path = self.dpath + "/{}".format(file_name)
        existed = os.path.exists(file_path)
        if not existed:
            print("新建文件夹：%s" % (file_name))
            os.makedirs(file_path)
        else:
            pass

    def test(self):
        start_url = self.baseurl.format(self.id, self.page)
        req = requests.get(start_url, headers=self.headers)
        albumData = json.loads(req.content)
        self.key = albumData['data']['hasMore']
        self.album = albumData['data']["tracksAudioPlay"][0]['albumName']
        return albumData['data']["tracksAudioPlay"]

    def get_info(self, albumData):
            for i in albumData:
                yield {'name': i["trackName"], "url": i["src"]}

    def download(self, name, url):
        _name = re.sub('\?|:|"|', "", name)
        req = requests.get(url, headers=self.headers)
        total_size = int(req.headers['Content-Length'])
        temp_size = 0
        with open(self.dpath + '\{}\{}.m4a'.format(self.album, _name), 'ab') as f:
            print('download:' + _name)
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    temp_size += len(chunk)
                    f.write(chunk)
                    f.flush()
                    #############花哨的下载进度部分###############
                    done = int(50 * temp_size / total_size)
                    sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                    sys.stdout.flush()
        print()

    def get_m4a(self):
        m4a_data = self.test()
        self.make_album_dir(self.album)
        for track in self.get_info(m4a_data):
            sleep(1)
            self.download(track['name'], track["url"])
        if self.key == True:
            self.page += 1
            self.get_m4a()
        else:
            pass

if __name__ == '__main__':
    album_id = "11219907"
    Ximalaya(album_id)


