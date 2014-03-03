#!/usr/bin/python

import unittest

class AppCode:
    def verify_dao_name(self, dao_name):
        assert (dao_name == "etlDao"), "Invalid DAO"

    def verify_tbl_name(self, tbl):      
        assert (tbl == "etl_process_status"), "Incorrect Table"


class RunPyUT(unittest.TestCase):
    def runTest(self):
        test_obj = AppCode()
        test_obj.verify_dao_name("EtlDao")
        #test_obj.verify_dao_name("etlDao")
        test_obj.verify_tbl_name("etlDao")


if __name__ == '__main__':
    ut_obj = RunPyUT()

    runner = unittest.TextTestRunner()
    runner.run(ut_obj)

