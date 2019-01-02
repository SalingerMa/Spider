# -*- coding: utf-8 -*-
import urllib.request, http.cookiejar

filename = "cookies.txt"
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = "http://staging.authorize.zb.mi.srv/auth/index"
response = opener.open(url)
cookie.save(ignore_discard=True, ignore_expires=True)
