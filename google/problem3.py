#!/usr/bin/env python

"""
Print out the prime numbers between 1 and 100. As a first pass, don't worry about writing an efficient algorithm. 
Just write clear code that is easy to follow. Once you've done that, consider different possible optimizations.
"""

for i in range(1,100):
    if not(i%2 == 0 or i%3 == 0 or  i%5 == 0 or i%7 == 0):
        print i
    else:
      continue
