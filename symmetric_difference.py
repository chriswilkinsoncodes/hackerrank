#!/usr/bin/env python3

M = input()
set_M = set(input().split())
N = input()
set_N = set(input().split())
# diff_set1 = set_M.difference(set_N)
# diff_set2 = set_N.difference(set_M)
# diff_set = (diff_set1.union(diff_set2))
diff_set = (set_M.difference(set_N).union(set_N.difference(set_M)))
print(*sorted(map(int, diff_set)), sep='\n')

'''
sample input - don't know why 'M' & 'N' were included
4
2 4 5 9
4
2 4 11 12
'''
