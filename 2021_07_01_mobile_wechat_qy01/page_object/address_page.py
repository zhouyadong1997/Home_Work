# -*- coding = utf-8 -*-
# @time:2021/7/3 15:43
# Author:Leo
# @File:address_page.py
# @Software:PyCharm

"""
    企业微信：主页相关操作
        1.通讯录->添加成员
"""
import time
from logging import info

import allure
from appium.webdriver.common.mobileby import MobileBy

from base_class.base_class_appium import BaseClassAppium


@allure.feature("通讯录页面")
class AddressPage(BaseClassAppium):
    __users = (MobileBy.CLASS_NAME, "android.widget.TextView")
    def goto_add_user(self):
        from page_object.hand_add import HandAdd
        with allure.step("全局滑动点击添加成员"):
            info("全局滑动点击添加成员")
            self.qjhd_search("添加成员")
            info("进入添加成员页面")
        return HandAdd(self.driver)

    def get_user(self):
        # com.tencent.wework:id/df9
        info("获取所有的人员名单")
        users = self.find_elements(self.__users).text
        return users

