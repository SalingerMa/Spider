# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import random
import re


def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        ip_td = ip_info.find_all("td")
        ip = ip_td[1].text + ":" + ip_td[2].text
        speed = re.findall("width:(.*)%", str(ip_td[6]))[0]
        link_time = re.findall("width:(.*)%", str(ip_td[7]))[0]
        alive_time = ip_td[8].text
        if int(speed) < 90 or int(link_time) < 90 or "分钟" in alive_time:
            pass
        else:
            ip_list.append(ip)
    return ip_list

def get_random_ip(ip_list):
    proxy_ip = random.choice(ip_list)
    proxies = {'http': proxy_ip}
    return proxies


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    url = 'http://www.xicidaili.com/nn/'
    ip_list = get_ip_list(url, headers=headers)
    print(ip_list)
    proxies = get_random_ip(ip_list)
    print(proxies)





