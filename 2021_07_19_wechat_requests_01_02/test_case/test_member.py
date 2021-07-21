# -*- coding = utf-8 -*-
# @time:2021/7/19 21:44
# Author:Leo
# @File:test_member.py
# @Software:PyCharm

from base_class.member import Member
from logging import error, info
from faker import Faker
import allure
import pytest


@allure.feature("通讯录-增删改查")
class TestMember:

    @allure.title("开始准备前置条件")
    @allure.story("开始准备前置条件")
    def setup_class(self):
        info("实例化成员接口对象：Member()")
        self.m = Member()
        info("实例化Faker对象,并将人员信息归属地设置成中国")
        self.faker = Faker(locale='zh_CN')

    @allure.title("所有测试用例执行完毕，恢复环境")
    @allure.story("所有测试用例执行完毕，恢复环境")
    def teardown_class(self):
        info("所有测试用例执行完毕，恢复环境")
        pass

    @allure.title("添加成员")
    @allure.story("添加成员")
    def test_add_member(self):
        with allure.step("添加成员"):
            info("添加成员")
            re = self.m.add(userid=self.faker.bban(), name=self.faker.name(),
                            mobile=self.faker.phone_number())
        with allure.step("进行断言"):
            info("进行断言")
            assert re.json().get('errcode') == 0
            assert re.status_code == 200

    @allure.title("删除成员")
    @allure.story("删除成员")
    @pytest.mark.parametrize("userid", [
        "JCDL37922103811952", "KLXB65939475907302", "NKLL10047395214863"
    ])
    def test_delete_member(self, userid):
        """
        删除成员信息
        :param userid:成员UserID。对应管理端的帐号
        :return:删除成员后的response对象
        """
        with allure.step("delete成员"):
            re = self.m.delete(userid)
            info(f"发送请求，进行删除成员{userid}")
        with allure.step("进行断言"):
            info("进行断言")
            assert re.json().get("errcode") == 0
            assert re.status_code == 200

    @allure.title("更新成员")
    @allure.story("更新成员")
    def test_update_member(self):
        """
        更新成员信息
        :return: 更新成员后的response对象
        """
        with allure.step("添加成员"):
            info("添加成员")
            userid = self.faker.bban()
            self.m.add(userid=userid, name=self.faker.name(),
                       mobile=self.faker.phone_number())
        with allure.step("更新成员信息"):
            info("更新成员信息")
            re2 = self.m.update(userid=userid, name=self.faker.name())
        with allure.step("进行断言"):
            info("进行断言")
            assert re2.json().get("errcode") == 0
            assert re2.status_code == 200

    @allure.title("获取成员信息")
    @allure.story("获取成员信息")
    @pytest.mark.parametrize("userid", [
        "IEJC89868771140512", "CVYL48947731480257", "DGKU56100056788894"
    ])
    def test_get_member(self, userid):
        """
        获取成员信息
        :param userid: 成员UserID。对应管理端的帐号，企业内必须唯一。
        :return:获取成员信息后的response对象
        """
        with allure.step("获取成员信息"):
            re = self.m.get(userid)
            info(f"发送请求，获取成员{userid}信息")
        with allure.step("进行断言"):
            assert re.json().get("errcode") == 0
            assert re.status_code == 200
