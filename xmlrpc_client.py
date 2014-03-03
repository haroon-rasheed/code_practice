#!/usr/bin/python

import xmlrpclib
from xmlrpclib import *

server = ServerProxy('http://localhost:8765', verbose=True)
result = server.hello()
print "RES 1 =>", result
result = server.name()
print "RES 2 =>", result
#server.login

#server = xmlrpclib.ServerProxy("http://phpxmlrpc.sourceforge.net/server.php")
#result = server.examples.getStateName(2)
#print result
for method_name in server.system.listMethods():
    print '=' * 60
    print "NAME  ==>", method_name
    print '-' * 60
    print "HELPEEE ==>", server.system.methodHelp(method_name)
    print


#svc = xmlrpclib.ServerProxy('http://ws.audioscrobbler.com/2.0/')
#print svc.system.listMethods()
