#!/usr/bin/python
# -*- coding: utf-8 -*- 

from subprocess import call

from ELTTestBaseFactory import ELTTestBaseFactory
from TestLoad.LoadTestBaseFactory import LoadTestBaseFactory

"""
Dummy class that exhibits the usage of Test Framework
"""

class FabricTest(object):

    def __init__(self):
        """
        Init here as you required, being a demo class, initializer is empty
        """
        pass


    def verify_file_data(self):
        # USING THE TOOLS FROM FACTORY/ USING THE FACTORY IN TOOL MODE

        # Assuming that below code is generating CTRL files

        print "Simulating Expected Result generation....\n\n\n"
        call("Utils/TableComparator.py --r E --mode=S --tc=71 --tbl=etl_process_status \
            --pk=BATCH_SK,PROCESS_SK,ENV_CD --npk=PROCESS_NAME \
            --wh=\"PROCESS_NAME,=,'wf_SFF_BRANCHED_QUESTIONS' \" ", \
            shell=True)

        '''
        print "Using Tool Mode to generate Actual Results....\n\n\n"
        # Get the Abstract Factory Interface
        test_factory = ELTTestBaseFactory()
        
        # Framing all necessary argument list to pass to the DB Comparision Tool, they are...
        # Test Case no
        # Table Name
        # Primary Keys
        # Non Primary Keys
        # Where clause
        #args = ["71", "etl_process_status", ["BATCH_SK,PROCESS_SK"], ["MIN_BATCH_ID,PROCESS_NAME"], ["PROCESS_NAME,=,'wf_SFF_BRANCHED_QUESTIONS' " ] ]
        r_args = {  "test_case_no" : "71",
                  "table" : "etl_process_status",
                  "pkey" : "BATCH_SK,PROCESS_SK",
                  "non_pkey" : "MIN_BATCH_ID,PROCESS_NAME",
                  "where" : "PROCESS_NAME,=,'wf_SFF_BRANCHED_QUESTIONS'",
                  "mode" : "S",
                  "run" : "A",
                 }

        # Initialize  the DB Comparision Tool
        test_factory.init_test_tool("DBCompTool", r_args)

        # That’s it call run_test() of factory, it will do the job.
        # Take care of assertion errors. 
        # In case of discrepancy/issues it will throw Assertion Error
        test_factory.run_check()


        # USING THE FACTORY TO RUN A TEST CASE 
        # Assuming that below code is generating CTRL files
        ctrl_file = "actual_results/ps_sfat_lead_rule_EDWDEV.out.ctl"
        with open(ctrl_file) as to_read:
            lines = [line for line in to_read if line.strip()]

        with open(ctrl_file, "w") as to_write:
            for line in lines:
                line = line.strip()
                line += str("  text_inject") + "\n"
                to_write.write(line)

        '''

        # Get the Concrete factory(Load, Extract, Transform)
        #load_ut_factory = LoadTestBaseFactory
        load_ut_factory = ELTTestBaseFactory.get_test_factory("Load")
                             
        # Initialize the test suite Unit/Regression 
        load_ut_factory.init_test_suite('UNIT-TEST', 2)

        # Get the test case
        load_ut_factory.get_test_case()

        # Run the test
        load_ut_factory.run_test()


if __name__ == '__main__':
    # Tool & Test Case Modes 
    tester = FabricTest()
    tester.verify_file_data()

    # Suite Mode
    #load_test_factory = LoadTestBaseFactory()
    #load_test_factory.run_suite("UNIT-TEST")
