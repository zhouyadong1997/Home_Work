# -*- coding = utf-8 -*-
# @time:2021/7/3 15:45
# Author:Leo
# @File:test_add_user.py
# @Software:PyCharm
"""
    添加用户
"""
from logging import info

import allure
import pytest
from page_object.home_page import HomePage
from base_class.base_class_appium import BaseClassAppium


class TestAddUser():

    def setup_class(self):
        self.b = BaseClassAppium()
        info("开始执行测试用例")

    def setup(self):
        info("打开APP")
        self.b.driver.launch_app()

    def teardown(self):
        info("回到手机桌面")
        self.b.back(5)

    def teardown_class(self):
        self.b.quit()
        info("用例执行结束，释放资源")

    @allure.story("添加新的成员")
    @pytest.mark.parametrize("username, phone_number", [
        ["许攸", 151717910012], ["吕布", 15171791011]], ids=["add xuyou", "add lvbu"])
    def test_add_user(self, username, phone_number):
        toast_text = self.b.goto_home().goto_address().goto_add_user().hand_add().add_user(username,
                                                                                           phone_number)
        info(f"当前page_source{toast_text}")
        assert toast_text == "添加成功"

    @allure.story("添加已存在的成员")
    @pytest.mark.parametrize("username, phone_number", [
        ["马超", 15171791007], ["马岱", 15171791009]], ids=["add machao", "add madai"
                                                        ])
    def test_add_repetition_user(self, username, phone_number):
        text = self.b.goto_home().goto_address().goto_add_user().hand_add().repetition_user(username, phone_number)

        assert "手机已存在于通讯录，无法添加" == text

    @allure.story("删除成员")
    @pytest.mark.parametrize("name", ["曹操"])
    def test_del_user(self, name):
        users = self.b.goto_home().goto_address().remove_user(name).goto_edit().edit_user().get_user()
        assert name not in users
