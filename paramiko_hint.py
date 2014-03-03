#!/usr/bin/env python

import paramiko
cmd = "python -c \"import os; os.system('sudo shutdown -hk 5')\""
print "CMD =>", cmd
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())
ssh.connect('NukonaAC.symc.com', username='ACUser', password='temp')
#stdin, stdout, stderr = ssh.exec_command("ps -A | grep mysql")
stdin, stdout, stderr = ssh.exec_command(cmd)
print "out =>", stdout.readlines()
print "err =>", stderr.readlines()

"""
#Executing sudo commands, its needs a tty to run, we cant run it like above
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('NukonaAC.symc.com', username='ACUser', password='temp')
#channel = ssh.get_transport().open_session()
#channel.invoke_shell()
#channel = ssh.invoke_shell()
#channel.get_pty()
ssh.invoke_shell()
stdin, stdout, stderr = ssh.exec_command("sudo shutdown -hk 5 \"Poda Vennai\"")
print "out =>", stdout.readlines()
print "err =>", stderr.readlines()
if( channel.send_ready()):
    try:
        print "Running sudo command"
        channel.send("sudo shutdown -hk 5 \"Poda Vennai\"")
        resp = channel.recv(65536)
        print "resp", resp
    except Exception as err:
        print "GIRR =.", err.args
"""
