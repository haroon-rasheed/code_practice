#! /usr/bin/python

import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
#from ELTTestBaseFactory import ELTTestBaseFactory
from ELTTestScripts.ELTTestBaseFactory import ELTTestBaseFactory

if __name__ == '__main__':
	test_case = ELTTestBaseFactory.get_test_factory('LOAD').get_unittest(1)
	runner = unittest.TextTestRunner()
	runner.run(test_case)
