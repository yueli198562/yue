#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *

class Interface_test2(unittest.TestCase):
    u''' 险类详情查询 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://10.10.62.101:9090/insurance/insuranceClasses/"
        sql(config_file_path, classes1, database_name)

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, classes2, database_name)

    def test1(self):
        u''' 险类id存在 '''
        base_url=self.base_url+"XL12345"
        r = requests.get(base_url)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test2(self):
        u''' 险类id不存在 '''
        base_url = self.base_url + "erterter"
        r = requests.get(base_url)
        result = r.json()
        self.assertEqual(result['code'], 1006)
        self.assertEqual(result['msg'], u"没有满足条件的数据")

    def test3(self):
        u''' 险类id为空 默认险类展示列表第1页 '''
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
