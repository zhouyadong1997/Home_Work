# -*- coding = utf-8 -*-
# @time:2021/7/5 20:52
# Author:Leo
# @File:personal_Information.py
# @Software:PyCharm
from logging import info

import allure

from base_class.base_class_appium import BaseClassAppium
from appium.webdriver.common.mobileby import MobileBy




class PersonalInformation(BaseClassAppium):
    """
    点击右上角三个点，进入个人信息编辑页面
    """
    __more_button = (MobileBy.ID, "com.tencent.wework:id/hc9")


    def goto_edit(self):
        with allure.step("点击右上角更多"):
            from page_object.edit_user import EditUser
            info("点击更多")
            self.find_element(self.__more_button).click()

        return EditUser(self.driver)
