# -*- coding = utf-8 -*-
# @time:2021/7/3 15:39
# Author:Leo
# @File:home_page.py
# @Software:PyCharm

"""
    企业微信：主页相关操作
        1.主页->通讯录
        2.主页->工作台
"""
import time
from logging import info
import allure
from base_class.base_class_appium import BaseClassAppium
from appium.webdriver.common.mobileby import MobileBy


@allure.feature("主页面")
class HomePage(BaseClassAppium):
    # 通讯录
    __txl = (MobileBy.XPATH, '//*[@text="通讯录"]')

    @allure.title("进入通讯录页面")
    def goto_address(self):
        """
        主页->通讯录
        :return: AddressPage(self.driver)
        """
        from page_object.address_page import AddressPage
        with allure.step("主页"):
            info("当前页面：企业微信主页")
        time.sleep(1)
        with allure.step("点击通讯录"):
            info("点击通讯录")
            self.find_element(self.__txl).click()
        with allure.step("进入通讯录页面"):
            info("进入通讯录页面")
        return AddressPage(self.driver)
