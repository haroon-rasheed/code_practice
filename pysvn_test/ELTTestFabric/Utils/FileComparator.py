#! /usr/bin/python
'''
Utility for file and directory comparison
'''

import os, sys, difflib, optparse
import filecmp
from filecmp import dircmp
import unittest
import string

from StatusCodes import StatusCodes
from UtilsManager import UtilsManager

class VerifyDSFiles:

    def __init__(self):
        pass

    def __call__(self):
        name = "Class: ".join(str.format(self.__class__.__name__))
        return repr( name )

    def main(self, exec_type=None, run_args={}):
        """
        Main method and entry point for the test
        """

        usage = "usage: "+ "[options] ActualResultsDirectoryPath ExpectedResultsDirectoryPath" 
        parser = optparse.OptionParser(usage, version = self.__class__.__name__ + ' Version 1.0')
        parser.add_option("--tc", default="_defl", help="Test Case Number")
        parser.add_option("--mode", metavar="C/V", type="choice", default="V", choices=['C', 'V'], help='C => Compare the results and Produce a consolidated directory level output. V => Compare the results and Produce a verbose HTML side by side diff file')
        parser.add_option("-v", action="store_true", default=True, help='Compare the results and Produce a verbose HTML side by side diff file')
        parser.add_option("--rm", action="store_true", default=False, help="Clean the existing old results file \"results.html\"")

        result = ""

        if (exec_type == "API"):
            if ( len(run_args) > 0 ):
                act_res_path = run_args['act_res_dir']
                exp_res_path = run_args['exp_res_dir']
                tc_no = run_args['test_case_no']
        
                result = self.run_check(act_res_path, exp_res_path, "V", tc_no)
        else:
            (options, args) = parser.parse_args()
            if ( ( len(args) == 0 ) and ( not options.rm )  ):
                parser.print_help()
                return StatusCodes.ERROR
            elif ( (len(args) == 0) and (options.rm) ):    
                print "Cleaning Existing/Old results file"
                os.remove('./results.html')
                return
            elif ( len(args) != 2 and ( options.mode ) ):
                parser.error("need to specify both a actual results directory and expected results directory")

            act_res_path, exp_res_path = args
            result = self.run_check(act_res_path, exp_res_path, options.mode, options.tc)

        return result


    def run_check(self, act_res_path, exp_res_path, run_mode, tc_no):

        result = ""
        result = self.is_res_dir_exist(act_res_path, exp_res_path)

        if ( result == StatusCodes.SUCCESS):
            act_res_path = act_res_path + "/"
            exp_res_path = exp_res_path + "/"

            print "\n Actual Results Directory = ", act_res_path
            print " Expected Results Directory = ", exp_res_path, "\n"

            dcmp = dircmp(act_res_path, exp_res_path)
            result = self.compare_res_dirs(dcmp, run_mode, tc_no)
            return result
        else:
            return StatusCodes.ERROR


    def is_res_dir_exist(self, act_res_path, exp_res_path):
        """
        check if Actual and Expected Results Directories are existing or not
        False is an exceptional condition and hence exit
        """
        dir_check = UtilsManager().check_existance([act_res_path,exp_res_path], "d")

        if (dir_check == True):
            return (StatusCodes.SUCCESS)
        elif (dir_check[0] == False):
            print "Lookup Failure, check whether these files/dirs %s exist(s)" %(dir_check[1])
            return (StatusCodes.ERROR)



    def compare_res_dirs(self, dcmp, run_mode="V", tc_no="_defl"):

        if (tc_no == "_delf"):
            print repr("Test case ID not given, taking default => 'defl' as prefix")

        new_files_one_side = False

        if ( len(dcmp.left_only) > 0 ):
            print "-"*140
            print "Below are the list of new files present only in \"Actual Results\" DIR"

            for counter in range(len(dcmp.left_only)):
                print "(",counter+1,") ", dcmp.left_only[counter]

            new_files_one_side = True
            print "-"*140

        if ( len(dcmp.right_only) > 0 ):
            print "-"*140
            print "Below are the list of new files present only in \"Expected Results\" DIR"

            for counter in range(len(dcmp.right_only)):
                print "(",counter+1,") ", dcmp.right_only[counter]

            new_files_one_side = True
            print "-"*140

        print "-"*140
        print "Procdeeding to compare the Data Set in the matching(common) files for both Directories \n"    
        print "Number of Data Files with common Name and different DATA =", len(dcmp.diff_files)

        if ( len(dcmp.diff_files) > 0 ):
            print "\n\nFound Discrepancy in data content across Data files \n\n\n"

            if (run_mode == 'C'):
                print 'Running Simple Directory level check \n\n'
                print "-"*140
                dcmp.report_full_closure()
            elif (run_mode == 'V'):
                print 'Running in Verbose Mode'
                self.tear_down(dcmp, tc_no)

            #return "Mismatch-BUG"
            return (StatusCodes.ERROR)
        elif ( (len(dcmp.common_files) > 1)  and (len(dcmp.diff_files) == 0) and (new_files_one_side == True) ):
            print 'No Data files exist with same name in Actual and Expected results Directories.Pls check.'
            #return 'Match-NoDATAFiles-BUG'
            return (StatusCodes.ERROR)
        else:
            print 'Actual results are good, no discrepancy in data found against expected results'
            #return 'Match-NOBUG'
            return (StatusCodes.SUCCESS)


    def tear_down(self, dcmp, tc_no):
        """
        will generate a detailed HTML side by side diff output
        """
        print "Generating HTML Diff\n"
        print "-"*140

        match_files_list = []
        diff_files_list = [] 

        for name in dcmp.same_files:
            #print "Matching Data file \"%s\", Expected Res:\"%s\" and Actual Res \"%s\":-" %(name, dcmp.left, dcmp.right)
            match_files_list.append(name)
    
        for name in dcmp.diff_files:
            #print "Mismatching Data file \"%s\", Expected Res:\"%s\" and Actual Res \"%s\":-" %(name, dcmp.left, dcmp.right)
            diff_files_list.append(name)
        
        print "Data files with inconsistency in results are: "
        for counter in range(len(diff_files_list)):
            print "(",counter+1,") ", diff_files_list[counter]
   
        res_file = "tc" + str(tc_no) + "_" + UtilsManager().get_file_comp_res_file()

        #Erase the old content in output file
        open(res_file, "w").close()

        res_file_ptr = open(res_file, "a")

        for i in range( len(diff_files_list) ):
            act_res_file = dcmp.left + diff_files_list[i]
            exp_res_file = dcmp.right + diff_files_list[i]

            self.compare_files(act_res_file, exp_res_file, tc_no, res_file_ptr)

        res_file_ptr.close()
        
        print "-"*140
        print "Done data comparision. Check",res_file,"file for details \n"




    def compare_files(self, act_res_file_name, exp_res_file_name, tc_no, output_file_ptr):
        std_out_orig = sys.stdout
        sys.stdout = output_file_ptr


        act_res_file = open(act_res_file_name, 'r')
        exp_res_file = open(exp_res_file_name, 'r')

        act_res_lines = act_res_file.readlines()
        exp_res_lines = exp_res_file.readlines()
    
        diff = difflib.HtmlDiff().make_file(act_res_lines, exp_res_lines)
    
        print "<br><br>Displaying the Difference in Result Set <br>"
        print "Actual Result File : %s <br>" %( act_res_file_name )
        print "Expected Result File: %s <br>" %( exp_res_file_name )
        print  "<br>"
        sys.stdout.writelines(diff)
        act_res_file.close()
        exp_res_file.close()

        sys.stdout = std_out_orig

"""    
For using doctest Framework in furute
def _test():
    import doctest
    doctest.testmod()
"""
if __name__ == '__main__':
    VerifyDSFiles().main()
    #exec(file_comp.main.__code__, {file_comp})

