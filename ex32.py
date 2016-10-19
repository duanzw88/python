#-*- coding:utf-8 -*-
#
#列表list
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d " % number
for fruit in fruits:
    print "A fruit of type:%s" % fruit

for i in change:
    print "I got %r" % i

elements = [0,2,4,6,8,10]
# for i in range(0,10,2):
#     print "Adding %d to the list." % i
#     elements.append(i)

for element in elements:
    print "---------------"
    print "Element was:%d" % element

    print "--------------\n\n"

# datas = range(0,10)
# for data in datas:
#     print "data = %d" % data
#     data = data + 2;
