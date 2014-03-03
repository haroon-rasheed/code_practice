#!/usr/bin/env python

"""
class hello:
  
  #@classmethod
  def print_func(self):
      print "welcome"

def list(ar):
  print ar

if __name__ == '__main__':
    #hello:print_func()
    #new hello().print_func()
    #hello.print_func()
    #hello->print_func()
    lt = list("an")
    print lt

class parent(object):
    def __init__(self, param):
      self.v1 = param

class child(parent):
    def __init__(self, param):
        self.v2 = param

obj = child(11)
print '%d %d' % (obj.v1, obj.v2)


x = 10
y = 0
if( y != 0 and x/y < 100 ):
    print "In If"
else:
    print "In Else"

import array
a = array.array('c', 'A and B')
a[0] = 'S'
a[-4:] = array.array('c', 'toast')
print  ' '.join(a)


for letter in 'ABC':
    if letter == 'C':
      pass
    print 'Hi', letter, 

"""

lst = ['spam', 'and', 'eggs']
lst[2] = 'toast'
print ' '.join(lst)

