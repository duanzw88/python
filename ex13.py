#-*- coding:utf-8 -*-

#将python模块加入到自己脚本中
from sys import argv

script,first,second,third = argv;

arg = int(raw_input("Input a num:"));

print "The script is Called:",script
print "Your first available is:",first
print "Your second available is:",second
print "Your third available is:",third
print "input num = %d" % arg
