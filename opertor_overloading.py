#!/usr/bin/env python

class OpOverload(object):
    """
    operator overloading example
    """

    def __init__(self, ele):
        self.ele = ele

    def __add__(self, ele):
        print "I'm overloaded"
        self.ele += ele 
        return self.ele

    def __str__(self):
       return self.ele

if __name__ == '__main__':
    ol = OpOverload("hello")
    ol + "world"
    print ol
