#-*- coding:utf-8 -*-
#
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input(">")

if door == "1":
    print "This is door 1"
    print "1.Take the cake."
    print "2.Scream at the bear."
    bear = raw_input(">>")
    if bear == "1":
        print "choose 1,The bear eats your face off!."
    elif bear == "2":
        print "choose 2,The bear eats your legs off!."
    else:
        print "better."
elif door == "2":
    print "This is door 2"
    print "1. blue"
    print "2. yellow"
    print "3. understand"
    instanity  = raw_input("choose:>>")
    if instanity == "1" or instanity == "2":
        print "choose right"
    else:
        print "choose error"
else:
    print "input error"
