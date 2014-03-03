#!/usr/bin/python 

import sys
import py_compile

print "Compiling", sys.argv[1]
py_compile.compile(sys.argv[1], doraise=True)
