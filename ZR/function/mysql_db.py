# coding=utf8
import sys, os
import ConfigParser
import MySQLdb,time

def read_db_conf(config_file_path):  #定义一个函数，传入配置文件地址
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)
    db_conf = {}  #创建空的字典，用于存放配置文件内容
    #db_conf['host'] host作为字典的key，cf.get("db_conf", "host")作为字典的value
    db_conf['host'] = cf.get("db_conf", "host")
    db_conf['user'] = cf.get("db_conf", "user")
    db_conf['password'] = cf.get("db_conf", "password")
    db_conf['port'] = cf.get("db_conf", "port")
    return db_conf

def get_db_conn(config_file_path): #定义一个函数，传入配置文件地址
    db_conf = read_db_conf(config_file_path) #调用read_db_conf函数，返回字典
    #创建数据库连接
    conn = MySQLdb.connect(
        host=db_conf['host'],
        port=int(db_conf['port']),
        user=db_conf['user'],
        passwd=db_conf['password'],
        charset="utf8")
    cur = conn.cursor() #创建游标
    return conn,cur

def close_db(conn,cur): #定义函数，传入两个参数，数据库连接和游标
    conn.commit() #提交数据库
    cur.close()  # 关闭游标
    conn.close() #关闭数据库连接

#插入数据，删除数据
def insert_one(cur,conn,database_name, sql):
    conn.select_db(database_name) #选择数据库
    cur.execute(sql) #执行sql语句

#插入删除数据封装
def sql(config_file_path,sql,database_name):
    conn, cur = get_db_conn(config_file_path)
    insert_one(cur, conn,database_name,sql)
    close_db(conn, cur)

#获取一样数据
def select_all(config_file_path, sql, sql_name):
    conn, cur = get_db_conn(config_file_path)
    conn.select_db(sql_name)
    cur.execute(sql)  # 执行sql语句
    qeury_result = cur.fetchone()  # 读取全部数据
    return qeury_result
