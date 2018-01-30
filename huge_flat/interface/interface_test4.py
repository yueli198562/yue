#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *


class Interface_test4(unittest.TestCase):
    u''' 修改险类 '''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://10.10.62.101:9090/insurance/insuranceClasses"
        sql(config_file_path, classes1, database_name)

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, classes2, database_name)

    def test1(self):
        u''' 所有参数为空 '''
        r = requests.put(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险类编码不能为空！")

    def test2(self):
        u''' 险类编码insuranceClassesId为空  '''
        data = {"insuranceClassesName": "XL险类名称", "insuranceClassesDes": "XL描述",
                "isParent": 'Y'}
        r = requests.put(self.base_url,data)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险类编码不能为空！")

    def test3(self):
        u''' 险类名称insuranceClassesName为空  '''
        data = {"insuranceClassesId": "XL12345",  "insuranceClassesDes": "XL描述",
                "isParent": 'Y'}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险类名称不能为空！")

    def test4(self):
        u''' 是否为根节点isParent为空  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL险类名称", "insuranceClassesDes": "XL描述",}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：是否为根节点选项不能为空")

    def test5(self):
        u''' 是否为根节点isParent为Y,parentId为空  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL修改险类名称", "insuranceClassesDes": "XL修改描述",
                "isParent": 'Y'}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test6(self):
        u''' 是否为根节点isParent为N,parentId非空  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "XL修改险类名称",
                "insuranceClassesDes": "XL修改描述",
                "isParent": 'N', "parentId": "DFGDF"}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test7(self):
        u''' 险类编码insuranceClassesId不存在  '''
        data = {"insuranceClassesId": "y12346", "insuranceClassesName": "XL修改险类名称",
                "insuranceClassesDes": "yl增加险类描述",
                "isParent": 'N', "parentId": "DFGDF"}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1005)
        self.assertEqual(result['msg'], u"数据修改失败！:修改的该险类不存在！")


    def test8(self):
        u''' 险类编码insuranceClassesId存在  '''
        data = {"insuranceClassesId": "XL12345", "insuranceClassesName": "yl修改增加险类名称",
            "insuranceClassesDes": "yl增加险类描述",
            "isParent": 'Y',"parentId": 0}
        r = requests.put(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
