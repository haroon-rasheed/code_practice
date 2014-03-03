#import unittest
from ELTTestBaseFactory import ELTTestBaseFactory
#from ELTTestScripts.TestLoad.UnitTest import LoadUnitTestImpl
#from TestLoad.UnitTest.LoadUnitTestImpl import LoadUnitTestImpl
from TestLoad.UnitTest.unittest_namespaces import *

#class LoadTestBaseFactory(ELTTestBaseFactory, unittest.TestCase):
class LoadTestBaseFactory(ELTTestBaseFactory):
	
	"""
	def __init__(self, ts_type, test_case_choice ):
	#def __init__(self):
		self.ts_type = ts_type
		self.test_case_choice = test_case_choice
		unittest.TestCase.__init__(self, ts_type, test_case_choice)
		#self.create_test_suite()
		#pass
	"""

	def init_test_suite(self, ts_type, test_case_choice):
		self.ts_type = ts_type
		self.test_case_choice = test_case_choice
		

	def create_test_suite(self):
		#self.ts_type = ts_type
		#self.test_case_choice = test_case_choice
		if (self.ts_type == 'UNIT-TEST'):
			self.test_runner = test_case_namespaces[self.test_case_choice]
			#unit_test_ptr = LoadUnitTestImpl(1)
			#return unit_test_ptr
			#return LoadUnitTestImpl(1)
			#return LoadUnitTestImpl()
			print "TTEECC =>", self.test_runner
			return self.test_runner

		elif (self.ts_type == 'REGN-TEST'):
			return LoadRegnTestImpl()

	def runTest(self):
		exec_test_case = self.create_test_suite()
		print "TC ==> ", exec_test_case
		exec_test_case.main()

#t = LoadTestBaseFactory('UNIT-TEST', 1) 
