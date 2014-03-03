#!/usr/bin/env python

"""
Start with an array of integers, 1 through 5. First, square all the elements in the array. Then, sum all the elements of the squared array
"""
arr = range(1,5)
print arr
sq_list = [i*i for i in arr ]
print sq_list
print reduce((lambda x,y: x+y), sq_list)
