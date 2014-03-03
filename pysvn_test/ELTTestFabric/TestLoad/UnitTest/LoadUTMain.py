#! /usr/bin/python

import sys, os
import unittest
from TestLoad.LoadTestBaseFactory import LoadTestBaseFactory
from LoadUTNamespace import test_case_namespace


if __name__ == '__main__':
    print "Below are test cases available: \n"
    
    for k, v in test_case_namespace.iteritems():
        print "Test Case No:", v[1]    
        
    print "-"*150, "\n\n\n"
    user_input = input("Please select the test case no to run: ")
    

    test_case_factory = LoadTestBaseFactory()
    test_case_factory.init_test_suite('UNIT-TEST', user_input)
    test_case = test_case_factory.get_test_case()
    
    test_case.run_test()

    """
    test_case_factory = LoadTestBaseFactory()
    test_case_factory.run_suite('UNIT-TEST')

    """
