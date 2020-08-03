#!/usr/bin/env python3

from itertools import permutations as perm


if __name__ == '__main__':
    word, n = input().split()
    print('\n'.join([''.join(i) for i in perm(sorted(word), int(n))]))