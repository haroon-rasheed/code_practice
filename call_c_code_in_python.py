#!/usr/bin/python

"""
shows how to run C code inside python
"""
#Way 1

import ctypes
from ctypes import *
#cdll.LoadLibrary("/usr/lib/libc.dylib")        # this is also one way
libc = ctypes.CDLL("/usr/lib/libc.dylib")
message_string = "Hello World! Hello Python!\n"
libc.printf("Testing :%s",message_string)

#Way 1
libc = ctypes.CDLL( '/usr/lib/libc.dylib' )   # under MAC
t = libc.time(None)                      # equivalent C code: t = time(NULL)
print t
