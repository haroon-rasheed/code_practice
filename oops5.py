#!/usr/bin/python

"""
Shows how to cCheck whether method of an object is callable or not

"""

class Example(object):
    
    def __init__(self):
        pass

    def dp(self, Name):
        print "Inside DP"
        print "N =>", Name

print "Is callable way 1=>", callable(Example().dp)
print "Is callable way 2=>", callable( getattr(Example,"dp") )
print "Is callable way 3=>", callable( getattr(Example,"__call__") )
print "Dir =>", dir(Example)
Example.dp(Example(), "Yesy")   #Another way to call a instance method with class
