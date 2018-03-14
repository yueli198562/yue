#coding:utf-8
import requests,unittest

from db_fixture.test_data import *
from db_fixture.mysql_db import *

class Interface_test8(unittest.TestCase):
    u''' 修改险种 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+ip+"/insurance/riskInfo"
        get_mysql_data(classes1)
        get_mysql_data(risk1)

    @classmethod
    def tearDownClass(cls):
        get_mysql_data(classes2)
        get_mysql_data(risk2)

    def test1(self):
        u''' 修改险种内容 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId":"XL12345", "riskFlag": "A","riskGroupFlag":"A","riskShortFlag":"S"}
        f={"updateFiles":open(updateFiles,'r')}
        r = requests.put(self.base_url,data=data,files=f)
        result = r.json()
        a = get_mysql_data('select * from t_risk_info where risk_id="XZ12345"')
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        self.assertIn("XL12345", a)
        self.assertIn(u"XZ修改险种名称", a)
        self.assertIn(u"XZ修改描述", a)
        self.assertIn('A', a)
        self.assertIn('A', a)
        self.assertIn('S', a)

    def test2(self):
        u''' 险种编码riskId不存在 '''
        data = {"riskId": "XZ12345666", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 60202)
        self.assertEqual(result['msg'], u"所属险种不存在")

    def test3(self):
        u''' 险种编码riskId为空 '''
        data = { "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10201)
        self.assertEqual(result['msg'], u"险种编码不能为空")

    def test4(self):
        u''' 险种编码riskId大于20个字符 '''
        data = {"riskId": "XZ123456sfdgertwertwertwertwertwert", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400201)
        self.assertEqual(result['msg'], u"险种编码不能超过20个字符")

    def test5(self):
        u''' 险种名称riskName为空 '''
        data = {"riskId": "XZ12345", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10202)
        self.assertEqual(result['msg'], u"险种名称不能为空")

    def test6(self):
        u''' 险种名称大于20个字符 '''
        data = {"riskId": "XZ12345", "riskName": "XZ险种名称ldfasdfasdfasdfadfasdfasdf", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400205)
        self.assertEqual(result['msg'], u"险种名称不能超过20个字符")

    def test7(self):
        u''' 险种描述大于200个字符 '''
        data = {"riskId": "XZ12345", "riskName": "XZ险种名称ls",
                "riskDesc": """他让他让他让他让他开始试测试测试开始自动化
                测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突然抬头突，
                他让他让他让他让他开始试测试测试开始自动化测试测试突然抬头突然突然让他让他让他让他让他让他突抬""",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400206)
        self.assertEqual(result['msg'], u"险种描述不能超过200个字符")

    def test8(self):
        u''' 所属险类insuranceClassesId为空 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10203)
        self.assertEqual(result['msg'], u"所属险类不能为空")

    def test9(self):
        u''' 所属险类insuranceClassesId不存在 '''
        data = {"riskId": "XZ12345", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "Xghghj5", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 60201)
        self.assertEqual(result['msg'], u"所属险类不存在")

    def test_10(self):
        u''' 主附加险标识riskFlag为空 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345","riskGroupFlag": "A", "riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10204)
        self.assertEqual(result['msg'], u"主险附加险选项参数不能为空")

    def test_11(self):
        u''' 主附加险标识riskFlag非M和A '''
        data = {"riskId": "XZ12345", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "f", "riskGroupFlag": "G", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400204)
        self.assertEqual(result['msg'], u"主险附加险选项参数不合法")

    def test_12(self):
        u''' 团个险标识riskGroupFlag为空 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A","riskShortFlag": "S"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10205)
        self.assertEqual(result['msg'], u"团体个人选项参数不能为空")

    def test_13(self):
        u''' 团个险标识riskGroupFlag非G和A '''
        data = {"riskId": "XZ12345", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "P", "riskShortFlag": "L"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400202)
        self.assertEqual(result['msg'], u"团体个人选项参数不合法")

    def test_14(self):
        u''' 长短险标识riskShortFlag为空 '''
        data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
                "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10206)
        self.assertEqual(result['msg'], u"长期短期选项参数不能为空")

    def test_15(self):
        u''' 长短险标识riskShortFlag非L和S '''
        data = {"riskId": "XZ12345", "riskName": "XZ险种名称l", "riskDesc": "XZ描述",
                "insuranceClassesId": "XL12345", "riskFlag": "M", "riskGroupFlag": "G", "riskShortFlag": "R"}
        f = {"updateFiles": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400203)
        self.assertEqual(result['msg'], u"长期短期选项参数不合法")
    #
    # def test9(self):
    #     u''' 修改updateFiles上传文件 '''
    #     data = {"riskId": "XZ12345", "riskName": "XZ修改险种名称", "riskDesc": "XZ修改描述",
    #             "insuranceClassesId": "XL12345", "riskFlag": "A", "riskGroupFlag": "A", "riskShortFlag": "S"}
    #     f = {"updateFiles": open(updateFilesb, 'r')}
    #     r = requests.put(self.base_url,data=data,files=f)
    #     result = r.json()
    #     self.assertEqual(result['code'], 200)
    #     self.assertEqual(result['msg'], u"成功")

if __name__ == '__main__':
    unittest.main()
