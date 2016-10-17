#-*- coding:utf-8 -*-
#
#定义x字符串
x = "There are %d types of people" % 10
#定义binary字符串
binary = "binary"
# 定义do_not字符串
do_not = "don't"
# 定义y字符串
y = "Those who known %s and those who %s" %(binary,do_not)

# 打印x变量
print x
#打印y变量
print y

print "I said:%r." % x
print "I alse said:'%s'." % y

#定义hailarious变量
hilarious = False;
# 定义格式化的字符串
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

#字符串叠加
print w + e;
