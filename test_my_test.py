#-*- coding: utf-8 -*-

"""
@auther:tester
@data:2020/4/23
@Project:test0310
@FileName:test_my_test.py
@Desc:

"""
import  unittest

class MyTest(unittest.TestCase):

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print('test aaa')

    @unittest.skipIf(3>2,'条件为真时跳过测试')
    def test_skipIf(self):
        print('test  bbb')

    @unittest.skipUnless(3>2,"当条件为真时，执行测试")
    def test_skipUnless(self):
        print("test ccc")

    @unittest.expectedFailure
    def test_excepected_failure(self):
        self.assertEqual(2,3)


if __name__ == '__main__':
    unittest.main()
