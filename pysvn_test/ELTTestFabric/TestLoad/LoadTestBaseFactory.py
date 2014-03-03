#!/usr/bin/python

import sys
import re
import unittest

from ELTTestBaseFactory import ELTTestBaseFactory
from Utils.StatusCodes import StatusCodes

from TestLoad.UnitTest.LoadUTNamespace import test_case_namespace

class LoadTestBaseFactory(ELTTestBaseFactory):

    tc_list = []

    """
    def __init__(cls):
        pass
    Be aware if you want to override init more than one args then override unittest.Testcase init also
    else it will end up in Attribute Error
    AttributeError: 'LoadTestBaseFactory' object has no attribute '_testMethodName'
    """


    @classmethod        
    def init_test_suite(cls, ts_type, test_case_choice):
        cls.ts_type = ts_type
        cls.test_case_choice = test_case_choice
        

    @classmethod        
    def get_test_case(cls):

        if (cls.ts_type == 'UNIT-TEST'):
            try:
                test_case_pkg = test_case_namespace[cls.test_case_choice]
            except KeyError:
                print "Invalid test case selection: ", cls.test_case_choice
                return (StatusCodes.ERROR)

            cls.test_case_class = test_case_pkg[0]
            cls.test_case_info = test_case_pkg[1]
            cls.test_case_args = test_case_pkg[2]
            cls.test_case_class.init_attribs(cls.test_case_args)

        elif (cls.ts_type == 'REGN-TEST'):
            # TBD
            #return LoadRegnTestImpl()
            pass


    def _runTest(self):
        cls = self.__class__
        print "\n\n\n Running Load Unit Test Case No....", cls.test_case_choice
        print "Argumets passed to the test case -=>", cls.test_case_args, "\n\n\n"
        tc_ref = unittest.TestLoader().loadTestsFromTestCase(cls.test_case_class)
        cls.ut_suite = unittest.TestSuite()
        cls.ut_suite.addTest(tc_ref)
        unittest.TextTestRunner(verbosity=2).run(cls.ut_suite)



    @classmethod        
    def run_test(cls):
        cls()._runTest()
        

    @classmethod        
    def run_suite(cls, suite_type):
    
        load_ut_suite = unittest.TestSuite()

        print "\n\n\n INITIALIZING LOAD UNIT TEST SUITE....\n\n\n"

        if (suite_type == "UNIT-TEST"):
            try:
                for tc_no, tc_class_pkg in test_case_namespace.iteritems():
                    cls.test_case_class = tc_class_pkg[0]
                    cls.test_case_args = tc_class_pkg[2]
                    cls.test_case_class.init_attribs(cls.test_case_args)
                    print "\nInitializing Load Unit Test Case No....", tc_no
                    print "Argumets passed to the test case -=>", cls.test_case_args, "\n"
                    tc_ref = unittest.TestLoader().loadTestsFromTestCase(cls.test_case_class)
                    load_ut_suite.addTest(tc_ref)
            except KeyError:
                print "Invalid test case selection "
                return (StatusCodes.ERROR)
            print "\n\n\n RUNNING LOAD UNIT TEST SUITE....\n\n\n"
            unittest.TextTestRunner(verbosity=2).run(load_ut_suite)
