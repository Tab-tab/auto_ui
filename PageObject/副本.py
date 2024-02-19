#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
项目管理页面
"""
# 页面元素对象层
from selenium.webdriver import ActionChains
from Base.base import Base
from Common.readelement import Element
from Base.times import sleep
from PageObject import login_page

# 引入元素数据源
date_project = Element('superuser_config')


# 元素层
class ProjectListElement:
    def __init__(self, driver):
        self.driver = driver

    def common_ele(self, locator):
        ele = Base(self.driver).find_element(locator)
        return ele


# 操作层
class ProjectOperation:
    def __init__(self, driver):
        self.driver = ProjectListElement(driver)
        self.driver = driver

    def ddd(self):
        pass


# 页面层
class ProjectPage:
    def __init__(self, driver):
        self.driver = ProjectOperation(driver)


    def kkk(self):
        pass