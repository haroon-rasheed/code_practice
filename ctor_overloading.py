#!/usr/bin/env python

class CtorOverload(object):
    """
    INITOR overloading example
    The below code has overloaded INITORs. 
    Until I write the line 29 "o2 = CtorOverload()", I wont get run time error. 
    If I don’t have that line I can run the module without any error even having the two INITORs in my class.
    """

    def __init__(self):
        pass

    def __init__(self, ele):
        print "In INITOR"
        self.ele = ele

    def __add__(self, ele):
        print "I'm overloaded"
        self.ele += ele 
        return self.ele

    def __str__(self):
       return self.ele

if __name__ == '__main__':
    ol = CtorOverload("hello")
    ol + "world"
    o2 = CtorOverload()
    print "O1 ==", ol
    print "O2 ==", o2
