#!/usr/bin/env python

import re

query = "Symantec App Center On Premise Multi-tenancy Installation Guide 2.0"
#query = "Symantec App Center On Premise Multi-tenancy Installation Guide 20"
#query = "Multi-tenancy"
#query = "App-Center-User-Guide-415"

""""
#if not re.match(r'^[\w\s-]+$', query, re.UNICODE):
if not re.match(r'^[\w\s\.-]+$', query, re.UNICODE):
  print "NOOOOO"
else:
  print "YAhOO"    
"""

if re.match(r'^[\w\s-]+$', query, re.UNICODE):
  print "Yahoo"
else:
  print "Ohno"    
