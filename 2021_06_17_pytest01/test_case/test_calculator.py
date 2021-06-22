# encoding=utf-8
"""
针对计算器进行测试
    allure：装饰器
            1.fixture 模块名（类）
            2.story 子模块名（方法）
            3.title 测试用例标题
            4.step 关键步骤
            5.
"""
import pytest
import allure
from logging import info, debug, error
from test_base.calculator import Calculator
from test_base.get_yaml import GetYaml
from decimal import *

@allure.feature("计算器测试")
class TestCalculator:

    def setup_class(self):
        self.c = Calculator()

    def teardown_class(self):
        print("所有测试用例执行完毕，清理环境")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    path = "E:\\Home_Work\\2021_06_17_pytest01\\test_data\\calculator.yaml"
    g = GetYaml().get_yaml(path)

    @allure.testcase("https://www.baidu.com/","打开网页")
    @allure.story("整数之间的加法计算")
    @pytest.mark.parametrize("a, b, expect", g["add_int"]["datas"],
                             ids=g["add_int"]["ids"])
    def test_add_int(self, a, b, expect):
        assert expect == self.c.add(a, b)

    @allure.story("浮点数之间的加法计算")
    @pytest.mark.parametrize("a, b, expect", g["add_float"]["datas"],
                             ids=g["add_float"]["ids"])
    def test_add_float(self, a, b, expect):
        assert expect == round((self.c.add(a, b)), 10)

    @allure.story("整数和浮点数之间的加法计算")
    @pytest.mark.parametrize("a, b, expect", g["int_float"]["datas"],
                             ids=g["int_float"]["ids"])
    def test_add_int_float(self, a, b, expect):
        assert expect == self.c.add(a, b)

    @allure.story("数字和字符之间的加法计算")
    @pytest.mark.parametrize("a, b, expect", g["number_str"]["datas"],
                             ids=g["number_str"]["ids"])
    def test_add_number_str(self, a, b, expect):
        with pytest.raises(TypeError):
            self.c.add(a, b)

    @allure.story("字符串之间的加法计算")
    @pytest.mark.parametrize("a, b, expect", g["add_str"]["datas"],
                             ids=g["add_str"]["ids"])
    def test_add_str(self, a, b, expect):
        assert expect == self.c.add(a, b)

    @allure.story("整数之间的除法计算")
    @pytest.mark.parametrize("a, b, expect", g["div_int"]["datas"],
                             ids=g["div_int"]["ids"])
    def test_div_int(self, a, b, expect):
        assert expect == self.c.div(a, b)

    @allure.story("除数为0的除法计算")
    @pytest.mark.parametrize("a, b, expect", g["division_zero"]["datas"],
                             ids=g["division_zero"]["ids"])
    def test_div_division_zero(self, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            assert expect == self.c.div(a,b)


    @allure.story("浮点数之间的除法计算")
    @pytest.mark.parametrize("a, b, expect", g["div_float"]["datas"],
                             ids=g["div_float"]["ids"])
    def test_div_float(self, a, b, expect):
        assert expect == self.c.div(a, b)

    @allure.story("被除数为0的除法计算")
    @pytest.mark.parametrize("a, b, expect", g["divisor_zero"]["datas"],
                             ids=g["divisor_zero"]["ids"])
    def test_div_divisor_zero(self, a, b, expect):
        assert expect == self.c.div(a, b)
