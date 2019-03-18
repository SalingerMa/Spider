# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import requests
import os
from hashlib import md5
import re
from multiprocessing.pool import Pool

# 获取网页内容，返回JSON数据
def get_page(offset):
    params = {
        'aid': 24,
        'offset': offset,
        'format': 'json',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = "https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D" + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

# 解析返回的JSON数据，以字典的形式提取照片的URL和title，并返回一个生成器
def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                origin_image = re.sub('list', 'origin', image.get('url'))
                yield {
                    'image': origin_image,
                    'title': title
                }

# 保存图片
def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')

    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            # 图片的名称使用其内容的MD5值，这样可以去除重复
            file_name = '{name}.{suffix}'.format(name=md5(response.content).hexdigest(), suffix='jpg')
            file_path = img_path + os.path.sep + file_name
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)

# 主函数，输入OFFSET，下载照片
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 7

if __name__ == '__main__':
    # 使用多线程的线程池，调用其map()方法实现多线程下载
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])  # 构造一个offset数组，遍历offset
    pool.map(main, groups)
    pool.close()
    pool.join()
