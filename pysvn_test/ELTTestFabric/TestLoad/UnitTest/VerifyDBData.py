#!/usr/bin/python


from Utils.StatusCodes import StatusCodes
from Utils.TableComparator import TableComparator
from Utils.UtilsManager import UtilsManager

from LoadUnitTestImpl import LoadUnitTestImpl

class VerifyDBData(LoadUnitTestImpl):

    r_args = {}

    @classmethod 
    def runTest(cls):
        result = cls.execute_tc()
        cls().assertEqual(result, StatusCodes.SUCCESS), "Inconsistency, seems having an issue. Please verify"

    
    @classmethod 
    def init_attribs(cls, p_args):
        cls.r_args = p_args
        # Debug
        #cls.dump_vars()


    def __str__(self):
        # Enable the below if you need text info and remove Empty return
        """
        usage =  "Test Case to verify the integrity of CTRL/DATA Files"
        return repr(usage)
        """
        return ""

    
    @classmethod 
    def set_up(cls):
        """ 
        Hook method for setting up the test fixture before exercising it
        Below is just a sample and not necessary for this case, as File Comparison
        tool will take care the below check.
        """
        pass
    
    @classmethod 
    def execute_tc(cls):
        DB_checker = TableComparator()
        result = DB_checker.main("API", cls.r_args)
        return result


    
    @classmethod 
    def verify(cls):
        print "Executing Sample Unit Test Case Verify()"
        pass


    @classmethod 
    def tearDown(cls):
        print "Executing Sample Unit Test Case tearDown()"
        pass


