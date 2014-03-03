#!/usr/bin/python
#-*- coding : utf-8 -*-

"""
Dequeue stuffs
"""
from collections import deque

lt = ["VerifyCTRLData", "Verify CTRL files for Integrity", {"act_res_dir"  : "actual_results", "exp_res_dir" : "expected_results", "test_case_no" : "99" }  ]
dq = deque(lt)
print "DQ =>", dq
print "DQ pop 1", dq.pop()
print "DQ pop 2", dq.pop()
print "DQ pop 3", dq.pop()
dq = deque(lt)
dq.reverse()
print "reversed", dq
