#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import requests
from common.testLogin import login,is_login_sucess

class TestCaseCSH(unittest.TestCase):
    '''禅道登录'''
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    def tearDown(self):
        self.s.cookies.clear()
    # def setUp(self):
    #     self.s = requests.session()
    #
    # def tearDown(self):
    #     self.s.close()

    def testlogin01(self):
        '''测试用例01'''
        res = login(self.s,"admin","e10adc3949ba59abbe56e057f20f883e")
        result = is_login_sucess(res)
        #期望结果，登录成功True
        self.assertTrue(result)


    def testlogin02(self):
        '''测试用例02'''
        res = login(self.s,"dmin","e10adc3949ba59abbe56e057f20f883e")
        result = is_login_sucess(res)
        #期望结果，登录失败False
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()








