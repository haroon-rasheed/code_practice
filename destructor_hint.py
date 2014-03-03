#!/usr/bin/env python
__author__ = 'haroon_rashedu'


class Base():
    def __new__(cls, *args, **kwargs):
        print "base initializer"
        pass
        obj = Super(Base, self).__new__(cls, *args, **kwargs)
        #obj = object.__new__(cls, *args, **kwargs)
        return obj

    def __init__(self):
        print "in Base CTOR"

    def __del__(self):
        print "In Base DTOR"

    def display(self):
        print "Base class method"

class Derived(Base):
    def __new__(cls, *args, **kwargs):
        print "derived initializer"
        #super(Derived, self).__init(self, *args, **kwargs)
        obj = Super(Derived, self).__new__(cls, *args, **kwargs)
        #obj = object.__new__(cls, *args, **kwargs)
        return obj


    def __init__(self):
        print "in Derived CTOR"


    def __del__(self):
        print "In Derived DTOR"


if __name__ == '__main__':
    d1 = Derived()
    d1.display()
    print "One =>", d1.display

    print Base().display

    #b1 = Base()
