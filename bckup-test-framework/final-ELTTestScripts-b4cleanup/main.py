#! /usr/bin/python


#from ELTTestBaseFactory import ELTTestBaseFactory
import unittest
#from TestLoad.UnitTest.VerifyDSFiles import VerifyDSFiles
from TestLoad.LoadTestBaseFactory import LoadTestBaseFactory

if __name__ == '__main__':
	test_case_factory = LoadTestBaseFactory()
	test_case_factory.init_test_suite('UNIT-TEST', 1)
	#test_case_factory = LoadTestBaseFactory('UNIT-TEST', 1)
	#test_case_factory.create_test_suite()
	runner = unittest.TextTestRunner()
	runner.run(test_case_factory)
