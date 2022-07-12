# coding=utf-8
import unittest
import json
import urllib3
import requests
from ruamel.yaml import YAML

# 库引入
from Libraries_Self.inHttp import inHttp
from Libraries_Self.inToken import inToken
from Libraries_Self.inCookies import inCookies
from Libraries_Self.Base.Request_Run import run_main


class login(unittest.TestCase):
    """ 登陆 """

    def setUp(self):
        urllib3.disable_warnings()
        pass

    def tearDown(self):
        pass

    def test_01(self):
        url = 'http://bbs.xmfish.com/read-htm-tid-16811308.html'
        headers = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome /'
                          ' 87.0.4280.88Safari / 537.36',
            # 请求类型格式
            # 'Accept': 'application/json,text/plain,*/*',
            # 'Content-Type': 'application/json,text/plain,*/*',
            # 'Content-Type': 'application/x-www-form-urlencoded',

            # 凭证权限
            # 'cookies': 'PHPSESSID=' + inCookies(),
            # 'Authorization': 'Basic ' + inToken(),
        }
        # for i in range(9999):
        #     if i % 3:
        #         print('不')
        #     else:
        #         print('可')

        data = {
            'username': 'mouliz',
            'password': 'Qw123123'
        }
        # proxies = {
        #     'http': 'http://113.229.6.31:9999',
        #     'https': 'http://113.229.6.31:9999'
        # }
        response = requests.get(url, headers, data=data,)
        if response.status_code == 200:
            print(response.text)
            # responseDict = response.json()
            # print(responseDict)
            # self.assertEqual(responseDict['code'], 0,
            #                  print('\n' + json.dumps(responseDict, ensure_ascii=False, sort_keys=True, indent=2)))
            # # 存入token---access_token-------------------------------------------
            # # 存放格式
            # extraction = {'token': responseDict['data']['token']}
            # # 取出路径
            # yamlPath = r'..\Libraries_Self\Libraries_Yaml\token.yaml'
            # with open(yamlPath, mode='w', encoding='utf-8') as file:
            #     YAML().dump(extraction, file)
        else:
            print(response)
