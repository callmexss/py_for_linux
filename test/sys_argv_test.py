#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: sys_argv_test.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-02-14 11:23:29
"""""""""""""""""""""""""""""""""""""""""""""""

import os
import sys


def main():
    # used for avoiding argv out of range error
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise SystemExit(filename + " does not exists")
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename + " is not accessable")
    else:
        print(filename + " is accessable")


if __name__ == '__main__':
    main()
    print(sys.argv)
