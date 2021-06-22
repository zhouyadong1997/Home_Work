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



@allure.feature("计算器测试")
class TestCalculator:

    # 使用pytest-fixture实现teardown、setup功能
    @pytest.fixture(autouse=True)
    def calculator_terset(self):
        c = Calculator()
        info("开始计算")
        yield c
        info("结束计算")

    @allure.story("整数之间的加法计算")
    @allure.title("整数之间的加法计算")
    def test_add_int(self, get_yaml_int, calculator_terset):
        """

        :param get_yaml_int: 获取数据yaml_int
        :param calculator_terset: fixture 实现setup和teardown
        :return: None
        """
        self.c = calculator_terset
        a = get_yaml_int[0]
        b = get_yaml_int[1]
        expect = get_yaml_int[2]
        assert expect == self.c.add(a, b)

    @allure.story("浮点数之间的加法计算")
    @allure.title("浮点数之间的加法计算")
    def test_add_float(self, calculator_terset, get_yaml_float):
        """

        :param get_yaml_float: 获取数据yaml_float
        :param calculator_terset: fixture 实现setup和teardown
        :return: None
        """
        self.c = calculator_terset
        a = get_yaml_float[0]
        b = get_yaml_float[1]
        expect = get_yaml_float[2]
        assert expect == round((self.c.add(a, b)), 10)

    @allure.story("整数和浮点数之间的加法计算")
    @allure.title("整数和浮点数之间的加法计算")
    def test_add_int_float(self, calculator_terset, get_yaml_int_float):
        """

        :param get_yaml_int_float: 获取数据int_float
        :param calculator_terset: fixture 实现setup和teardown
        :return: None
        """
        self.c = calculator_terset
        a = get_yaml_int_float[0]
        b = get_yaml_int_float[1]
        expect = get_yaml_int_float[2]
        assert expect == self.c.add(a, b)

    @allure.story("数字和字符之间的加法计算")
    @allure.title("数字和字符之间的加法计算")
    def test_add_number_str(self, calculator_terset, get_yaml_number_str):
        """

         :param get_yaml_number_str: 获取数据number_str
         :param calculator_terset: fixture 实现setup和teardown
         :return: None
         """
        self.c = calculator_terset
        a = get_yaml_number_str[0]
        b = get_yaml_number_str[1]
        with pytest.raises(TypeError):
            self.c.add(a, b)

    @allure.story("字符串之间的加法计算")
    @allure.title("字符串之间的加法计算")
    def test_add_str(self, calculator_terset, get_yaml_add_str):
        """

          :param get_yaml_add_str: 获取数据str
          :param calculator_terset: fixture 实现setup和teardown
          :return: None
          """
        self.c = calculator_terset
        a = get_yaml_add_str[0]
        b = get_yaml_add_str[1]
        expect =get_yaml_add_str[2]
        assert expect == self.c.add(a, b)

    @allure.story("整数之间的除法计算")
    @allure.title("整数之间的除法计算")
    def test_div_int(self, calculator_terset, get_yaml_div_int):
        """

          :param get_yaml_div_int: 获取数据div_int
          :param calculator_terset: fixture 实现setup和teardown
          :return: None
          """
        self.c = calculator_terset
        a = get_yaml_div_int[0]
        b = get_yaml_div_int[1]
        expect =get_yaml_div_int[2]
        assert expect == self.c.div(a, b)

    @allure.story("除数为0的除法计算")
    @allure.title("除数为0的除法计算")
    def test_div_division_zero(self,calculator_terset, get_yaml_division_zero):
        """

          :param get_yaml_division_zero: 获取数据division_zero
          :param calculator_terset: fixture 实现setup和teardown
          :return: None
          """
        self.c = calculator_terset
        a = get_yaml_division_zero[0]
        b = get_yaml_division_zero[1]
        expect =get_yaml_division_zero[2]
        with pytest.raises(ZeroDivisionError):
            assert expect == self.c.div(a, b)

    @allure.story("浮点数之间的除法计算")
    @allure.title("浮点数之间的除法计算")
    def test_div_float(self, calculator_terset,get_yaml_div_float):
        """

          :param get_yaml_div_float: 获取数据div_float
          :param calculator_terset: fixture 实现setup和teardown
          :return: None
          """
        self.c = calculator_terset
        a = get_yaml_div_float[0]
        b = get_yaml_div_float[1]
        expect =get_yaml_div_float[2]
        assert expect == self.c.div(a, b)

    @allure.story("被除数为0的除法计算")
    @allure.title("被除数为0的除法计算")
    def test_div_divisor_zero(self, calculator_terset, get_yaml_divisor_zero):
        """

          :param get_yaml_divisor_zero: 获取数据ddivisor_zero
          :param calculator_terset: fixture 实现setup和teardown
          :return: None
          """
        self.c = calculator_terset
        a = get_yaml_divisor_zero[0]
        b = get_yaml_divisor_zero[1]
        expect =get_yaml_divisor_zero[2]
        assert expect == self.c.div(a, b)
