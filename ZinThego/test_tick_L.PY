# coding=utf-8
import unittest
import urllib3
from Libraries_Self.Base.Request_Run import run_main


class login(unittest.TestCase):
    """ 登陆 """
    def setUp(self):
        urllib3.disable_warnings()
        pass

    def tearDown(self):
        pass

    def test_api(self):
        # 兑付接口
        number = 31
        url = 'http://192.168.0.139:8888/common/enum/test3?ticketId=' + str(number)

        headers = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome /'
                          ' 87.0.4280.88Safari / 537.36',
            # 请求类型格式
            # 'Accept': 'application/json,text/plain,*/*',
            # 'Content-Type': 'application/json,text/plain,*/*',
            # 'Content-Type': 'application/x-www-form-urlencoded',

            # 凭证权限
            # 'cookies': 'PHPSESSID=' + inCookies(),
            'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImNyZWF0ZWQiOjE2MjA3MjE5NDE0OTgsImV4cCI6MTYyMDg'
                             'wODM0MX0.YIbn449l_mNiBBYQefowc6uEdxRuyaZN-MaVJ893_Io',
        }
        response = run_main('get', url, headers,)
        print(response)
        exResponse = response.json()
        print(exResponse)

        # responseDict = response.json()
        # print(responseDict)
        # if response.status_code == 200:
        #     responseDict = response.json()
        #     print(responseDict)
        # else:
        #     print('或未找到接口' + response.text)
