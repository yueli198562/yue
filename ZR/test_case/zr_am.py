#coding:utf-8
import requests,unittest
from function.function import *
from function.mysql_db import *
from function.test_data import *

class test_zr1(unittest.TestCase):
    u'''普通案件报案接口 '''
    @classmethod
    def setUpClass(cls):
        cls.url1 = "http://10.10.62.88:8083/jtCase/vCore1/commonReport"#普通案件
        cls.url2 = "http://10.10.62.88:8083/jtCase/vCore1/commonClaims" #人伤
        cls.url3 = "http://10.10.62.88:8083/jtCase/vCore1/claimConfirmSync" #自如理赔
        cls.url4 = "http://10.10.62.88:8083/caseDeal/vCore1/caseClosed" #am结案接口
        cls.url5 = "http://10.10.62.88:8083/caseDeal/vCore1/payStateSync" #支付状态同步接口
        cls.url6 = "http://10.10.62.88:8083/caseDeal/vCore1/reportNoSync" #报案号同步接口
        cls.url7 = "http://10.10.62.88:8083/caseDeal/vCore1/claimConfirmSync" #am理赔确认接口

    def test1(self):
        u'''普通案件接口'''
        data = """{
            "serialNumber":"1123456789123456",
            "houseNo":"t-101",
            "provinceCode":"150000",
            "cityCode":"150100",
            "districtCode":"150105",
            "houseAddress":"天津@@@#######",
            "accidentTime":"2017-12-12 13:26:59",
            "accidentDetail":"事故经过…………",
            "estimateLoss":100.53,
            "reportName":"小李",
            "reportTime":"2017-12-13 13:26:59",
            "contactPeople":"天天",
            "contactTelephone":"010-62202788",
            "contactEmail":"xxxx@jiangtai.com",
            "isPeopleHurt":"1",
            "isBigCase":"N",
            "isNaturalDisaster": "N",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.url1, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"报案成功")

    def test2(self):
        u'''人伤'''
        data = """{
            "serialNumber":"1110112113116",
            "reportNo":"62222519",
            "totalEstimateLoss":500,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":400}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.url2, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"已提交")
        self.assertEqual(result['data']['reportNo'], u"62222519")
        self.assertEqual(result['data']['acceptedHurtNo'], u"1110112113116")

    def test3(self):
        u'''zr理赔'''
        data = '''{"serialNumber": "4110112113114",
            "reportNo": "jt_150000150100a2667deca2c74c34b8d5b93e59a36857",
            "confirmFlag": 1,
            "confirmDesc": "房屋的损失也应该加上",
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.url3, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"理赔确认成功")

    def test4(self):
        u'''am结案接口'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"泰康在线财产保险股份有限公司",
                "reportNo":"62222519",
                "PolicyNo":"RV2H227002017900189",
                "insPeriod":"2017-03-16 00:00:00到2017-03-20 23:59:59",
                "actualAmount":120.05,
                "accidentPeriod":"2017-03-18 13:53:41",
                "payNature":"4",
                "HouseNo":"YZ-102",
                "HouseAddress":"天府大道199号4号楼",
                "calculationProcess":"***<赔付标的：>***",
                "auditTime":"2017-03-18 13:53:41",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.url4, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']["resultCode"], u"00000")
        self.assertEqual(result['data']["resultMsg"], u"结案成功")

    def test5(self):
        u'''支付状态同步接口'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.url4, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']["resultCode"], u"00000")
        self.assertEqual(result['data']["resultMsg"], u"支付状态同步成功")

    def test6(self):
        u'''参数正确'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '421212333',
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.url6, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"报案号同步成功")

    def test7(self):
        u'''参数正确'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"小白"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.url7, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"提交确认理赔成功")

if __name__ == '__main__':
    unittest.main()


