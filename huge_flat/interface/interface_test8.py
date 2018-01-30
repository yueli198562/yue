#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *

class Interface_test8(unittest.TestCase):
    u''' 修改险种 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://10.10.62.101:9090/insurance/riskInfo"
        sql(config_file_path, classes1, database_name)
        sql(config_file_path, risk1, database_name)

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, classes2, database_name)
        sql(config_file_path, risk2, database_name)

    def test1(self):
        u''' 修改险种内容 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId":"XL12345", "riskFlag": "A","riskGroupFlag":"A","riskShortFlag":"S"}
        f={"updateFiles":open(updateFiles,'r')}
        r = requests.put(self.base_url,data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

    def test2(self):
        u''' 险种编码riskId不存在 '''
        data = {"riskId": "XZ12345666", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()

        self.assertEqual(result['code'], 1005)
        self.assertEqual(result['msg'], u"数据修改失败！:修改的险种不存在")

    def test3(self):
        u''' 险种编码riskId为空 '''
        data = { "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险种编码不能为空！")

    def test4(self):
        u''' 险种名称riskName为空 '''
        data = {"riskId": "XZ12345", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险种名称不能为空！")

    def test5(self):
        u''' 所属险类insuranceClassesId为空 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1005)
        self.assertEqual(result['msg'], u"数据修改失败！:修改的险种所属的险类不存在")

    def test6(self):
        u''' 主附加险标识riskFlag为空 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345","riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：请选择险种为主险还是附加险")

    def test7(self):
        u''' 团个险标识riskGroupFlag为空 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A","riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：请选择险种为团体还是个人")

    def test8(self):
        u''' 长短险标识riskShortFlag为空 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：请选择险种为长期还是短期")

    def test9(self):
        u''' 修改updateFiles上传文件 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFilesb, 'r')}
        r = requests.put(self.base_url,data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
