#-*- coding:utf-8 -*-
formatter = "%r %r %r %s"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True);
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ("I had this thing.",
                    "That you could type up right",
                    "But id didn't sing.",
                    "So I said goodnight  测试中文")