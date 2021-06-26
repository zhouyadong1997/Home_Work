# -*- coding = utf-8 -*-
# @time:2021/6/26 16:28
# Author:Leo
# @File:test_wechat_linkman.py
# @Software:PyCharm
"""
步骤：
     1.打开复用功能，扫码登录企业微信，获取cookies
     2.打开新的网页，添加联系人
     3.使用复用实现绕过扫码登录
     4.使用yaml参数化
"""
import time
import pytest
import yaml
from selenium import webdriver
from logging import info, debug
from test_base.cookies_yaml import TestCookies
import allure

@allure.feature("企业微信")
class TestWechatLinkman:
    g = TestCookies()

    @allure.story("企业微信复用")
    @allure.title("企业微信复用")
    def test_wechat_fy(self):
        # 第一部分：打开企业微信网页，扫码登录，获取cookies
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver_opt = webdriver.Chrome(options=opt)
        driver_opt.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies_opt = driver_opt.get_cookies()
        # 将cookies以yaml文件的格式保存
        self.g.cookies_file(cookies_opt, file_path="E:\\Home_Work\\webautotest01\\test_data\\cookies.yaml")

    path = r"E:\Home_Work\webautotest01\test_data\user.yaml"

    @allure.story("增加联系人")
    @allure.testcase("https://work.weixin.qq.com/wework_admin/frame")
    @pytest.mark.parametrize("username, username2, zhanghao, phone_number",
                             TestCookies().get_cookies(path)["user"]
        , ids=TestCookies().get_cookies(path)["ids"])
    def test_add_linkman(self, username, username2, zhanghao, phone_number):
        # 第二部分：参数化实现批量添加联系人
        with allure.step("实例化webdriver对象"):
            info("实例化webdriver对象")
            driver = webdriver.Chrome()
            driver.implicitly_wait(10)

        with allure.step("打开企业微信", ):
            info("打开企业微信")
            driver.get("https://work.weixin.qq.com/wework_admin/frame")

        with allure.step("浏览器最大化"):
            info("浏览器最大化")
            driver.maximize_window()

        with allure.step("获取cookies"):
            cookies = self.g.get_cookies("E:\\Home_Work\\webautotest01\\test_data\\cookies.yaml")
            info("获取cookies")

        with allure.step("遍历cookies，添加到selenium中"):
            info("遍历cookies，添加到selenium中")
            for cookie in cookies:
                driver.add_cookie(cookie)

        with allure.step("再次登录企业微信"):
            info("再次登录企业微信")
            driver.get("https://work.weixin.qq.com/wework_admin/frame")

        with allure.step("点击通讯录"):
            driver.find_element_by_id("menu_contacts").click()
            time.sleep(2)

        with allure.step("点击添加成员"):
            info("点击添加成员")
            driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()

        with allure.step("填写姓名"):
            info("填写姓名:{0}".format(username))
            driver.find_element_by_id("username").send_keys(username)
            time.sleep(1)

        with allure.step("填写别名"):
            driver.find_element_by_id("memberAdd_english_name").send_keys(username2)
            time.sleep(1)
            # 输入账号
            driver.find_element_by_css_selector("#memberAdd_acctid").send_keys(zhanghao)
            time.sleep(1)
            # 输入手机号
            driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys(phone_number)
            time.sleep(1)

        with allure.step("截图"):
            info("进行截图")
            # 对搜索后的页面进行截图
            driver.save_screenshot("E:\\Home_Work\\webautotest01\\test_png\\{0}.png".format(username))
            # 将保存后的截图，添加到测试报告中
            allure.attach.file("E:\\Home_Work\\webautotest01\\test_png\\{0}.png".format(username),
                               attachment_type=allure.attachment_type.PNG)

        with allure.step("将滚动条移动到页面的底部"):
            info("将滚动条移动到页面的底部")
            js = "var q=document.documentElement.scrollTop=100000"
            driver.execute_script(js)
            time.sleep(3)

        with allure.step("点击保存"):
            info("点击保存")
            driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
            time.sleep(2)

        with allure.step("进行断言"):
            eles = driver.find_elements_by_xpath(
                "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[5]")
            phone_numbers = [i.text for i in eles]
            # 断言手机号码是不是在列表中
            assert phone_number in phone_numbers

        with allure.step("退出当前浏览器"):
            info("退出当前浏览器")
            driver.close()
