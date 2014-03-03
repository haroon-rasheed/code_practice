#!/usr/bin/python

import tarfile
with tarfile.open("test.tar", "r") as tar:
    for ele in tar:
        if ele.isfile():
            print "is a file", ele
        elif ele.isdir():
            print "is a dir", ele


