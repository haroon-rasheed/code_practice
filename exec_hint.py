#!/usr/bin/python

"""
shows how to call a python fun code without invoking it directly like fun()
"""

def fun1():
    print "welcome"

exec(fun1.__code__, {})
#simple call and run a python file
fptr = open("zip_hint.py", "r")
exec(fptr, {})

exec('print \"str parameter now\" ', {})

tp = (1,2,3,)
exec('help', globals())
