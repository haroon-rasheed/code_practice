#!/usr/bin/python

"""
Shows how to create class and instance variable on the fly

"""

class Example(object):
    
    def __init__(self):
        print "Inside init"

e1 = Example
e2 = Example()

