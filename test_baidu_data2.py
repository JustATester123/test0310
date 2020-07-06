#-*- coding: utf-8 -*-

"""
@auther:wangjiong
@data:2020/7/6
@Project:test0310
@FileName:test_baidu_data.py
@Desc:

"""
import unittest
import csv
import codecs
from time import sleep
from itertools import islice
from selenium import webdriver

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com/"
        cls.test_data =[]
        with codecs.open('baidu_data.csv','r','utf_8_sig') as f:
            data = csv.reader(f)
            for line in islice(data,1,None):
                cls.test_data.append(line)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(3)

    def test_search_selenium(self):
        self.baidu_search(self.test_data[0][1])
    def test_search_unittest(self):
        self.baidu_search(self.test_data[1][1])
    def test_search_appium(self):
        self.baidu_search(self.test_data[2][1])



if __name__ == '__main__':
    unittest.main(verbosity=2)