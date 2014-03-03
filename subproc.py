#! /usr/bin/python

from subprocess import *

call("ls -l", shell=True)
call(["ls", "-l"])
