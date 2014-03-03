#!/usr/bin/python

"""
Shows how to cCheck whether method of an object is callable or not

"""

class Example(object):
    
    def __init__(self):
        pass

    def dp(self):
        print "Inside DP"


def fun1(self):
    print "Inside Member fun 1"

def fun2(obj):
    print "Inside Member fun 2222"

print "CLass =>", Example
print "Obj =>", Example()
print "Module =>", Example.__module__
print "-"*140
#create a class on the fly
Test = type("Test", (), {})   # created a class
print Test
print Test()
Test.fun1 = fun1
Test().fun1()         # CREATED A MEMBER FUNTION IN THE CLASS
#print dir("Test")

#creating a derived class of Test on the fly
Test1 = type("Test1", (Test,), {})
print Test1
print Test1()

# check the MRO to get base class of Test1 to verify
import inspect
print "MRO =>", inspect.getmro(Test1)
print hasattr(Test1, "fun1")    # Yes it got the member fun fun1() also

#create another class with an method and derive it from Test1
Sample = type("Sample", (Test1,), {"fun2" : fun2} )
print Sample
print Sample()
#print dir("Sample")
print "MRO =>", inspect.getmro(Sample)
print hasattr(Sample, "fun2")    # Yes it got the member fun fun1() also
Sample().fun2()
