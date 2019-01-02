# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
url = "http://upgrade.g.mi.srv/upgrade/get"
dr.get(url)
dr.implicitly_wait(10)
all_frame = dr.find_elements_by_tag_name("iframe")
dr.switch_to.frame(all_frame[0])
dr.find_element_by_id("update_btn").click()
sleep(1)