#!/usr/bin/python
# -*- coding:utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
import unittest,time


test_dir="./case" #指定测试用例为当前文件夹下的case目录
dis=unittest.defaultTestLoader.discover(test_dir, pattern="*test.py")

if __name__=="__main__":
    # now_time=time.strftime("%y-%m-%d %H_%M_%S") #获取当前格式化日期
    filename="./test_report/reports.html" #测试报告路径
    f=open(filename,"wb")
    runner=HTMLTestRunner(stream=f,title=u"江泰道路运输保险网",description=u'测试客运保费计算')
    runner.run(dis)
    f.close()
    
    
    









