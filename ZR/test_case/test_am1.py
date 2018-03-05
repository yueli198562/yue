#coding:utf-8
import requests,unittest
from function.function import *
from function.mysql_db import *
from function.test_data import *

class test_am1(unittest.TestCase):
    u'''结案接口'''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://"+url+"/caseDeal/vCore1/caseClosed"
        sql(config_file_path, case_form, database_name) #案件信息表插入数据
        sql(config_file_path, CONFIRM, database_name)  # 确认信息表插入数据
        sql(config_file_path, MASTER, database_name)  # 结案主表插入数据
        sql(config_file_path, AUXILIARY, database_name)  # 自如案件辅助表插入数据

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, case_form2, database_name)  # 案件信息表插入数据
        sql(config_file_path, CONFIRM1, database_name)  # 确认信息表插入数据
        sql(config_file_path, MASTER1, database_name)  # 结案主表插入数据
        sql(config_file_path, AUXILIARY1, database_name)  # 自如案件辅助表插入数据
        sql(config_file_path, AUXILIARY1, database_name)  # 自如案件辅助表插入数据

    def test1(self):
        u'''保险公司交易流水号为空'''
        data = '''{
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
                "HouseAddress":"天府大道199号8号楼",
                "calculationProcess":"***<赔付标的：>***",
                "auditTime":"2017-02-24 13:51:30",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号不存在")

    def test2(self):
        u'''保险公司交易流水号不存在'''
        data='''{
            "serialNumber":"asdfgadfgsdfgnn1n",
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
                "auditTime":"2017-02-24 13:51:30",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url,data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号不存在")

    def test3(self):
        u'''结案类型为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"结案类型有误;")

    def test4(self):
        u'''结案类型非112、113、114的整数'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":115,
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"结案类型有误;")

    def test5(self):
        u'''结案方式为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"结案方式有误;")

    def test6(self):
        u'''结案方式非1、2、3、4'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"88",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"结案方式有误;")

    def test7(self):
        u'''赔付总金额为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"结算总金额不能为空;")

    def test8(self):
        u'''赔付总金额未精确的两位小数'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.055,
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"结算总金额格式有误;")

    def test9(self):
        u'''赔付总金额非Double类型'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":"贰佰元整",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"结算总金额格式有误;")

    def test_10(self):
        u'''赔付计算书列表为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"理赔计划书列表为空;")

    def test_11(self):
        u'''承保机构为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的承保机构不一致;")

    def test_12(self):
        u'''承保机构不存在'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"werwerwerwerwrwr",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的承保机构不一致;")

    def test_13(self):
        u''' 保险公司报案号为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"泰康在线财产保险股份有限公司",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未查询到对应的理赔计划书;")

    def test_14(self):
        u''' 保险公司报案号错误'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"泰康在线财产保险股份有限公司",
                "reportNo":"4564654",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未查询到4564654对应的理赔计划书;")

    def test_15(self):
        u'''保单号为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"泰康在线财产保险股份有限公司",
                "reportNo":"62222519",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的保单号不一致;")

    def test_16(self):
        u'''保单号错误'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"泰康在线财产保险股份有限公司",
                "reportNo":"62222519",
                "PolicyNo":"5654654654",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的保单号不一致;")

    def test_17(self):
        u'''保险期限为空'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"泰康在线财产保险股份有限公司",
                "reportNo":"62222519",
                "PolicyNo":"RV2H227002017900189",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的保险期限不一致;")

    def test_18(self):
        u'''保险期限不一致'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"泰康在线财产保险股份有限公司",
                "reportNo":"62222519",
                "PolicyNo":"RV2H227002017900189",
                "insPeriod":"2017-03-16 00:00:00到2018-03-20 23:59:59",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的保险期限不一致;")

    def test_19(self):
        u'''保险期限格式错误'''
        data = '''{
            "serialNumber":"AM2018228123456789",
            "caseClosedType":112,
            "caseClosedMode":"4",
            "payAmount":120.05,
            "claimCalculationList":[{
                "insCompany":"泰康在线财产保险股份有限公司",
                "reportNo":"62222519",
                "PolicyNo":"RV2H227002017900189",
                "insPeriod":"2017/03/16 00:00:00到2017/3-20 23:59:59",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的保险期限不一致;")

    def test_20(self):
        u'''实际赔付金额为空'''
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的实际赔付金额不一致;")

    def test_21(self):
        u'''实际赔付金额未精确的两位小数'''
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
                "actualAmount":120.059,
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的实际赔付金额不一致;")

    def test_22(self):
        u'''实际赔付金额非Double类型'''
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
                "actualAmount":"贰佰元整",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的实际赔付金额不一致;")

    def test_23(self):
        u'''出险日期为空'''
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的出险日期不一致;")

    def test_24(self):
        u'''出险日期格式错误'''
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
                "accidentPeriod":"2017/03/18 13:53:41",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的出险日期不一致;")

    def test_25(self):
        u'''赔付性质为空'''
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的赔付性质不一致;")

    def test_26(self):
        u'''赔付性质非(1 2 3 4)(销案 零结案 拒赔 赔付)'''
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
                "payNature":"5",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的赔付性质不一致;")

    def test_27(self):
        u'''出险的房源号为空'''
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的房源号不一致;")

    def test_28(self):
        u'''出险房源号不一致'''
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
                "HouseNo":"Y-101",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的房源号不一致;")

    def test_29(self):
        u'''出险的详细地点为空'''
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
                "calculationProcess":"***<赔付标的：>***",
                "auditTime":"2017-03-18 13:53:41",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的详细地址不一致;")

    def test_30(self):
        u'''出险的详细地点不一致'''
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
                "HouseAddress":"天府大道199号5号楼",
                "calculationProcess":"***<赔付标的：>***",
                "auditTime":"2017-03-18 13:53:41",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的详细地址不一致;")

    def test_31(self):
        u'''理赔计算公式为空'''
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
                "auditTime":"2017-03-18 13:53:41",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的理赔计算公式不一致;")

    def test_32(self):
        u'''理赔计算公式不一致'''
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
                "calculationProcess":"654***<赔付标的：>***",
                "auditTime":"2017-03-18 13:53:41",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的理赔计算公式不一致;")

    def test_33(self):
        u'''核赔时间为空'''
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
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的核赔时间不一致;")

    def test_34(self):
        u'''核赔时间不一致'''
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
                "auditTime":"2017-03-20 13:53:41",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的核赔时间不一致;")

    def test_35(self):
        u'''核赔人为空'''
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
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的核赔人不一致;")

    def test_36(self):
        u'''核赔人不一致'''
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
                "auditPerson":"毛毛"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号62222519理赔计算书的核赔人不一致;")

    def test_37(self):
        u'''来源标识为空'''
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
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_38(self):
        u'''来源标识错误'''
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
            "channelSource":"564654564"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_39(self):
        u'''参数正确'''
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
        r = requests.post(self.base_url, data)
        result = r.json()
        for i in result:
            print i, result[i]
        for i in result["data"]:
            print i, result["data"][i]
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']["resultCode"], u"00000")
        self.assertEqual(result['data']["resultMsg"], u"结案成功")

    def test_40(self):
        u'''重复结案'''
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
                "auditTime":"2017-03-19 13:51:30",
                "auditPerson":"菲菲"
            }],
            "remarks":"备注",
            "channelSource":"jts0oe7silrxv3upx5"
        }'''
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"访问成功")
        self.assertEqual(result['data']["resultCode"], u"11111")
        self.assertEqual(result['data']["resultMsg"], u"重复结案")

if __name__ == '__main__':
    unittest.main()
