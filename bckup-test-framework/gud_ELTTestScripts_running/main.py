#! /usr/bin/python

import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ELTTestBaseFactory import ELTTestBaseFactory
#from TestLoad.LoadTestBaseFactory import LoadTestBaseFactory
#from TestLoad.UnitTest.LoadUnitTestBase import LoadUnitTestBase
#from ELTTestScripts.ELTTestBaseFactory import ELTTestBaseFactory
import unittest
from TestLoad.UnitTest.VerifyDSFiles import VerifyDSFiles
#from test_ns import *

if __name__ == '__main__':
	#test_case = ELTTestBaseFactory.get_test_factory('LOAD').get_unittest()
	base_factory = ELTTestBaseFactory()
	factory  =  base_factory.get_test_factory('LOAD')
	print factory
	#test_case = factory.get_unittest(1)
	test_case = factory.get_test_case()
	print test_case
	runner = unittest.TextTestRunner()
	runner.run(test_case)
