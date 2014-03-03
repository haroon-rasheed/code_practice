#!/usr/bin/python

"""
Shows how to create class and instance variable on the fly

"""

class Example(object):
    
    var_123 = "vada_pochey"

    @classmethod
    def c_display(cls):
        print "CLass Var =>", cls.cls_var
        print "CLS Points to =>", cls

    def o_display(self):
        print "Inst Var =>", self.inst_var
        print "CLs Var Inside Inst Method =>", self.var_123
        print "Sef Points to =>", self
        print "Type of global cls var", type(self.var_123.__class__.__name__)
        print "Type of global cls var", type(Example.var_123.__class__.__name__)


Example.cls_var = "problem"
Example.c_display()

e = Example()
e.inst_var = "2ndproblem"
e.o_display()
print e.__doc__
