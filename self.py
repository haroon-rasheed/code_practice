#!/usr/bin/python

"""
self is not a reserved keyword, you can use anything
"""

class Test(object):
    def __init__(abcd):
        abcd.name = "TestName"

    def disp(xyz):
        print "Kill Self =>", xyz.name


t1 = Test()
t1.disp()
