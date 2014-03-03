
#import sys,os.path
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#from TestLoad.LoadTestBaseFactory import LoadTestBaseFactory

#import sys

"""
class LoadTestBaseFactory:
	pass
"""

#from TestLoad.UnitTest.LoadUnitTestBase import LoadUnitTestBase

import unittest
from test_ns import *
#from TestLoad.UnitTest.VerifyDSFiles import VerifyDSFiles


class ELTTestBaseFactory(object):

	def __init__(self):
		pass
		#self.load = LoadTestBaseFactory()
	
	#@staticmethod	
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
		#print self.test_case
		#test_case = self.get_test_case()
		test_case = VerifyDSFiles()
		print test_case
		test_case.main()
