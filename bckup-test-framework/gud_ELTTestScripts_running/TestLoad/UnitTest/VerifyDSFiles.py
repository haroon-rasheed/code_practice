#! /usr/bin/python

import os, sys, difflib, optparse
import filecmp
from filecmp import dircmp
import unittest
import string
#from ELTTestBaseFactory import LoadUnitTestBase

class UTError(Exception):
	def __init__(self, err_type, component):
		self.err_type = err_type
		self.component = component

	def __str__ (self):
		if (self.err_type == IOError ):
			err_msg = "Lookup Failure, check whether these files/dirs %s exist(s)" %(self.component)
			return repr(err_msg)

class RunUT(unittest.TestCase):
	def runTest(self):
		test_runner = VerifyDSFiles()
		#test_runner = VerifyDSFiles
		test_runner.main()


#class VerifyDSFiles(LoadUnitTestBase):
class VerifyDSFiles(object):

	def __init__(self):
		pass

	def main(self):
		"""
		Main method and entry point for the test
		"""

		usage = "usage: %prog [options] ActualResultsFilePath ExpectedResultsFilePath" 
		parser = optparse.OptionParser(usage, version='%prog Version 1.0')
		parser.add_option("-c", action="store_true", default=False, help='Compare the results and Produce a consolidated directory level output')
		parser.add_option("-v", action="store_true", default=True, help='Compare the results and Produce a verbose HTML side by side diff file')
		parser.add_option("--rm", action="store_true", default=False, help="Clean the existing old results file \"results.html\"")

		(options, args) = parser.parse_args()

		if ( ( len(args) == 0 ) and ( not options.rm )  ):
			parser.print_help()
			sys.exit(1)
		elif ( (len(args) == 0) and (options.rm) ):	
			print "Cleaning Existing/Old results file"
			os.remove('./results.html')
			sys.exit(0)
		elif ( len(args) != 2 and ( options.c or options.v) ):
			parser.error("need to specify both a actual results directory and expected results directory")

		""" Neither Actual results DIR Nor Expected Results DIR is present, then stop """
		act_res_path, exp_res_path = self._setup_testcase(args)

		act_res_path = act_res_path + "/"
		exp_res_path = exp_res_path + "/"

		print "\n Actual Results Directory = ", act_res_path
		print " Expected Results Directory = ", exp_res_path, "\n"

		dcmp = dircmp(act_res_path, exp_res_path)
		result = ""

		if options.c:
			print 'Running Simple Directory level check'
			dcmp.report_full_closure()
		elif options.v:
			print 'Running in Verbose Mode'
			result = self._execute_tc(dcmp)

		return result

	def _setup_testcase(self, args):
		"""
		check if Actual and Expected Results Directories are existing or not
		False is an exceptional condition and hence exit
		"""
		act_res_path, exp_res_path = args
		lookup_fail = None

		if ( not(os.path.isdir(act_res_path)) ):
			print 'Actual Results Directory \"%s\" does not exist' %(act_res_path)
			lookup_fail = act_res_path

		if ( not(os.path.isdir(exp_res_path) )):	
			print "Expected Results Directory \"%s\" does not exist" %(exp_res_path)
			lookup_fail += str("," + exp_res_path)


		if ( not(lookup_fail == None) ):
			raise UTError(IOError, lookup_fail)

		return act_res_path, exp_res_path	


	def _execute_tc(self, dcmp):
		"""
		run the result checker in verbose mode
		"""

		if ( len(dcmp.left_only) > 0 ):
			print "-"*140
			print "Below are the list of new files present only in \"Actual Results\" DIR"
			for counter in range(len(dcmp.left_only)):
				print "(",counter+1,") ", dcmp.left_only[counter]
			print "-"*140

		if ( len(dcmp.right_only) > 0 ):
			print "-"*140
			print "Below are the list of new files present only in \"Expected Results\" DIR"
			for counter in range(len(dcmp.right_only)):
				print "(",counter+1,") ", dcmp.right_only[counter]
			print "-"*140

		print "-"*140
		print "Procdeeding to compare the Data Set in the matching(common) files for both Directories \n"	


		if ( len(dcmp.diff_files) > 0 ):
			print "\n\nFound Discrepancy in data content across Data files, Generating HTML Diff\n"
			self._verify_teardown(dcmp)
			return "Mismatch-BUG"
		else:
			print 'Actual results are good, no discrepancy in data found against expected results'
			return 'Match-NOBUG'

	def _verify_teardown(self, dcmp):
		"""
		will generate a detailed HTML side by side diff output
		"""

		match_files_list = []
		diff_files_list = [] 

		for name in dcmp.same_files:
			#print "Matching Data file \"%s\", Expected Res:\"%s\" and Actual Res \"%s\":-" %(name, dcmp.left, dcmp.right)
			match_files_list.append(name)
	
		for name in dcmp.diff_files:
			#print "Matching Data file \"%s\", Expected Res:\"%s\" and Actual Res \"%s\":-" %(name, dcmp.left, dcmp.right)
			diff_files_list.append(name)
	
		try:
			res_file = open("results.html", "wa", 0)
		except IOError:
			raise IOError("Cannot open results.html file")

		std_out_orig = sys.stdout
		sys.stdout = res_file

		
		print "Data files with inconsistency in results are: <br>"
		for counter in range(len(diff_files_list)):
			print "(",counter+1,") ", diff_files_list[counter], "<br>"
	
	
		for i in range( len(diff_files_list) ):
			act_res_file = open(dcmp.left + diff_files_list[i]  , 'r')
			exp_res_file = open(dcmp.right + diff_files_list[i], 'r')
	
			act_res_line = act_res_file.readlines()
			exp_res_line = exp_res_file.readlines()
	
			diff = difflib.HtmlDiff().make_file(act_res_line, exp_res_line)
	
			print "<br><br>Displaying the Difference in Result Set <br>"
			print "Actual Result File : %s <br>" %( dcmp.left + diff_files_list[i] )
			print "Expected Result File: %s <br>" %( dcmp.right + diff_files_list[i] )
			print  "<br>"
			sys.stdout.writelines(diff)
			act_res_file.close()
			exp_res_file.close()
		
		sys.stdout = std_out_orig
		print "-"*140
		print "Done data comparision. Check the results.html file for details"



"""	
For using doctest Framework in furute
def _test():
	import doctest
	doctest.testmod()


if __name__ == '__main__':
	testCase = RunUT()
	runner = unittest.TextTestRunner()
	runner.run(testCase)

"""
