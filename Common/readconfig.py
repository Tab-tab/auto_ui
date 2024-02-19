#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import configparser
from Config.conf import cm

HOST = 'HOST'
HOST_9 = 'HOST_9'
DATA = 'DATA'
DRIVERPATH = 'DRIVERPATH'


class ReadConfig(object):
    """配置文件"""

    def __init__(self):
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)

    @property
    def url_9(self):
        return self._get(HOST_9, HOST_9)

    @property
    def get_data(self):
        return self._get(DATA, DATA)

    @property
    def get_driver_path(self):
        return self._get(DRIVERPATH, DRIVERPATH)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
