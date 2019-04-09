# -*- coding: utf-8 -*-
"""
目的：获取熊猫直播的LOL直播间排名：等级、姓名、人数

"""

import re
from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/cjzc?pdt=1.24.s1.59.2hahede8gvc'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 获取HTML
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    # 数据分析提取
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    # 数据精炼提取
    def __data_refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }
        return map(l, anchors)

    # 数据排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_key, reverse=True)
        return anchors

    # 数据排序键
    def __sort_key(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    # 数据排序展示
    def __data_show(self, anchors):
        anchors_data = []
        for rank in range(0, len(anchors)):
            anchor_data = {}
            anchor_data["rank"] = str(rank + 1)
            anchor_data["name"] = anchors[rank]["name"]
            anchor_data["number"] = anchors[rank]['number']
            anchors_data.append(anchor_data)
            data = str(rank + 1) + ': ' + anchors[rank]['name'] + '   ' + anchors[rank]['number']
            print(data)
        return anchors_data

    # 执行函数
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__data_refine(anchors))
        anchors = self.__sort(anchors)
        anchors_data = self.__data_show(anchors)
        return anchors_data

Spider().go()
