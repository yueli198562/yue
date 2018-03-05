#coding:utf-8
import requests,unittest
from function.function import *
from function.mysql_db import *
from function.test_data import *

a="SELECT id from case_close_master where insurance_serial_no='AM2018228123456789'"  #查询结案主表id

class test_am4(unittest.TestCase):
    u'''理赔确认接口'''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+url+"/caseDeal/vCore1/claimConfirmSync"
        sql(config_file_path, case_form1, database_name)  # 案件信息表插入数据
        sql(config_file_path, CONFIRM2, database_name)  # 确认信息表插入数据
        sql(config_file_path, MASTER, database_name)  # 结案主表插入数据
        b = select_all(config_file_path, a, database_name)
        MASTERid = str(b[0])
        CASE = 'INSERT into case_close_form VALUES(9,"2017-03-18 13:53:41",120.05,"2017-03-19 13:51:30",\
         "菲菲","***<赔付标的：>***","' + MASTERid + '",1,1,1,112,"' + nowtime + '","泰康在线财产保险股份有限公司","2016-03-16 00:00:00到2017-03-20"\
         ,"' + nowtime + '","描述描述",120.05,"2017-03-20 13:51:30","支付说明",1,4,10,"RV2H227002017900189",62222519,"' + nowtime + '",\
         "小李","' + nowtime + '")'
        sql(config_file_path, CASE, database_name)  # 结案从表

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, case_form2, database_name)
        sql(config_file_path, CONFIRM1, database_name)
        sql(config_file_path, MASTER1, database_name)
        sql(config_file_path, CASE_CLOSE_FORM1, database_name)

    def test1(self):
        u'''保险公司交易流水号为空'''
        data = '''{
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号不存在")

    def test2(self):
        u'''保险公司交易流水号错误'''
        data = '''{
            "serialNumber":"546546",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号不存在")

    def test3(self):#bug 返回成功
        u'''赔付总金额为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"赔付总金额格式有误;")

    def test4(self):
        u'''赔付总金额未精确的两位小数'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15564,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"赔付总金额格式有误;")

    def test5(self):
        u'''赔付总金额非Double类型'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":"贰佰元整",
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"赔付总金额格式有误;")

    def test6(self):
        u'''赔付计算书列表为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"赔付计算书列表为空;")

    def test7(self):
        u'''保险公司报案号为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号和保单号RV2H227002017900189与流水号不一致;")

    def test8(self):
        u'''保险公司报案号不存在'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"654654645",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号654654645和保单号RV2H227002017900189与流水号不一致;")

    def test9(self):
        u'''保单号为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519和保单号与流水号不一致;")

    def test_10(self):
        u'''保单号错误'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"5465445",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519和保单号5465445与流水号不一致;")

    def test_11(self):
        u'''实际赔付金额为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的实际赔付金额格式有误;")

    def test_12(self):
        u'''实际赔付金额未精确的两位小数'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.1545646,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的实际赔付金额格式有误;")

    def test_13(self):
        u'''实际赔付金额非Double类型'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":"贰佰元整",
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的实际赔付金额格式有误;")

    def test_14(self):
        u'''理赔计算公式为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的计算公式不能为空;")

    def test_15(self):
        u'''核赔时间为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的核赔时间格式有误;")

    def test_16(self):
        u'''核赔时间格式错误'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017/03/20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的核赔时间格式有误;")

    def test_17(self):
        u'''核赔时间时间晚于当前时间'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"5000-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的核赔时间超出系统时间;")

    def test_18(self):
        u'''核赔人为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的核赔人不能为空;")

    def test_19(self):
        u'''来源标识为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_20(self):
        u'''来源标识错误'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"5464654"}'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_21(self):
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
        r = requests.post(self.base_url, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"提交确认理赔成功")

    def test_22(self):
        u'''重复提交确认理赔'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "payAmount":200.15,
            "claimCalList":[{
                "reportNo":"62222519",
                "policyNo":"RV2H227002017900189",
                "actualAmount":200.15,
                "calculationProcess":"<赔付标的：>*** ",
                "auditTime":"2017-03-20 13:40:29",
                "auditPerson":"肥肥"}],
            "channelSource":"jts0oe7silrxv3upx5"}'''
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
        self.assertEqual(result['data']['resultCode'], u"11111")
        self.assertEqual(result['data']['resultMsg'], u"重复提交确认理赔")

if __name__ == '__main__':
    unittest.main()
