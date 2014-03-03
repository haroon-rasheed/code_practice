#! /usr/bin/python

import sys,pickle

"""
class Foo:
    attr = 'a class attr'

picklestring = pickle.dumps(Foo)
try:
    import cPickle as pickle
except:
	import pickle

import pprint

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'DATA:',
pprint.pprint(data)

data_string = pickle.dumps(data)
print 'PICKLE:', data_string
"""

import cPickle as pickle

"""
class test:
	def __init__(self):
		pass
	
	def print1(self):
		print "hello"

t1 = test()
#t1.print1()
f = open("temp", "w")
pickle.dump(t1,f)
f.close()
f = open("temp", "r")
obj1 = pickle.load(f)
print obj1
"""


data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
		          'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
