#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Main Base Abstract Factory 
This is the interface to get in to other factories as well as utilities
"""
import abc
import unittest

from Utils.UtilsNamespace import utils_namespace
from Utils.StatusCodes import StatusCodes


class ELTTestBaseFactory(unittest.TestCase, object):
    __metaclass__ = abc.ABCMeta

    test_tool = None

    '''
    Return the child(concrete factory)
    '''
    @classmethod
    def get_test_factory(cls, factory_type):
        if (factory_type == "Load"):
            for cl in cls.__subclasses__():
                if (factory_type in cl.__name__):
                    return cl

    '''
    Using factory in Tool Mode
    '''
    
    def init_test_tool(self, key, args):
        tool = None
        try:
            tool = utils_namespace[key]
        except KeyError:
            print "Invalid Tool Selection"
            return (StatusCodes.ERROR)
        self.test_tool = tool
        self.args = args


    def runTest(self):
        print "\nRunning tool", self.test_tool.__class__.__name__
        result = self.test_tool.main("API", self.args)
        assert (result == StatusCodes.SUCCESS), "Inconsistency, seems having an issue. Please verify"

        return result

    def run_check(self):
        unittest.TextTestRunner(verbosity=2).run(self)

