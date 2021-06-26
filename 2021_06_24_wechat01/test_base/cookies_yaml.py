# -*- coding = utf-8 -*-
# @time:2021/6/26 17:00
# Author:Leo
# @File:cookies_yaml.py
# @Software:PyCharm
"""
读写cookies的方法
"""
import yaml


class TestCookies:
    # path = "E:\\Home_Work\\webautotest01\\test_data\\cookies.yaml"

    def get_cookies(self, file):
        with open(file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def cookies_file(self, data, file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data=data, stream=f)


if __name__ == '__main__':
    pass
