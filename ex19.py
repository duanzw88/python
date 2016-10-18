#-*- coding:utf-8 -*-
#

# 定义函数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    cheese_count += 1;
    boxes_of_crackers += 1;
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

cheese = 20;
cracker = 30;
print "We can just give the function numbers directly"
cheese_and_crackers(cheese,cracker);
print "cheese = %d, cracker = %d" %(cheese,cracker)

# print "Or,we can use variables from our script:"
# amount_of_cheese = 10;
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#
# print "We can even do math inside too:"
# cheese_and_crackers(10+20,5+6);
# print "And we can combine the two,variables and math:"
# cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000);
