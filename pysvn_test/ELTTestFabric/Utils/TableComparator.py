#!/usr/bin/python

import sys, socket, os, optparse, re
import traceback
import string

import filecmp
from filecmp import dircmp

from StatusCodes import StatusCodes
from FileComparator import VerifyDSFiles
from UtilsManager import UtilsManager

class TableComparator:

    def __init__(self):
		self.host = ""
		self.port = 0
		self.dao  = ""
		self.table = ""
		self.query_str = ""
		self.pks = ""
		self.npks = ""
		self.where = ""
		self.db_client = None
		self.core_log_file = None
		self.log_file = None
		self.act_dir = ""
		self.exp_dir = ""
		self.skip_clean = True
		self.mode = ""

    def main(self, exec_type=None, run_args={}):
        """
        Main method and entry point for the test
        """
        usage = "usage: "+ '[options] --r (Actual Run/Expected Run) A/E --ho=Host<optional>, --po=Port<optional> \
--dao=dao_name, --tbl=table_name, --pk=PKEYS, --npk=NPKS --wh=WHERE '
        parser = optparse.OptionParser(usage, version = self.__class__.__name__ + ' Version 1.0')
        parser.add_option("--r", metavar="Run", type="choice", default='A', choices=['A', 'E'], help="Type of Run: Actual/Expected, default is Actual")
        parser.add_option("--mode", metavar="S/C", type="choice", default='S', choices=['S', 'C'], help="Mode of Run: Save/Compare, Save => Just saves the DB results. Compare => Saves and compares the results, will produce side-by-side HTML diff file") 
        parser.add_option("--tc", metavar="Test Case No", default='_defl', help="Test Case Number")
        parser.add_option("--ho", metavar="Host", help="Host Name <optional>")
        parser.add_option("--po", metavar="Port", default=0, type="int", help="Port Name <optional>")
        parser.add_option("--dao", metavar="Dao Name", help="Database Name <optional>")
        parser.add_option("--tbl", metavar="Table Name", help="Table Name")
        parser.add_option("--pk", metavar="Primary Keys", help=" \'list of primary keys seperated by comma-passed in single quotes\'")
        parser.add_option("--npk", metavar="Non Primary Keys", help=" \'list of non-primary/other keys seperated by comma-passed in single quotes\'")
        parser.add_option("--wh", metavar="WHERE Conditions ", help=" \'where conditions if any, seperated by comma<optional>-passed in single quotes\'")

        (options,args) = parser.parse_args()

        if (exec_type == "API"):
            if ( len(run_args) > 0 ):
                options.tc = run_args['test_case_no'] 
                options.tbl = run_args['table']
                options.pk = run_args['pkey']
                options.npk = run_args['non_pkey']
                options.wh = run_args['where']
                try:
                    options.mode = run_args['mode']
                except KeyError as e:
                    options.mode = "C"
                try:
                    options.r = run_args['run']
                except KeyError as e:
                    options.r = "A"
                self.skip_clean = False

        self.mode = options.mode
        self.run_type = options.r

        res = self.set_attributes(options)

        if (options.tc == "_defl"):
            print repr("Test case ID not given, taking default => 'defl' as prefix")

        if (res == StatusCodes.SUCCESS):
            res = self.execute_SQL_query()
        else:
            return StatusCodes.ERROR

        if (res != StatusCodes.ERROR):
            self.parse_results(res)
        else:
            return StatusCodes.ERROR

        if ( (res != StatusCodes.ERROR) and ( options.mode    == 'C') ):
            res = self.verify(options.tc)
           
        return res


    def set_attributes(self, options):

        res = self._set_conn_attributes(options)

        if(res == StatusCodes.SUCCESS):
            res = self._set_tbl_primary_keys(options)

        if(res == StatusCodes.SUCCESS):
            res = self._set_non_primary_keys(options)

        if(res == StatusCodes.SUCCESS):
            res = self._set_where(options)

        if(res == StatusCodes.SUCCESS):
            res = self._setup_results_dir(options)

        # For Debugging
        self.dump()    
        
        return res

        

    def _set_conn_attributes(self, options):
        from envvar import Env

        if( options.ho is not None):
            if (self.skip_clean == True):
                self.host = re.sub("[ \t]+", '', options.ho).strip()
            else:
                self.host = options.ho
        else:
            print "Reading Host from ENV"
            self.host = Env('', '').etl_map['Host']

        if (  options.po != 0 ):
            self.port = int(options.po)
        else:
            print "Reading Port from ENV"
            self.port = Env('', '').etl_map['MD_DB_PORT']

        if( options.dao is not None):
            if (self.skip_clean == True):
                self.dao = re.sub("[ \t]+", '', options.dao).strip()
            else:
                self.dao = options.dao    
        else:
            print "Reading dao from ENV"
            self.dao = Env('', '').etl_map['MD_DB_DAO']
        
        return (StatusCodes.SUCCESS)






    def _set_tbl_primary_keys(self, options):

        if( options.tbl is not None):
            if (self.skip_clean == True):
                self.table = re.sub("[ \t]+", '', options.tbl).strip()
            else:
                self.table = options.tbl
        else:
            print "Please enter Table Name. Exiting"
            return (StatusCodes.KEY_NOT_FOUND)

        if( options.pk is not None):
            if (self.skip_clean == True):
                self.pks = re.sub("[ \t]+", '', options.pk).strip()
            else:
                for i,v in enumerate(options.pk):
                    self.pks += v
        else:
            print "Please enter Primary Keys. Exiting"
            return (StatusCodes.KEY_NOT_FOUND)
            
        return (StatusCodes.SUCCESS)





    def _set_non_primary_keys(self, options):

        if( options.npk is not None):
            if (self.skip_clean == True):
                self.npks = re.sub('[ \t]+', '', options.npk).strip()
            else:
                for i,v in enumerate(options.npk):
                    self.npks += v
        else:
            print "Please enter Non Primary Keys. Exiting"
            return (StatusCodes.KEY_NOT_FOUND)

        return (StatusCodes.SUCCESS)




    def _set_where(self, options):
        
        if( options.wh is not None):
            if (self.skip_clean == True):
                self.where = re.sub('[ \t]+', '', options.wh).strip()
            else:
                self.where = options.wh
        else:
            print "No where clause opted"

        return (StatusCodes.SUCCESS)




    def _setup_results_dir(self, options):        

        cfg_reader = UtilsManager().get_config_parser()

        try:
            self.act_dir = cfg_reader.get('db_comparision', 'actual_res_dir')
            self.exp_dir = cfg_reader.get('db_comparision', 'expected_res_dir')
            self.core_log_file = "tc" + str(options.tc) + "_" + cfg_reader.get('db_comparision', 'log_file')
        except Exception as e:
            print "Error while parsing config file", e.args
            return (StatusCodes.ERROR)

        if  (options.r == 'A'): 
            if ( UtilsManager().check_existance([self.act_dir], "d") != True ):
                os.mkdir( self.act_dir )
            file_store = self.act_dir + "/" + self.core_log_file
            os.system("touch " + file_store) 
        elif (options.r == 'E'): 
            if ( UtilsManager().check_existance([self.exp_dir], "d") != True ):
                os.mkdir( self.exp_dir )
            file_store = self.exp_dir + "/" + self.core_log_file
            os.system("touch " + file_store) 

        self.log_file = file_store

        return (StatusCodes.SUCCESS)




    def dump(self):
        print "Host = ", self.host
        print "Port = ", self.port
        print "DAO = ", self.dao
        print "Table = ", self.table
        print "Primary Key= ", self.pks
        print "Non Primary Keys= ", self.npks
        print "Where = ", self.where
        print "Mode =", (lambda : "Save" if (self.mode == "S") else "Compare")()
        print "Run =", (lambda : "Actual" if (self.run_type == "A") else "Expected")()


    # Deprecated and kept for future use
    def connect(self):    
        # Get Host and Port 
        if ( (len(self.host) == 0) or (self.host == None) ):
            from envvar import Env
            print "Reading Host from ENV"
            self.host = Env('', '').etl_map['Host']

        if( self.port == 0 ):    
            from envvar import Env
            print "Reading Port from ENV"
            self.port = Env('', '').etl_map['MD_DB_PORT']

        # Still no info about Host and Port, GO BACK 
        if ( (self.host is None) or (self.port == 0) ):
            print "Unable to get Host and Port"
            return (StatusCodes.ERROR)
    
        os.system("clear")
        print "Connecting to Host:",self.host,":",self.port
        from tdscli import TDSClient 

        self.db_client = TDSClient()

        try:
            self.db_client.connect(self.host, self.port)
        except Exception as e:
            print "Unable to connect: Details Below"
            #print "Error Code: ", e.errno
            #print "Error String: ", e.strerror
            print e.message
            return (StatusCodes.ERROR)
            
        print "Connected ..."
        return  (StatusCodes.SUCCESS)

        


    def disconnect(self):
        print "Disconnecting from Host: ", self.host
        self.db_client.disconnect()


    def prepare_query(self):
        self.query_str = "select "

        self.query_str += self.pks + ", "

        self.query_str += self.npks

        self.query_str += " from " + (self.table) + " "

        if( len(self.where) != 0 ):
                if (self.skip_clean == True):
                    self.query_str += " where " + re.sub(',', ' ', self.where)
                else:
                    self.query_str += " where "
                    for i,v in enumerate(self.where):
                        v = re.sub(',', ' ', v)
                        self.query_str += v


        print "\nSQL Query to run = ", self.query_str    


    def execute_SQL_query(self):
        from tdscli import TDSError, TDSClient

        self.db_client = TDSClient()
        self.prepare_query()

        print "Connecting to Host:",self.host,":",self.port, "To execute SQL"

        try:
            result_set = self.db_client.execute_sql(self.host, self.port, self.dao, self.query_str)
        except TDSError as err_info:
            print "Error while executing SQL"
            print err_info
            return (StatusCodes.ERROR)
        except socket.error as e:
            print "Error while executing SQL"
            print e
            return (StatusCodes.ERROR)

        return result_set



    def get_logger(self):
        import logging

        logger = logging.getLogger("Result Set Logger")
        logger.setLevel(logging.DEBUG)
        ch = logging.FileHandler(self.log_file, "w")
        logger.addHandler(ch)

        return logger




    def parse_results(self, result_set):

        print_progress_bar = True

        try:
            from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed
        except ImportError, e:
            print_progress_bar = False

        logger = self.get_logger()

        print "\nLogging Results to ", self.log_file

        if (print_progress_bar == True):
            """ Just to make Run as pretty  """
            widgets = ['Progress: ', Percentage(), ' ', Bar(marker='-',left='[',right=']'),
                ' ', ETA(), ' ', FileTransferSpeed()]
            prog_bar = ProgressBar(widgets=widgets, maxval=300)
            prog_bar.start()

        for runner in range( len(result_set) ):
            logger.debug("\nRecord No: %d", runner+1)
            for column, value in result_set[runner].iteritems():
                logger.debug("%s %s %s ", column, "=>", value)
                if (print_progress_bar == True):
                    prog_bar.update(runner/100)

        if (print_progress_bar == True):            
            prog_bar.finish()

        print "\n\n"




    def verify(self, tc_no):
        """
        Comparision utility(VerifyDSFiles) will be used for the same
        """
        res_file = "tc" + str(tc_no) + "_" + UtilsManager().get_file_comp_res_file()

        #Erase the old content in output file
        open(res_file, "w").close()

        res_file_ptr = open(res_file, "a")

        self.act_dir += "/"
        self.exp_dir += "/"

        act_res_file = self.act_dir + self.core_log_file

        if ( UtilsManager().check_existance([act_res_file], "f") != True ):
            return StatusCodes.ERROR

        exp_res_file = self.exp_dir + self.core_log_file

        if ( UtilsManager().check_existance([exp_res_file], "f") != True ):
            return StatusCodes.ERROR

        file_comp_tool = VerifyDSFiles()
        result = file_comp_tool.compare_files(act_res_file, exp_res_file, tc_no, res_file_ptr)
        res_file_ptr.close()

        print "-"*140
        print "Done data comparision. Check",res_file,"file for details \n"

        return result


    def tear_down(self):
        """
        Comparision utility(VerifyDSFiles) will be used for the same
        """
        pass

if __name__ == '__main__':
    TableComparator().main()
