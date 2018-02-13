#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: click_test3.py
"
"        Author: xss - callmexss@126.com
"   Description: Mimic a fc command by click
"        Create: 2018-02-14 01:44:46
"""""""""""""""""""""""""""""""""""""""""""""""
import click
import os


message = click.edit()
os.system(message)
