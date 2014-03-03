#!/usr/bin/python

"""
to work with enums, A greate code
"""

lt = ["one", "two", "three"]
print list(enumerate(lt))

#create ENUMS
def enum(*args):
    enums = dict( zip(args, range(len(args))) )
    return type("enum", (), enums)

en =  enum("one", "two")
print en.one
print en.two
