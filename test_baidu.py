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

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.baidu.com/"

    def test_search_selenium(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title,"selenium_百度搜索")

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()




