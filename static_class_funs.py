#!/usr/bin/python

class A(object):
    def __init__(self, name):
        self.name = name

    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)
        print self.name

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)
        #print cls.name

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    
        print self.name

a=A("Test_Name")

a.foo(1)
a.class_foo(1)
a.static_foo(1)
'''
print(a.foo)
print(a.class_foo)
print(a.static_foo)
'''
