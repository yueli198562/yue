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
        data = {"riskId": "XZ12345", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId":"XL12345", "riskFlag": "M","riskGroupFlag":"G","riskShortFlag":"L"}
        f={"updateFiles":open(updateFiles,'r')}
        r = requests.post(self.base_url,data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 90201)
        self.assertEqual(result['msg'], u"险种编码已经存在")

    def test2(self):
        u''' 险种编码riskId不存在 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        #删除插入数据
        risk = 'delete from t_risk_info where risk_id="XZ123456";'
        insurance_clause = 'delete from t_insurance_clause where their_id="XZ123456"'
        for i in [risk,insurance_clause]:
            sql(config_file_path, i, database_name)

    def test3(self):
        u''' 险种编码riskId为空 '''
        data = {"riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url,data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 10201)
        self.assertEqual(result['msg'], u"险种编码不能为空")

    def test4(self):
        u''' 险种编码riskId大于20个字符 '''
        data = {"riskId": "XZ123456sfdgertwertwertwertwertwert", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400201)
        self.assertEqual(result['msg'], u"险种编码不能超过20个字符")

    def test5(self):
        u''' 险种名称riskName为空 '''
        data = {"riskId": "XZ123456", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10202)
        self.assertEqual(result['msg'], u"险种名称不能为空")

    def test6(self):
        u''' 险种名称大于20个字符 '''
        data = {"riskId": "XZ123456","riskName": "XZ险种名称ldfasdfasdfasdfadfasdfasdf","riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400205)
        self.assertEqual(result['msg'], u"险种名称不能超过20个字符")

    def test6(self):
        u''' 险种描述大于200个字符 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称ls",
                "riskDesc":"""他让他让他让他让他开始试测试测试开始自动化
                测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突抬""",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400206)
        self.assertEqual(result['msg'], u"险种描述不能超过200个字符")

    def test7(self):
        u''' 所属险类insuranceClassesId为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                 "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10203)
        self.assertEqual(result['msg'], u"所属险类不能为空")

    def test8(self):
        u''' 所属险类insuranceClassesId不存在 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "Xghghj5","riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 60201)
        self.assertEqual(result['msg'], u"所属险类不存在")

    def test9(self):
        u''' 主附加险标识riskFlag为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10204)
        self.assertEqual(result['msg'], u"主险附加险选项参数不能为空")

    def test_10(self):
        u''' 主附加险标识riskFlag非M和A '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345","riskFlag": "f","riskGroupFlag": "G","riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400204)
        self.assertEqual(result['msg'], u"主险附加险选项参数不合法")

    def test_11(self):
        u''' 团个险标识riskGroupFlag为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M","riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10205)
        self.assertEqual(result['msg'], u"团体个人选项参数不能为空")

    def test_12(self):
        u''' 团个险标识riskGroupFlag非G和A '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "P", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400202)
        self.assertEqual(result['msg'], u"团体个人选项参数不合法")

    def test_13(self):
        u''' 长短险标识riskShortFlag为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10206)
        self.assertEqual(result['msg'], u"长期短期选项参数不能为空")

    def test_14(self):
        u''' 长短险标识riskShortFlag非L和S '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G","riskShortFlag": "R"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400203)
        self.assertEqual(result['msg'], u"长期短期选项参数不合法")

    def test_15(self):
        u''' 上传文件updateFiles文件名不合法 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M","riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles":""}
        r = requests.post(self.base_url, data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 9)
        self.assertEqual(result['msg'], u"文件上传失败")

    def test_16(self):
        u''' 上传文件updateFiles为空 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"": ""}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 8)
        self.assertEqual(result['msg'], u"上传文件为空")

    def test_17(self):
        u''' 上传多个文件 '''
        data = {"riskId": "XZ123456", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = [
            ("updateFiles", open(updateFilesb, "rb")),
            ("updateFiles", open(updateFiles, "rb")),
        ]
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        # 删除插入数据
        risk = 'delete from t_risk_info where risk_id="XZ123456";'
        insurance_clause = 'delete from t_insurance_clause where their_id="XZ123456"'
        for i in [risk, insurance_clause]:
            sql(config_file_path, i, database_name)

if __name__ == '__main__':
    unittest.main()
