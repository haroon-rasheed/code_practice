#! /usr/bin/python

import sys

from TestLoad.LoadTestBaseFactory import LoadTestBaseFactory
from TestExtract.ExtractTestBaseFactory import ExtractTestBaseFactory
from TestTransform.TransformTestBaseFactory import TransformTestBaseFactory

class ELTTestBaseFactory(object):
	
	@staticmethod
	def get_test_factory( factory_type ):
		if factory_type == 'EXTRACT':
			return ExtractTestBaseFactory()

		elif factory_type == 'LOAD':
			return LoadTestBaseFactory()

		elif factory_type == 'TRANSFORM':	
			return TransformTestBaseFactory()

