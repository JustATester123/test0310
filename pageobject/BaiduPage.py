#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/7/22
@Project:test0310
@FileName:BaiduPage.py
@Desc:

"""
from pageobject.base import BasePage

class BaiduPage(BasePage):
    url = "https://www.baidu.com"

    def search_input(self,search_key):
        self.by_id("kw").send_keys(search_key)

    def search_button(self):
        self.by_id("su").click()




