import unittest
#from test_namespaces import *


class LoadUnitTestImpl(object):

	#def __init__(self, test_case_choice):
	def __init__(self):
		#self.test_case_choice = test_case_choice
		#self.get_test_case()
		pass

	"""
	def get_test_case(self, test_case_choice):
			self.test_case = test_case_namespaces[test_case_choice]
			#print test_case
			return self.test_case
		#if( self.test_case_choice == 1 ):
			#return VerifyDSFiles()
		#pass
	"""

	def _setup_testcase(self):
		pass
	
	def _execute_tc(self):
		pass

	def _verify_teardown(self):
		pass

	"""
	def runTest(self):
		self.test_case = self.get_test_case()
		self.test_case.main()
	"""

#t1 = LoadUnitTestImpl(1)
#t1 = LoadUnitTestImpl().get_test_case(1)
