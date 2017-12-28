#coding:utf-8
import xlrd,os

#==========读取excel文件==========
base_dir=os.path.dirname(os.path.dirname(__file__)) #返回当前文件所在目录的上级目录
excel_file=base_dir+'\\case_data.xlsx'

f=xlrd.open_workbook(excel_file) #打开一个xlsx文件

#读取测试数据
sheet1=f.sheets()[0]  #读取第一个sheet1页面
sheet1_B1=sheet1.row(0)[1].value #读取url
sheet1_B2=str(int(sheet1.row(1)[1].value)) #读取用户名
sheet1_B3=int(sheet1.row(2)[1].value) #读取密码
sheet1_B4=str(int(sheet1.row(3)[1].value)) #运输地域下拉框内容选择
sheet1_B5=int(sheet1.row(4)[1].value) #客运经营类型选择


#读取元素
sheet2=f.sheets()[1] #读取sheet2页面
B1=sheet2.row(0)[1].value #读取用户名输入框元素
B2=sheet2.row(1)[1].value #读取密码输入框元素
B3=sheet2.row(2)[1].value #读取密码输入框元素
B4=sheet2.row(3)[1].value #左侧菜单在线投保
B5=sheet2.row(4)[1].value #左侧菜单在线投保下的子菜单-在线投保
B6=sheet2.row(5)[1].value #客运立即投保按钮
B7=sheet2.row(6)[1].value #已阅读复选框
B8=sheet2.row(7)[1].value #同意并下一步按钮
B9=sheet2.row(8)[1].value #被保险人是否与投保人一致，是
B10=sheet2.row(9)[1].value #统一社会信用代码填写
B11=sheet2.row(10)[1].value #点击上传营业执照-上传图片按钮
B12=sheet2.row(11)[1].value #上传图片exe文件地址
B13=sheet2.row(12)[1].value #道路运输经营许可证输入框
B14=sheet2.row(13)[1].value #许可证图片上传按钮
B15=sheet2.row(14)[1].value #运输地域下拉框
B16=sheet2.row(15)[1].value #客运经营范围选择所有所有复选框
B17=sheet2.row(16)[1].value #客运经营范围选择-其他客运输入框
B18=sheet2.row(17)[1].value #点击【保存并添加车辆】按钮
