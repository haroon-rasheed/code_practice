#!/usr/bin/python
from __future__ import division
##-*- coding: utf-8 -*-

from string import Template
import string

"""
shows some samples for string operations
"""

#template()

td_db = "DB"
td_uid = "UID"
td_psw = "TD_PSW"
ctl_file_name = "CTL_FILE_NAME"
loader_type = "LOADER_TYPE"
log_file_name = "LOG_FILE_NAME"

#WAY 1
# The below is the good way using $ with {}
cmd_tpl = Template("sed -e 's/tdpid/${TERADATA_DB}/' -e 's/loginid/${TERADATA_UIDCTRL},${TERADATA_PWDCTRL}/'" + "< ${ctl_file_name} | ${loader_type} > ${log_file_name}")
#cmd_tpl = Template("sed -e 's/tdpid/$TERADATA_DB/' -e 's/loginid/$TERADATA_UIDCTRL,$TERADATA_PWDCTRL/'" + "< $ctl_file_name | $loader_type > $log_file_name")
cmd = cmd_tpl.substitute(TERADATA_DB = td_db, TERADATA_UIDCTRL = td_uid, TERADATA_PWDCTRL = td_psw, ctl_file_name = ctl_file_name, loader_type = loader_type, log_file_name = log_file_name)

#Way 2
cmd_tpl = "sed -e 's/tdpid/${TERADATA_DB}/' -e 's/loginid/${TERADATA_UIDCTRL},${TERADATA_PWDCTRL}/'" + "< ${ctl_file_name} | ${loader_type} > ${log_file_name}"
Template(cmd_tpl).substitute(TERADATA_DB = td_db, TERADATA_UIDCTRL = td_uid, TERADATA_PWDCTRL = td_psw, ctl_file_name = ctl_file_name, loader_type = loader_type, log_file_name = log_file_name)

noun = "kill"
print Template("${noun}ification").substitute(noun=noun)

#print "CMD =>", cmd

#String Formatting
st = "repr() shows quote: {!r} but str() no quotes: {!s}"
st = st.format('test', 'test')
print st

#Text alignment
print "LEFT => {:<50}".format("align this")
print "RIGHT => {:>50}".format("align this")
print "Center => {:^50}".format("align this")
print "Fill => {:*^50}".format("align this")

#Number Formatting
print "binary bin: {0:b}".format(12)
#All together
print "ALL => int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)

# with 0x, 0o, or 0b as prefix:
print "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)

#print a percentage %
#the below will give only ZERO, to get proper O/P we have to convert any one as float
no = 8/12      # =>  WRONG
no = (float(8)/12)  # =>  correct
print "No =>", no
print "Percentage {:.2%}".format(float(1)/2)
#or use the below
# from __future__ import division, which the forces / to adopt Python 3.x's behavior that always returns a float.

print "Percentage11 {:.2%}".format(float(3)/4)

print string.ljust("Python", 20, "-")
print string.rjust("Python", 20, "-")
print string.center("Python", 20, "-")

print string.zfill("python", 20)

print string.swapcase("python")
print string.swapcase("PYTHOn")
