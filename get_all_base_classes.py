#!/usr/bin/python

"""
shows how to get list of all base classes that a class is derived from
"""
import unittest

class One(unittest.TestCase, object):
    pass

class A(One):
    pass

class B(A):
    pass

import inspect
print "1 =>", inspect.getmro(B)     # will print all base class hierarchy
print "2 =>", B.__bases__           # will print very immediate base class only
#print inspect.getclasstree(inspect.getmro(B))  #Confusing O/P but works