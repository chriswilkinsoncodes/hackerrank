#!/usr/bin/env python3

from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    vals = input().split()
    k = ' '.join(vals[:-1])
    v = int(vals[-1])
    d[k] = d.get(k, 0) + v
for k, v in d.items():
        print(k, v)

'''
sample input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
'''
