# coding=utf8
#coding:utf-8
from setting import *
import MySQLdb

def get_mysql_data(sql,data=None):
    '''
    这个函数用来执行sql，返回数据
    :param sql: sql语句
    :return:
    '''
    try:
        #捕捉mysql连接异常
        conn = MySQLdb.connect(host=MySQL_CONFIG['HOST'], port=MySQL_CONFIG['PORT'],
                               user=MySQL_CONFIG['USER'], passwd=MySQL_CONFIG['PASSWORD'],
                               db=MySQL_CONFIG['DB'], charset='utf8'
                               )
    except Exception as e:
        print('mysql连接失败')
        return 'mysql_error'
    else:
        cursor = conn.cursor() #创建游标,需要指定游标的类型，字典类型
        try:
            #捕捉sql错误异常
            cursor.execute(sql,data)#这样执行sql是为了防止sql注入
        except Exception as e:
            print('sql执行失败，请检查sql！')
            return 'sql_error'
        else:
            #如果sql执行成功的话，提交一下，返回数据
            conn.commit()
            if sql[:6]=='select':#如果是select语句的话，返回查询结果
                return cursor.fetchone()
            else:
                return cursor.lastrowid#如果不是select语句的话，返回自增长id
        finally:#不管sql执行成功没执行成功，都关闭连接
            cursor.close()
            conn.close()
