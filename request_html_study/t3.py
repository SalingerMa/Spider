# -*- coding: utf-8 -*-
import sys
import os
from yaml import load

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")


class ReadConfig:
    """ 读取各类YAM配置文件"""

    @staticmethod
    def get_conf(path_name):
        config_path = os.path.join(os.path.dirname(__file__), path_name)
        with open(config_path) as f:
            cont = f.read()
        return load(cont)

print(ReadConfig.get_conf(r'C:\Users\mhm\Desktop\WorkNote\test\config.ini'))