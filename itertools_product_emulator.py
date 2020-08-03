#!/usr/bin/env python3

A = list(map(int, input().split()))
B = list(map(int, input().split()))
product = ((x,y) for x in A for y in B)
print(*product)


''' input ex.
1 2
3 4
'''