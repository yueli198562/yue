#coding:utf-8
import os
base_dir=os.path.dirname(os.path.dirname(__file__)) #返回当前文件所在目录的上级目录
base_dir=base_dir.replace("/","\\") #将路径"/"替换为"\"

exe_file=base_dir+'\\photographa\\a.exe' #找到exe文件路径
photo_file=base_dir+'\\photographa\\p1.jpg'  #找到图片路径

