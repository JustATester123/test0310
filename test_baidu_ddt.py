#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/7/7
@Project:test0310
@FileName:test_baidu_ddt.py
@Desc:

"""
import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt,data,file_data,unpack

@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver =webdriver.Chrome()
        cls.base_url ="https://www.baidu.com/"
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def search_baidu(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(3)

    # @data(["case1","selenium"],["case2","ddt"],["case3","python"])
    # @unpack
    # def test_search1(self,case_name,search_key):
    #     print("第一组测试记录：",case_name)
    #     self.search_baidu(search_key)
    #     self.assertEqual(self.driver.title,search_key+"_百度搜索")
    #
    # @data(("case1","selenium"),("case2","ddt"),("case3","python"))
    # @unpack
    # def test_search2(self,case_name,search_key):
    #     print("第二组测试记录：",case_name)
    #     self.search_baidu(search_key)
    #     self.assertEqual(self.driver.title,search_key+"_百度搜索")
    #
    # @data({"search_key":"selenium"},{"search_key":"ddt"},{"search_key":"python"})
    # @unpack
    # def test_search3(self,search_key):
    #     print("第三组测试记录：",search_key)
    #     self.search_baidu(search_key)
    #     self.assertEqual(self.driver.title,search_key+"_百度搜索")
    #
    #
    # @file_data('ddt_data_file.json')
    # def test_search4(self,search_key):
    #     print("第四组测试用例：",search_key)
    #     self.search_baidu(search_key)
    #     self.assertEqual(self.driver.title,search_key+"_百度搜索")


    # 这个用例总是报错，不知道如何解决
    @file_data('ddt_data_file.yaml')
    def test_search5(self,case):
        # data=eval(case[0])
        search_key = case[0]['search_key']
        print("第五组测试用例：",search_key)
        self.search_baidu(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")



if __name__ =='__main__':
    unittest.main(verbosity=2)