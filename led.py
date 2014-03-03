#!/usr/bin/python

import paramiko
import os

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('NukonaAC.symc.com', username='ACUser', password='temp')

chan = ssh.invoke_shell()

# Ssh and wait for the password prompt.
chan.send('sudo shutdown -h now') 
buff = ''
resp = chan.recv(65346)
buff += resp
print resp
