# -*- coding = utf-8 -*-
# @time:2021/7/3 15:50
# Author:Leo
# @File:hand_add.py
# @Software:PyCharm

"""
    企业微信：主页相关操作
        1.添加成员：
"""
import time
from logging import info

import allure
from appium.webdriver.common.mobileby import MobileBy

from base_class.base_class_appium import BaseClassAppium


@allure.feature("手动添加")
class HandAdd(BaseClassAppium):
    __hand_add = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
    @allure.title("手动添加")
    def hand_add(self):
        from page_object.add_user import AddUserPage
        with allure.step("点击手动添加"):
            info("点击手动添加")
            self.find_element(self.__hand_add).click()

        return AddUserPage(self.driver)
