#!/usr/bin/python

def va_arg(*args, **kwargs):
    print "Args =>", args
    print "Keyword Args =>", kwargs


va_arg(1,2,3,four=4,five=5)
