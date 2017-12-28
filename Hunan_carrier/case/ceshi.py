#coding:utf-8
import os
base_dir=os.path.dirname(os.path.dirname(__file__)) #返回当前文件所在目录的上级目录
excel_file=base_dir+'/photographa/p1.jpg'
excel_file=excel_file.replace("/","\\")
print excel_file
print "E:\\py\\Hunan_carrier\\photographa\\p1.jpg"