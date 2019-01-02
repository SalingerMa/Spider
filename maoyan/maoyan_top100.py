# -*- coding: utf-8 -*-
import requests
import re
import json
import time

def get_one_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        return result.text
    return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = pattern.findall(html)
    for item in items:
        yield {
            "index": item[0],
            "image": item[1],
            "name": item[2],
            "actor": item[3].strip(),
            "time": item[4].strip()[5:],
            "score": item[5] + item[6],
        }
def write_to_file(content):
    with open("maoyan_top100.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)