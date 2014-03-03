#!/usr/bin/python

"""
Shows how to get code of a fun or class
also how to run code of a function without directly calling or invoking it

"""

class Example(object):
    
    def __init__(self):
        pass

    def dp(self, Name):
        print "Inside DP"
        print "N =>", Name

def fun1():
    print "inside fun1"


print fun1.__code__
exec(fun1.__code__, {})
