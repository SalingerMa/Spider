# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from time import sleep
import pymongo
from pyquery import PyQuery as pq

MONGO_URL = 'localhost'
MONGO_DB = 'mingyueBook'
MONGO_COLLECTION = 'books'
KEYWORD = 1
MAX_PAGE = 8
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        base_url = 'http://www.cyuedu.com/xiaoshuosort{key}/0/{page}.html'
        url = base_url.format(key=KEYWORD, page=page)
        browser.get(url)
        if page > 1:
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            sleep(1)
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#pageinput')))
            submit = wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/input[2]')))
            input.clear()
            input.send_keys(page)
            submit.click()
        sleep(1)
        get_products()
    except TimeoutException:
        index_page(page)

def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = pq(html, parser="html")
    lines = doc('.line')
    for line in lines.items():
        url = line.find('a').attr('href')
        title = line.find('a').text()
        author = line.find('span').text()
        print(url, title, author)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')

def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    index_page(1)