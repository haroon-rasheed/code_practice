#!/usr/bin/python

import os

file = "MyTestAccount.py"
print "File Name =>", os.path.splitext(file)[0].strip()
print "Ext =>", os.path.splitext(file)[1].strip()

print 'Ext Name without . => ', os.path.splitext(file)[1][1:]
