#!/usr/bin/python

import pysvn,getpass

def get_login(realm, username, may_save ):
    uname = raw_input("SVN Username:")
    passwd = getpass.getpass("Password: ")
    return True, uname, passwd, True 

client = pysvn.Client()
#entry = client.info('.')
#print 'Url:',entry.url
client.callback_get_login = get_login
client.checkout("http://istsvn.corp.apple.com:1080/SVNROOT/EDW/branches/Common_Framework/CORE-ETL/PythonUtilities/ELTTestFabric", ".")
