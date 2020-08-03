#!/usr/bin/env python3

from itertools import groupby


s = input()
for k, g in groupby(s):
    # print((sum(1 for _ in g), int(k)), end=' ')
    print((len(list(g)), int(k)), end=' ')
