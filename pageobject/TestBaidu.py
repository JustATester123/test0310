#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/7/22
@Project:test0310
@FileName:TestBaidu.py
@Desc:

"""
import unittest
from selenium import webdriver
from time import sleep
from pageobject.BaiduPage import BaiduPage

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver =webdriver.Chrome()

    def test_baidu_search_case(self):
        page =BaiduPage(self.driver)
        page.open()
        page.search_input("selenium")
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(),"selenium_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        

if __name__ == '__main__':
    unittest.main(verbosity=2)

