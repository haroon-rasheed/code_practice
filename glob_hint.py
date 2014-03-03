#!/usr/bin/python
#-*- coding: utf-8 -*-


"""
The glob module finds all the pathnames matching a specified pattern according
to the rules used by the Unix shell. No tilde expansion is done, but *, ?, and
character ranges expressed with [] will be correctly matched. 
"""

import glob, os

for i in glob.glob("*.py"):
    #print i
    pass

iter = glob.iglob("*.py")

"""
for i in len(iter):
    print iter.next()
while( True ):
    try:
        i=iter.next()
    except Exception as e:
        break
    else:
        print i
"""
print glob.glob(".??*")
#print os.remove(" ".join(glob.glob("jt_tmp_f*")))
os.remove("jt_tmp_f1 jt_tmp_f2")

