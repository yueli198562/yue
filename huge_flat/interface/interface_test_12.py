#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *

class Interface_test12(unittest.TestCase):
    u''' 增加责任 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+ip+"/liability/insuranceLiability"
        get_mysql_data(risk1)
        for i in [liability1,liability_limit1,limit_values1,insurance_clause1]:
            get_mysql_data(i)

    @classmethod
    def tearDownClass(cls):
        for i in [liability2, liability_limit2, limit_values2, insurance_clause2]:
            get_mysql_data(i)
        get_mysql_data(risk2)

    def test1(self):
        u''' 修改责任 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR修改责任名称1", "insuranceLiabilityType":1,
                "insuranceLiabilityDesc":"ZR修改责任描述l","riskName":"XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y修改限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues":"4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType":"1"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url,data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y修改限额名称1"'
        get_mysql_data(limit_values)

    def test2(self):
        u''' 责任编码不存在 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR修改责任名称1", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR修改责任描述", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y修改限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 60302)
        self.assertEqual(result['msg'], u"责任ID不存在")

    def test3(self):
        u''' 险种名称不存在 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称1", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述", "riskName": "XZ险种名称yuiyui",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 60301)
        self.assertEqual(result['msg'], u"险种名称不存在")

    def test4(self):
        u''' 修改一个限额名称对应一个限额值 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR修改责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR修改责任描述6",  "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y修改新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        #-----删除测试数据-------
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        get_mysql_data(limit_values)

    def test5(self):
        u''' 修改多个限额名称，1个限额名称对应1个限额值 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR修改责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR修改责任描述6",  "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y修改新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[1].liabilityLimitName":"y修改新增限额名称2",
                "limitVoList[1].llvVOList[0].liabilityLimitValues": "5万元",
                "limitVoList[1].llvVOList[0].liabilityLimitValuesType": "1",
               }
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        #-----删除测试数据-------
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        limit_values_1= 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称2"'
        for i in [limit_values,limit_values_1]:
            get_mysql_data(i)

    def test6(self):
        u''' 修改多个限额名称，1个限额名称对应多个限额值 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR修改责任名称6",
                "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR修改责任描述6",  "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y修改新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].llvVOList[1].liabilityLimitValues": "5万元",
                "limitVoList[0].llvVOList[1].liabilityLimitValuesType": "2",
                "limitVoList[1].liabilityLimitName": "y修改限额名称2",
                "limitVoList[1].llvVOList[0].liabilityLimitValues": "6万元",
                "limitVoList[1].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[1].llvVOList[1].liabilityLimitValues": "7万元",
                "limitVoList[1].llvVOList[1].liabilityLimitValuesType": "2",}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['msg'], u"成功")
        # -----删除测试数据-------
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        limit_values_1 = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称2"'
        for i in [ limit_values, limit_values_1]:
            get_mysql_data(i)

    def test7(self):
        u''' 责任编码为空 '''
        data = {"insuranceLiabilityName": "ZR修改责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR修改责任描述6",  "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y修改新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10301)
        self.assertEqual(result['msg'], u"责任ID为空")

    def test9(self):
        u''' 责任类型为空 '''
        data = {"InsuranceLiabilityId": "ZR12345","insuranceLiabilityName": "ZR责任名称6",
                "insuranceLiabilityDesc": "ZR责任描述6",  "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10303)
        self.assertEqual(result['msg'], u"责任类型为空")

    def test_10(self):
        u''' 责任类型非0或1 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 3,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskName": "XZs险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400301)
        self.assertEqual(result['msg'], u"责任类型参数不合法")

    def test_11(self):
        u''' 险种名称为空 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10304)
        self.assertEqual(result['msg'], u"险种名称为空")

    def test_12(self):
        u''' 限额名称为空 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
            "insuranceLiabilityDesc": "ZR责任描述6", "riskName": "XZ险种名称",
            "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
            "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
            "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10305)
        self.assertEqual(result['msg'], u"责任限额名称为空")

    def test_13(self):
        u''' 限额名称大于50个字符 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6",
                "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'abcdefghijklmnopqrstuvwxyz12345678912341254784545aq',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 70303)
        self.assertEqual(result['msg'], u"限额名称长度不能超过50个字符编码")

    def test_14(self):
        u''' 限额值为空 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10306)
        self.assertEqual(result['msg'], u"限额值为空")
    #
    # # def test_15(self):#以后添加
    # #     u''' 限额值类型不合法 '''
    # #     data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6",
    # #             "insuranceLiabilityType": 1,
    # #             "insuranceLiabilityDesc": "ZR责任描述6", "riskName": "XZ险种名称",
    # #             "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
    # #             "limitVoList[0].llvVOList[0].liabilityLimitValues": "wer455",
    # #             "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1"}
    # #     f = {"multipartFile": open(updateFiles, 'r')}
    # #     r = requests.post(self.base_url, data=data, files=f)
    # #     result = r.json()
    # #     self.assertEqual(result['code'], 400302)
    # #     self.assertEqual(result['msg'], u"限额值类型参数不合法")
    # #
    def test_15(self):  #
        u''' 限额类型为空 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
            "insuranceLiabilityDesc": "ZR责任描述6",  "riskName": "XZ险种名称",
            "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
            "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 10307)
        self.assertEqual(result['msg'], u"限额值类型为空")

    def test_16(self):
        u''' 限额类型非1、2、3 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6",
                "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "5"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 400302)
        self.assertEqual(result['msg'], u"限额值类型参数不合法")

    def test_17(self):
        u''' 上传文件为空 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
            "insuranceLiabilityDesc": "ZR责任描述6",  "riskName": "XZ险种名称",
            "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
            "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
            "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
            "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"": ""}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 8)
        self.assertEqual(result['msg'], u"上传文件为空")

    def test_18(self):
        u''' 上传文件不合法 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
            "insuranceLiabilityDesc": "ZR责任描述6",  "riskName": "XZ险种名称",
            "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
            "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
            "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
            "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": ""}
        r = requests.put(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 9)
        self.assertEqual(result['msg'], u"文件上传失败：文件名称格式不合法！")

if __name__ == '__main__':
    unittest.main()
