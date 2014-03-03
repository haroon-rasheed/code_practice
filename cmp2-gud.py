#! /usr/bin/python

import os, sys, difflib
import filecmp 
from filecmp import dircmp

#act_res_path = '/Volumes/DATA/Haroon/ETL-Python/work/code_practice/'
#exp_res_path = '/Volumes/DATA/Haroon/ETL-Python/work/code_practice-1/'

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

	res_file = open("results.html", "wa", 0)
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

		#diff = difflib.HtmlDiff().make_file(act_res_line, exp_res_line, './txt1', './txt2') 
		diff = difflib.HtmlDiff().make_file(act_res_line, exp_res_line)
		# diff = difflib.HtmlDiff().make_table(act_res_line, exp_res_line)

		print "<br><br>Difference in Result Set <br>"
		print "Actual Result File : %s <br>" %(act_res_file_path) 
		print "Expected Result File: %s <br>" %( exp_res_file_path)
		print  "<br>"
		sys.stdout.writelines(diff)
		import cPickle as pickle
		f = open("temp", "w")
		pickle.dump(diff, f)


	act_res_file.close()
	exp_res_file.close()

if __name__ == '__main__':

	dcmp = dircmp(act_res_path, exp_res_path)

	compare_result(dcmp)

