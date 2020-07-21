#!/usr/bin/env python3

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    A, B = [], []
    for _ in range(n):
        A.append(input())
    for _ in range(m):
        B.append(input())
    d = defaultdict(list)
    for i in range(n):
        d[A[i]].append(i+1)
    for i in B:    
        print(*d[i]) if i in d else print(-1)
