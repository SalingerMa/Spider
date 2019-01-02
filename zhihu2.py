# -*- coding: utf-8 -*-
import requests
import scrapy
base_url = "https://www.zhihu.com/signup?next=%2F"
cookie_path = r"C:\Users\mhm\Desktop\test"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

session = requests.session()
session.get(base_url, headers=header, verify=False)
for i in session.cookies.items():
    print(i[1])
