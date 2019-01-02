# -*- coding: utf-8 -*-

from urllib import request, parse

url = "http://www.httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "Host": "httpbin/org"
}
dict = {
    "name": "Gremey"
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url, data=data, headers=headers, method="POST")
response = request.urlopen(req)

print(response.read().decode('utf-8'))




