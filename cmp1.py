#! /usr/bin/python


import filecmp 
from filecmp import dircmp

#print filecmp.cmp('txt1', 'txt3')
#match_files_list = []
#diff_files_list = []


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
	dcmp.report_full_closure()	
	
	print "Matching Data files" 
	for counter in range(len(match_files_list)):
		print counter+1, match_files_list[counter]

	"""	
	#print match_files_list
	print "New Data files" 
	print diff_files_list 
	"""

dcmp = dircmp('/Volumes/DATA/Haroon/ETL-Python/work/code_practice', '/Volumes/DATA/Haroon/ETL-Python/work/code_practice-1')

compare_result(dcmp)

