#!/usr/bin/env python

import re

tenant = {'phone': '9822052560', 'company': 'VD_149 Corp', 'name': 'i####mYteNaNt'}
print "input tenant name:", tenant['name']

if (re.search('[A-Z]', tenant['name'])):
    tenant['name'] = tenant['name'].lower()
    print "Lower cased tenant:", tenant['name']
else:
    print "Tenant Name AS IS:", tenant['name']

