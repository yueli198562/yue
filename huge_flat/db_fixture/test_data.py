# coding:utf-8
from db_fixture.mysql_db import *

database_name="jtproducts"  #数据库名

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) )# 返回当前文件所在目录的上级目录
config_file_path= base_dir + "\\db_config.ini"
updateFiles=base_dir + "\\updateFiles\\c.txt"
updateFilesb=base_dir + "\\updateFiles\\b.txt"
nowtime=time.strftime("%y-%m-%d %H:%M:%S")
nowtime="20"+nowtime

#险类插入和删除数据
classes1='INSERT into t_insurance_classes VALUES("XL12345","XL险类名称","XL描述","Y",1,'+ '"'+nowtime+'"'+','+ '"'+nowtime+'"'+','+'"XL创建人",0)'
classes2='delete from t_insurance_classes where insurance_classes_id="XL12345"'
#险种插入和删除数据
risk1='INSERT into t_risk_info VALUES("XZ12345","XZ险种名称","XZ描述","XL12345","M","G","L",'+ '"' + nowtime + '",'+'"XZ险种创建人",'+'"' + nowtime + '")'
risk2='delete from t_risk_info where risk_id="XZ12345";'
#责任插入和删除数据
liability1='INSERT into t_insurance_liability VALUES("ZR12345","ZR责任名称",1,"ZR责任描述","XZ12345","XZ险种名称",'+ '"' + nowtime + '",'+'"ZR创建人",'+'"' + nowtime + '")'
liability2='delete from t_insurance_liability where insurance_liability_id="ZR12345"'
#责任限额名称插入和删除数据
liability_limit1='INSERT into t_liability_limit\
 VALUES("XE责任限额id","XE责任限额名称1","XE责任限额描述","ZR12345","ZR责任名称",'+ '"' + nowtime + '","' + nowtime + '","' + nowtime + '","' + nowtime + '")'
liability_limit2='delete from t_liability_limit where insurance_liability_id="ZR12345"'
#责任限额值插入和删除数据
limit_values1='INSERT into t_liability_limit_values(liability_limit_values_type,liability_limit_values,liability_limit_id,liability_limit_name,status,create_time)\
 VALUES(1,"3万元","XE责任限额id","XE责任限额名称1","1",'+ '"' + nowtime + '")'
limit_values2='delete from t_liability_limit_values where liability_limit_id="XE责任限额id"'
#责任条款插入和删除数据
insurance_clause1='INSERT into t_insurance_clause(insurance_clause_name,insurance_clause_url,their_type,their_id,status,create_time)\
VALUES("c.txt","clause_url",2,"ZR12345",1,'+'"' + nowtime + '")'
insurance_clause2='delete from t_insurance_clause where their_id="ZR12345"'

for i in [liability2, liability_limit2, limit_values2, insurance_clause2]:
    sql(config_file_path, i, database_name)
sql(config_file_path, risk2, database_name)