# coding:utf-8
import yaml
import os

cur = os.path.dirname(os.path.realpath(__file__))


# Libraries_Yaml


def inCookies(yamlName="./Libraries_Yaml/cookies.yaml"):
    p = os.path.join(cur, yamlName)
    f = open(p)
    a = f.read()
    t = yaml.load(a, Loader=yaml.FullLoader)
    f.close()
    # 标记
    return t['cookies']


if __name__ == "__main__":
    print(inCookies())
