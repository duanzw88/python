#-*- coding:utf-8 -*-

from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copying from %s to %s" %(from_file,to_file)

#we could do these two on one line ,how?
#从输入的文件中打开文件
in_file = open(from_file);
#读取文件内容
indata = in_file.read();

print "The input file is %d bytes long" % len(indata);

#判断文件是否存在
print "Does the output file exist? %r" % exists(to_file)
print "Ready,hit Return to continue,CTRL-C to abort."
raw_input();

#以写模式，打开输出文件，如果文件不存在，则会创建文件
out_file = open(to_file,"w");
# 写入
out_file.write(indata)

print "Alright,all done."
# 关闭文件
out_file.close();
in_file.close();
