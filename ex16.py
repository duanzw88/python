#-*- coding:utf-8 -*-

from sys import argv

#从参数中读取文件
script,filename = argv

print "We're going erase %r." % filename
print "If you don't want that. hit CTRL-C(^C)."
print "If you want that,hit RETURN."
raw_input("?")

# 打开文件
print "Opening the file..."
target = open(filename,"w")

# 清空文件
print "Truncating the file.Goodbye!"
# target.truncate();

# 输入要写入文件的内容
print "Now I'm goint to ask you for three lines."
line1 = raw_input("line1:");
line2 = raw_input("line2:");
line3 = raw_input("line3:");

# 写入文件
print "I'm going to write these to the file."
target.write(line1+"\n");
# target.write("\n");
target.write(line2);
target.write("\n");
target.write(line3);
target.write("\n");

print "And finally,we colse it"
target.close();
