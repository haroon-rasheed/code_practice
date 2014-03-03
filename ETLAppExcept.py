#!/usr/bin/python
"""
shows how to call a base method inside base class, two ways
also how to  print current class name
"""

from inherit import BaseException

class ETLError(BaseException):

	def __init__(self):
		pass
	
	def print_info(self):
		BaseException.get_error_info(self.__class__.__name__)				# way 1
		super(ETLError, self).get_error_info(self.__class__.__name__)		# way 2
		#super(BaseException, self).get_error_info(self.__class__.__name__)		# way 2
		pass	


if __name__ == '__main__':
	error = ETLError()
	error.print_info()
