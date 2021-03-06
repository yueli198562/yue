#coding:utf-8
import requests
import unittest

from db_fixture.test_data import *
from db_fixture.mysql_db import *

class Interface_test4(unittest.TestCase):
    u''' 修改险类 '''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+ip+"/insurance/insuranceClasses"
        get_mysql_data(classes1)
        get_mysql_data(classes_1)

    @classmethod
    def tearDownClass(cls):
        get_mysql_data(classes2)
        get_mysql_data(classes_2)

    def test1(self):
        u''' 所有参数为空 '''
        r = requests.put(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 10101)
        self.assertEqual(result['msg'], u"险类编码不能为空")

    def test2(self):
        u''' 险类编码insuranceClassesId为空  '''
        data = {"insuranceClassesName": "XL险类名称", "insuranceClassesDes": "XL描述",
                "isParent": 'Y'}
        r = requests.put(self.base_url,data)
        result = r.json()
        self.assertEqual(result['code'], 10101)
        self.assertEqual(result['msg'], u"险类编码不能为空")

    def test3(self):
        u''' 险类编码超过20个字符'''
        data = {"insuranceClassesId": "XL123456789101112131415",
                "insuranceClassesName": "XL险类名称1",
                "insuranceClassesDes": "XL描述", "isParent": 'Y'}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 40101)
        self.assertEqual(result['msg'], u"险类编码不能超过20个字符")

    def test4(self):
        u''' 险类名称insuranceClassesName为空  '''
        data = {"insuranceClassesId": "XL12345",  "insuranceClassesDes": "XL描述",
                "isParent": 'Y'}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 10102)
        self.assertEqual(result['msg'], u"险类名称参数为空")

    def test5(self):
        u''' 险类名称超过20个字符'''
        data = {"insuranceClassesId": "XL12345",
                "insuranceClassesName": "XL险类名称1789101112131415",
                "insuranceClassesDes": "XL描述", "isParent": 'Y'}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 40104)
        self.assertEqual(result['msg'], u"险类名称不能超过20个字符")

    def test6(self):
        u''' 险类描述超过200个字符'''
        data = {"insuranceClassesId": "XL12345",
                "insuranceClassesName": "XL险类名称1",
                "insuranceClassesDes": """他让他让他让他让他开始试测试测试开始自动化
                测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突抬""",
                "isParent": 'Y'}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 40103)
        self.assertEqual(result['msg'], u"险类描述不能超过200个字符")

    def test7(self):
        u''' 是否为根节点isParent为空  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL险类名称", "insuranceClassesDes": "XL描述",}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 10103)
        self.assertEqual(result['msg'], u"是否为父类选型不能为空")

    def test8(self):
        u''' 是否为根节点isParent为Y,parentId为空  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL修改险类名称", "insuranceClassesDes": "XL修改描述",
                "isParent": 'Y'}
        r = requests.put(self.base_url, data)
        result = r.json()
        a = get_mysql_data('select * from t_insurance_classes where insurance_classes_id="XL12345"')
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        self.assertIn("XL12345",a)
        self.assertIn(u"XL修改险类名称",a)
        self.assertIn(u"XL修改描述", a)
        self.assertIn('N', a)

    def test9(self):
        u''' 是否为根节点isParent为N,parentId不存在  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL修改险类名称",
                "insuranceClassesDes": "XL修改描述",
                "isParent": 'N', "parentId": "DFGDF"}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 80101)
        self.assertEqual(result['msg'], u"父类险类不存在")

    def test_10(self):
        u''' 是否为根节点isParent为N,parentId存在  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL修改险类名称",
                "insuranceClassesDes": "XL修改描述",
                "isParent": 'N', "parentId": "XL123456"}
        r = requests.put(self.base_url, data)
        result = r.json()
        a = get_mysql_data('select * from t_insurance_classes where insurance_classes_id="XL12345"')
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        self.assertIn("XL12345", a)
        self.assertIn(u"XL修改险类名称", a)
        self.assertIn(u"XL修改描述", a)
        self.assertIn('N', a)
        self.assertIn('XL123456', a)

    def test_11(self):
        u''' 是否有节点isParent非Y或N'''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL险类名称l3", "insuranceClassesDes": "XL描述",
                "isParent": 'M', "parentId": 18}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 40105)
        self.assertEqual(result['msg'], u"是否为父类选型参数不合法")

    def test_12(self):
        u''' 修改含有子级险类 '''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL修改险类名称l",
                "insuranceClassesDes": "XL修改描述",
                "isParent": 'Y'}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 30101)
        self.assertEqual(result['msg'], u"含有子级险类的险类不能进行修改")

    def test_13(self):
        u''' 险类编码insuranceClassesId不存在  '''
        data = {"insuranceClassesId": "y12346", "insuranceClassesName": "XL修改险类名称",
                "insuranceClassesDes": "yl增加险类描述",
                "isParent": 'N', "parentId": "DFGDF"}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 80102)
        self.assertEqual(result['msg'], u"险类不存在")

    def test_14(self):
        u''' 险类编码insuranceClassesId存在  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL修改险类名称",
            "insuranceClassesDes": "XL修改描述",
            "isParent": 'Y',"parentId": 0}
        r = requests.put(self.base_url, data)
        result = r.json()
        a = get_mysql_data('select * from t_insurance_classes where insurance_classes_id="XL12345"')
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        self.assertIn("XL12345", a)
        self.assertIn(u"XL修改险类名称", a)
        self.assertIn(u"XL修改描述", a)
        self.assertIn('N', a)
        self.assertIn('0', a)

if __name__ == '__main__':
    unittest.main()
