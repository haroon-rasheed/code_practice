#! /usr/bin/python

import logging

logger = logging.getLogger("LSD")
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler("LA.log", "w")


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
#ch.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.info('info message 11')
logger.debug('debug message 11')
logger.warn('warn message 11')
logger.error('error message 11')
logger.critical('critical message 11') 

