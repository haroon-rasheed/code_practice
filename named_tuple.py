#!/usr/bin/python
#-*- coding : utf-8 -*-

"""
Example of collections.NamedTuple Class
namedtuple is accessible by attribute lookup as well as being indexable and iterable
Instances of the subclass also have a helpful docstring (with typename and
field_names) and a helpful __repr__() method which lists the tuple contents in a
name=value format.
"""
from collections import namedtuple

test_case_namespace = { 
                        1 : ["VerifyCTRLData", "Verify CTRL files for Integrity", {"act_res_dir"  : "actual_results", "exp_res_dir" : "expected_results", "test_case_no" : "99" }  ],  
                        2 : ["VerifyDBData", "Test Case 2", {"test_case_no" : "71",  "table" : "etl_process_status", "pkey" : "BATCH_SK,PROCESS_SK", "non_pkey" : "MIN_BATCH_ID,PROCESS_NAME", "where" : "PROCESS_NAME,=,'wf_SFF_BRANCHED_QUESTIONS'", "mode" : "C",   "run" : "A",} ], 
                        3 : ["SampleTC3", "Test Case 3", {"3" : "3"}],
                     }   


args = namedtuple("args", "act_res_dir exp_res_dir test_case_no")

tc2 = args(act_res_dir="actual_results", exp_res_dir="expected_results", test_case_no="99")
#indexed access
print tc2[0]
# iterative access
print tc2.next()
#attribute access
print tc2.test_case_no
print dir(tc2)
#repr
print "REPR =>", tc2.__repr__()
#doc
print "Doc =>", tc2.__doc__
