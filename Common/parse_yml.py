#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import yaml

'''
通过传递文件名，section和key，取yml文件中的内容
value = parse_yml('my_yaml_3.yml', 'websites', 'URL')
'''

#
# def parse_yml(file, section, key):
#     with open(file, 'r', encoding='utf8') as f:
#         data = yaml.load(f, Loader=yaml.FullLoader)
#         return data[section][key]


def parse_yml(file, section):
    with open(file, 'r', encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data[section]


if __name__ == '__main__':
    pass
