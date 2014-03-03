#!/usr/bin/env python
import paramiko
"""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('NukonaAC.symc.com',username='ACUser', password="temp")
chan = ssh.get_transport().open_session()
chan.get_pty()
#chan.exec_command('tty')
chan.exec_command('poweroff')
print(chan.recv(65536))
"""

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('NukonaAC.symc.com',username='ACUser', password="temp")
stdin, stdout, stderr = ssh.exec_command("sudo shutdown -hk 5 \"Ayyo\"")
stdin.write('\n')
stdin.flush()
print "Out =>", stdout.readlines()
print "Err =>", stderr.readlines()
ssh.close()
