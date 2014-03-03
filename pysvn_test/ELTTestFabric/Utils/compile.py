#!/usr/bin/python 
# -*- coding: utf-8 -*-

'''
Compiler Module for Python 
Helps to compile all files in a source code root and see the errors in one go.
Also will clean the compiled Python files => .pyc in current directory or else recursively through all sub directories from current directory (options –r & -e)
Aim:
Write all the necessary files, compile them all in one go, fix errors, enjoy.
Check the help message to use it.

'''

import sys,os,glob
import py_compile
import compileall
import optparse

def main():
	
	usage = "usage: %prog [options] File/Dir to compile"
	parser = optparse.OptionParser(usage, version='%prog Version 1.0')
	parser.add_option("-f", action="store_true", default=False, help='Compile a single python file')
	parser.add_option("-d", action="store_true", default=False, help='Compile current directory for all python files')
	parser.add_option("-a", action="store_true", default=False, help='Compile current directory for all python files including sub dirs')
	parser.add_option("-r", action="store_true", default=False, help='Clean all existing compiled python files *.pyc in current DIR ')
	parser.add_option("-e", action="store_true", default=False, help='Clean all existing compiled python files *.pyc in current DIR + sub dir')
	
	(options, args) = parser.parse_args()
		
	#if ( len(args) != 1 ):
	#	parser.error("need to specify a file/dir to compile")

	if (options.f):
		print "Compiling python file", sys.argv[2]
		py_compile.compile(sys.argv[2], doraise=True)

	elif (options.d):	
		for files in glob.glob("*.py"):
			compile_src = files
			print "Compiling python file", compile_src
			py_compile.compile(compile_src, doraise=True)

	elif (options.a):	
		for r,d,f in os.walk(os.getcwd()):
			for files in f:
				if files.endswith(".py"):
					compile_src = os.path.join(r,files)
					print "Compiling file", compile_src
					py_compile.compile(compile_src, doraise=True)

	elif (options.r):	
		for files in glob.glob("*.pyc"):
			print "Cleaning file", files
			os.remove(files)

	elif (options.e):	
		#sys.exit(1)
		for r,d,f in os.walk(os.getcwd()):
			for files in f:
				if files.endswith(".pyc"):
					to_del = os.path.join(r,files)
					print "Cleaning file", to_del
					os.remove(to_del)

if __name__ == '__main__':
	main()
