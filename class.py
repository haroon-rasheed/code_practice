import sys

class Base(object):

	def name_n(self):	
		print "Base"

	def display(self):
		print "Base"

	def nen(self):
		print "Base nen"
		str = "printing class name  "+ self.__class__.__name__ +" : done"
		print str
		print self.__class__.__name__
	
class Derived(Base):
	
	def name_n(self):	
		print "Child"
	
	def display(self):
		print "child"

t = Base()
t = Derived()
t.display()
t.name_n()
t.nen()
