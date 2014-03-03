#! /usr/bin/python
"""
shows how to print a method name
also shows how to access base method from derived obj
"""
class two(one):
	def run(self):
		print "hey"

t1  = two()
t1.get_it()
#t1 = one("one", 1)
#t1()		# CALLS __call__
print t1	# CALLS __str__
#t1().run()
