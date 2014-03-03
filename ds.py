#! /usr/bin/python

import sys

def list_fun():
	list_1 = [ 'this', 'is' , 'a' , 'list', 1, 'test']
	#list_1 =  'this', 'is' , 'a' , 'list', 1, 'test'		# without '[' this var will be treated as tuple by default
	print list_1
	list_1.insert(3, "first")
	print list_1


def tuple_fun():
	tple_1 =  'this', 'is' , 'a' , 'tuple', 1, 'test'		# without '[' this var will be treated as tuple by default
	print tple_1
	#tple_1.insert(2, "first")

if  __name__ == "__main__" :
	list_fun()
	tuple_fun()
