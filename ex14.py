#-*- coding:utf-8 -*-

#加载sys模块
from sys import argv

script = "ss"
user_name,family = argv
prompt = 'input:>'

print "Hi %s,I'm the %s(%s) script." % (user_name,family,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright,so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes,lives,computer)
