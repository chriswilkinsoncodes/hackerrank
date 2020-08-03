#!/usr/bin/env python3

from itertools import combinations as cnr


if __name__ == '__main__':
    word, n = input().split()
    for m in range(1,int(n)+1):
        print('\n'.join([''.join(i) for i in cnr(sorted(word), m)]))