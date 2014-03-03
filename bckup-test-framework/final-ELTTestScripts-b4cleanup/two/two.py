#! /usr/bin/python

import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from one import one

class two(one):
	def __init__(self):
		pass
