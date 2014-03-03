#!/usr/bin/env python

def with_hint(in_file):
	"""
	with keyword exmaple
	"""
	
	with open(in_file, 'r') as src:
		for line in src.readlines():
			print line

if __name__ == '__main__':
	with_hint("input.txt")
