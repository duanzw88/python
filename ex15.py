#-*- coding:utf-8 -*-

from sys import argv

# 从参数中接收脚本名和文件名
script,filename = argv

# 打开文件
txt = open(filename);

print "Here's you file %r:" % filename
# 读取文件的内容 并打印
print txt.read()
txt.close();

print "Type the filename again:"
# 重新输入文件内容
file_again = raw_input(">");
# 打开文件
txt_again = open(file_again);
print txt_again.read();
txt_again.close();
