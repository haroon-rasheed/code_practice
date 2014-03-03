#!/usr/bin/env python

def problem1():
		"""
    Explain the difference between the following quoting in Python:
		"""
		my_string = 'the cat sat on the mat'
		print "1", my_string
		my_string = "the cat sat on the mat"
		print "2", my_string
		my_string = """the cat sat on the mat"""
		print "3", my_string
		my_string = '''the cat sat on the mat'''
		print "4", my_string

print problem1.__doc__
