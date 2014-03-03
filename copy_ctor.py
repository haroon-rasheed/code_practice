#!/usr/bin/env python

from copy import deepcopy, copy

class Test(object):
    def __init__(self, name):
        self.name = name

    def __copy__(self):
        print "Normal copy ctor"
        print "Name =>", self.name
        return type(self)(self.name)

    def __deepcopy__(self, memo):
        print "deep copy ctor"
        #return type(self)(deepcopy(self.name)) # This is good for only one instance variable 
        return Test(deepcopy(self.__dict__))   # this is the best way if we have more than one instance variables.

t1 = Test("haroon")
t2 = deepcopy(t1)
t3 = copy(t1)
t4 = t1
