#!/usr/bin/python

import re

spe_char = "wha$$$t    999999 #####!!!!!!$%^&9()))) cha+++++++r is th****is?"
#spe_char = "what    999999 "
print "B4 =>", spe_char
print "Using str.isalnum =>"
print ''.join(e for e in spe_char if e.isalnum())

spe_char = re.sub("[^A-Za-z0-9]+", "", spe_char)
print "Using RE =>", spe_char

string = "Special $#! characters   spaces 888323"
print ''.join(e for e in string if e.isalnum())

name = "john"
st = ".".join(name)
print st
