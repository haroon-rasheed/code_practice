#!/usr/bin/python

import sys

class A(object):
    def __init__(self):
        print 'This is A'
    def foo(self):
        print "foo"

    def one(self):
        pass

    def one(self, x):
        pass

    def two(self, x):
        pass

class B(object):
    def __init__(self):
        print 'This is B'
    def foo(self):
        print "bar"

def getObject(cond):
    if cond:
        classname = 'A'
    else:
        classname = 'B'
    object = globals()[classname]
    return object()

myobject = getObject(1)
myobject.foo()
print "DIR =>", dir(myobject)
print "Callable", callable(myobject)
sys.exit(1)

print

a = A()
a.foo()
print dir(a)

print

myobject = getObject(0)
myobject.foo()
print dir(myobject)

print

b = B()
b.foo()
print dir(b)
