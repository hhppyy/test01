#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import requests

class QQtest(unittest.TestCase):
    '''qq号测试吉凶'''
    def setUp(self):
        '''测试前置'''
        self.url = "http://japi.juhe.cn/qqevaluate/qq"
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
        }
        self.s = requests.session()

    def tearDown(self):
        '''清除数据'''
        self.s.close()
    def test001(self):
        '''测试用例001'''
        self.params ={
            "qq":"741841851",
            "key":"49c47ae3d1e8e3e49578f03cee1e7a7a"
        }
        r = self.s.get(self.url,params=self.params,headers=self.headers,verify=False)
        result = r.json()
        # print(result)
        reason = result['reason']#获取接口状态
        data = result['result']['data']['conclusion']#获取吉凶数据
        self.assertEqual(reason,'success')

    def test002(self):
        '''测试用例002'''
        self.params ={
            "qq":"",
            "key":"49c47ae3d1e8e3e49578f03cee1e7a7a"
        }
        r = self.s.get(self.url,params=self.params,headers=self.headers,verify=False)
        result = r.json()
        print(result)
        reason = result['reason']#获取接口状态
        # data = result['result']['data']['conclusion']#获取吉凶数据
        self.assertEqual(reason,'错误的请求参数')

if __name__ == '__main__':
    unittest.main()