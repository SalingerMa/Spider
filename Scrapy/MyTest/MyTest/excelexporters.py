# -*- coding: utf-8 -*-
from scrapy.exporters import BaseItemExporter
import xlwt
import xlsxwriter
import re

class ExcelExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file = file
        self.wbook = xlwt.Workbook()
        self.wsheet = self.wbook.add_sheet('scrapy')
        self.row = 0
        self._headers_not_written = True

    def finish_exporting(self):
        self.wbook.save(self.file)

    def export_item(self, item):
        fields = self._get_serialized_fields(item)  # 调用基类方法获取item所有字段的迭代器
        if self._headers_not_written:
            self._headers_not_written = False
            for col, v in enumerate(x for x, _ in fields):
                self.wsheet.write(self.row, col, v)

        for col, v in enumerate(x for _, x in fields):
            self.wsheet.write(self.row, col, v)
        self.row += 1

