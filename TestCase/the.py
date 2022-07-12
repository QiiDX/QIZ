# coding=utf-8
import io
import sys
import threading
import json

import requests

# 解决console显示乱码的编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class MyThread(threading.Thread):
    """This class customizes the output thu overriding the run() method"""

    def __init__(self, obj):
        super(MyThread, self).__init__()

        self.obj = obj

    def run(self):
        ret = self.obj.test_search_tags_movie()

        print('result--%s:\n%s' % (self.getName(), ret))


class test_th(object):
    """A class containing interface test method of Douban object"""

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
                        }

    def get_response(self, url, data):
        resp = requests.post(url=url, data=data, headers=self.headers)

        return resp

    def test_search_tags_movie(self):
        url = 'https://movie.douban.com/j/search_tags'
        post_data = {
            # 'type': 'movie',
            # 'source': 'index'
        }
        resp = self.get_response(url=url, data=post_data)
        asda = resp.json()
        print(json.dumps(asda, indent=2, ensure_ascii=False,))
        # return resp


if __name__ == '__main__':
    douban = test_th()
    thDs = []
    for i in range(10):
        thd = MyThread(douban)
        thd.start()
        thDs.append(thd)

    for thd in thDs:
        thd.join()
