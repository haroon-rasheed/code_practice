#!/usr/bin/python
#-*- coding: utf-8 -*-

from pprint import pprint


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
pprint (basket, depth=3, indent=8)
print basket[:]

fruit = set(basket)
print fruit
