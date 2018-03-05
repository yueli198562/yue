# coding:utf-8
from mysql_db import *

database_name="zrjt"  #数据库名
url="218.241.156.112:8083"

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) )# 返回当前文件所在目录的上级目录
config_file_path= base_dir + "\\db_config.ini"
nowtime=time.strftime("%y-%m-%d %H:%M:%S")
nowtime="20"+nowtime

#机构项目关系表插入数据和删除数据MECHANISMP_ROJECT
MECHANISMP_ROJECT='INSERT into mechanismp_roject VALUES("1","'+nowtime+'","180btk69juwlxj62mb1030odkj5cf00x","123","1","jts0oe7silrxv3upx5","123","'+nowtime+'",1)'
MECHANISMP_ROJECT1='delete from mechanismp_roject where insurance_classes_id="1"'

#CASE_FORM 案件信息表
case_form='INSERT into case_form VALUES("9","'+nowtime+'","出险事故经过描述",2000.00,"jts0oe7silrxv3upx5",15000,\
"xx@qq.com","小李",13433333333,"2018-02-12 14:14:19",150002,"天府大道199号4号楼","AM2018228123456789",1,1,1,"62222519","'+nowtime+'",\
"'+nowtime+'",62222519,15000,"备注备注备注","'+nowtime+'","报案人姓名小天","1110112113116",1,500.00,"'+nowtime+'")'
        #----测试理赔确认接口 状态改为4
case_form1='INSERT into case_form VALUES("9","'+nowtime+'","出险事故经过描述",2000.00,"jts0oe7silrxv3upx5",15000,\
"xx@qq.com","小李",13433333333,"2018-02-12 14:14:19",150002,"天府大道199号4号楼","AM2018228123456789",1,1,4,"62222519","'+nowtime+'",\
"'+nowtime+'",62222519,15000,"备注备注备注","'+nowtime+'","报案人姓名小天","1110112113116",4,500.00,"'+nowtime+'")'
case_form2='DELETE from case_form where id=9'

#结案主表CASE_CLOSE_MASTER
MASTER='INSERT into case_close_master(close_date,close_mode,close_status,close_type,insurance_serial_no,jt_code_id,pay_amount,pay_status,remarks) \
    VALUES("'+nowtime+'",0,0,0,"AM2018228123456789","9",300.00,0,0)'
MASTER1='DELETE from case_close_master where jt_code_id=9'

#CASE_CLOSE_FORM 结案从表
CASE_CLOSE_FORM ='INSERT into case_close_form VALUES(9,"2017-03-18 13:53:41",120.05,"2017-03-19 13:51:30",\
"菲菲","***<赔付标的：>***","123",1,1,1,112,"'+nowtime+'","泰康在线财产保险股份有限公司","2016-03-16 00:00:00到2017-03-20"\
,"'+nowtime+'","描述描述",120.05,"2017-03-20 13:51:30","支付说明",1,4,10,"RV2H227002017900189",62222519,"'+nowtime+'",\
"小李","'+nowtime+'")'
CASE_CLOSE_FORM2 ='INSERT into case_close_form VALUES(9,"2017-03-18 13:53:41",120.05,"2017-03-19 13:51:30",\
"菲菲","***<赔付标的：>***","123",1,1,1,112,"'+nowtime+'","泰康在线财产保险股份有限公司","2016-03-16 00:00:00到2017-03-20"\
,"'+nowtime+'","描述描述",120.05,"2017-03-20 13:51:30","支付说明",1,4,20,"RV2H227002017900189",62222519,"'+nowtime+'",\
"小李","'+nowtime+'")'
CASE_CLOSE_FORM1='DELETE from case_close_form where id=9'

# COMPENSATE_CONFIRM 确认赔付信息表
CONFIRM='INSERT into compensate_confirm(accident_period_date,actual_amount,audit_date,audit_person,calculation_process,\
claim_state,create_date,ins_company,ins_period,jt_code_id,msg,pay_explain,pay_method,pay_nature,pay_state,pay_time,policy_no,\
report_no,update_date,compensate_id,state) VALUES("2017-03-18 13:53:41",120.05,"2017-03-18 13:53:41","菲菲","***<赔付标的：>***"\
,1,"'+nowtime+'","泰康在线财产保险股份有限公司","2017-03-16 00:00:00到2017-03-20 23:59:59",9,"备注","支付说明",1,4,10,\
"'+nowtime+'","RV2H227002017900189",62222519,"'+nowtime+'",1,0)'
CONFIRM2='INSERT into compensate_confirm(accident_period_date,actual_amount,audit_date,audit_person,calculation_process,\
claim_state,create_date,ins_company,ins_period,jt_code_id,msg,pay_explain,pay_method,pay_nature,pay_state,pay_time,policy_no,\
report_no,update_date,compensate_id,state) VALUES("2017-03-18 13:53:41",120.05,"2017-03-18 13:53:41","菲菲","***<赔付标的：>***"\
,2,"'+nowtime+'","泰康在线财产保险股份有限公司","2017-03-16 00:00:00到2017-03-20 23:59:59",9,"备注","支付说明",1,4,10,\
"'+nowtime+'","RV2H227002017900189",62222519,"'+nowtime+'",1,0)'
CONFIRM1='DELETE from compensate_confirm where jt_code_id=9'

#ZR_CASE_AUXILIARY 自如案件信息辅助表
AUXILIARY='INSERT into zr_case_auxiliary VALUES(9,"'+nowtime+'","天府大道199号4号楼","YZ-102",9,"'+nowtime+'")'
AUXILIARY1='DELETE from zr_case_auxiliary where id=9'

#自如备份表
ZR_CASE_FLOW="DELETE from zr_case_flow where zr_flowing_no=1110112113116"

#INSURED 出险人信息
INSURED="DELETE from insured where report_no=62222519"

#COMPENSATE_MASTER 理赔主表 插入数据
l='INSERT into compensate_master(compensate_explain,confirm_amount,confirm_status,create_date,\
jt_code_id,uid,update_date) VALUES("同意",500,0,"'+nowtime+'",9,1,"'+nowtime+'")'
l1="DELETE from compensate_master where jt_code_id=9"

sql(config_file_path, case_form2, database_name)
sql(config_file_path, CONFIRM1, database_name)
sql(config_file_path, MASTER1, database_name)
sql(config_file_path, CASE_CLOSE_FORM1, database_name)