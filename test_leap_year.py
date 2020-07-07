#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/3/18
@Project:test0310
@FileName:test_leap_year.py
@Desc:

"""
import unittest
from leap_year import LeapYear
class TestLeapYear(unittest.TestCase):
    def test_2000(self):
        lp = LeapYear(2000)
        self.assertEqual("2000是闰年",lp.answer())

if __name__ == "__main__":
    unittest.main()