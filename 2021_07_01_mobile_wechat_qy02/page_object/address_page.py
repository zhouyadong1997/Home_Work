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

    @allure.title("进入增加成员页面")
    def goto_add_user(self):
        from page_object.hand_add import HandAdd
        with allure.step("全局滑动点击添加成员"):
            info("全局滑动点击添加成员")
            self.qjhd_search("添加成员")
            info("进入添加成员页面")
        return HandAdd(self.driver)

    @allure.title("获取通讯录所有成员信息")
    def get_user(self):
        # com.tencent.wework:id/df9
        with allure.step("获取所有的人员名单"):
            info("获取所有的人员名单")
            elements = self.find_elements(self.__users)
            users = [ele.text for ele in elements if ele.text != "添加成员"]
            time.sleep(3)
            info(f"所有成员和部门信息为{users}")
        return users

    @allure.title("删除成员")
    def remove_user(self, name):
        from page_object.personal_Information import PersonalInformation
        """
        删除联系人
        :return:
        """
        # 滑动查找，删除name
        with allure.step(f"滑动查找，删除{name}"):
            self.qjhd_search(name)
        return PersonalInformation(self.driver)
