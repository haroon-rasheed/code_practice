#!/usr/bin/python

import logging
from logging import handlers, Formatter


logger = logging.getLogger("BaseLogger")
logger.setLevel(logging.DEBUG)

ch = logging.handlers.RotatingFileHandler("PLE.LOG", maxBytes=10, backupCount=10)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)

for i in range(20):
	logger.debug("debug message")
	logger.info("info message")
	logger.warn("warning message")
	logger.error("error message")
	logger.critical("critical message")
