#! /usr/bin/python
'''
How to pass argumants to a function through cmd line like call
'''

def spam():
	print "spam and", eggs

exec(spam.__code__, {'eggs':'pasta'})	
