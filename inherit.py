#! /usr/bin/python

import sys

class BaseException(Exception, object):
	"Mother of all exceptions"

	def __init__(self):
		pass

	@classmethod
	def get_error_info(cls, caller):
		print "This exception has been raised from", caller

