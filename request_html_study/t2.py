# -*- coding: utf-8 -*-
from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

async def get_pythonorg():
    r = await asession.get('https://python.org/')
    return r
async def get_google():
    r = await asession.get('https://google.com/')
    return r

result = asession.run(get_google, get_pythonorg)
print(result)