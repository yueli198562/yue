#coding:utf-8
import requests,unittest
from function.function import *
from function.mysql_db import *
from function.test_data import *

class test_zr3(unittest.TestCase):
    u'''理赔确认接口 '''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+url+"/jtCase/vCore1/claimConfirmSync"
        sql(config_file_path, case_form, database_name)
        sql(config_file_path, l, database_name)

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, l1, database_name)
        sql(config_file_path, case_form2, database_name)
        sql(config_file_path, ZR_CASE_FLOW, database_name)

    def test1(self):
        u'''流水号为空'''
        data = '''{
            "reportNo": "62222519",
            "confirmFlag": 1,
            "confirmDesc": "房屋的损失也应该加上",
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号不能为空;")

    def test2(self):
        u'''江泰报案流水号为空'''
        data = '''{"serialNumber": "1110112113116",
            "confirmFlag": 0,
            "confirmDesc": "房屋的损失也应该加上",
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"参数无报案号")

    def test3(self):
        u'''江泰报案流水号不存在'''
        data = '''{"serialNumber": "1110112113116",
            "reportNo": "622225df19",
            "confirmFlag": 0,
            "confirmDesc": "房屋的损失也应该加上",
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"案件不存在")

    def test4(self):
        u'''是否同意为空'''
        data = '''{"serialNumber": "1110112113116",
            "reportNo": "62222519",
            "confirmDesc": "房屋的损失也应该加上",
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"是否同意结案不能为空;")

    def test5(self):
        u'''是否同意非0或1'''
        data = '''{"serialNumber": "1110112113116",
            "reportNo": "62222519",
            "confirmFlag": 9,
            "confirmDesc": "房屋的损失也应该加上",
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"同意类型有误;")

    def test6(self):
        u'''是否同意为0时，确认描述为空'''
        data = '''{"serialNumber": "1110112113116",
            "reportNo": "62222519",
            "confirmFlag": 0,
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"不同意时描述不能为空;")

    def test7(self):
        u'''来源标识为空'''
        data = '''{"serialNumber": "1110112113116",
            "reportNo": "62222519",
            "confirmFlag": 0,
            "confirmDesc": "房屋的损失也应该加上",}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test8(self):
        u'''来源标识错误'''
        data = '''{"serialNumber": "1110112113116",
            "reportNo": "62222519",
            "confirmFlag": 0,
            "confirmDesc": "房屋的损失也应该加上",}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test9(self):
        u'''入参正确'''
        data = '''{"serialNumber": "1110112113116",
            "reportNo": "62222519",
            "confirmFlag": 0,
            "confirmDesc": "房屋的损失也应该加上",
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"理赔确认成功")
        self.assertEqual(result['data']['reportNo'], u"62222519")

    def test_10(self):
        u'''重复确认'''
        data = '''{"serialNumber": "1110112113116",
            "reportNo":
            "62222519",
            "confirmFlag": 0,
            "confirmDesc": "房屋的损失也应该加上",
            "channelSource": "jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"成功")
        self.assertEqual(result['data']['resultCode'], u"11111")
        self.assertEqual(result['data']['resultMsg'], u"重复确认")
        self.assertEqual(result['data']['reportNo'], u"62222519")

if __name__ == '__main__':
    unittest.main()
