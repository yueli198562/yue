#coding:utf-8
import requests,unittest

from db_fixture.test_data import *
from db_fixture.mysql_db import *

class Interface_test10(unittest.TestCase):
    u''' 责任详情查询 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+ip+"/liability/insuranceLiability"
        get_mysql_data(risk1)
        for i in [liability1, liability_limit1, limit_values1, insurance_clause1]:
            get_mysql_data(i)

    @classmethod
    def tearDownClass(cls):
        for i in [liability2, liability_limit2, limit_values2, insurance_clause2]:
            get_mysql_data(i)
            get_mysql_data(risk2)

    def test1(self):
        u''' 责任id存在 '''
        base_url=self.base_url+"/ZR12345"
        r = requests.get(base_url)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test2(self):
        u''' 责任id不存在 '''
        base_url = self.base_url + "/erterter"
        r = requests.get(base_url)
        result = r.json()
        self.assertEqual(result['code'], 6)
        self.assertEqual(result['msg'], u"没有满足条件的数据")


    def test3(self):
        u''' 责任id为空 默认险类展示列表第1页 '''
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
