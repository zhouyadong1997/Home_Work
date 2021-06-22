# 使用pytest—fixture实现参数化
import pytest
from test_base.get_yaml import GetYaml

path = "E:\\Home_Work\\2021_06_20_pytest2\\test_data\\calculator.yaml"

g = GetYaml().get_yaml(path)


@pytest.fixture(params=g["add_int"]["datas"], ids=g["add_int"]["ids"])
def get_yaml_int(request):
    return request.param


@pytest.fixture(params=g["add_float"]["datas"], ids=g["add_float"]["ids"])
def get_yaml_float(request):
    return request.param


@pytest.fixture(params=g["int_float"]["datas"], ids=g["int_float"]["ids"])
def get_yaml_int_float(request):
    return request.param


@pytest.fixture(params=g["number_str"]["datas"], ids=g["number_str"]["ids"])
def get_yaml_number_str(request):
    return request.param


@pytest.fixture(params=g["add_str"]["datas"], ids=g["add_str"]["ids"])
def get_yaml_add_str(request):
    return request.param


@pytest.fixture(params=g["div_int"]["datas"], ids=g["div_int"]["ids"])
def get_yaml_div_int(request):
    return request.param


@pytest.fixture(params=g["division_zero"]["datas"], ids=g["division_zero"]["ids"])
def get_yaml_division_zero(request):
    return request.param


@pytest.fixture(params=g["div_float"]["datas"], ids=g["div_float"]["ids"])
def get_yaml_div_float(request):
    return request.param


@pytest.fixture(params=g["divisor_zero"]["datas"], ids=g["divisor_zero"]["ids"])
def get_yaml_divisor_zero(request):
    return request.param
