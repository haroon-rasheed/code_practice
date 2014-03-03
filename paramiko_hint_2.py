#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko, sys

try:
    trans = paramiko.Transport(('NukonaAC.symc.com', 22))
    trans.start_client()
    trans.auth_password("ACUser", "temp")
    #tunnel = trans.open_channel('direct-tcpip', "NukonaAC.symc.com")
    channel = trans.open_channel('session', "NukonaAC.symc.com")

    """
    transport = paramiko.Transport(tunnel)
    transport.start_client()
    transport.auth_password("ACUser", "temp")
    """
except Exception as err:
    print "Error while establishing SSH tunnel", err.args
    sys.exit()


channel.get_pty()
channel.invoke_shell()

if( channel.send_ready()):
    print "Tunnel is ready for communication. Starting interactive session to run \"su –\" "
    try:
        print "Logging in as su - <user>"
        #channel.send('sudo shutdown -hk 5 "DOne Deal"')
        channel.send('sudo -s shutdown -kh 1')
    except Exception as err:
        print "now", err.args
    buff = ''
    while True:
        resp = channel.recv(9999)
        buff += resp
        print buff


