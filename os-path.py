#! /usr/bin/python

'''
some good stuffs about paths
'''
import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, file = os.path.split(full_path)
print(path + ' --> ' + file + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

print "Using os.abspath"
print os.path.abspath(full_path)

print "expand vars"
print os.path.expandvars(full_path)
