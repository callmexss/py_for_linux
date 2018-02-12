#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: logging_test2.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-02-12 11:13:25
"""""""""""""""""""""""""""""""""""""""""""""""
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename='app.log2'
    )


logging.debug("debug message")
logging.info("info message")
logging.warn("warn message")
logging.error("error message")
logging.critical("critical message")
