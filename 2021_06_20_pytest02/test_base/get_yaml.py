"""
获取yaml中的数据，并转成Python数据对象
"""
import yaml


class GetYaml:

    def get_yaml(self, file_path):
        """

        :param file_path: yaml文件的地址
        :return: yaml文件转化后的Python对象
        """
        with open(file_path) as f:
            yaml_data = yaml.safe_load(f)

        return yaml_data

if __name__ == '__main__':
    t = GetYaml()
    print(t.get_yaml("E:\\Home_Work\\2021_06_17_pytest01\\test_data\\calculator.yaml"))