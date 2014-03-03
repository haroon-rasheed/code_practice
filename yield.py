#!/usr/bin/python

'''
yield statement will makes a function as generator function.
'''

def generate_integers(N):
    for i in range(N):
        yield i

gen = generate_integers(3)
print gen
print gen.next()
print gen.next()
print gen.next()
