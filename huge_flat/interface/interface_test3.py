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
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL险类名称", "insuranceClassesDes": "XL描述",
                "isParent": 'Y', "parentId": "DFGDF"}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 3001)
        self.assertEqual(result['msg'], u"ID已存在")

    def test2(self):
        u''' 险类编码不存在'''
        data = {"insuranceClassesId": "XL123456","insuranceClassesName":"XL险类名称",
                "insuranceClassesDes":"XL描述","isParent":'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        classes = 'delete from t_insurance_classes where insurance_classes_id="XL123456"'
        sql(config_file_path, classes, database_name)

    def test3(self):
        u''' isParent为N，parentId为空 '''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL险类名称", "insuranceClassesDes": "XL描述",
                "isParent": 'N'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险类不是根节点，上级险类不能为空！")

    def test4(self):
        u''' isParent为N，parentId不为空 '''
        data = {"insuranceClassesId": "XL123456", "insuranceClassesName": "XL险类名称",
                "insuranceClassesDes": "XL描述",
                "isParent": 'N',"parentId":18}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        #------删除插入数据------
        classes = 'delete from t_insurance_classes where insurance_classes_id="XL123456"'
        sql(config_file_path, classes, database_name)

    def test5(self):
        u''' 所有参数为空 '''
        r = requests.post(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险类编码不能为空！")

    def test6(self):
        u''' 险类编码insuranceClassesId为空'''
        data = {"insuranceClassesName": "XL险类名称",
                "insuranceClassesDes": "XL描述", "isParent": 'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险类编码不能为空！")

    def test7(self):
        u''' 险类名称insuranceClassesName为空'''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesDes": "XL描述",
                "isParent": 'Y'}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险类名称不能为空！")

    def test8(self):
        u''' 是否有节点isParent为空'''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL险类名称", "insuranceClassesDes": "XL描述",
                "parentId":18}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：是否为根节点选项不能为空")

if __name__ == '__main__':
    unittest.main()
