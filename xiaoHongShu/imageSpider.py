# -*- coding: utf-8 -*-
from requests_html import HTMLSession
import re
session = HTMLSession()

url = "https://www.xiaohongshu.com/discovery/item/5ca09cba000000000e02808e"

r = session.get(url)

html = r.html
title = html.find('title')[0].text
images = html.find('.slide li span')
for image in images:
    imageStyle = image.attrs['style']
    imageUrl = 'http:' + re.search('background-image:url\((.*?)\);', imageStyle).group(1)
    print(imageUrl)
    imageR = session.get(imageUrl)
    imageName = re.findall('.com/(.*?)\?', imageUrl)[0]
    print(imageName)
    with open('./%s/%s.jpg' % (title, imageName), 'ab') as f:
        f.write(imageR.content)
