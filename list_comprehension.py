#!/usr/bin/env python

lt = [x if x % 2 else x * 100 for x in range(1, 10) ]
lt1 = [ x for x in range(1,10) if x %2 == 0 ]
print "list =>", lt
print "list 1 =>", lt1
