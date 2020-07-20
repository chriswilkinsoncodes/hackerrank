#!/usr/bin/env python3

n, m = map(int,input().split())

def print_line(m, i):
    print(('.|.' * (1 + 2 * i)).center(m, '-'))

for i in range(n//2):
    print_line(m, i)

print('WELCOME'.center(m, '-'))

for i in range(n//2-1, -1, -1):
    print_line(m, i)
