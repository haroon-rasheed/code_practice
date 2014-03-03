#! /usr/bin/python
"""
shows the usage ABC module in python 
ABC = Abstract Base Class 
Advantages of using ABC im python

o	Provides an excellent framework that any developer ( who has not actually designed the framework) can do implementation or add API's when he is extending. 
o	Helps us to grow our framework larger and larger keeping any number of sub classes, we no need to remember all those classes in our mine.
Simply a call to the <base_class>.__subclasses__() will list all sub classes.
o	Both abstract and concrete classes can provide implementations. If you want to access base class method it's pretty simple as below
	super(concrete_class, self).retrieve_values(arguments)
o	We are using sub classing approach which avoids incomplete implementations (implementation errors by mistake ( hence a programmer can't let anything incomplete. In future If this is not helpful in our case, this can easily be altered by avoiding sub classing and by using register() to cope with abstract base class. 

"""

import abc

class one(object):
	__metaclass__ = abc.ABCMeta

	"""
	the below must be overrided in all sub calsses or else will get compile time error
	TypeError: Can't instantiate abstract class two with abstract methods __call__
	"""
	
	@abc.abstractmethod
	def __call__(self):
		print "in __call__ of ONE"

	def __str__(self):
		print "Type = ", type(self.__class__.__name__)
		return repr(self.__class__.__name__)
		#return repr( "In __str__")
	
	def get_it(self):
		print "Base", self.get_it.__name__		# How to print a method name


class two(one):
	def __call__(self):
		print "in __call__ of TWO"
	def run(self):
		print "hey"


class three(one):
	"""
	not necessary to override abstract base method __call__ here, as it's already done in two
	"""
	def run(self):
		print "hey"



t1  = two()
for sc in one.__subclasses__():		# prints all subclasses of "one" i.e., two, three
	print sc
