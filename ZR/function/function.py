#coding:utf-8
import time
import binascii
import json,hashlib
import sys
reload(sys)
sys.setdefaultencoding("utf8")

#当前时间
nowtime=time.strftime("%y-%m-%d %H:%M:%S")
nowtime = "20" + nowtime
#保险期间
insPeriod="2018-01-01 00:00:00到2018-12-31 23:59:59"

#根据当前日期，找到T+1日
def t_1(nowtime):
    m = ['01-31', '02-28', '03-31', '04-30', '05-31', '06-30', '07-31', '08-31', '09-30', '11-30', '10-31', "12-31"]
    nowdate = nowtime[:10]
    if nowdate[5:]==m[-1]:#如果月日为12月31日,年份直接加上1年,月日为01月01日
        nowdate=nowdate.replace(nowdate[0:4],str(int(nowdate[0:4])+1))
        nowdate =nowdate.replace("12-31","01-01")+nowtime[10:]
    elif nowdate[5:] in m: #如果月日在列表中,月分加上1,日期替换为01日
        nowdate = nowdate.replace(nowdate[6:8], str(int(nowdate[6:7])+1)+"-")
        nowdate = nowdate.replace(nowdate[-3:], "-01")+nowtime[10:]
    elif nowdate[8:9]=="0":
        nowdate = nowdate.replace(nowdate[-3:], "-0"+str(int(nowdate[-2:]) + 1))+nowtime[10:]
    else:
        nowdate = nowdate.replace(nowdate[-3:], "-"+str(int(nowdate[-2:]) + 1))+nowtime[10:]
    startDate=nowdate
    return startDate
startDate=t_1(nowtime)

#判断字符串中是否包含中文
def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        return False

#定义函数将数字和字母转为Unicode
def charToUnic(ch):
    tmp_ch = hex(ord(ch))[2:]
    return "u"+tmp_ch
#定义函数将中文转为Unicode
def chineseToUnic(ch):
    cch=ch.decode('utf-8').encode('unicode_escape')[2:]
    return "u"+cch

#接口data值16进制转换，sign两次MD5加密
def transform_md5(data):
    # 字符串转16进制这里
    transform = binascii.b2a_hex(data)
    # 将data转为Unicode
    a=data.decode('utf-8')
    list = []
    for i in a:
        if check_contain_chinese(i):  # 判断字符是否包含中文，
            list.append(chineseToUnic(i))
        else:
            list.append(charToUnic(i))
    a = '\\' + '\\'.join(list)
    #固定的MD5key的值
    MD5key="180btk69juwlxj62mb1030odkj5cf00x"
    # 创建md5对象，第一次加密MD5key+a
    hash = hashlib.md5()
    hash.update(MD5key+a)#要对哪个字符串进行加密，就放这里
    b=hash.hexdigest()#拿到加密字符串
    # 创建md5对象，第二次加密
    hash = hashlib.md5()
    hash.update(b)
    md5=hash.hexdigest()#拿到加密字符串
    return transform,md5 #返回

#