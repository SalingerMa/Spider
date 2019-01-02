# -*- coding: utf-8 -*-
import requests
from lxml import etree
import re
from urllib.request import urlretrieve
#1 获取视频id
#2 拼接完整URL
#3 获取视频播放地址
#4 下载视频

def download(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    # url='http://www.pearvideo.com/category_9'
    #获取页面源代码
    html = requests.get(url, headers=headers).text
    #把文本文件处理成可解析的对象
    html=etree.HTML(html)
    video_id=html.xpath('//div[@class="vervideo-bd"]/a/@href')
    # 获取页面中所有的div//
    #列表
    video_url=[]
    starturl = 'http://www.pearvideo.com'

    # 拼接完整url
    for id in video_id:
        newurl=starturl+'/'+id
        video_url.append(newurl)

    # 获取视频播放地址
    for playurl in video_url:
        # 获取页面源代码
        html=requests.get(playurl).text
        # 正则匹配 .*?匹配所有
        req='srcUrl="(.*?)"'
        # 增加效率的
        # req=re.compile(req)
        # 视频真正的播放url
        purl=re.findall(req,html)
        # print(purl)
        print(purl[0])
        # 获取视频名称
        req='<h1 class="video-tt">(.*?)</h1>'
        pname=re.findall(req,html)
        print("正在下载视频:%s"%pname[0])
        # 下载的url 下载的地址
        urlretrieve(purl[0],'./video/%s.mp4'%pname[0])
url = "http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=1"

download(url)


def downloadmore():
    n=12
    while True:
        if n>48:
            # 跳出循环的
            return
        url = "http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=%d"%n
        n+=12
        download(url)
# downloadmore()