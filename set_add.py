#!/usr/bin/env python3

s = set()
for _ in range(int(input())):
    s.add(input())
print(len(s))


''' OR using comprehension...
s = {input() for _ in range(int(input()))}
print(len(s))
'''

''' sample input
7
UK
China
USA
France
New Zealand
UK
France
'''
