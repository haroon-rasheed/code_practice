#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
s = paramiko.SSHClient()
s.set_missing_host_key_policy( paramiko.AutoAddPolicy())
s.connect('NukonaAC.symc.com', username="ACUser", password="temp")
t = s.get_transport()
chan = t.open_session()
chan.exec_command("sudo shutdown -h 5 \"Shutting Down…Pls\"")

print 'writing password'
password="temp"
chan.send(password + '\n')

print 'write command'
chan.send('whoami\n')
print "try to read"
print chan.recv(9999)
