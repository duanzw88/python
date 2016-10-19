#-*- coding:utf-8 -*-
#
i = 0;
numbers = []

def check_while(size):
    i = 0;
    while(i < size):
        print "At the top i is %d" % i
        numbers.append(i);

        i = i + 1;
        print "Numbers now:",numbers
        print "At the bottom i is %d" % i

check_while(10);
print "The numbers:"
for num in numbers:
    print num
