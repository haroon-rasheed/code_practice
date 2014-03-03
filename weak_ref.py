#!/usr/bin/python

"""
Shows how to get reference count of an object
reference count = The number of references to an object

"""

import sys, gc
import weakref

class Example(object):
    
    obj_count = 0

    def __init__(self):
        #print "Inside INIT"
        pass

    def __new__(cls):
        #print "Inside new"
        cls.obj_count += 1
        return object.__new__(cls)

    def _dp(self, Name):
        print "Inside DP"
        print "N =>", Name

    @staticmethod
    def get_count():
        print "Count =>", Example.obj_count

    def __del__(self):
        print "Died"

    def __weakref__(self):
        print "Inside weakref"

a = Example()
b = weakref.proxy(a)
# b = a
#b = weakref.ref(a)
print a,b

'''
c = Example()
Example.get_count()
'''
#print "EE =>", sys.getrefcount(Example())
#print "EAA=>", sys.getrefcount(Example)
b._dp("LL")
#b._dp("LL")
print a.__hash__
#del a
gc.collect()
print b.__hash__
print weakref.getweakrefcount(a)
print weakref.getweakrefs(a)
print "ID :a() =>", id(a)
print "ID :b() =>", id(b)
print "HASH :a() =>", hash(a)


#Proxy objects are not hashable regardless of the referent; this avoids a number of problems related to their fundamentally mutable nature, and prevent their use as dictionary keys.
print "HASH :b() =>", hash(b)
