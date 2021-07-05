# -*- coding = utf-8 -*-
# @time:2021/7/5 21:01
# Author:Leo
# @File:edit_user.py
# @Software:PyCharm
from logging import info

import allure

from base_class.base_class_appium import BaseClassAppium
from appium.webdriver.common.mobileby import MobileBy


class EditUser(BaseClassAppium):
    """
    点击编辑成员，删除成员
    """
    __edit_user = (MobileBy.ID, "com.tencent.wework:id/b5r")
    __confirm = (MobileBy.ID, "com.tencent.wework:id/bg8")

    def edit_user(self):
        with allure.step("点击编辑成员"):
            from page_object.address_page import AddressPage
            info("点击编辑成员")
        with allure.step("滑动查找删除成员"):
            self.find_element(self.__edit_user).click()
            info("滑动查找删除成员")
        with allure.step("滑动查找删除成员"):
            self.qjhd_search("删除成员")
        with allure.step("滑动查找删除成员"):
            info("确定删除成员")
            self.find_element(self.__confirm).click()

        return AddressPage(self.driver)
