#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/3/10
@Project:test0310
@FileName:calculator.py
@Desc:

"""
class calculator:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b
