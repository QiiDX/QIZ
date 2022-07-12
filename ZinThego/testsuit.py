# coding=utf-8
import unittest
import HTMLTestRunner
import time

for i in range(1):
    if __name__ == '__main__':
        # 实例化TestSuite创建测试套件
        test_suit = unittest.TestSuite()
        loader_a = unittest.TestLoader()

        # 定位case文件
        case_list_a = loader_a.discover('TestCase', 'test_*.py')

        # 把用例test_01添加到测试套件中
        test_suit.addTests(case_list_a)

        # run()方法是运行测试套件的测试用例，入参为suite测试套件。
        # print(unittest.TextTestRunner().run(test_suit))

        # 存放路径地址
        htmlPath = 'C:/Users/cyl/Desktop/canSo/'

        # 报告命名并保存为HTML格式
        creteNewWord = time.strftime("%Y-%m-%d %H_%M_%S.HTML")
        filename = htmlPath + creteNewWord
        fp = open(filename, 'wb')
        reportRunner = HTMLTestRunner.HTMLTestReportCN(
            stream=fp, title='apiTest', description='')
        reportRunner.run(test_suit)
        fp.close()
    time.sleep(0.5)
    print('↑', i + 1)
