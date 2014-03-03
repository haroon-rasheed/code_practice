#!/usr/bin/python

import fnmatch, os

print fnmatch.filter(os.listdir("."), "*.txt")

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "*.py"):
        print file

# case sensitive version fnmatch.fnmatchcase
