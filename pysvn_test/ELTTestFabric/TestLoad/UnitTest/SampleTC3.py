#!/usr/bin/python

from LoadUnitTestImpl import LoadUnitTestImpl

class SampleTC3(LoadUnitTestImpl):
    def runTest(self):
        self.set_up()
        print "In Main-3"
        self.execute_tc()
        self.verify()

    @classmethod
    def init_attribs(cls, p_args):
        cls.arg1 = p_args['3'] 
        # Debug
        #cls.dump_vars()

    def set_up(self):
        print "Executing Sample Unit Test Case setUp()-3"
    
    def execute_tc(self):
        print "Executing Sample Unit Test Case execute_tc()-3"


    def verify(self):
        print "Executing Sample Unit Test Case Verify()-3"


    def tearDown(self):
        print "Executing Sample Unit Test Case tear_down()-3"

    def str(self):
        usage =  "Sample Test Case 3"
        usage += "Class => " + self.__class__.__name__
        return repr(usage)
