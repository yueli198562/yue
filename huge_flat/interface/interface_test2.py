#coding:utf-8
import requests,unittest

from db_fixture.test_data import *
from db_fixture.mysql_db import *

class Interface_test2(unittest.TestCase):
    u''' 险类详情查询 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+ip+"/insurance/insuranceClasses/"
        get_mysql_data(classes1)

    @classmethod
    def tearDownClass(cls):
        get_mysql_data(classes2)

    def test1(self):
        u''' 险类id存在 '''
        base_url=self.base_url+"XL12345"
        r = requests.get(base_url)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test2(self):
        u''' 险类id不存在 '''
        base_url = self.base_url + "erterter"
        r = requests.get(base_url)
        result = r.json()
        self.assertEqual(result['code'], 6)
        self.assertEqual(result['msg'], u"没有满足条件的数据")

    def test3(self):
        u''' 险类id为空 默认险类展示列表第1页 '''
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
