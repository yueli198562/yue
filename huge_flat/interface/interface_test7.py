#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *

class Interface_test7(unittest.TestCase):
    u''' 增加险种 '''

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
        u''' 险种编码riskId已存在 '''
        data = {"riskId": "XZ12345", "riskName": "XZ险种名称", "riskDesc": "XZ描述",
                "insuranceClassesId":"XL12345", "riskFlag": "M","riskGroupFlag":"G","riskShortFlag":"L"}
        f={"updateFiles":open(updateFiles,'r')}
        r = requests.post(self.base_url,data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 3001)
        self.assertEqual(result['msg'], u"ID已存在请重新输入险种编码")

    def test2(self):
        u''' 险种编码riskId不存在 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        # 删除插入数据
        risk = 'delete from t_risk_info where risk_id="XZ123456";'
        sql(config_file_path, risk, database_name)

    def test3(self):
        u''' 险种编码riskId为空 '''
        data = {"riskName": "XZ险种名称", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url,data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险种编码不能为空！")

    def test5(self):
        u''' 险种名称riskName为空 '''
        data = {"riskId": "XZ123456", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险种名称不能为空！")

    def test6(self):
        u''' 所属险类insuranceClassesId为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称", "riskDesc": "XZ描述",
                 "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：所属险类不能为空")

    def test7(self):
        u''' 主附加险标识riskFlag为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：请选择险种为主险还是附加险")

    def test8(self):
        u''' 团个险标识riskGroupFlag为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M","riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：请选择险种为团体还是个人")

    def test9(self):
        u''' 长短险标识riskShortFlag为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：请选择险种为长期还是短期")

    def test_10(self):
        u''' 上传文件updateFiles文件名不合法 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M","riskGroupFlag": "G", "riskShortFlag": "L"}
        # f = {"updateFiles":""}
        f = {"": ""}
        r = requests.post(self.base_url, data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 2002)
        self.assertEqual(result['msg'], u"文件上传失败！：文件名称格式不合法！")

    def test_11(self):
        u''' 上传文件updateFiles为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"": ""}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 2001)
        self.assertEqual(result['msg'], u"上传文件为空！")

if __name__ == '__main__':
    unittest.main()
