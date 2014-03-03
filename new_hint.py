#!/usr/bin/python

"""
Explains new()

1. Method __new__() creates the object.

2. __new__ gets called when you call the class. Call the class means issuing the
statement "a=A(1,2)". Here A(1,2) is like calling the class. A is a class and we
put two parenthesis in front of it and put some arguments between the
parenthesis. So, its like "calling the class" similar to calling a method.

3. __new__ must return the created object.

4. Only when __new__ returns the created instance then __init__ gets called. If
__new__ does not return an instance then __init__ would not be called. Remember
__new__ is always called before __init__.

5. __new__ gets passed all the arguments that we pass while calling the class.
Also, it gets passed one extra argument that we will see soon.

"""


class Example(object):

    def __new__(cls, name, no):
        print "Inside New"
        example_obj = object.__new__(cls, name, no)
        setattr(example_obj, "name", name)
        setattr(example_obj, "no", no)
        return example_obj

    
    def __init__(self, name, no):
        object.__init__(self, name, no)
        print "Inside init"
        print "Name =", self.name
        print "No =", self.no

    def dp(self):
        print "welcome"

#e1 = Example
#e2 = Example()
e3 = Example.__new__(Example, "ASM", 99)
print "E33333", e3

e4 = Example("HA", 88)
print "Type E4 =>", e4.__class__
print e4
e4.dp()

class One(object):
    pass

t1 = One()
print "t1 =>", t1
