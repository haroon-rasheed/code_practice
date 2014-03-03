"""
Base Factory and other interface factories
"""


import unittest
from test_ns import *


class ELTTestBaseFactory(object):

	def __init__(self):
		pass
		#self.load = LoadTestBaseFactory()
	
	def get_test_factory(self, factory_type ):
		if factory_type == 'EXTRACT':
			return ExtractTestBaseFactory()

		elif factory_type == 'LOAD':
			#fact_inst = LoadTestBaseFactory()	
			return LoadTestBaseFactory()
			#return fact_inst

		elif factory_type == 'TRANSFORM':	
			return TransformTestBaseFactory()

class LoadTestBaseFactory(ELTTestBaseFactory):

	#def get_unittest(self, test_case):
	#def get_unittest(self):
	def get_test_case(self):
		#return LoadUnitTestBase(test_case)
		return LoadUnitTestBase()

	def get_regntest(self, test_case):
		return LoadRegnTestBase(test_case)


class LoadUnitTestBase(unittest.TestCase, LoadTestBaseFactory):

	def get_test_case(self):
		#if( self.test_case_choice == 1 ):
		#	print "inside get tc"
		return VerifyDSFiles()
	
	def _setup_testcase(self):
		pass
	
	def _execute_tc(self):
		pass
	
	def _verify_teardown(self):
		pass
	
	def runTest(self):
		test_case = VerifyDSFiles()
		test_case.main()
