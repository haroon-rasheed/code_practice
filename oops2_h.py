#! /usr/bin/python
"""
shows how to print a method name
also shows how to access base method from derived obj
"""

class one(object):
	"""
	def __init__(self, name, choice):
		self.name = name
		self.choice =  choice
		self.get_inst()

	def get_inst(self):
		if ( self.choice == 1 ):
			return two( self, self.choice )

	"""	
	def __call__(self):
		print "in _-call__"

	def __str__(self):
		return repr( "In __str__")
	
	def get_it(self):
		print "Base", self.get_it.__name__		# How to print a method name


class two(one):
	def run(self):
		print "hey"

t1  = two()
t1.get_it()
#t1 = one("one", 1)
t1()		# CALLS __call__
print t1	# CALLS __str__
#t1().run()
