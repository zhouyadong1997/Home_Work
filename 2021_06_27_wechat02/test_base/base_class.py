# -*- coding = utf-8 -*-
# @time:2021/6/27 17:51
# Author:Leo
# @File:base_class.py
# @Software:PyCharm

"""
    完成对selenium的二次封装，
    如打开浏览器、定位元素、点击元素等等
"""
from selenium import webdriver
from logging import debug, info, error

from selenium.webdriver.remote.webdriver import WebDriver

from test_base.base_yaml import BaseYaml


class BaseClass:

    # 初始化
    def __init__(self, driver_base: WebDriver = None):

        # 第一部分：打开企业微信网页，扫码登录，获取cookies
        self.opt = webdriver.ChromeOptions()
        self.opt.debugger_address = "127.0.0.1:9222"
        self.driver_opt = webdriver.Chrome(options=self.opt)
        self.driver_opt.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies_opt = self.driver_opt.get_cookies()
        # 将cookies以yaml文件的格式保存
        self.y = BaseYaml()
        self.y.get_file(cookies_opt, file_path=r"E:\Home_Work\2021_06_27_wechat02\test_data\cookies.yaml")

        if driver_base is None:
            # 第二次登陆
            self.driver = webdriver.Chrome()
            info("实例化webdriver")
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            info("浏览器全屏显示")
            self.driver.maximize_window()
            self.driver.implicitly_wait(12)
            cookies = self.y.get_yaml(r"E:\Home_Work\2021_06_27_wechat02\test_data\cookies.yaml")

            info("遍历cookies，添加到selenium中")
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver = driver_base

    # 打开浏览器二次封装
    def get(self, url):
        info("打开url", url)
        self.driver.get(url)

    # 定位元素
    def find_element(self, location):
        debug("开始进行元素定位", location)
        try:
            element = self.driver.find_element(*location)
        except Exception as e:
            error("元素定位失败:", e)
        else:
            info("元素定位成功，return对象")
            return element

    # send_keys
    def send_keys(self, location, value):
        info("开始传值")
        self.find_element(location).send_keys(value)

    # click
    def click(self, location):
        info("开始点击元素", location)
        self.find_element(location).click()

    def quit(self):
        info("关闭所有浏览器")
        self.driver.quit()

    def close(self):
        info("关闭当前浏览器")
        self.driver.close()

    # 隐私等待
    def implicitly_wait(self, t):
        info("隐私等待时间为{0}s".format(t))
        self.driver.implicitly_wait(t)
