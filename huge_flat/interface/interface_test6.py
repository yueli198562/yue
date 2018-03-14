#coding:utf-8
import requests,unittest

from db_fixture.test_data import *
from db_fixture.mysql_db import *

class Interface_test6(unittest.TestCase):
    u''' 险种详情查询 '''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+ip+"/insurance/riskInfo/"
        get_mysql_data(classes1)
        get_mysql_data(risk1)

    @classmethod
    def tearDownClass(cls):
        get_mysql_data(classes2)
        get_mysql_data(risk2)

    def test1(self):
        u''' 险种id存在 '''
        base_url=self.base_url+"XZ12345"
        r = requests.get(base_url)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test2(self):
        u''' 险种id不存在 '''
        base_url = self.base_url + "erterter"
        r = requests.get(base_url)
        result = r.json()
        self.assertEqual(result['code'], 6)
        self.assertEqual(result['msg'], u"没有满足条件的数据")

    def test3(self):
        u''' 险种id为空 默认显示险类展示列表第1页 '''
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
