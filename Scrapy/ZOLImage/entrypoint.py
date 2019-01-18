# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'book'])
execute(['scrapy', 'crawl', 'zolimage', '--nolog', '-a', 'tag=fengjing'])
