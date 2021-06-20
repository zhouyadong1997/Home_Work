"""
创建一个计算器
"""
from decimal import *

class Calculator:
    def add(self, a, b):
        return a + b

    def jianfa(self, a, b):
        return a - b

    def chengfa(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


if __name__ == '__main__':
    c = Calculator()