# coding=utf-8
import unittest
import json
import urllib3
import threading
from ruamel.yaml import YAML

# 库引入
from Libraries_Self.inHttp import inHttp
from Libraries_Self.Base.Request_Run import run_main


class MyThread(threading.Thread):
    """This class customizes the output thu overriding the run() method"""

    def __init__(self, obj):
        super(MyThread, self).__init__()

        self.obj = obj

    def run(self):
        # ret = self.obj.test_search_tags_movie()

        print('result--%s:\n%s' % (self.getName(), login()))


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

            # 权限
            # 'Authorization': 'Bearer ' + inToken(),
            # 'Authorization': 'Basic cGlnOnBpZw==',
        }
        data = {
            'username': 'mouliz',
            'password': 'Qw123123'
        }
        response = run_main('post', url, headers, data)
        if response.status_code == 200:
            responseDict = response.json()
            # print(responseDict)
            self.assertEqual(responseDict['code'], 0,
                             print('\n' + json.dumps(responseDict, ensure_ascii=False, sort_keys=True, indent=2)))
            # 存入 token-------------------------------------------------
            with open(r'..\Libraries_Self\Libraries_Yaml\token.yaml', mode='w', encoding='utf-8') as file:
                YAML().dump({'token': responseDict['data']['token']}, file)
            # 存入 cookies--------'PHPSESSID='?--------------------------
            response.cookies.get_dict()
            with open(r'..\Libraries_Self\Libraries_Yaml\cookies.yaml', mode='w', encoding='utf-8') as file:
                YAML().dump({'cookies': response.cookies.get_dict()}, file)
        else:
            print(response + response.text)


if __name__ == '__main__':
    douban = login()
    thDs = []
    for i in range(2):
        thd = MyThread(douban)
        thd.start()
        thDs.append(thd)

    for thd in thDs:
        thd.join()
