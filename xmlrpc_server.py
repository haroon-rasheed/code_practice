#!/usr/bin/python

import platform
from xmlrpclib import *
from SimpleXMLRPCServer import SimpleXMLRPCServer, list_public_methods
import inspect

'''
server = SimpleXMLRPCServer(('localhost',8765), logRequests=True, allow_none=False)
server.register_introspection_functions()
server.serve_forever()
server.register_multicall_functions()
#server.login
'''

class ServerFood(object):
    '''
    server will eat this class
    '''

    def _listMethods(self):
        return list_public_methods(self)

    def _methodHelp(self, method):
        f = getattr(self, method)
        return inspect.getdoc(f)

    def hello(self):
        return "Get out"


    def name(self):
        return platform.mac_ver()

server = SimpleXMLRPCServer(('127.0.0.1', 8765), allow_none=True)
server.register_introspection_functions()
server.register_multicall_functions()
server.register_instance(ServerFood())
server.serve_forever()
