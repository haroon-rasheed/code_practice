#!/usr/bin/python

"""
shows how to run C code inside python
"""
#Way 1

import ctypes
from ctypes import *
#cdll.LoadLibrary("/usr/lib/libc.dylib")        # this is also one way
libc = ctypes.CDLL("./pylib.so")
libc.Foo_new()

libc.Foo_bar()
