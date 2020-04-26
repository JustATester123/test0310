#-*- coding: utf-8 -*-

"""
@auther:wangjiong
@data:2020/3/18
@Project:test0310
@FileName:run_tests.py
@Desc:

"""
import unittest
from HTMLTestRunner import HTMLTestRunner
import  string
test_dir = '.'
suits = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')


# if __name__ =='__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suits)

if __name__ == "__main__":
    fp = open('./result.html','wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='hahahhh',description = 'hahahh')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='百度搜索测试报告',description = '运行环境')

    # runner =HTMLTestRunner.
    runner.run(suits)
    fp.close()
