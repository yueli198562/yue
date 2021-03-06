#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *

class Interface_test1(unittest.TestCase):
    u''' 险类展示列表 '''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+ip+"/insurance/insuranceClasses"
        get_mysql_data(classes1)
    @classmethod
    def tearDownClass(cls):
        get_mysql_data(classes2)

    def test1(self):
        u''' 所有参数为空 '''
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test2(self):
        u''' 传入参数page 非int类型 '''
        params = {'page':"'"+ "1"+"'"}
        r = requests.get(self.base_url,params)
        result = r.json()
        self.assertEqual(result['code'], 400)
        self.assertEqual(result['msg'], u"参数不合法")

    def test3(self):
        u''' 传入参数page int类型 '''
        params = {'page': 1}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test4(self):
        u''' 传入参数page 大于实际页数 '''
        params = {'page': 10}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test5(self):
        u''' 传入参数page为0 '''
        params = {'page': 0}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test6(self):
        u''' 传入参数name，name存在 '''
        params = {'name': "XL险类名称"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test7(self):
        u''' 传入参数name，模糊查找 '''
        params = {'name': "XL险"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test8(self):
        u''' 传入参数name，name不存在 '''
        params = {'name': "y12345"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 6)
        self.assertEqual(result['msg'], u"没有满足条件的数据")

    def test9(self):
        u''' 传入参数creatBy，creatBy存在 '''
        params = {'creatBy': "XL创建人"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test_10(self):
        u''' 传入参数creatBy，creatBy存在 '''
        params = {'creatBy': "月亮月亮b"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 6)
        self.assertEqual(result['msg'], u"没有满足条件的数据")

    def test_11(self):
        u''' 只传入page和name '''
        params = {'page': 1,"name":"XL险类名称"}
        r = requests.get(self.base_url,params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test_12(self):
        u''' 只传入page和creatBy '''
        params = {'page': 1, 'creatBy': "XL创建人"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

    def test_13(self):
        u''' 只传入name和creatBy '''
        params = {"name":"XL险类名称", 'creatBy': "XL创建人"}
        r = requests.get(self.base_url, params)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
