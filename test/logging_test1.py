#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: logging_test1.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-02-12 11:08:49
"""""""""""""""""""""""""""""""""""""""""""""""

import logging


logging.basicConfig(filename='app.log', level=logging.INFO)


logging.debug("debug message")
logging.info("info message")
logging.warn("warn message")
logging.error("error message")
logging.critical("critical message")
