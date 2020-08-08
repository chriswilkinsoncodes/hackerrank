#!/usr/bin/env python3

from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    word = input()
    d[word] = d.get(word, 0) + 1
print(len(d))
for v in d.values():
    print(v, end=' ')

'''
sample input
4
bcdef
abcdefg
bcde
bcdef
'''
