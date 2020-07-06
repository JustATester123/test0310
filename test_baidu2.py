#-*- coding: utf-8 -*-

"""
@auther:wangjiong
@data:2020/4/23
@Project:test0310
@FileName:test_baidu.py
@Desc:

"""
import unittest
from time import sleep
from selenium import webdriver


class TestBaiDu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com/"

    def baidu_search(cls,search_key):
        cls.driver.get(cls.base_url)
        cls.driver.find_element_by_id("kw").send_keys(search_key)
        cls.driver.find_element_by_id("su").click()

    def test_search_selenium(cls):
        '''这是百度的测试用例'''
        cls.baidu_search("selenium")
        sleep(2)
        title = cls.driver.title
        cls.assertEqual(title,"selenium_百度搜索")

    def test_search_unittest(cls):
        '''这是百度的测试用例'''
        # 不清楚这个方法有两个参数，在这调用的时候却传了一个参数
        cls.baidu_search("unittest")
        sleep(2)
        title = cls.driver.title
        cls.assertEqual(title,"unittest_百度搜索")


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ =='__main__':
    unittest.main()




