#!/usr/bin/env python3

from itertools import combinations as cnr


n = int(input())
L = input().split()
k = int(input())
combos = cnr(L, k)

sum_a, len_combos = 0, 0
for combo in combos:
    len_combos += 1
    if 'a' in combo:
        sum_a += 1

print(f'{sum_a/len_combos:.3f}')

'''
sample input
4
a a b c
2
result
0.833 (i.e. 5/6)
'''