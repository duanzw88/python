#-*- coding:utf-8 -*-
#
class Parent(object):

    def override(self):
        print "Parent:override()"

    def implicit(self):
        print "Parent:implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "Child: override()"

    def altered(self):
        print "Child,Befor parent altered()"
        super(Child,self).altered();
        print "Child,After parent altered()"

dad = Parent()
son = Child()

print '-' * 10
dad.implicit()
son.implicit()
print '-' * 10
dad.override()
son.override()
print '-' * 10

dad.altered()
son.altered()
