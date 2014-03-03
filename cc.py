#!/usr/bin/env python
from copy import deepcopy

class Foo(object):
    def __init__(self, bar):
        self.bar = bar
        #self.spam = expression + that * generates - ham   # calculated

    def __copy__(self):
        # self.spam is to be ignored, it is calculated anew for the copy
        # create a new copy of ourselves *reusing* self.bar
        return type(self)(self.bar)

    def __deepcopy__(self, memo):
        # self.spam is to be ignored, it is calculated anew for the copy
        # create a new copy of ourselves with a deep copy of self.bar
        # pass on the memo mapping to recursive calls to copy.deepcopy
        return type(self)(deepcopy(self.bar, memo))

t1 = Foo("haroon")
t2 = Foo(t1)
