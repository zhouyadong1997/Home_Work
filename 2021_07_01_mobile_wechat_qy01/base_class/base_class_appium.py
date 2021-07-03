# -*- coding = utf-8 -*-
# @time:2021/7/3 15:36
# Author:Leo
# @File:base_class_appium.py
# @Software:PyCharm

"""
    对appnium基本方法的二次分装，如click、find_element等
"""
from logging import error

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BaseClassAppium:

    # 打开手机APP
    def __init__(self, driver_base: WebDriver = None):
        desired_caps = {
            "settings[waitForIdleTimeout]": 0,  # 等待应用闲置时间
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '9',  # 手机安卓版本
            'deviceName': 'Mi9',  # 设备名，安卓手机可以随意填写
            'appPackage': 'com.tencent.wework',  # 启动APP Package名称
            'appActivity': '.launch.LaunchSplashActivity',  # 启动Activity名称
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'noReset': True,  # 不要重置App
            "skipDeviceInitialization": True,  # 跳过设备初始化
            'newCommandTimeout': 6000,  # 在假定客户端退出并结束会话之前，Appium将等待来自客户端的新命令（以秒为单位）
            'automationName': 'UiAutomator2'  # 使用哪个自动化引擎
            # 'app': r'd:\apk\bili.apk',
        }
        if driver_base == None:
            # appium server和手机建立连接，并向appium server传递字典对象（包含手机与APP信息）
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
        else:
            self.driver = driver_base
        self.driver.implicitly_wait(12)

    # appium的二次封装
    def find_element(self, location):
        try:
            element = self.driver.find_element(*location)
        except Exception as e:
            error("元素定位失败：", e)
        else:
            return element

    def find_elements(self, location):
        try:
            elements= self.driver.find_elements(*location)
        except Exception as e:
            error("元素定位失败：", e)
        else:
            return elements

    # 传值
    def send_keys(self, location, value):
        self.find_element(location).send_keys(value)

    # 滑动添加成员
    def qjhd_search(self,text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("{0}").instance(0));'.format(text)).click()
