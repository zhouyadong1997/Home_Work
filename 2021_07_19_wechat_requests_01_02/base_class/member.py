# -*- coding = utf-8 -*-
# @time:2021/7/19 19:32
# Author:Leo
# @File:member.py.py
# @Software:PyCharm
"""
access_token	是	调用接口凭证。获取方法查看“获取access_token”
userid	是	成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。
name	是	成员名称。长度为1~64个utf8字符
alias	否	成员别名。长度1~32个utf8字符
mobile	否	手机号码。企业内必须唯一，mobile/email二者不能同时为空
department	是	成员所属部门id列表,不超过100个
"""

from logging import error, info
from base_class.base_api import BaseApi


class Member(BaseApi):

    def add(self, userid: str, name: str, mobile: str, department=None):
        """
        添加成员
        :param userid: 成员UserID。对应管理端的帐号
        :param name: 成员名字
        :param mobile: 成员手机号（手机号邮箱二者必须要填一个）
        :param department: 成员列表
        :return:
        """
        info(f"添加成员{name}，userid为{userid}")
        if department is None:
            info("department is None, default value is [1]")
            department = [1]
        url = f"user/create?access_token={self.token}"
        data = {
            "userid": str(userid),
            "name": str(name),
            "mobile": str(mobile),
            "department": department
        }
        info("发送post请求，返回response")
        return self.send_request("POST", url, json=data)

    def delete(self, userid: str):
        """
        删除成员
        :param userid: 成员UserID。对应管理端的帐号
        :return:
        """
        info(f"删除成员，成员id为{userid}")
        url = f"user/delete?access_token={self.token}&userid={userid}"
        info("发送get请求，返回response")
        return self.send_request("GET", url)

    def update(self, userid: str, **kwargs: dict):
        """
        更新成员信息
        :param userid: 成员UserID。对应管理端的帐号
        :param kwargs: 更新的数据 or 非必填数据
        :return:
        """
        info(f"更新成员，成员id为{userid}")
        url = f"user/update?access_token={self.token}"
        json = {
            "userid": userid,
        }
        json.update(kwargs)
        re = self.send_request("POST", url, json=json)
        return re

    def get(self, userid: str):
        """
        获取成员的所有信息
        :param userid: 成员UserID。对应管理端的帐号
        :return:
        """
        info(f"添加成员{userid}")
        url = f"user/get?access_token={self.token}&userid={userid}"
        re = self.send_request("GET", url)
        return re


if __name__ == '__main__':
    m = Member()
    # print(m.delete("MaChao").json())
    # print(m.update().json())
    # # print(m.add().json())
    print(m.delete("MaDai01").json())
