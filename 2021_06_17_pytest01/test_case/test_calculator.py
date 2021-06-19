# encoding=utf-8
"""
针对计算器进行测试
"""
import pytest
from logging import info, debug, error
from test_base.calculator import Calculator
from test_base.get_yaml import GetYaml


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

    @pytest.mark.parametrize("a, b, expect", g["add_int"]["datas"],
                             ids=g["add_int"]["ids"])
    def test_add_int(self, a, b, expect):
        assert expect == self.c.add(a, b)

    @pytest.mark.parametrize("a, b, expect", g["add_float"]["datas"],
                             ids=g["add_float"]["ids"])
    def test_add_float(self, a, b, expect):
        assert expect == self.c.add(a, b)

    @pytest.mark.parametrize("a, b, expect", g["int_float"]["datas"],
                             ids=g["int_float"]["ids"])
    def test_add_int_float(self, a, b, expect):
        assert expect == self.c.add(a, b)

    @pytest.mark.parametrize("a, b, expect", g["number_str"]["datas"],
                             ids=g["number_str"]["ids"])
    def test_add_number_str(self, a, b, expect):
        try:
            assert expect == self.c.add(a, b)
        except Exception as e:
            print("字符串不能和数字相加", e)

    @pytest.mark.parametrize("a, b, expect", g["add_str"]["datas"],
                             ids=g["add_str"]["ids"])
    def test_add_str(self, a, b, expect):
        assert expect == self.c.add(a, b)

    @pytest.mark.parametrize("a, b, expect", g["div_int"]["datas"],
                             ids=g["div_int"]["ids"])
    def test_div_int(self, a, b, expect):
        assert expect == self.c.div(a, b)

    @pytest.mark.parametrize("a, b, expect", g["division_zero"]["datas"],
                             ids=g["division_zero"]["ids"])
    def test_div_division_zero(self, a, b, expect):
        try:
            assert expect == self.c.div(a, b)
        except Exception as e:
            print("0 不能作为除数", e)

    @pytest.mark.parametrize("a, b, expect", g["div_float"]["datas"],
                             ids=g["div_float"]["ids"])
    def test_div_float(self, a, b, expect):
        assert expect == self.c.div(a, b)

    @pytest.mark.parametrize("a, b, expect", g["divisor_zero"]["datas"],
                             ids=g["divisor_zero"]["ids"])
    def test_div_divisor_zero(self, a, b, expect):
        assert expect == self.c.div(a, b)
