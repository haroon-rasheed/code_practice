#!/usr/bin/python

str1="/old_ssl_certs/sub_ssl_holder"
str2 = "/old_ssl_certs"
print "split 1", str1.split("/", 2)
print "arrea", str1.split("/")[1]
print "split 2", str1.partition("/")
#print "split 3", str2.split("/", 2)
print "split 3", str2.split("/")
print "split 4", str2.partition("/")
