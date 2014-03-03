#! /usr/bin/python

import sys


class Test(object):
	def __init__(self):
		pass

	def display(self):
		print "Yesy"

	"""
	def __getattr__(self, attr):
		print "insde __getattr__" 

		#WRONG, BELOW CODE ENDS UP IN INFINITE LOOP

		try:
			return self.__getitem__(attr)
		except KeyError:	
			raise AttributeError(attr)

		if hasattr(self, attr):
			return getattr(self, attr)
		else:
			raise AttributeError(attr)

	"""

	def __getattribute__(self, attr):
		print "insde __getattribute__" 

		"""
		#WRONG, BELOW CODE ENDS UP IN INFINITE LOOP

		try:
			return self.__getitem__(attr)
		except KeyError:	
			raise AttributeError(attr)
		"""	

		if hasattr(self, attr):
			return getattr(self, attr)
		else:
			raise AttributeError(attr)
			

if __name__ == '__main__':
	t = Test()
	t.display()
	print getattr(t, "display")
	print getattr(t, "dsplay")
