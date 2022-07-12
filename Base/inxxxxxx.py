# coding:utf-8
import yaml
import os

cur = os.path.dirname(os.path.realpath(__file__))

# Libraries_Yaml


FileName = 'xxxxxxxxx.yaml'
insideName = 'xxxxxxxxx'


def xxxxxxxxxx(yamlName='./Libraries_Yaml/' + FileName):
    """
    从token.yaml读取token值
    param yamlName: 配置文件名称
    return: token值
    """
    p = os.path.join(cur, yamlName)
    f = open(p)
    a = f.read()
    t = yaml.load(a, Loader=yaml.FullLoader)
    f.close()
    return t[insideName]


if __name__ == "__main__":
    print(xxxxxxxx())
