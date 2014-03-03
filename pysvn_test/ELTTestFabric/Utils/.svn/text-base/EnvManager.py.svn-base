#! /usr/bin/python

'''
Set all necessary variables to run the project
'''
import os, sys

class EnvManager(object):

	src_root = None
	config_dir = None
	config_file = None
	utils_dir = None

	def __init__(self):
		pre_file = os.path.realpath(__file__)
		pre_dir, f = os.path.split(pre_file)
		pre_dir, f = os.path.split(pre_dir)
		self.src_root = os.path.abspath( pre_dir )
		self.config_dir = self.src_root + "/" + "Config"
		self.config_file = self.config_dir +"/"+ "config.cfg"
		self.utils_dir = self.src_root + "/" + "Utils"
		self.set_env_vars()

	def set_env_vars(self):
		os.environ['PJ_ROOT'] = self.src_root
		os.environ['PJ_CONFIG_DIR'] = self.config_dir
		os.environ['PJ_CONFIG_FILE'] = self.config_file
		os.environ['PJ_UTILS_DIR'] = self.utils_dir
		

	def get_env_var(self, var):

		value = ""
	
		value = os.getenv(var)
	
		if( value is not None ):
			# Uncomment the below print for debugging mode
			#print var[3:] , "=", value
			return value
		else:
			print "Environment Variable", var[3:] , "not set"
			return None

	def dump_all_vars(self):
		for k,v in self.__dict__.iteritems():
			print k,"=",v
