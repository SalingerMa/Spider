# -*- coding: gbk -*-
import scrapy

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    start_urls = [
        "http://www.dmoztools.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        # �����ʦ��Ϣ�ļ���
        # items = []
        # for each in response.xpath("//div[@class='li_txt']"):
        #     # �����ǵõ������ݷ�װ��һ�� `ItcastItem` ����
        #     item = ItcastItem()
        #     # extract()�������صĶ���unicode�ַ���
        #     name = each.xpath("h3/text()").extract()
        #     title = each.xpath("h4/text()").extract()
        #     info = each.xpath("p/text()").extract()
        #
        #     # xpath���ص��ǰ���һ��Ԫ�ص��б�
        #     item['name'] = name[0]
        #     item['title'] = title[0]
        #     item['info'] = info[0]
        #
        #     items.append(item)
        #
        # # ֱ�ӷ����������
        # return items

