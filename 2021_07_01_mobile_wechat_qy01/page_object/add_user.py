# -*- coding = utf-8 -*-
# @time:2021/7/3 15:54
# Author:Leo
# @File:add_user.py
# @Software:PyCharm
import time
from logging import info

import allure
from appium.webdriver.common.mobileby import MobileBy

from base_class.base_class_appium import BaseClassAppium


@allure.feature("添加用户页面")
class AddUserPage(BaseClassAppium):
    __user_name = (MobileBy.ID, "com.tencent.wework:id/b09")
    __phone_number = (MobileBy.ID, "com.tencent.wework:id/f7y")
    __bz = (MobileBy.ID, "com.tencent.wework:id/ad2")
    __repetition_text = (MobileBy.ID, "com.tencent.wework:id/bg4")
    __txl = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def add_user(self, username, phone_number):
        from page_object.address_page import AddressPage
        time.sleep(2)
        with allure.step("输入姓名"):
            info("输入姓名")
            self.send_keys(self.__user_name, username)
        with allure.step("输入手机号"):
            info("输入手机号")
            self.send_keys(self.__phone_number, phone_number)
        with allure.step("点击保存"):
            info("点击保存")
            self.find_element(self.__bz).click()

        with allure.step("进行截图"):
            info("进行截图")
            self.driver.save_screenshot(
                "E:\\Home_Work\\2021_07_01_mobile_wechat_qy01\\png\\{0}.png".format(self.__user_name))

        with allure.step("页面回退"):
            info("页面回退")
            self.driver.back()
            # self.driver.back()
        #
        # with allure.step("点击通讯录"):
        #     self.find_element(self.__txl)
        return AddressPage(self.driver)

    def repetition_user(self, username, phone_number):
        time.sleep(2)
        with allure.step("输入姓名"):
            info("输入姓名")
            self.send_keys(self.__user_name, username)
        with allure.step("输入手机号"):
            info("输入手机号")
            self.send_keys(self.__phone_number, phone_number)
        with allure.step("点击保存"):
            info("点击保存")
            self.find_element(self.__bz).click()
        with allure.step("进行截图"):
            self.driver.save_screenshot(
                "E:\\Home_Work\\2021_07_01_mobile_wechat_qy01\\png\\re_{0}.png".format(self.__user_name))
        with allure.step("获取已存在通讯录，无法添加的文本"):
            text = self.find_element(self.__repetition_text).text

        return text
