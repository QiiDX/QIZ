# coding=utf-8
import requests
import json


def send_post(url, headers, data):
    result = requests.post(
        url=url,
        headers=headers,
        data=data,
        verify=False
    )
    # if result.status_code == 200:
    #     responseDict = result.json()
    #     res = json.dumps(responseDict, ensure_ascii=False, sort_keys=True, indent=2)
    #
    # else:
    #     print(result, result.text)
    return result


def send_get(url, headers, data):
    result = requests.get(url=url, headers=headers, data=data, verify=False)
    res = result
    return res


def send_put(url, headers, data):
    result = requests.put(
        url=url,
        headers=headers,
        data=data,
        verify=False
    )
    res = result
    return res


def run_main(method, url=None, headers=None, data=None):
    result = None
    if method == 'post':
        result = send_post(url, headers, data)
    elif method == 'get':
        result = send_get(url, headers, data)
    elif method == 'put':
        result = send_put(url, headers, data)
    else:
        print("调用的封装方法错误")
    return result


class RunMain:
    pass
# if __name__ == '__main__':
#     url = 'http://www.testdns361.net/uc/login'
#     data = {
#         "username": "18759299016",
#         "password": "Qw1231",
#     }
#     # 实例化RunMain类
#     run = RunMain()
#     res = run.run_main("post",url,data)
#     print(res)
