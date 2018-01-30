#coding:utf-8

import unittest,os
import HTMLTestRunner

base_dir = os.path.dirname(os.path.abspath(__file__)) # 返回当前文件所在目录的上级目录

html=base_dir + "\\report\\report.html"
discover=unittest.defaultTestLoader.discover("./interface",pattern="interface_test*.py")
if __name__=="__main__":
    f = open(html, 'wb')
    # 定义测试报告，stream：报告存放路径，title：报告标题，description：描述
    runner = HTMLTestRunner.HTMLTestRunner(stream= f, title=u'大平台接口测试报告', description=u'大平台接口测试报告')
    runner.run(discover)  # 运行测试用例
    f.close()


