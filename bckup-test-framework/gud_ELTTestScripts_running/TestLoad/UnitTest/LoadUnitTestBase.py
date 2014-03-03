import unittest

#from ELTTestBaseFactory import ELTTestBaseFactory

class LoadUnitTestBase(LoadTestBaseFactory, unittest.TestCase):
#class LoadUnitTestBase(unittest.TestCase):

	def __init__(self, test_case_choice):
		self.test_case_choice = test_case_choice

	def get_test_case(self):
		if( self.test_case_choice == 1 ):
			return VerifyDSFiles()

	"""
	def __call__(self):
		if (test_case_choice == 1):
			return VerifyDSFiles()
	"""	

	def _setup_testcase(self):
		pass
	
	def _execute_tc(self):
		pass

	def _verify_teardown(self):
		pass

	def runTest(self):
		test_case = self.get_test_case()
		test_case.main()
