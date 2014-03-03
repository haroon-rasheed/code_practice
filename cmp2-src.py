#! /usr/bin/python

import os, sys, difflib
import filecmp 
from filecmp import dircmp

#print filecmp.cmp('txt1', 'txt3')
#match_files_list = []
#diff_files_list = []

act_res_path = '/Volumes/DATA/Haroon/ETL-Python/work/code_practice/'
exp_res_path = '/Volumes/DATA/Haroon/ETL-Python/work/code_practice-1/'

def compare_result(dcmp):
	match_files_list = []
	diff_files_list = [] 

	for name in dcmp.same_files:
		#print "Matching Data file \"%s\", Expected Res:\"%s\" and Actual Res \"%s\":-" %(name, dcmp.left, dcmp.right)
		match_files_list.append(name)

	for name in dcmp.diff_files:
		#print "Matching Data file \"%s\", Expected Res:\"%s\" and Actual Res \"%s\":-" %(name, dcmp.left, dcmp.right)
		diff_files_list.append(name)

	#dcmp.report()	
	#dcmp.report_full_closure()	
	
	"""
	print "Matching Data files" 
	for counter in range(len(match_files_list)):
		print counter+1, match_files_list[counter]
	"""

	for i in range( len(diff_files_list) ):
		act_res_file_path = act_res_path + diff_files_list[i]
		exp_res_file_path = exp_res_path + diff_files_list[i]

		act_res_file = open(act_res_file_path, 'r')
		exp_res_file = open(exp_res_file_path, 'r')


		act_res_line = act_res_file.readlines()
		exp_res_line = exp_res_file.readlines()

		#diff = difflib.HtmlDiff().make_file(act_res_line, exp_res_line, './txt1', './txt2') 
		diff = difflib.HtmlDiff().make_file(act_res_line, exp_res_line)
		# diff = difflib.HtmlDiff().make_table(act_res_line, exp_res_line)
		buf =  sys.stdout.writelines(diff)
		print "Buffer = %s" %(buf)
		

		#res_file = open("results.html", "w")
		res_file = open("results.html", "w", 0)
		sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0) 
		os.dup2( res_file.fileno(), sys.stdout.fileno() )
		#res_file.write("<br><br>Difference in Result Set <br>")
		#res_file.write( "Actual Result File : %s <br>" %(act_res_file_path) )
		#res_file.write( "Expected Result File: %s <br>" %( exp_res_file_path) )
		#res_file.write( "<br>" )
		#res_file.write( sys.stdout.writelines(diff) )
		print diff
		sys.stdout.writelines(diff)
		#res_file.close()

		act_res_file.close()
		exp_res_file.close()

if __name__ == '__main__':

	dcmp = dircmp(act_res_path, exp_res_path)

	compare_result(dcmp)

