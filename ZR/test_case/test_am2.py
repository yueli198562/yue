#coding:utf-8
import requests,unittest
from function.function import *
from function.mysql_db import *
from function.test_data import *

class test_am2(unittest.TestCase):
    u'''支付状态同步接口'''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://10.10.62.88:8083/caseDeal/vCore1/payStateSync"
        sql(config_file_path, case_form, database_name)  # 案件信息表插入数据
        sql(config_file_path, MASTER, database_name)  # 结案主表插入数据
        sql(config_file_path, CASE_CLOSE_FORM2, database_name)  # 结案从表插入数据

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, case_form2, database_name)
        sql(config_file_path, MASTER1, database_name)
        sql(config_file_path, CASE_CLOSE_FORM1, database_name)

    def test1(self):
        u'''保险公司交易流水号为空'''
        data = """{
            "reportStateList":[{
                "reportNo":"62222519 ",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号不存在")

    def test2(self):
        u'''保险公司交易流水号错误'''
        data = """{
            "serialNumber":"112123131312",
            "reportStateList":[{
                "reportNo":"62222519 ",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号不存在")


    def test3(self):
        u'''案件列表为空'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"案件列表为空;")

    def test5(self):
        u'''保险公司报案号为空'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未查询到对应的案件;")


    def test6(self):
        u'''保险公司报案号错误'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"56646546",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未查询到56646546对应的案件;")


    def test7(self):
        u'''保单号为空'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件的保单号不一致;")

    def test8(self):
        u'''保单号错误'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227sdfsdfsdf189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件的保单号不一致;")

    def test9(self):
        u'''支付状态编码为空'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件支付状态有误;")

    def test_10(self):
        u'''支付状态编码非（10,20,30,90）'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"100",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件支付状态有误;")

    def test_11(self):
        u'''支付状态为10，支付时间为空'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件日期格式有误;")

    def test_12(self):
        u'''支付状态为10，支付时间格式错误'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017/03/19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件日期格式有误;")


    def test_13(self):
        u'''支付状态为10，支付时间晚于当前时间'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2200-02-27 14:12:47",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件日期格式有误;")

    def test_14(self):
        u'''支付状态为10，支付方式为空'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件支付方式有误;")


    def test_15(self):#bug返回成功
        u'''支付状态为10，支付方式非（1,2,3,4,5）'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"9",
                "description":"支付说明"}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519案件支付方式有误;")

    def test_16(self):
        u'''支付状态为90，支付说明为空'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"90",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":1,}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519未说明支付失败的原因;")

    def test_17(self):
        u'''来源标识为空'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")


    def test_18(self):
        u'''来源标识错误'''
        data = """{
            "serialNumber":"AM2018228123456789",
            "reportStateList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "state":"10",
                "payTime":"2017-03-19 13:40:29",
                "payMethod":"1",
                "description":"支付说明"}],
            "channelSource":"tsrterter"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_19(self):
        u'''参数正确（支付状态同步成功）'''
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
        r = requests.post(self.base_url, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']["resultCode"], u"00000")
        self.assertEqual(result['data']["resultMsg"], u"支付状态同步成功")

    def test_20(self):
        u'''重复支付'''
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']["resultCode"], u"11111")
        self.assertEqual(result['data']["resultMsg"], u"重复支付")

if __name__ == '__main__':
    unittest.main()




