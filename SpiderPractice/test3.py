# -*- coding: utf-8 -*-
import http.cookiejar, urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load("cookies.txt", ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

url = "http://staging.authorize.zb.mi.srv/auth/index"

response = opener.open(url)
print(response.read().decode("utf-8"))
