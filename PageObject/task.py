#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
企业管理列表页面
"""
# 页面元素对象层
from selenium.webdriver import ActionChains
from Base.base import Base
from Common.readelement import Element
from Base.times import sleep
from PageObject import login_page

# 引入元素数据源
date_task = Element('task_page')


# 元素层
class TaskListElement:
    def __init__(self, driver):
        self.driver = driver

    def common_ele(self, locator):
        # 通用元素
        ele = Base(self.driver).find_element(locator)
        return ele



# 操作层
class TaskListOperation:
    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.Task_list_Oper = TaskListElement(driver)
        self.driver = driver

    # ========登录操作-可复用==========
    def input_username(self, username):
        # 对用户名输入框做clear和send_keys操作
        ele_user = date_task["用户账号框"]
        self.Task_list_Oper.common_ele(ele_user).clear()
        self.Task_list_Oper.common_ele(ele_user).send_keys(username)

    def input_password(self, password):
        # 对密码输入框做clear和send_keys操作
        ele_password = date_task["用户密码框"]
        self.Task_list_Oper.common_ele(ele_password).clear()
        self.Task_list_Oper.common_ele(ele_password).send_keys(password)

    def click_login_btn(self):
        # 对登录按钮做点击操作
        ele_button = date_task["登录按钮"]
        self.Task_list_Oper.common_ele(ele_button).click()

    # ==============正式表单-类型为技术报告====================
    def click_add_btn(self):
        # 对用户名输入框做clear和send_keys操作
        ele_add_list = date_task["展开任务数据新建下拉框"]
        ele_add = date_task["任务数据新建按钮"]
        self.Task_list_Oper.common_ele(ele_add_list).click()
        self.Task_list_Oper.common_ele(ele_add).click()


    def input_task_name(self, task_name):
        # 输入任务数据名称
        ele_task_name = date_task["输入任务数据名称"]
        self.Task_list_Oper.common_ele(ele_task_name).clear()
        self.Task_list_Oper.common_ele(ele_task_name).send_keys(task_name)

    def section_model(self):
        # 选择所属机型
        ele_model_section = date_task["展开所属机型下拉框"]
        ele_model = date_task["选中所属机型"]
        self.Task_list_Oper.common_ele(ele_model_section).click()
        self.Task_list_Oper.common_ele(ele_model).click()
        sleep(0.5)

    def section_document_template(self):
        # 选择文档模板
        ele_document_section = date_task["展开文档模板下拉框"]
        ele_document = date_task["选中文档模板"]
        self.Task_list_Oper.common_ele(ele_document_section).click()
        self.Task_list_Oper.common_ele(ele_document).click()
        sleep(0.5)

    def section_development_phase(self):
        # 选择研制阶段
        ele_development_section = date_task["展开研制阶段下拉框"]
        ele_development = date_task["选中研制阶段"]
        self.Task_list_Oper.common_ele(ele_development_section).click()
        self.Task_list_Oper.common_ele(ele_development).click()

    def section_integral_file_type(self):
        # 选择积分文件类型
        ele_integral_file_type_section = date_task["展开积分文件类型下拉框"]
        ele_integral_file_type = date_task["选中积分文件类型"]
        ele_integral_file_type_define = date_task["积分文件类型对话框确定"]
        self.Task_list_Oper.common_ele(ele_integral_file_type_section).click()
        self.Task_list_Oper.common_ele(ele_integral_file_type).click()
        self.Task_list_Oper.common_ele(ele_integral_file_type_define).click()
        sleep(0.5)

    def section_application_number(self):
        # 选择申请编号
        ele_application_number_section = date_task["展开申请编号下拉框"]
        ele_application_number = date_task["选中申请编号类型"]
        self.Task_list_Oper.common_ele(ele_application_number_section).click()
        self.Task_list_Oper.common_ele(ele_application_number).click()
        sleep(1)

    def section_encoding_rules(self):
        # 选择编码规则
        ele_encoding_rules_section = date_task["展开编码规则下拉框"]
        ele_encoding_rules = date_task["选中编码规则类型"]
        self.Task_list_Oper.common_ele(ele_encoding_rules_section).click()
        self.Task_list_Oper.common_ele(ele_encoding_rules).click()
        sleep(2)

    # 所属方案、描述...... pass

    def click_task_define(self):
        # 点击确定按钮
        ele_define = date_task["任务数据新建对话框确定"]
        self.Task_list_Oper.common_ele(ele_define).click()

    def find_add_Task_after(self):
        # 验证数据有没有存在
        ele_Task_after = date_task["任务数据列表数据验证"]
        return self.Task_list_Oper.common_ele(ele_Task_after).text

    def select_task_list(self, number):
        # 选中任务数据列表下的数据
        ele_select_task = date_task["任务数据列表数据选中"].format(str(number))
        return self.Task_list_Oper.common_ele(ele_select_task).click()

    def click_setting_security(self):
        # 点击设置密级按钮
        ele = date_task["展开密级控制下拉框"]
        ele_ = date_task["点击设置数据密级按钮"]
        self.Task_list_Oper.common_ele(ele).click()
        self.Task_list_Oper.common_ele(ele_).click()

    def select_security(self):
        # 点击设置密级按钮
        ele = date_task["展开密级下拉框"]
        ele_ = date_task["选中密级类型"]
        self.Task_list_Oper.common_ele(ele).click()
        self.Task_list_Oper.common_ele(ele_).click()

    def click_security_define(self):
        # 点击密级对话框确定按钮
        ele = date_task["密级对话框确定按钮"]
        self.Task_list_Oper.common_ele(ele).click()



# 页面业务层面
class TaskPage:
    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.Task_page = TaskListOperation(driver)

    def login_common(self, username, password):
        self.Task_page.input_username(username)
        self.Task_page.input_password(password)
        self.Task_page.click_login_btn()
        sleep(0.5)

    def add_Task(self, task_name):
        # 添加企业,13个操作
        self.Task_page.click_add_btn()
        self.Task_page.input_task_name(task_name)
        self.Task_page.section_model()
        self.Task_page.section_document_template()
        self.Task_page.section_development_phase()
        self.Task_page.section_integral_file_type()
        self.Task_page.section_application_number()
        self.Task_page.section_encoding_rules()
        self.Task_page.click_task_define()
        sleep(3)


if __name__ == "__main__":
    # 调试
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time, TaskPage


    chromedriver = "../Driver/chromedriver.exe"

    driver = webdriver.Chrome(executable_path=chromedriver)
    driver.maximize_window()
    # driver.implicitly_wait(20)
    # 访问登录页
    driver.get("http://172.16.205.10/eap")
    url_task_page = "172.16.205.10/p2m/p2m-web/departmentPlanPages/department_plan_detail.html?planId=202204171538470008232a418ca8057f4d0c8d6b&currentType=yearMount&name=Auto计划&jurisdiction=true"

    """
    用户账号框: 'xpath==//*[@id="loginName"]'
    用户密码框: 'xpath==//*[@id="loginPassword"]'
    登录按钮: 'xpath==//*[@id="submit"]'
    """

    driver.find_element_by_xpath('//*[@id="loginName"]').send_keys("hz_shizhuren")

    driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys("123456")

    click_ele = '//*[@id="submit"]'
    # driver.find_element_by_xpath(click_ele).click()
    driver.find_element(By.XPATH, click_ele).click()

    time.sleep(3)
    print("==================123456789===================")

    # 新用例部分

    driver.get(url_task_page)

    sleep(3)
    driver.quit()
