# -*- coding = utf-8 -*-
# @time:2021/7/19 19:21
# Author:Leo
# @File:base_api.py
# @Software:PyCharm

"""
    基础API封装
    包含token获取，
"""
import requests
from logging import info

class BaseApi:
    CORP_ID = "ww1ae11d7d07084a17"
    CORP_SECRET = "-qzY50acSAJLzxBIixR3Pi4ytIoFzacp-GTKeLV8crc"
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        info("开始初始化，获取token")
        self.token = self.get_token()

    def get_token(self):
        url = f"{self.BASE_URL}gettoken?corpid={self.CORP_ID}&corpsecret={self.CORP_SECRET}"
        self.token = requests.get(url).json().get("access_token")
        return self.token

    def send_request(self, method, url, **kwargs):
        """
        requests.request 为get、post的底层实现
        :param method: 请求方法名，如get、post
        :param url: 请求路由
        :param kwargs: 其他参数
        :return:
        """
        url = self.BASE_URL + url
        return requests.request(method, url, **kwargs)
