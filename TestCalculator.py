#-*- coding: utf-8 -*-

"""
@auther:wangjiong
@data:2020/3/10
@Project:test0310
@FileName:TestCalculator.py
@Desc:

"""
import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("Test start:")

    def tearDown(self):
        print("Test over")

    def test_add(self):
        c = calculator(3,5)
        result = c.add()
        self.assertEqual(result,8)

    def test_sub(self):
        c = calculator(2,1)
        result = c.sub()
        self.assertEqual(result,1)

    def test_div(self):
        c = calculator(4,2)
        result = c.div()
        self.assertEqual(result,1)

if __name__ =='__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator("test_add"))
    suit.addTest(TestCalculator("test_sub"))
    suit.addTest(TestCalculator("test_div"))

    runner = unittest.TextTestRunner()
    runner.run(suit)



