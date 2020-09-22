#!/usr/bin/env python3

import re

for _ in range(int(input())):
    try:
        # re.compile(input())
        # print('True')
        print(bool(re.compile(input())))
    except re.error:
        print('False')

''' sample input
2
.*\+
.*+
'''
