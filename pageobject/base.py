#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/7/22
@Project:test0310
@FileName:base.py
@Desc:

"""
import  time
# from selenium import webdriver
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    #打开页面
    def open(self,url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def by_id(self,id_):
        return self.driver.find_element_by_id(id_)

    def by_class(self,class_name):
        return self.driver.find_element_by_class(class_name)

    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_css(self,css):
        return self.driver.find_element_by_css_selector(css)

    def get_title(self):
        return self.driver.title

    def get_text(self,xpath):
        return self.by_xpath(xpath).text

    def js(self,script):
        self.driver.execute_script(script)


