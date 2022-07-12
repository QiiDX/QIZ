# coding=utf-8
import unittest
import json
import urllib3

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
        url = inHttp() + '/api/index.register/login'
        print()
        headers = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome /'
                          ' 87.0.4280.88Safari / 537.36',
            # 请求类型格式
            # 'Accept': 'application/json,text/plain,*/*',
            # 'Content-Type': 'application/json,text/plain,*/*',
            # 'Content-Type': 'application/x-www-form-urlencoded',

            # 凭证权限
            'cookies': 'PHPSESSID=' + inCookies(),
            'Authorization': 'Basic ' + inToken(),
        }
        data = {
            'username': 'mouliz',
            'password': 'Qw123123'
        }
        response = run_main('post', url, headers, data)
        if response.status_code == 200:
            responseDict = response.json()
            self.assertEqual(responseDict['code'], 0,
                             print('\n' + json.dumps(responseDict, ensure_ascii=False, sort_keys=True, indent=2)))
        else:
            print('或未找到接口' + response.text)
