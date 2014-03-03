#! /usr/bin/python

import os, sys, difflib, optparse
import getopt
import filecmp 
from filecmp import dircmp
import unittest


class RunUT(unittest.TestCase):
	def runTest(self):
		test_runner = VerifyDSFiles()
		test_runner.main()


class VerifyDSFiles(object):

		def __init__(self):
			pass

		def main(self):
			usage = "usage: %prog [options] ActualResultsFilePath ExpectedResultsFilePath" 
			parser = optparse.OptionParser(usage)
			parser.add_option("-c", action="store_true", default=False, help='Compare the results and Produce HTML side by side diff')
			#parser.add_option('--version', action="version", dest="version", default=1.0, help='Print Version')
			#parser.add_option("--version", action="version", version="%(prog)s 1.0")

			(options, args) = parser.parse_args()

			if len(args) == 0:
				parser.print_help()
				sys.exit(1)

			if len(args) != 2:
				parser.error("need to specify both a actual results file and expected results file")

			act_res_path, exp_res_path = args	

			act_res_path = act_res_path + "/"
			exp_res_path = exp_res_path + "/"

			print "\n Actual Results Directory = ", act_res_path
			print " Expected Results Directory = ", exp_res_path, "\n"

			self.compare_results(act_res_path, exp_res_path)


		def compare_results(self,act_res_path, exp_res_path):
			dcmp = dircmp(act_res_path, exp_res_path)

			#dcmp.report_full_closure()

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
			print "Procdeeding to compare the Data Set in the matching(common) files for both Directories \n\n\n"	

			match_files_list = []
			diff_files_list = [] 

			if ( len(dcmp.diff_files) > 0 ):
				print "\n\n\nFound Discrepancy in data content across Data files, Generating HTML Diff\n"
				for name in dcmp.same_files:
					#print "Matching Data file \"%s\", Expected Res:\"%s\" and Actual Res \"%s\":-" %(name, dcmp.left, dcmp.right)
					match_files_list.append(name)
		
				for name in dcmp.diff_files:
					#print "Matching Data file \"%s\", Expected Res:\"%s\" and Actual Res \"%s\":-" %(name, dcmp.left, dcmp.right)
					diff_files_list.append(name)
			
				res_file = open("results.html", "wa", 0)
				std_out_orig = sys.stdout
				sys.stdout = res_file
				
				print "Data files with inconsistency in results are: <br>"
				for counter in range(len(diff_files_list)):
					print "(",counter+1,") ", diff_files_list[counter], "<br>"
			
			
				for i in range( len(diff_files_list) ):
					act_res_file_path = act_res_path + diff_files_list[i]
					exp_res_file_path = exp_res_path + diff_files_list[i]
			
					act_res_file = open(act_res_file_path, 'r')
					exp_res_file = open(exp_res_file_path, 'r')
			
			
					act_res_line = act_res_file.readlines()
					exp_res_line = exp_res_file.readlines()
			
					diff = difflib.HtmlDiff().make_file(act_res_line, exp_res_line)
			
					print "<br><br>Displaying the Difference in Result Set <br>"
					print "Actual Result File : %s <br>" %(act_res_file_path) 
					print "Expected Result File: %s <br>" %( exp_res_file_path)
					print  "<br>"
					sys.stdout.writelines(diff)
					act_res_file.close()
					exp_res_file.close()
				
				sys.stdout = std_out_orig
				print "-"*140
				print "Done data comparision. Check the results.html file for details"
				return "Mismatch-BUG"

			else:
				print 'Actual results are good, no discrepancy in data found against expected results'
				return 'Match-NOBUG'


"""	
For using doctest Framework in furute
def _test():
	import doctest
	doctest.testmod()

"""

if __name__ == '__main__':
	testCase = RunUT()
	runner = unittest.TextTestRunner()
	runner.run(testCase)

