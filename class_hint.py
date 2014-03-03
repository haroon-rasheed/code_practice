#!/usr/bin/python


dic = { 'int_var': 786, 'dict_var': {'c': 2}, 'str_var': "hi", 'list_var' : [1,2,3] }

class Test:
    cls_var1 = "cls_var1"
    cls_var2 = "cls_var2"

    def __init__(self):
        self.mem_var1 = "mem_var1"
        self.mem_var2 = "mem_var2"

    def display(self):
        print "Member Vars"
        for k,v in self.__dict__.iteritems():
            print k, "=>", v

        print "\n\n\n"

        print "All Class Atttibutes"
        for k,v in self.__class__.__dict__.iteritems():
            print k, "=>", v

        print "\n\n\n"

    """excellent way to set member vars from a dict """
    def set_mem_vars_from_dict(self):
        for var, value in dic.iteritems():
            if isinstance(value, (int,dict,str,list)):
                setattr(self, var, value)

t = Test()
#t.display()
t.set_mem_vars_from_dict()
t.display()
