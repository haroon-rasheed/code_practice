#!/usr/bin/python

"""
Excellent example to use lambda
"""

mode = "A"
print "Mode =>", (lambda : "Save" if mode=="S" else "Compare")  
# will print the function address as <function <lambda> at 0x1004b56e0>
# So use the below technique to get the function O/P
print "Mode =>", (lambda : "Save" if mode=="S" else "Compare")()
fn = lambda x: (x % 2 == 0 and x % 3 == 0)
print filter(fn, range(1, 20))
