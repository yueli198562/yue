#coding:utf-8
import requests,unittest
from function.function import *
from function.mysql_db import *
from function.test_data import *

class test_am3(unittest.TestCase):
    u'''报案号同步接口'''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+url+"/caseDeal/vCore1/reportNoSync"
        sql(config_file_path, case_form, database_name) #普通案件信息表里插入数据

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, case_form2, database_name) #删除普通案件信息表数据

    def test1(self):
        u'''保险公司交易流水号为空'''
        data = """{
        'reportNoList': [{
        'reportNo': '3333321',
        'policyNo': '3223H227002017900189',
        'splitTime': '2017-03-20 13:40:29',
        'splitPerson': '小明'},
        {
        'reportNo': '44444',
        'policyNo': 'ss2f227002017900189',
        'splitTime': '2017-03-20 13:40:29',
        'splitPerson': '小白'}],
        'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u'40103')
        self.assertEqual(result['message'], u"流水号不存在")

    def test2(self):
        u'''保险公司交易流水号不存在'''
        data = """{'serialNumber': '11100020asdasdasd',
            'reportNoList': [{
            'reportNo': '3333321212333 ',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '444444412333 ',
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u'40103')
        self.assertEqual(result['message'], u"流水号不存在")

    def test3(self):
        u'''案件列表为空'''
        data = """{'serialNumber': 'AM2018228123456789',
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"案件列表为空;")

    def test4(self):
        u'''拆分为多单保险公司报案号为空'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"案件列表中含有重复的报案号;")

    def test5(self):
        u'''拆分为一单保险公司报案号为空'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号为空;")

    def test6(self):
        u'''拆分为两单以上时保险公司报案号是否唯一'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '321212333',
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"案件列表中含有重复的报案号;")

    def test7(self):
        u'''拆分为多单保单号为空'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '421212333',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"案件列表中含有重复的保单号;")

    def test8(self):
        u'''拆分为一单保单号为空'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"保单号格式有误;")

    def test9(self):
        u'''拆分为两单以上时保单号相同'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '421212333',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"案件列表中含有重复的保单号;")


    def test_10(self):
        u'''案件拆分时间为空'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'policyNo': '3223H227002017900189',
            'splitPerson': '小明'},
            {
            'reportNo': '421212333',
            'policyNo': 'ss2f227002017900189',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号321212333拆分日期格式有误;报案号421212333拆分日期格式有误;")

    def test_11(self):
        u'''案件拆分时间格式错误'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017/03/20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '421212333',
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017/03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号321212333拆分日期格式有误;报案号421212333拆分日期格式有误;")

    def test_12(self):
        u'''案件拆分时间晚于当前时间'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'policyNo': '3223H227002017900189',
            'splitTime': '3017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '421212333',
            'policyNo': 'ss2f227002017900189',
            'splitTime':'3017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号321212333拆分日期超出系统时间;报案号421212333拆分日期超出系统时间;")

    def test_13(self):
        u'''案件拆分人为空'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '321212333',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
           },
            {
            'reportNo': '421212333',
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            }],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号321212333拆分人不能为空;报案号421212333拆分人不能为空;")

    def test_14(self):
        u'''来源标识为空'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '3333321212333 ',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '444444412333 ',
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            }"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_15(self):
        u'''来源标识错误'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '3333321212333 ',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '444444412333 ',
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'eqetwertwertwert'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_16(self):
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
        r = requests.post(self.base_url, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"报案号同步成功")

    def test_17(self):
        u'''重复提交报案号'''
        data = """{'serialNumber': 'AM2018228123456789',
            'reportNoList': [{
            'reportNo': '3333321212333 ',
            'policyNo': '3223H227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小明'},
            {
            'reportNo': '444444412333 ',
            'policyNo': 'ss2f227002017900189',
            'splitTime': '2017-03-20 13:40:29',
            'splitPerson': '小白'}],
            'channelSource': 'jts0oe7silrxv3upx5'}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u'200')
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']['resultCode'], u"11111")
        self.assertEqual(result['data']['resultMsg'], u"重复提交报案号")

if __name__ == '__main__':
    unittest.main()
