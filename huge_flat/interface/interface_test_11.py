#coding:utf-8
import requests,unittest
from db_fixture.mysql_db import *
from db_fixture.test_data import *

class Interface_test11(unittest.TestCase):
    u''' 增加责任 '''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://10.10.62.117:9090/liability/insuranceLiability"
        sql(config_file_path,risk1,database_name)
        for i in [liability1,liability_limit1,limit_values1,insurance_clause1]:
            sql(config_file_path, i, database_name)

    @classmethod
    def tearDownClass(cls):
        for i in [liability2, liability_limit2, limit_values2, insurance_clause2]:
            sql(config_file_path, i, database_name)
        sql(config_file_path, risk2, database_name)

    def test1(self):
        u''' 责任编码已存在 '''
        data = {"InsuranceLiabilityId": "ZR12345", "insuranceLiabilityName": "ZR责任名称", "insuranceLiabilityType":1,
                "insuranceLiabilityDesc":"ZR责任描述","riskId":"XZ12345","riskName":"XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1', "limitVoList[0].llvVOList[0].liabilityLimitValues":"4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType":"1" ,"limitVoList[0].liabilityLimitDesc":"y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url,data=data,files=f)
        result = r.json()
        self.assertEqual(result['code'], 3001)
        self.assertEqual(result['msg'], u"ID已存在请重新输入责任编码")
        liability = 'delete from t_insurance_liability where insurance_liability_id="ZR123456"'
        liability_limit = 'delete from t_liability_limit where insurance_liability_id="ZR123456"'
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        insurance_clause = 'delete from t_insurance_clause where their_id="ZR123456"'
        for i in [liability, liability_limit, limit_values, insurance_clause]:
            sql(config_file_path, i, database_name)

    def test2(self):
        u''' 添加一个限额名称对应一个限额值 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        #-----删除测试数据-------
        liability = 'delete from t_insurance_liability where insurance_liability_id="ZR123456"'
        liability_limit = 'delete from t_liability_limit where insurance_liability_id="ZR123456"'
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        insurance_clause = 'delete from t_insurance_clause where their_id="ZR123456"'
        for i in [liability, liability_limit, limit_values, insurance_clause]:
            sql(config_file_path, i, database_name)

    def test3(self):
        u''' 添加多个限额名称，1个限额名称对应1个限额值 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc":"y新增责任限额描述1",
                "limitVoList[1].liabilityLimitName":"y新增限额名称2",
                "limitVoList[1].llvVOList[0].liabilityLimitValues": "5万元",
                "limitVoList[1].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[1].liabilityLimitDesc": "y新增责任限额描述2"
               }
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        #-----删除测试数据-------
        liability = 'delete from t_insurance_liability where insurance_liability_id="ZR123456"'
        liability_limit = 'delete from t_liability_limit where insurance_liability_id="ZR123456"'
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        limit_values_1= 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称2"'
        insurance_clause = 'delete from t_insurance_clause where their_id="ZR123456"'
        for i in [liability, liability_limit, limit_values,limit_values_1, insurance_clause]:
            sql(config_file_path, i, database_name)

    def test4(self):
        u''' 添加多个限额名称，1个限额名称对应多个限额值 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6",
                "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].llvVOList[1].liabilityLimitValues": "5万元",
                "limitVoList[0].llvVOList[1].liabilityLimitValuesType": "2",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述1",
                "limitVoList[1].liabilityLimitName": "y新增限额名称2",
                "limitVoList[1].llvVOList[0].liabilityLimitValues": "6万元",
                "limitVoList[1].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[1].llvVOList[1].liabilityLimitValues": "7万元",
                "limitVoList[1].llvVOList[1].liabilityLimitValuesType": "2",
                "limitVoList[1].liabilityLimitDesc": "y新增责任限额描述2"
                }
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        # -----删除测试数据-------
        liability = 'delete from t_insurance_liability where insurance_liability_id="ZR123456"'
        liability_limit = 'delete from t_liability_limit where insurance_liability_id="ZR123456"'
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        limit_values_1 = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称2"'
        insurance_clause = 'delete from t_insurance_clause where their_id="ZR123456"'
        for i in [liability, liability_limit, limit_values, limit_values_1, insurance_clause]:
            sql(config_file_path, i, database_name)

    def test5(self):
        u''' 责任编码为空 '''
        data = {"insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：责任编码不能为空！")

    def test6(self):
        u''' 责任类型为空 '''
        data = {"InsuranceLiabilityId": "ZR123456","insuranceLiabilityName": "ZR责任名称6",
                "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：责任类型不能为空！")

    def test7(self):#、、、、、、、、
        u''' 关联险种id为空 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        # -----删除测试数据-------
        liability = 'delete from t_insurance_liability where insurance_liability_id="ZR123456"'
        liability_limit = 'delete from t_liability_limit where insurance_liability_id="ZR123456"'
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        limit_values_1 = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称2"'
        insurance_clause = 'delete from t_insurance_clause where their_id="ZR123456"'
        for i in [liability, liability_limit, limit_values, limit_values_1, insurance_clause]:
            sql(config_file_path, i, database_name)

    def test8(self):
        u''' 险种名称为空 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：险种名称不能为空！")

    def test9(self):
        u''' 限额名称为空 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
            "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
            "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
            "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
            "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：限额名称不能为空！")

    def test_10(self):
        u''' 限额值为空 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1001)
        self.assertEqual(result['msg'], u"参数为空：限额值不能为空！")

    def test_11(self):  #
        u''' 限额类型为空 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
            "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
            "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
            "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
            "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": open(updateFiles, 'r')}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        #删除数据
        liability = 'delete from t_insurance_liability where insurance_liability_id="ZR123456"'
        liability_limit = 'delete from t_liability_limit where insurance_liability_id="ZR123456"'
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        insurance_clause = 'delete from t_insurance_clause where their_id="ZR123456"'
        for i in [liability, liability_limit, limit_values, limit_values, insurance_clause]:
            sql(config_file_path, i, database_name)

    def test_12(self):
        u''' 上传文件为空 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
            "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
            "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
            "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
            "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
            "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"": ""}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 2001)
        self.assertEqual(result['msg'], u"上传文件为空！")

    def test_13(self):
        u''' 上传文件不合法 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
            "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
            "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
            "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
            "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
            "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = {"multipartFile": ""}
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 2002)
        self.assertEqual(result['msg'], u"文件上传失败！：文件名称格式不合法！")

    def test_14(self):
        u''' 添加多个文件 '''
        data = {"InsuranceLiabilityId": "ZR123456", "insuranceLiabilityName": "ZR责任名称6", "insuranceLiabilityType": 1,
                "insuranceLiabilityDesc": "ZR责任描述6", "riskId": "XZ12345", "riskName": "XZ险种名称",
                "limitVoList[0].liabilityLimitName": 'y新增限额名称1',
                "limitVoList[0].llvVOList[0].liabilityLimitValues": "4万元",
                "limitVoList[0].llvVOList[0].liabilityLimitValuesType": "1",
                "limitVoList[0].liabilityLimitDesc": "y新增责任限额描述"}
        f = [
            ("multipartFile", open(updateFilesb, "rb")),
            ("multipartFile", open(updateFiles, "rb")),
        ]
        r = requests.post(self.base_url, data=data, files=f)
        result = r.json()
        self.assertEqual(result['code'], 1002)
        self.assertEqual(result['msg'], u"成功")
        # -----删除测试数据-------
        liability = 'delete from t_insurance_liability where insurance_liability_id="ZR123456"'
        liability_limit = 'delete from t_liability_limit where insurance_liability_id="ZR123456"'
        limit_values = 'delete from t_liability_limit_values where liability_limit_name="y新增限额名称1"'
        insurance_clause = 'delete from t_insurance_clause where their_id="ZR123456"'
        for i in [liability, liability_limit, limit_values, insurance_clause]:
            sql(config_file_path, i, database_name)

if __name__ == '__main__':
    unittest.main()
