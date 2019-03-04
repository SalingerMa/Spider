# -*- coding: utf-8 -*-
# 本段代码是爬取喜马拉雅免费的音频，根据专辑号来爬取

import requests
import json
import re
import os
import sys
from time import sleep
import argparse
import win32api, win32con

class Common():
    @classmethod
    def get_desktop(self):
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                                  r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', 0,
                                  win32con.KEY_READ)
        return win32api.RegQueryValueEx(key, 'Desktop')[0]
    @classmethod
    def make_dir(self, file_path):
        result = '{}'
        try:
            if not os.path.exists(file_path):
                result = "[新建文件夹] {}"
                os.makedirs(file_path)
            else:
                result = '[文件夹已存在] {}'
        except:
            result = '[创建文件夹失败] {}'
        finally:
            print(result.format(file_path))

class ArgParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-i', '--xid', help='专辑ID', required=True)
        self.parser.add_argument('-p', '--path', help='下载路径，默认下载到桌面')
        self.args = self.parser.parse_args()

class Ximalaya():
    def __init__(self):
        args = ArgParser().args
        id_ = args.xid
        path_ = args.path
        self.id = id_
        self.dpath = path_ if path_ != None else Common.get_desktop()
        self.page = 1
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        self.baseurl = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}"
        self.key = True
        self.album = ''
        self.loop_one_code = True

    def get_json_data(self, url):
        try:
            req = requests.get(url, headers=self.headers)
            return json.loads(req.content)
        except:
            print('requests请求失败')

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
        _url = self.baseurl.format(self.id, self.page)
        albumData = self.get_json_data(_url)
        self.key = albumData['data']['hasMore']
        m4a_data = albumData['data']["tracksAudioPlay"]

        if self.loop_one_code:
            self.album = m4a_data[0]['albumName']
            file_path = self.dpath + "\%s" % self.album
            Common.make_dir(file_path)
            self.loop_one_code = False

        for track in m4a_data:
            sleep(0.5)
            self.download(track["trackName"], track["src"])

        if self.key:
            self.page += 1
            self.get_m4a()

if __name__ == '__main__':
    Ximalaya().get_m4a()
    # python ximalaya.py -i 11219907 -p C:\Users\saler\Desktop --page 3
    # 




