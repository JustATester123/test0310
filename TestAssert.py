#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/3/18
@Project:test0310
@FileName:TestAssert.py
@Desc:

"""

import unittest

class TestAssert(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(2+2,4)
        self.assertEqual("python","python")
        self.assertNotEqual("hello","python")

    def test_in(self):
        self.assertIn("hello","hello world")
        self.assertNotIn("hi","hello world")

    def test_true(self):
        self.assertTrue(True)
        self.assertFalse(False)

if __name__ =='__main__':
    unittest.main()
