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


class TestAddUser():

    def setup_class(self):
        print("开始执行测试用例")

    def teardown_class(self):
        HomePage().driver.quit()
        info("用例执行结束，释放资源")

    @allure.story("添加新的成员")
    @pytest.mark.parametrize("username, phone_number", [
        ["马超", 15171791007], ["马岱", 15171791008]], ids=["add machao", "add madai"])
    def test_add_user(self, username, phone_number):
        users = HomePage().goto_address().goto_add_user().hand_add().add_user(username,
                                                                              phone_number).get_user()
        print("当前users", users)
        assert username in users
        info(username, " 添加成功")

    @allure.story("添加已存在的成员")
    @pytest.mark.parametrize("username, phone_number", [
        ["张飞", 15171791003], ["赵云", 15171791004]], ids=["add zhangfei", "add zhaoyun"])
    def test_add_repetition_user(self, username, phone_number):
        text = HomePage().goto_address().goto_add_user().hand_add().repetition_user(username, phone_number)

        assert "手机已存在于通讯录，无法添加" == text
