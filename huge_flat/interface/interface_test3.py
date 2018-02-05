#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *

class Interface_test3(unittest.TestCase):
    u''' 增加险类 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://10.10.62.101:9090/insurance/insuranceClasses"
        sql(config_file_path, classes1, database_name)

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, classes2, database_name)

    def test1(self):
        u''' 险类编码已存在 '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL险类名称l", "insuranceClassesDes": "XL描述",
                "isParent": 'Y', "parentId": "DFGDF"}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 90101)
        self.assertEqual(result['msg'], u"险类编码已经存在")

    def test2(self):
        u''' 险类编码不存在'''
        data = {"insuranceClassesId": "XL123456","insuranceClassesName":"XL险类名称1",
                "insuranceClassesDes":"XL描述","isParent":'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        #数据库删除插入数据
        classes = 'delete from t_insurance_classes where insurance_classes_id="XL123456"'
        sql(config_file_path, classes, database_name)

    def test3(self):
        u''' 险类编码超过20个字符'''
        data = {"insuranceClassesId": "XL123456789101112131415",
                "insuranceClassesName": "XL险类名称1",
                "insuranceClassesDes": "XL描述", "isParent": 'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 400101)
        self.assertEqual(result['msg'], u"险类编码不能超过20个字符")

    def test4(self):
        u''' 险类名称已存在'''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL险类名称",
                "insuranceClassesDes": "XL描述", "isParent": 'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 90102)
        self.assertEqual(result['msg'], u"险类名称已经存在")

    def test5(self):
        u''' 险类名称超过20个字符'''
        data = {"insuranceClassesId": "XL123456",
                "insuranceClassesName": "XL险类名称1789101112131415",
                "insuranceClassesDes": "XL描述", "isParent": 'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 400104)
        self.assertEqual(result['msg'], u"险类名称不能超过20个字符")

    def test6(self):
        u''' 险类描述超过200个字符'''
        data = {"insuranceClassesId": "XL123456",
                "insuranceClassesName": "XL险类名称1",
                "insuranceClassesDes": """他让他让他让他让他开始试测试测试开始自动化
                测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突抬""",
                "isParent": 'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 400103)
        self.assertEqual(result['msg'], u"险类描述不能超过200个字符")

    def test7(self):
        u''' isParent为N，parentId为空 '''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL险类名称l", "insuranceClassesDes": "XL描述",
                "isParent": 'N'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 10104)
        self.assertEqual(result['msg'], u"父类节点不能为空")

    def test8(self):
        u''' isParent为N，parentId存在 '''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL险类名称l",
                "insuranceClassesDes": "XL描述",
                "isParent": 'N',"parentId":'XL12345'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        #------删除插入数据------
        classes = 'delete from t_insurance_classes where insurance_classes_id="XL123456"'
        sql(config_file_path, classes, database_name)

    def test9(self):
        u''' isParent为N，parentId不存在 '''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL险类名称l",
                "insuranceClassesDes": "XL描述",
                "isParent": 'N', "parentId": 'XLFDFG66556'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 80101)
        self.assertEqual(result['msg'], u"父类险类不存在")

    def test_10(self):#
        u''' 是否有节点isParent为空'''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL险类名称l", "insuranceClassesDes": "XL描述",
                "parentId": 18}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 10103)
        self.assertEqual(result['msg'], u"是否为父类选型不能为空")

    def test_11(self):
        u''' 是否有节点isParent非Y或N'''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL险类名称l", "insuranceClassesDes": "XL描述",
                "isParent": 'M',"parentId": 18}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 400105)
        self.assertEqual(result['msg'], u"是否为父类选型参数不合法")

    def test_12(self):
        u''' 所有参数为空 '''
        r = requests.post(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 10101)
        self.assertEqual(result['msg'], u"险类编码不能为空")

    def test_13(self):
        u''' 险类编码insuranceClassesId为空'''
        data = {"insuranceClassesName": "XL险类名称l",
                "insuranceClassesDes": "XL描述", "isParent": 'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 10101)
        self.assertEqual(result['msg'], u"险类编码不能为空")

    def test_14(self):
        u''' 险类名称insuranceClassesName为空'''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesDes": "XL描述",
                "isParent": 'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 10102)
        self.assertEqual(result['msg'], u"险类名称参数为空")

if __name__ == '__main__':
    unittest.main()
