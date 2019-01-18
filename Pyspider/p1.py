import re
import requests
from bs4 import BeautifulSoup

url="https://www.douban.com/"
headers = {'Cookie':'ll="108288"; bid=YpUGN5tyMNQ; __yadk_uid=vz4gFAsQ0XmUNuAhFpAQVjHqZHNrxZQJ; _vwo_uuid_v2=D7025139B266475FF505706A46508F94E|e23588dc8d194f7356007c5c12c93b86; __utmc=30149280; ps=y; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18987; douban-profile-remind=1; _ga=GA1.2.970738635.1542850189; _gid=GA1.2.1107384109.1547108873; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1547111767%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DxJtphneI5792wB7hsIRjB71kvWb6gtbLhQFGYkMKk4nDQREbJg-M2q2gBaFnzo6w%26wd%3D%26eqid%3D9a2a73da00012936000000035c370d54%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.970738635.1542850189.1547107540.1547111768.7; __utmz=30149280.1547111768.7.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_id.100001.8cb4=2adcb6f1206793ff.1542938497.6.1547111894.1547108869.; __utmb=30149280.3.10.1547111768; _gat_UA-7019765-1=1; dbcl2="189870745:qYsqXMM6sM0"',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
html=requests.get(url, headers=headers)
a = re.findall('kkk', str(html.text))
print(a)
