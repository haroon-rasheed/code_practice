#!/usr/bin/env python
import re

query = u'Perforce-fix'
print query
if not re.match(r'^[\w\s]+$', query, re.UNICODE):
  print "NOOOO"
