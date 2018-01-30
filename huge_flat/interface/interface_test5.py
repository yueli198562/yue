#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *

class Interface_test5(unittest.TestCase):
    u''' 险种展示列表 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://10.10.62.101:9090/insurance/riskInfo"
        sql(config_file_path, classes1, database_name)
        sql(config_file_path,risk1, database_name)

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, risk2, database_name)
        sql(config_file_path, classes2, database_name)

    def test1(self):
        u''' 所有参数为空 '''
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test2(self):
        u''' 传入参数page,非int类型 '''
        params = {'page':"A"}
        r = requests.get(self.base_url,params)
        result = r.json()
        self.assertEqual(result['code'], 400)
        self.assertEqual(result['msg'], u"参数不合法")

    def test3(self):
        u''' 传入参数name，name存在 '''
        params = {'name': "XZ险种名称"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test4(self):
        u''' 传入参数name，模糊查找 '''
        params = {'name': "XZ险"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test5(self):
        u''' 传入参数name，name不存在 '''
        params = {'name': "y12345"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 1006)
        self.assertEqual(result['msg'], u"没有满足条件的数据")

    def test6(self):
        u''' 传入参数creatBy，creatBy存在 '''
        params = {'creatBy': "XZ险种创建人"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test7(self):
        u''' 传入参数creatBy，creatBy存在 '''
        params = {'creatBy': "月亮月亮b"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 1006)
        self.assertEqual(result['msg'], u"没有满足条件的数据")

    def test8(self):
        u''' 只传入page和name '''
        params = {'page': 1,"name":"XZ险种名称"}
        r = requests.get(self.base_url,params)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test9(self):
        u''' 只传入page和creatBy '''
        params = {'page': 1, 'creatBy': "XZ险种创建人"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test_10(self):
        u''' 只传入name和creatBy '''
        params = {"name":"XZ险种名称", 'creatBy': "XZ险种创建人"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
