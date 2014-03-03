#! /usr/bin/python
# -*- coding : utf-8 -*-

"""
example for python logger
"""

import logging 
import logging.config

"""
logging.basicConfig(filename="example.log",level=logging.DEBUG) 
logging.debug("This message should go to the log file") 
logging.info("So should this")
logging.warning('And this, too')

# logging variables
logging.warning("%s before you %s", "Look", "leap!")

"""
# Changing the format of displayed messages
logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

#if i want to erase and write log file i can use below
ch = logging.FileHandler("PLE.LOG", "w")

# if i want just append i can use below, default is append
ch = logging.FileHandler("PLE.LOG")

# NOTE this should match to the above, if not then default is taken that is only warn, error, critical messages will be printed. Info, debug wont be printed
# Always good to set level=DEBUG, if we set other levels debug messages wont be printed
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.info('info message 11')
logger.debug('debug message 11')
logger.warn('warn message 11')
logger.error('error message 11')
logger.critical('critical message 11')

# WAY 2 - BEST
# best way just create a logger config file and do as below

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')

logger.debug('debug message 22')
logger.info('info message 22')
logger.warn('warn message 22')
logger.error('error message 22')
logger.critical('critical message 22')

