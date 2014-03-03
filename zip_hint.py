#!/usr/bin/python


l1 = [1,2,3,8]
l2 = [4,5,6]
zipped = zip(l1,l2)
print "Zipped =>", zipped
#unzipping
l3, l4 = zip(*zip(l1,l2))
print "UnZipped =>",l3, l4 
