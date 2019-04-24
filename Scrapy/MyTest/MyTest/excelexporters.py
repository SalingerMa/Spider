# -*- coding: utf-8 -*-
from scrapy.exporters import BaseItemExporter
import xlwt

class ExcelExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file = file
        




    def export_item(self, item):


    def start_exporting(self):
        pass

    def finish_exporting(self):
        pass
