#! /usr/bin/python


from ELTTestBaseFactory import ELTTestBaseFactory
import unittest
from TestLoad.UnitTest.VerifyDSFiles import VerifyDSFiles

if __name__ == '__main__':
	test_case = ELTTestBaseFactory().get_test_factory('LOAD').get_test_case()
	runner = unittest.TextTestRunner()
	runner.run(test_case)
