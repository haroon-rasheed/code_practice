#!/usr/bin/python

import os

from ConfigParser import SafeConfigParser

from Utils.StatusCodes import StatusCodes
from Utils.EnvManager import EnvManager

class UtilsManager(object):
    config_parser = None
    config_file = None

    def __init__(self): 
        self.config_parser = SafeConfigParser()
        self.config_file = EnvManager().get_env_var("PJ_CONFIG_FILE")

    def get_config_parser(self):

        self.get_config_file()

        if (self.config_file is not None):
            try: 
                self.config_parser.read(self.config_file)
            except Exception as err:
                print err 
                print "Unable to read config file"
                return (StatusCodes.ERROR)
        return (self.config_parser)
    
    def get_config_file(self):
        return (self.config_file)

    def get_file_comp_res_file(self):
        cfg_reader = self.get_config_parser()
        try:
            res_file = cfg_reader.get("file_comparision", "diff_file")
        except Exception as e:
            print e
            raise IOError("Cannot open output file results.html")
        else:
            return res_file

    def check_existance(self, src, type):
        lookup_fail = []
        if (type == "f"):
            for i,v in enumerate(src):
                if (os.path.isfile(v) == False ):
                    lookup_fail.append(v)
                    #print "Source File", src, "Does not exists."
                    #return (False, lookup_fail)
        elif (type == "d"):
            for i,v in enumerate(src):
                if (os.path.isdir(v) == False ):
                    lookup_fail.append(v)
                    #print "Source Directory", src, "Does not exists."
        if ( len(lookup_fail) > 0 ):
            return (False, lookup_fail)
            
        return True
