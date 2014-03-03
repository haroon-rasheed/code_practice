#!/usr/bin/python

import unittest

class SomeClass(unittest.TestCase):
    def testmain(self):
    # your testcode here
        print "t1"

    def testone(self):
        print "one-1"

    def testtwo(self):
        print "one-2"

class SomeOtherClass(unittest.TestCase):
    def testmain(self):
    # testcode of second class here
        print "t2"

    def testone(self):
        print "two-1"

    def testtwo(self):
        print "two-2"


class SomeClass1(unittest.TestCase):
    def testmain(self):
        print "Outter"

if __name__ == '__main__':
    # WAY 1
    test_suite = unittest.TestSuite()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(SomeClass)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(SomeOtherClass)
    test_suite.addTest(suite1)
    test_suite.addTest(suite2)
    unittest.TextTestRunner(verbosity=2).run(test_suite)

    #WAY 2

    test_fun_list = unittest.TestLoader().getTestCaseNames(SomeClass)
    print 'Fun List =>', test_fun_list

    print 'Map =>', map(SomeClass, test_fun_list) 
    print "Suite =>", suite1

    #unittest.TestSuite(map(SomeClass, test_fun_list))
    unittest.TextTestRunner(verbosity=3).run( unittest.TestSuite(map(SomeClass, test_fun_list)) )
