#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
登录页
'''

# 页面元素对象层
from selenium.webdriver import ActionChains
from Base.base import Base
from Common.readelement import Element
from Base.times import sleep


# 引入元素数据源
date_login = Element('base_page')


class LoginEle(object):
    def __init__(self, driver):
        # 私有方法
        self.driver = driver

    def find_username(self, locator):
        # 查找并返回用户名输入框元素

        ele = Base(self.driver).find_element(locator)
        return ele

    def find_password(self, locator):
        # 查找并返回密码输入框元素
        ele = Base(self.driver).find_element(locator)
        return ele

    def find_login_btn(self, locator):
        # 查找并返回登录按钮元素
        ele = Base(self.driver).find_element(locator)
        return ele

    def find_login_name(self, locator):
        # 查找并返回登录后的用户名元素
        ele = Base(self.driver).find_element(locator)
        return ele

    def find_login_after(self, locator):
        # 查找并返回登录后的用户名元素
        ele = Base(self.driver).find_element(locator)
        return ele

    # def find_login_failed_info(self, locator):
    #     # 查找并返回登录失败后的提示信息元素
    #     ele = Base(self.Driver).get_element('xpath,flash_error')
    #    return ele


# 页面元素操作层
class LoginOper(object):
    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.login_Oper = LoginEle(driver)
        self.driver = driver

    def input_username(self, username):
        # 对用户名输入框做clear和send_keys操作
        ele_user = date_login["用户账号框"]
        self.login_Oper.find_username(ele_user).clear()
        self.login_Oper.find_username(ele_user).send_keys(username)

    def input_password(self, password):
        # 对密码输入框做clear和send_keys操作
        ele_password = date_login["用户密码框"]
        self.login_Oper.find_password(ele_password).clear()
        self.login_Oper.find_password(ele_password).send_keys(password)

    def click_login_btn(self):
        # 对登录按钮做点击操作
        ele_button = date_login["登录按钮"]
        self.login_Oper.find_login_btn(ele_button).click()

    # def click_login_btn(self):
    #     # 对登录按钮做双击操作
    #     ele = self.login_page.find_login_btn()
    #     ActionChains(self.Driver).double_click(ele).perform()

    def get_login_name(self):
        # 返回登录后的用户名元素的文字
        ele_user_now = date_login["当前登录用户"]
        return self.login_Oper.find_login_name(ele_user_now).text

    def find_login_after(self):
        # 以登录成功的出现"模块目录"文本做校验
        ele_model = date_login["模块目录"]
        return self.login_Oper.find_login_name(ele_model).text

    # def get_login_failed_info(self):
    #     # 返回登录失败后提示信息的文字
    #     return self.login_page.find_login_failed_info().text


# 页面业务场景层
class LoginPage(object):
    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.login_page = LoginOper(driver)
        self.driver = driver

    def login(self, username, password):
        # 定义一个登录场景，用到了3个操作
        # sleep()
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login_btn()


if __name__ == "__main__":
    from selenium import webdriver
    import time
    chromedriver = "../Driver/chromedriver.exe"

    driver = webdriver.Chrome(executable_path=chromedriver)
    driver.maximize_window()
    driver.implicitly_wait(20)
    # 访问登录页
    driver.get("http://172.8.10.128/#/")

    user_ele = '//*[@id="loginName"]'

    driver.find_element_by_xpath(user_ele).send_keys("hz_shizhuren")

    password_ele = '//*[@id="loginPassword"]'

    driver.find_element_by_xpath(password_ele).send_keys("123456")

    click_ele = '//*[@id="submit"]'
    driver.find_element_by_xpath(click_ele).click()

    time.sleep(3)
    print("==================123456789===================")
    driver.quit()

