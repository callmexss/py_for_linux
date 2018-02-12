#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: test.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-02-12 11:07:30
"""""""""""""""""""""""""""""""""""""""""""""""

import time


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


start = time.time()
# li = [x for x in range(100000) if isPrime(x)]
li = []
generator = (x for x in range(100000) if isPrime(x))
try:
    while(1):
        li.append((next(generator)))
except:
    print("out of range")

end = time.time()

print(end - start)
