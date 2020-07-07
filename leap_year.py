#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/3/18
@Project:test0310
@FileName:leap_year.py
@Desc:

"""

class LeapYear:
    def __init__(self,year):
        self.year = int(year)

    def answer(self):
        if self.year % 100 ==0:
            if self.year % 400 ==0:
                return "{0}是闰年".format(self.year)
            else:
                return "{0}不是闰年".format(self.year)
        else:
            if self.year % 4 ==0:
                return "{0}是闰年".format(self.year)
            else:
                return"{0}不是闰年".format(self.year)

if __name__ =="__main__":
    lp = LeapYear("2000")
    print(lp.answer())

    lp = LeapYear(2100)
    print(lp.answer())

    lp = LeapYear(2020)
    print(lp.answer())

    lp = LeapYear(2021)
    print(lp.answer())