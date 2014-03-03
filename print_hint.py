#!/usr/bin/python

from __future__ import print_function
'''
def normal_print():
    st = "Test String \n"
    print str(st)
    print repr(st)
    Name = "yesy \t \n"
    print "%r" %(Name)
    print "%s" %(Name)
'''

def good_print():
    Name = "yesy \t \n"
    # To print without new line use new style print function above import stmt
    print(Name, end='')

#normal_print()
good_print()
