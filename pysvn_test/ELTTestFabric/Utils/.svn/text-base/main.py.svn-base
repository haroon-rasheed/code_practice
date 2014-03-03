#! /usr/bin/python


import os,sys
from EnvManager import EnvManager

if __name__ == '__main__':
	try:
		if(sys.argv[1] is not None):
			EnvManager().get_env_var(sys.argv[1])
			EnvManager().dump_all_vars()
	except IndexError:
		pass
