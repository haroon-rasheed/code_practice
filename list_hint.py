#!/usr/bin/python
#-*- coding : utf-8 -*-

"""
SOme list operations
"""


#lt = ["VerifyCTRLData", "Verify CTRL files for Integrity", {"act_res_dir"  : "actual_results", "exp_res_dir" : "expected_results", "test_case_no" : "99" }  ]
lt = ["VerifyCTRLData", "Verify CTRL files for Integrity", "act_res_dir"]
#print "LT =", lt

print "LT Reversed=", 
for i,v in enumerate(reversed(lt)):
    print i,v 

for v in lt:
    print v
#Make the list as iterative
def iter_list(lt):
    for v in lt:
        yield v

iter = iter_list(lt)
print iter.next()
print iter.next()
print iter.next()

#convert the list to string
str1 = " ".join(lt)
print "STR version of List =>", str1
