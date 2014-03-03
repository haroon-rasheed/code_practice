#! /usr/bin/python

# Class Decorator
class entryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__

@entryExit
def func1():
    print "inside func1()"

@entryExit
def func2():
    print "inside func2()"

#func1()
#func2()

#Function Decorator
def entryExit(f):
    def new_f():
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    return new_f
     

@entryExit
def func1():
    print "inside func1()"

@entryExit
def func2():
    print "inside func2()"
    
#func1()
#func2()
print func1.__name__
print func2.__name__

#CLEAR EXAMPLE
# The decorator to make it bold
def makebold(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return "<b>" + fn() + "</b>"
    return wrapper

# The decorator to make it italic
def makeitalic(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return "<i>" + fn() + "</i>"
    return wrapper

@makebold
@makeitalic
def say():
    return "hello"

print say() 
#outputs: <b><i>hello</i></b>

# This is the exact equivalent to 
def say():
    return "hello"
say = makebold(makeitalic(say))

print say() 
#outputs: <b><i>hello</i></b>