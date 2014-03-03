#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
FINALLY =>
A finally clause is always executed before leaving the try statement, whether an
exception has occurred or not. When an exception has occurred in the try clause
and has not been handled by an except clause (or it has occurred in a except or
else clause), it is re-raised after the finally clause has been executed. The
finally clause is also executed “on the way out” when any other clause of the
try statement is left via a break, continue or return statement. 
"""

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"

divide(2, 1)
divide(2, 0)
divide("2", "1")
