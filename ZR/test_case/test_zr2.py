#coding:utf-8
import requests,unittest
from function.function import *
from function.mysql_db import *
from function.test_data import *

class test_zr2(unittest.TestCase):
    u'''普通案件人伤接口 '''
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://10.10.62.88:8083/jtCase/vCore1/commonClaims"
        sql(config_file_path, case_form, database_name)

    @classmethod
    def tearDownClass(cls):
        sql(config_file_path, ZR_CASE_FLOW, database_name) #删除自如备份表数据
        sql(config_file_path, INSURED, database_name)  # 删除出险人数据
        sql(config_file_path, case_form2, database_name)


    def test1(self):
        u'''流水号为空'''
        data = """{
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号未查询到对应案件")

    def test2(self):
        u'''流水号不存在'''
        data = """{
            "serialNumber":"1101121131146qwe",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"流水号未查询到对应案件")

    def test3(self):
        u'''江泰报案流水号为空'''
        data = """{
            "serialNumber":"110112113114",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"报案号为空")

    def test4(self):
        u'''总估损金额为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
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
        self.assertEqual(result['message'], u"总估损金额不能为空;估损金额总和与估损总金额不一致;")

    def test5(self):
        u'''总估损金额未保留小数点后两位'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.1465,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"总估损金额格式有误;估损金额总和与估损总金额不一致;")

    def test6(self):
        u'''总估损金额非Double类型'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":"三百元",
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"总估损金额格式有误;估损金额总和与估损总金额不一致;")

    def test7(self):
        u'''出险人列表为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"出险人列表为空;估损金额总和与估损总金额不一致;")

    def test8(self):
        u'''出险人姓名为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"出险人姓名不能为空;")

    def test9(self):
        u'''出险人性别为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"性别不能为空;")

    def test_10(self):
        u'''出险人性别非1或0'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"8",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"性别有误;")

    def test_11(self):
        u'''年龄为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"年龄不能为空;")

    def test_12(self):
        u'''年龄非整数类型'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":"12.5",
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"年龄格式有误;")

    def test_13(self):
        u'''年龄非int类型'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":"二十五",
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"年龄格式有误;")

    def test_14(self):
        u'''证件类型为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"证件类型不能为空;")

    def test_15(self):
        u'''证件类型非01、02、03、04'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"05",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"证件类型有误;")

    def test_16(self):
        u'''证件号为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"证件号不能为空;")

    # def test_17(self):#未校验
    #     u'''证件为身份证时，证件号非数字类型'''
    #     data = """{
    #         "serialNumber":"110112113114",
    #         "reportNo":"62222519",
    #         "totalEstimateLoss":620.14,
    #         "PersonList":[{
    #             "insuredName":"小白",
    #             "sex":"1",
    #             "age":25,
    #             "certificateType":"01",
    #             "certificateNo":"证件号",
    #             "estimateLoss":100.02},
    #             {
    #             "insuredName":"小明",
    #             "sex":"0",
    #             "age":21,
    #             "certificateType":"03",
    #             "certificateNo":"G1002152",
    #             "estimateLoss":520.12}],
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
    #     self.assertEqual(result['message'], u"成功")

    # def test_18(self):
    #     u'''证件为身份证时，证件号小于18位'''
    #     data = """{
    #         "serialNumber":"110112113114",
    #         "reportNo":"62222519",
    #         "totalEstimateLoss":620.14,
    #         "PersonList":[{
    #             "insuredName":"小白",
    #             "sex":"1",
    #             "age":25,
    #             "certificateType":"01",
    #             "certificateNo":"G1000151",
    #             "estimateLoss":100.02},
    #             {
    #             "insuredName":"小明",
    #             "sex":"0",
    #             "age":21,
    #             "certificateType":"03",
    #             "certificateNo":"G1002152",
    #             "estimateLoss":520.12}],
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
    #     self.assertEqual(result['message'], u"成功")

    def test_19(self):
        u'''出险人列表大于等于2人时，出险人姓名和证件号相同'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小白",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"出险人列表中含有重复的证件号持有者;")

    def test_20(self):
        u'''估损金额为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"估损金额不能为空;估损金额总和与估损总金额不一致;")

    def test_21(self):
        u'''估损金额位未保留小数点后两位'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.0662},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"估损金额格式有误;估损金额总和与估损总金额不一致;")

    def test_22(self):
        u'''估损金额非金额类型'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":"贰佰元整"},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"估损金额格式有误;估损金额总和与估损总金额不一致;")

    def test_23(self):#
        u'''估损金额的和不等于总估损金额'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":200.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"估损金额总和与估损总金额不一致;")

    def test_24(self):
        u'''来源标识为空'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_25(self):
        u'''来源标识内容错误'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"54554645"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"40103")
        self.assertEqual(result['message'], u"未知来源")

    def test_26(self):
        u'''入参正确'''
        data = """{
            "serialNumber":"110112113114",
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
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"成功")
        self.assertEqual(result['data']['resultCode'], u"00000")
        self.assertEqual(result['data']['resultMsg'], u"已提交")
        self.assertEqual(result['data']['reportNo'], u"62222519")
        self.assertEqual(result['data']['acceptedHurtNo'], u"110112113114")

    def test_27(self):
        u'''重复提交'''
        data = """{
            "serialNumber":"110112113114",
            "reportNo":"62222519",
            "totalEstimateLoss":620.14,
            "PersonList":[{
                "insuredName":"小白",
                "sex":"1",
                "age":25,
                "certificateType":"03",
                "certificateNo":"G1000151",
                "estimateLoss":100.02},
                {
                "insuredName":"小明",
                "sex":"0",
                "age":21,
                "certificateType":"03",
                "certificateNo":"G1002152",
                "estimateLoss":520.12}],
            "channelSource":"jts0oe7silrxv3upx5"}"""
        t, m = transform_md5(data)
        data = {'data': t, 'sign': m}
        r = requests.post(self.base_url, data)
        result = r.json()
        self.assertEqual(result['code'], u"200")
        self.assertEqual(result['message'], u"成功")
        self.assertEqual(result['data']['resultCode'], u"11111")
        self.assertEqual(result['data']['resultMsg'], u"重复提交人伤信息")
        self.assertEqual(result['data']['reportNo'], u"62222519")
        self.assertEqual(result['data']['acceptedHurtNo'], u"110112113114")

if __name__ == '__main__':
    unittest.main()
