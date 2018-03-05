#coding:utf-8
import requests,unittest
from function.function import *
from function.mysql_db import *
from function.test_data import *

class test_zr1(unittest.TestCase):
    u'''普通案件报案接口 '''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+url+"/jtCase/vCore1/commonReport"
        sql(config_file_path, case_form, database_name)

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, case_form2, database_name)

    def test1(self):
        u'''自如流水号为空'''
        data = """{
            "houseNo":"123456",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号为空")

    def test2(self):
        u'''出险房源号为空'''
        data = """{
            "serialNumber":"qsdfsdfwer11",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"房源号或报案时间有误")

    # def test3(self):
    #     u'''房源所在省编号不存在'''
    #     data = """{
    #         "serialNumber":"1110112113116115116118",
    #         "houseNo":"123459",
    #         "provinceCode":"898978",
    #         "cityCode":"150100",
    #         "districtCode":"150105",
    #         "houseAddress":"天府大道199号4号楼",
    #         "accidentTime":"2017-12-12 13:26:59",
    #         "accidentDetail":"事故经过",
    #         "estimateLoss":100.53,
    #         "reportName":"飞天",
    #         "reportTime":"2017-12-13 13:26:59",
    #         "contactPeople":"飞天",
    #         "contactTelephone":"010-62202788",
    #         "contactEmail":"xxxx@jiangtai.com",
    #         "isPeopleHurt":"1",
    #         "isBigCase":"N",
    #         "isNaturalDisaster": "N",
    #         "channelSource":"jts0oe7silrxv3upx5"}"""
    #     t, m = transform_md5(data)
    #     data = {'data': t, 'sign': m}
    #     r = requests.post(self.base_url, data)
    #     result = r.json()
    #     for i in result:
    #         print i, result[i]
    #     for i in result["data"]:
    #         print i, result["data"][i]
    #     self.assertEqual(result['code'], 200)
    #     self.assertEqual(result['message'], u"成功")
    #
    # def test4(self):
    #     u'''房源所在市编号不存在'''
    #     data = """{
    #     "serialNumber":"1110112113116115116117",
    #     "houseNo":"YZ-102",
    #     "provinceCode":"150000",
    #     "cityCode":"9889898",
    #     "districtCode":"150105",
    #     "houseAddress":"天府大道199号4号楼",
    #     "accidentTime":"2017-12-12 13:26:59",
    #     "accidentDetail":"事故经过",
    #     "estimateLoss":100.53,
    #     "reportName":"飞天",
    #     "reportTime":"2017-12-13 13:26:59",
    #     "contactPeople":"飞天",
    #     "contactTelephone":"010-62202788",
    #     "contactEmail":"xxxx@jiangtai.com",
    #     "isPeopleHurt":"1",
    #     "isBigCase":"N",
    #     "isNaturalDisaster": "N",
    #     "channelSource":"jts0oe7silrxv3upx5"}"""
    #     t, m = transform_md5(data)
    #     data = {'data': t, 'sign': m}
    #     r = requests.post(self.base_url, json=data)
    #     result = r.json()
    #     for i in result:
    #         print i, result[i]
    #
    # def test5(self):
    #     u'''房源所在区编号不存在'''
    #     data = """{
    #     "serialNumber":"1110112113116115116117",
    #     "houseNo":"YZ-102",
    #     "provinceCode":"150000",
    #     "cityCode":"150100",
    #     "districtCode":"978987",
    #     "houseAddress":"天府大道199号4号楼",
    #     "accidentTime":"2017-12-12 13:26:59",
    #     "accidentDetail":"事故经过",
    #     "estimateLoss":100.53,
    #     "reportName":"飞天",
    #     "reportTime":"2017-12-13 13:26:59",
    #     "contactPeople":"飞天",
    #     "contactTelephone":"010-62202788",
    #     "contactEmail":"xxxx@jiangtai.com",
    #     "isPeopleHurt":"1",
    #     "isBigCase":"N",
    #     "isNaturalDisaster": "N",
    #     "channelSource":"jts0oe7silrxv3upx5"}"""
    #     t, m = transform_md5(data)
    #     data = {'data': t, 'sign': m}
    #     r = requests.post(self.base_url, json=data)
    #     result = r.json()
    #     for i in result:
    #         print i, result[i]
    #
    # def test6(self):
    #     u'''房源省编号市编号区编号不匹配'''
    #     data = """{
    #         "serialNumber":"1110112113116115116117",
    #         "houseNo":"YZ-102",
    #         "provinceCode": "150000",
    #         "cityCode": "140200",
    #         "districtCode": "210283",
    #         "houseAddress":"天府大道199号4号楼",
    #         "accidentTime":"2017-12-12 13:26:59",
    #         "accidentDetail":"事故经过",
    #         "estimateLoss":100.53,
    #         "reportName":"飞天",
    #         "reportTime":"2017-12-13 13:26:59",
    #         "contactPeople":"飞天",
    #         "contactTelephone":"010-62202788",
    #         "contactEmail":"xxxx@jiangtai.com",
    #         "isPeopleHurt":"1",
    #         "isBigCase":"N",
    #         "isNaturalDisaster": "N",
    #         "channelSource":"jts0oe7silrxv3upx5"}"""
    #     t, m = transform_md5(data)
    #     data = {'data': t, 'sign': m}
    #     r = requests.post(self.base_url, json=data)
    #     result = r.json()
    #     for i in result:
    #         print i, result[i]
    #     self.assertEqual(result['code'], 200)
    #     self.assertEqual(result['message'], u"成功")

    def test7(self):
        u''' 房源详细地址为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"房源详细地址不能为空;")

    def test8(self):
        u'''出险时间为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"出险时间不能为空;")

    def test9(self):
        u'''出险时间格式错误'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017/12/12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"出险时间格式有误;")

    def test_10(self):
        u'''出险时间晚于当前时间'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2022-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"出险时间超出系统时间;")

    def test_11(self):
        u'''事故经过为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"事故经过不能为空;")

    def test_12(self):
        u'''估损金额为空'''
        data = """{
        "serialNumber":"1110112113116",
        "houseNo":"YZ-102",
        "provinceCode":"150000",
        "cityCode":"150100",
        "districtCode":"150105",
        "houseAddress":"天府大道199号4号楼",
        "accidentTime":"2017-12-12 13:26:59",
        "accidentDetail":"事故经过",
        "reportName":"飞天",
        "reportTime":"2017-12-13 13:26:59",
        "contactPeople":"飞天",
        "contactTelephone":"010-62202788",
        "contactEmail":"xxxx@jiangtai.com",
        "isPeopleHurt":"1",
        "isBigCase":"N",
        "isNaturalDisaster": "N",
        "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"估损金额不能为空;")

    def test_13(self):
        u'''估损金额小数点后四位'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.5396,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"估损金额格式有误;")

    def test_14(self):
        u'''估损金额非Double类型'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":"三百元整",
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"估损金额格式有误;")

    def test_15(self):
        u'''报案人为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案人不能为空;")

    def test_16(self):
        u'''报案时间为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"房源号或报案时间有误")

    def test_17(self):
        u'''报案时间格式错误'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017/12/13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案时间格式有误;")

    def test_18(self):
        u'''报案时间晚于当前时间'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2022-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案时间超出系统时间;")

    def test_19(self):
        u'''联系人为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"联系人不能为空;")

    def test_20(self):
        u'''联系人电话为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"联系人电话不能为空;")

    # def test_21(self):#未校验
    #     u'''联系人电话格式错误'''
    #     data = """{
    #         "serialNumber":"1110112113116",
    #         "houseNo":"YZ-102",
    #         "provinceCode":"150000",
    #         "cityCode":"150100",
    #         "districtCode":"150105",
    #         "houseAddress":"天府大道199号4号楼",
    #         "accidentTime":"2017-12-12 13:26:59",
    #         "accidentDetail":"事故经过",
    #         "estimateLoss":100.53,
    #         "reportName":"飞天",
    #         "reportTime":"2017-12-13 13:26:59",
    #         "contactPeople":"飞天",
    #         "contactTelephone":"1565",
    #         "contactEmail":"xxxx@jiangtai.com",
    #         "isPeopleHurt":"1",
    #         "isBigCase":"N",
    #         "isNaturalDisaster": "N",
    #         "channelSource":"jts0oe7silrxv3upx5"}"""
    #     t, m = transform_md5(data)
    #     data = {'data': t, 'sign': m}
    #     r = requests.post(self.base_url, data)
    #     result = r.json()
    #     for i in result:
    #         print i, result[i]
    #     for i in result["data"]:
    #         print i, result["data"][i]
    #     self.assertEqual(result['code'], u"200")
    #     self.assertEqual(result['message'], u"访问成功")
    #     self.assertEqual(result['data']['resultCode'], u"00000")
    #     self.assertEqual(result['data']['resultMsg'], u"报案成功")

    # def test_22(self):
    #     u'''联系人邮箱格式错误'''
    #     data = """{
    #         "serialNumber":"1110112113116",
    #         "houseNo":"YZ-102",
    #         "provinceCode":"150000",
    #         "cityCode":"150100",
    #         "districtCode":"150105",
    #         "houseAddress":"天府大道199号4号楼",
    #         "accidentTime":"2017-12-12 13:26:59",
    #         "accidentDetail":"事故经过",
    #         "estimateLoss":100.53,
    #         "reportName":"飞天",
    #         "reportTime":"2017-12-13 13:26:59",
    #         "contactPeople":"飞天",
    #         "contactTelephone":"010-62202788",
    #         "contactEmail":"234234234234",
    #         "isPeopleHurt":"1",
    #         "isBigCase":"N",
    #         "isNaturalDisaster": "N",
    #         "channelSource":"jts0oe7silrxv3upx5"}"""
    #     t, m = transform_md5(data)
    #     data = {'data': t, 'sign': m}
    #     r = requests.post(self.base_url, data)
    #     result = r.json()
    #     for i in result:
    #         print i, result[i]
    #     for i in result["data"]:
    #         print i, result["data"][i]
    #     self.assertEqual(result['code'], u"200")
    #     self.assertEqual(result['message'], u"访问成功")
    #     self.assertEqual(result['data']['resultCode'], u"00000")
    #     self.assertEqual(result['data']['resultMsg'], u"报案成功")

    def test_23(self):
        u'''是否含人伤为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"是否含人伤不能为空;")

    def test_24(self):
        u'''是否含人伤非0或1'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"8",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"人伤类型有误;")


    def test_25(self):
        u'''重大事故为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"是否为重大事故不能为空;")

    def test_26(self):#重大事故非N或Y 返回成功
        u'''重大事故非N或Y'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"3",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"重大事故类型有误;")


    def test_27(self):
        u'''自然灾害为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"自然灾害不能为空;")


    def test_28(self):
        u'''自然灾害非Y或N'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "9",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"自然灾害类型有误;")


    def test_29(self):
        u'''来源标识为空'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_30(self):
        u'''来源标识内容错误'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0456464rxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_31(self):
        u'''入参正确'''
        data = """{
            "serialNumber":"1110112113116",
            "houseNo":"YZ-102",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天府大道199号4号楼",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过",
            "estimateLoss":100.53,
            "reportName":"飞天",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"飞天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"报案成功")

    def test_32(self):
        u'''流水号已存在'''
        data = """{
        "serialNumber":"1110112113116",
        "houseNo":"YZ-102",
        "provinceCode":"150000",
        "cityCode":"150100",
        "districtCode":"150105",
        "houseAddress":"天府大道199号4号楼",
        "accidentTime":"2017-12-12 13:26:59",
        "accidentDetail":"事故经过",
        "estimateLoss":100.53,
        "reportName":"飞天",
        "reportTime":"2017-12-13 13:26:59",
        "contactPeople":"飞天",
        "contactTelephone":"010-62202788",
        "contactEmail":"xxxx@jiangtai.com",
        "isPeopleHurt":"1",
        "isBigCase":"N",
        "isNaturalDisaster": "N",
        "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号已存在")

    def test_33(self):
        u'''同一个出险日期房源号已存在'''
        data = """{
        "serialNumber":"110112113116",
        "houseNo":"YZ-102",
        "provinceCode":"150000",
        "cityCode":"150100",
        "districtCode":"150105",
        "houseAddress":"天府大道199号4号楼",
        "accidentTime":"2017-12-12 13:26:59",
        "accidentDetail":"事故经过",
        "estimateLoss":100.53,
        "reportName":"飞天",
        "reportTime":"2017-12-13 13:26:59",
        "contactPeople":"飞天",
        "contactTelephone":"010-62202788",
        "contactEmail":"xxxx@jiangtai.com",
        "isPeopleHurt":"1",
        "isBigCase":"N",
        "isNaturalDisaster": "N",
        "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"获取成功")
        self.assertEqual(result['data']['resultCode'], u"11111")
        self.assertEqual(result['data']['resultMsg'], u"重复报案")

if __name__ == '__main__':
    unittest.main()
